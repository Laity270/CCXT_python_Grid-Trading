import ccxt
import time

# ————————————————————————————————————————————————————————————————————————————————
# 查看交易所

exchange = ccxt.exchanges  # exchanges 所有的交易所
print(exchange)

# ————————————————————————————————————————————————————————————————————————————————
# 定义交易所
bitstamp = ccxt.bitstamp()  #ccxt.交易所名称

# ————————————————————————————————————————————————————————————————————————————————
# 配置代理

bitstamp.proxies = ({
    'http':'socks5://127.0.0.1:10808',
    'https':'socks5h://127.0.0.1:10808'
})

# ————————————————————————————————————————————————————————————————————————————————
# 获取比特币信息

symbol = "BTC/USD"
BTC_ticker = bitstamp.fetch_ticker(symbol)  # .fetch_ticker() 获取 BTC 信息
print(BTC_ticker)  # ticker:数据摘要

# ————————————————————————————————————————————————————————————————————————————————
# 如何打印出 “最新价格/时间/... ：****” 这句话

ticker_symbol = BTC_ticker['symbol']  # symbol = 交易对
ticker_bid_price = BTC_ticker['bid']  # bid = 最新价格
ticker_time = BTC_ticker['datetime']  # datetime = 时间

print("交易对：", ticker_symbol)
print("最新价格：",ticker_bid_price)
print('时间',ticker_time)

# ————————————————————————————————————————————————————————————————————————————————
# if 语句

if ticker_bid_price > 30000:
    print("BTC价格大于30000")
else:
    print("BTC价格小于30000")

# ————————————————————————————————————————————————————————————————————————————————
# while 语句

x = True
while x:      # 只要 x 不是 0 或 False

    # 获取BTC价格
    symbol = "BTC/USD"
    BTC_ticker = bitstamp.fetch_ticker(symbol)  # .fetch_ticker() 获取 BTC 信息
    ticker_bid_price = BTC_ticker['bid']  # bid = 最新价格
    BTC_bid = ticker_bid_price

    print(BTC_bid)
    time.sleep(1)  # time.sleep() 用于在程序执行时暂停 1s

    # 如果 BTC 价格低于 30000，打印买入
    if BTC_bid < 30000:
        print("买入")
        time.sleep(1)  # time.sleep() 用于在程序执行时暂停 1s

    # 如果 BTC 价格高于 30005，打印卖出
    elif BTC_bid > 30005:
        print("卖出")
        time.sleep(1)  # time.sleep() 用于在程序执行时暂停 1s

    # 如果 BTC 价格在 30000 和 30005 之间，打印不动
    else:
        print("保持不动")
        time.sleep(1)  # time.sleep() 用于在程序执行时暂停 1s
print("程序退出")

# ————————————————————————————————————————————————————————————————————————————————














