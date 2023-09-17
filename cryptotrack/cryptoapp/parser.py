import requests
from requests import Response


class Crypto:
    URL = "https://yobit.net/api/3"

    def get_info(self):
        response = requests.get(url=f"{self.URL}/info")
        return response.text

    def get_ticker(self, coin1: str = "btc", coin2: str = "usd"):
        response = requests.get(url=f"{self.URL}/ticker/{coin1}_{coin2}?ignore_invalid=1")
        with open('file.txt', 'w') as f:
            f.write(response.text)
        return response.text

    def get_depth(self, coin1="btc", coin2="usd", limit=150):
        response: Response = requests.get(url=f"{self.URL}/depth/{coin1}_{coin2}?limit={limit}&ignore_invalid=1")

        bids = response.json()[f"{coin1}_usd"]["bids"]

        total_bids_amount = 0
        for item in bids:
            price = item[0]
            coin_amount = item[1]

            total_bids_amount += price * coin_amount

        return f"Total bids: {total_bids_amount} $"

    def get_trades(self, coin1="btc", coin2="usd", limit=150):
        response = requests.get(url=f"{self.URL}/trades/{coin1}_{coin2}?limit={limit}&ignore_invalid=1")

        total_trade_ask = 0
        total_trade_bid = 0

        for item in response.json()[f"{coin1}_{coin2}"]:
            if item["type"] == "ask":
                total_trade_ask += item["price"] * item["amount"]
            else:
                total_trade_bid += item["price"] * item["amount"]

        info = f"[-] TOTAL {coin1} SELL: {round(total_trade_ask, 2)} $\n[+] TOTAL {coin1} BUY: {round(total_trade_bid, 2)} $"

        return info

crypty = Crypto()
print(crypty.get_ticker())