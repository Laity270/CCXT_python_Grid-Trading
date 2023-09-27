import ccxt
import time

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
print(balance)  # balance，余额

# ————————————————————————————————————————————————————————————————————————————————
# 下单，限价单
# create_order(self, symbol: str, type: OrderType, side: OrderSide, amount, price=None, params={})

order_symbol = 'EOS/USDT'  # 交易对，表示要买入 EOS 以 USDT 为计价货币
order_type = 'limit'  # 订单类型，限价订单
order_side = 'buy'  # 订单方向，买入
order_amount = 2  # 购买 EOS 的数量
order_price = 0.1  # 限价订单的价格，表示每个 EOS 以 0.1 USDT 的价格购买

okx.create_order(order_symbol,order_type,order_side,order_amount,order_price)  # 创建订单的方法



