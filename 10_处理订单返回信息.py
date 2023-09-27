import ccxt
import time
from pprint import pprint  # pprint 代表 "pretty print"，即漂亮的打印

# ————————————————————————————————————————————————————————————————————————————————
# 定义交易所

okx = ccxt.okx({  #ccxt.交易所名称
    'apiKey':'d587f03f-b79f-44d7-b1ec-f092bf097970', # API Key
    'secret':'A237F182F7539384F6ED43127D30E7B9', # 密钥
    'password':'f!n5wX3rPppSNyE', # 密码 (Passphrase)
})

# ————————————————————————————————————————————————————————————————————————————————
# 配置代理

okx.proxies = ({
    'http':'socks5://127.0.0.1:10808',
    'https':'socks5h://127.0.0.1:10808'
})

# ————————————————————————————————————————————————————————————————————————————————
# 查询交易所余额

balance = okx.fetch_balance()  # .fetch_balance() 获取交易所账户的余额信息
pprint(balance)  # balance，账户余额

USDT_balance = balance['USDT']['free']  # USDT 余额
EOS_balance = balance['EOS']['free']  # EOS 余额
DOGE_balance = balance['DOGE']['free']  # DOGE 余额

pprint(USDT_balance)  # 打印 USDT 余额
pprint(EOS_balance)  # 打印 EOS 余额
pprint(DOGE_balance)  # 打印 DOGE 余额


# ————————————————————————————————————————————————————————————————————————————————
# 定义下单参数

order_symbol = 'EOS/USDT'  # 交易对，表示要买入 EOS 以 USDT 为计价货币
order_type = 'limit'  # 订单类型，限价订单
order_side = 'buy'  # 订单方向，买入
order_amount = 1  # 购买 EOS 的数量
order_price = 0.1  # 限价订单的价格，表示每个 EOS 以 0.1 USDT 的价格购买

# ————————————————————————————————————————————————————————————————————————————————
# 下单
# create_order(self, symbol: str, type: OrderType, side: OrderSide, amount, price=None, params={})

take_order = okx.create_order(order_symbol,order_type,order_side,order_amount,order_price)  # 创建订单的方法

# ————————————————————————————————————————————————————————————————————————————————
# 打印下单返回参数（参数定义）
# pprint(take_order)

take_order_id = take_order['id']  # ID
take_order_side = take_order['side']  # 方向，通常为 "buy"（买入）或 "sell"（卖出）
take_order_symbol = take_order['symbol']  # 交易对
take_order_type = take_order['type']  # 类型，通常为 "limit"（限价单）

print(take_order_id)  # ID
print(take_order_side)  # 方向，通常为 "buy"（买入）或 "sell"（卖出）
print(take_order_symbol)  # 交易对
print(take_order_type)  # 类型，通常为 "limit"（限价单）

# ————————————————————————————————————————————————————————————————————————————————
# 查询订单状态

order_status = okx.fetch_order_status(take_order_id,order_symbol)  # fetch_order_status 方法获取订单的状态
print(order_status)

'''

def parse_order_status(self, status):
    statuses = {
    '0': 'open',     # open，表示订单处于开放状态。
    '1': 'open',     # open，同样表示订单处于开放状态。
    '2': 'closed',   # closed，表示订单已关闭。
    '4': 'canceled', # canceled，表示订单已取消。
    '5': 'canceled', # canceled，同样表示订单已取消。
}

'''

# ————————————————————————————————————————————————————————————————————————————————
# 如果线上订单状态为 open ，我就下一个订单

if order_status == "open":
    print("下一个新的订单")
    take_new_order = okx.create_order(order_symbol, order_type, order_side, order_amount, order_price)
    print(take_new_order['id'])

print("程序运行结束")

# ————————————————————————————————————————————————————————————————————————————————
# 如果线上订单状态为 open ，我就每一秒下新的订单，直到钱用完

if order_status == "open":
    print("下一个新的订单")
    x = True
    while x:
        take_new_order = okx.create_order(order_symbol, order_type, order_side, order_amount, order_price)
        print(take_new_order['id'])
        time.sleep(1)

print("程序运行结束")

# ————————————————————————————————————————————————————————————————————————————————
# 如果线上订单状态为 open ，则每下一个单 ”委托价格 - 0.002“

if order_status == "open":
    print("下一个新的订单")
    x = True
    while x:
        take_new_order = okx.create_order(order_symbol, order_type, order_side, order_amount, order_price)
        print(take_new_order['id'])
        order_price -= 0.002
        time.sleep(1)

print("程序运行结束")

# ————————————————————————————————————————————————————————————————————————————————
# 如果线上订单状态为 open ，则一直下单；如果余额少于 0.5 U ，就不下单（程序要一直运行）

x = True
while x:

    # 查询交易所余额
    balance = okx.fetch_balance()  # .fetch_balance() 获取交易所账户的余额信息
    USDT_balance = balance['USDT']['free']

    # 判断状态和余额
    if order_status == 'open' and USDT_balance >= 0.5:
        # 下单
        print("USDT 余额：",USDT_balance)
        take_new_order = okx.create_order(order_symbol,order_type,order_side,order_amount,order_price)  # 创建订单的方法
        print(take_new_order['id'])
        time.sleep(1)
    else:
        print("USDT 余额：", USDT_balance)
        print("USDT 余额不足")
        time.sleep(1)
        # x = False  # 当 x 为 False 时，循环退出

print("程序运行结束")
















