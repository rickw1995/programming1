def ticker(filename):
    tickers = {}
    file = open("{}.txt".format(filename))
    lines = file.readlines()
    for line in lines:
        a = line.split(sep=":")

        tickers[a[0]]=a[1].strip("\n")
    return tickers

print("Ticker symbol: {}".format(ticker("ticker")[input('Enter company name: ')]))

ticker_in =input("Enter Ticker symbol: ")
for i in ticker("ticker"):
    if ticker("ticker")[i] == ticker_in:
        print("Company name: {}".format(i))