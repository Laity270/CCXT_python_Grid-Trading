import ccxt
import time
from pprint import pprint  # pprint 代表 "pretty print"，即漂亮的打印

# 定义交易所
okx = ccxt.okx({  #ccxt.交易所名称
    'apiKey':'d587f03f-b79f-44d7-b1ec-f092bf097970', # API Key
    'secret':'A237F182F7539384F6ED43127D30E7B9', # 密钥
    'password':'f!n5wX3rPppSNyE', # 密码 (Passphrase)
})

# 配置代理
okx.proxies = ({
    'http':'socks5://127.0.0.1:10808',
    'https':'socks5h://127.0.0.1:10808'
})

# 定义下单参数
order_symbol = 'EOS/USDT'  # 交易对，表示要买入 EOS 以 USDT 为计价货币
order_type = 'limit'  # 订单类型，限价订单
order_side = 'buy'  # 订单方向，买入
order_amount = 1  # 购买 EOS 的数量
order_price = 0.2  # 限价订单的价格，表示每个 EOS 以 0.1 USDT 的价格购买

# 获取 EOS 最新价格
# EOS_Last = okx.fetch_ticker(order_symbol)['last']  # 最新价格：last
# print("EOS 最新价格:",EOS_Last)

# 下单方法
# take_order = okx.create_order(order_symbol,order_type,order_side,order_amount,order_price)  # 创建订单的方法
# print(take_order)

# 获取线上订单 ID
# take_order_id = take_order['id']
# print(take_order_id)

# 查询订单状态
# order_status = okx.fetch_order_status(take_order_id,order_symbol)  # fetch_order_status 方法获取订单的状态
# print(order_status)
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
# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# 单个网格交易程序
# 需求：下一个订单，循环监控订单状态，如果买单成交，则下一个卖单，卖单成交，就下一个买单

# 下一个订单
take_order = okx.create_order(order_symbol,order_type,order_side,order_amount,order_price)  # 创建订单的方法
# print(take_order)

# 获取线上订单 ID
take_order_id = take_order['id']
# print(take_order_id)

# 获取线上订单方向 side
take_order_side = take_order['side']  # "Side" 是指获取订单的买卖方向
# print(take_order_side)  # 买入（Buy） / 卖出（Sell）

while 1:
    # 分割线
    print("————" * 10)

    # 获取 EOS 最新价格
    EOS_Last = okx.fetch_ticker(order_symbol)['last']  # 最新价格：last
    print("EOS 最新价格:",EOS_Last)

    # 获取线上订单 ID 和 方向
    print("take_order_id",take_order_id)
    print("take_order_side", take_order_side)

    # 查询订单状态
    order_status = okx.fetch_order_status(take_order_id, order_symbol)  # fetch_order_status 方法获取订单的状态
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

    # 如果下的单已取消
    if order_status == "canceled" and take_order_side == "buy":
        sell_side = "sell"  # 卖出（Sell）
        sell_price = order_price + 1  # 卖单价格 +1
        take_sell_order = okx.create_order(order_symbol,order_type,sell_side,order_amount,sell_price)  # 创建卖单

        take_order_id = take_sell_order['id']  # 获取卖单 id
        print("take_order_id",take_order_id)  # 打印卖单 id

        take_order_side = take_sell_order['side']  # 获取卖单方向
        print("take_order_side",take_order_side)  # 打印卖单方向

        time.sleep(1)

    elif order_status == "canceled" and take_order_side == "sell":
        buy_side = "buy"  # 买入（buy）
        buy_price = order_price - 0.1  # 买单价格 -0.1
        take_buy_order = okx.create_order(order_symbol, order_type, buy_side, order_amount, buy_price)  # 创建买单

        take_order_id = take_buy_order['id']  # 获取买单 id
        print("take_order_id",take_order_id)  # 打印买单 id

        take_order_side = take_buy_order['side']  # 获取买单方向
        print("take_order_side",take_order_side)  # 打印买单方向

        time.sleep(1)
    else:
        print("订单处于其他状态")
        time.sleep(1)



