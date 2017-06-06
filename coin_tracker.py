#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Displays wallet balance and value in local currency

Configuration parameters:
    - coin              : coin to display, supported coins are listed in COINS table
    - local_currency    : local currency to convert to (default is usd)
    - address           : your virtual wallet address
    - format            : text to diplay by default
    - format_clicked    : text to display when clicked
    - color             : set a static color

@author tldawson.github.io
'''

import json
try:
    # python3
    from urllib.request import urlopen, Request
except:
    from urllib2 import urlopen, Request


class Py3status:
    coin = None
    local_currency = 'usd'
    address = None
    format = '{local_symbol}{value} {ticker} '
    format_clicked = '{balance} {ticker} '
    color = None

    _ticker = None
    _local_symbol = None
    _balance = None
    _value = None
    _price = None
    _percent_change = None


    def on_click(self, event):
        if event['button'] == 1:
            self.format, self.format_clicked = self.format_clicked, self.format


    def _get_coin_info(self):
        url = 'https://api.coinmarketcap.com/v1/ticker/' + self.coin
        if self.local_currency != 'usd':
            url += '/?convert=' + self.local_currency
        try:
            url = urlopen(url).read().decode()
            data = json.loads(url)
            self._price = data[0]['price_' + self.local_currency]
            self._percent_change = data[0]['percent_change_24h']
            self._ticker = data[0]['symbol']
        except:
            self._price = 0
            self._percent_change = 0
            self._ticker = 'ERROR'
        return


    def _get_balance(self):
        def bitcoin():
            url = 'https://blockchain.info/q/addressbalance/' + self.address
            try:
                response = urlopen(url).read().decode()
                self._balance = int(response)/10**8
            except:
                self._balance = 0
            return

        def counterparty():
            url = 'https://xchain.io/api/balances/' + self.address
            try:
                response = urlopen(url).read().decode()
                assets = json.loads(response)['data']
                for asset in assets:
                    if asset['asset'] == self._ticker:
                        self._balance = float(asset['quantity'])
                    else:
                        if not self._balance:
                            self._balance = 0
            except:
                self._balance = 0
            return

        def digibyte():
            headers = {'User-Agent': 'Mozilla/5.0'}
            url = 'https://digiexplorer.info/api/addr/' \
                    + self.address \
                    + '/balance'
            try:
                req = Request(url, None, headers)
                response = urlopen(req).read().decode()
                self._balance = int(response)/10**8
            except:
                self._balance = 0
            return

        def dogecoin():
            url = 'http://dogechain.info/chain/Dogecoin/q/addressbalance/' \
                    + self.address
            try:
                response = urlopen(url).read().decode()
                self._balance = float(response)
            except:
                self._balance = 0
            return

        def ethereum():
            url = 'https://api.etherscan.io/api' \
                    + '?module=account' \
                    + '&action=balance' \
                    + '&address=' \
                    + self.address \
                    + '&apikey=D34DB33F'
            try:
                response = urlopen(url).read().decode()
                data = json.loads(response)
                self._balance = int(data['result'])/10**18
            except:
                self._balance = 0
            return

        def erc20():
            TOKENS = {
                'aragon': '0x960b236A07cf122663c4303350609A66A7B288C0',
                'augur': '0x48c80F1f4D53D5951e5D5438B54Cba84f29F32a5',
                'digixdao': '0xe0b7927c4af23765cb51314a0e0521a9645f0e2a',
                'firstblood': '0xAf30D2a7E90d7DC361c8C4585e9BB7D2F6f15bc7',
                'gnosis-gno': '0x6810e776880c02933d47db1b9fc05908e5386b96',
                'golem-network-tokens': \
                        '0xa74476443119A942dE498590Fe1f2454d7D4aC0d',
                'guppy': '0xf7b098298f7c69fc14610bf71d5e02c60792894c',
                'iconomi': '0x888666CA69E0f178DED6D75b5726Cee99A87D698',
                'melon': '0xBEB9eF514a379B997e0798FDcC901Ee474B6D9A1',
                'pluton': '0xD8912C10681D8B21Fd3742244f44658dBA12264E',
                'rlc': '0x607F4C5BB672230e8672085532f7e901544a7375',
                'round': '0x4993CB95c7443bdC06155c5f5688Be9D8f6999a5',
                'singulardtv': '0xaec2e87e0a235266d9c5adc9deb4b2e29b54d009',
                'tokencard': '0xaaaf91d9b90df800df4f55c205fd6989c977e73a',
                'swarm-city': '0xb9e7f8568e08d5659f5d29c4997173d84cdf2607',
                'wings': '0x667088b212ce3d06a1b553a7221E1fD19000d9aF',}

            if self.coin == 'guppy':
                divisor = 10**3
            else:
                divisor = 10**18

            url = 'https://api.etherscan.io/api' \
                    + '?module=account' \
                    + '&action=tokenbalance' \
                    + '&contractaddress=' \
                    + TOKENS[self.coin] \
                    + '&address=' \
                    + self.address \
                    + '&apikey=D34DB33F'
            try:
                response = urlopen(url).read().decode()
                data = json.loads(response)
                self._balance = int(data['result'])/divisor
            except:
                self._balance = 0
            return

        def waves():
            headers = {'User-Agent': 'Mozilla/5.0'}
            url = 'https://nodes.wavesnodes.com/addresses/balance/' \
                    + self.address
            try:
                req = Request(url, None, headers)
                response = urlopen(req).read().decode()
                data = json.loads(response)
                self._balance = data['balance']/10**8
            except:
                self._balance = 0
            return


        COINS = {'augur': erc20,
                 'aragon': erc20,
                 'bitcoin': bitcoin,
                 'bitcrystals': counterparty,
                 'counterparty': counterparty,
                 'databits': counterparty,
                 'digibyte': digibyte,
                 'digixdao': erc20,
                 'dogecoin': dogecoin,
                 'ethereum': ethereum,
                 'firstblood': erc20,
                 'foldingcoin': counterparty,
                 'gnosis-gno': erc20,
                 'golem-network-tokens': erc20,
                 'guppy': erc20,
                 'iconomi': erc20,
                 'melon': erc20,
                 'pepe-cash': counterparty,
                 'pluton': erc20,
                 'rare-pepe-party': counterparty,
                 'rlc': erc20,
                 'round': erc20,
                 'singulardtv': erc20,
                 'storjcoin-x': counterparty,
                 'swarm-city': erc20,
                 'tokencard': erc20,
                 'waves': waves,
                 'wings': erc20,}
        if self.coin in COINS:
            COINS[self.coin]()
        else:
            self._balance = 0
        return


    def _get_value(self):
        if self.local_currency != 'btc':
            self._value = round(float(self._price) * self._balance, 2)
        else:
            self._value = format(float(self._price) * self._balance, '.8f')
        return


    def _set_local_symbol(self):
        currencies = {'aud': 'A$',
                      'brl': 'r$',
                      'btc': 'Ƀ',
                      'cad': 'C$',
                      'chf': 'fr.',
                      'cny': '¥',
                      'eur': '€',
                      'gbp': '£',
                      'hkd': 'HK$',
                      'idr': 'Rp',
                      'inr': '₹',
                      'jpy': '¥',
                      'krw': '₩',
                      'mxn': 'Mex$',
                      'rub': '₽',
                      'usd': '$',}
        if self.local_currency in currencies:
            self._local_symbol = currencies[self.local_currency]
        else:
            self._local_symbol = 'ERROR'
        return


    def _set_color(self):
        if self.color:
            return

        if not self._percent_change:
            self._percent_change = 0

        if float(self._percent_change) > 0.5:
            self.color = '#88ff88'
        elif float(self._percent_change) > 5.0:
            self.color = '#44ff44'
        elif float(self._percent_change) > 10.0:
            self.color = '#00ff00'
        elif float(self._percent_change) > 50.0:
            self.color = '#ff00ff'

        if float(self._percent_change) < 0.5:
            self.color = '#ff8888'
        elif float(self._percent_change) < -5.0:
            self.color = '#ff4444'
        elif float(self._percent_change) < -10.0:
            self.color = '#ff0000'
        return


    def main(self):
        self._get_coin_info()
        self._get_balance()
        self._get_value()
        self._set_local_symbol()
        self._set_color()

        return {'full_text': self.format.format(
                                balance=self._balance,
                                value=self._value,
                                price=self._price,
                                ticker=self._ticker,
                                local_symbol=self._local_symbol,
                                percent_change=self._percent_change
                                ),
                'cached_until': self.py3.time_in(300),
                'color': self.color}

if __name__ == "__main__":
    x = Py3status()
    x.coin = 'bitcoin'
    x.address = '1JCe8z4jJVNXSjohjM4i9Hh813dLCNx2Sy'
    print(x.main())
