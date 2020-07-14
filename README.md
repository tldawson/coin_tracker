# coin_tracker  
  
*This module is unmaintained and non-working. When it was created, there weren't any modules to check the balances or prices of coins other than Bitcoin. Since then, it has been superceded by the [coin_balance](https://py3status.readthedocs.io/en/latest/modules.html#coin-balance) and [coin_market](https://py3status.readthedocs.io/en/latest/modules.html#coin-market) modules that come bundled with py3status.*

Display information about coin balances, prices, and percent change in price. Designed for [py3status](https://github.com/ultrabug/py3status).  
  
Configuration parameters:  
    - `coin` Required. Which coin to display info about.  
    - `local_currency` What currency to convert the coin's value. Default is USD.  
    - `address` Required. What coin address to track.   
    - `format` The formatting of the information displayed.  
    - `format_clicked` The formatting of the information displayed after being clicked. Toggles back when clicked again.  
    - `color` The color of the information displayed. Overrides dynamic coloring.  
  
Format placeholders:  
    - `{balance}` Wallet balance  
    - `{value}` Value of wallet balance  
    - `{price}` Price of each coin  
    - `{ticker}` Coin ticker symbol  
    - `{local_symbol}` Local currency symbol  
    - `{percent_change}` Percent change in price over 24 hours  
  
Coin options:  
    - `aragon` Aragon ANT  
    - `ark` Ark ARK  
    - `augur` Augur REP  
    - `bancor` Bancor BNT  
    - `basic-attention-token` Basic Attention Token BAT  
    - `binance-coin` Binance Coin BNB  
    - `bitcoin` Bitcoin BTC  
    - `bitcoin-cash` Bitcoin Cash BCH  
    - `bitcrystals` BitCrystals BCY  
    - `cardano` Cardano ADA  
    - `counterparty` Counterparty XCP  
    - `dash` Dash DASH  
    - `databits` Databits DTB  
    - `digibyte` DigiByte DGB  
    - `digixdao` DigixDAO DGD  
    - `dogecoin` Dogecoin DOGE  
    - `enjin-coin` Enjin Coin ENJ  
    - `eos` EOS EOS  
    - `ethereum` Ethereum ETH  
    - `ethereum-classic` Ethereum Classic ETC  
    - `ethlend` Ethlend LEND  
    - `firstblood` FirstBlood 1ST  
    - `foldingcoin` FoldingCoin FLDC  
    - `funfair` FunFair FUN  
    - `gas` Gas GAS  
    - `gnosis-gno` Gnosis GNO  
    - `golem-network-tokens` Golem GNT  
    - `guppy` Matchpool GUP  
    - `iconomi` Iconomi ICONOMI  
    - `litecoin` Litecoin LTC  
    - `melon` Melon MLN  
    - `neo` NEO NEO  
    - `omisego` OmiseGO OMG  
    - `pepe-cash` Pepecash PEPECASH  
    - `pluton` Pluton PLU  
    - `rare-pepe-party` Rare Pepe Party RAREPEPEPRTY  
    - `request-network` Request Network REQ  
    - `ripple` Ripple XRP  
    - `rlc` iExec RLC  
    - `round` Round ROUND  
    - `salt` Salt SALT  
    - `singulardtv` SingularDTV SINGLS  
    - `status` Status SNT  
    - `stellar` Stellar XLM  
    - `storj` Storj STORJ  
    - `storjcoin-x` Storjcoin-X SJCX  
    - `swarm-city` Swarm City SWT  
    - `tokencard` TokenCard TKN  
    - `waves` Waves WAVES  
    - `xenon` Xenon XNN  
    - `wings` Wings WINGS  
  
Local currency options:  
    - `aud` Australian dollar A$  
    - `brl` Brazilian Real r$  
    - `btc` Bitcoin Ƀ  
    - `cad` Canadian dollar C$  
    - `chf` Swiss franc fr.  
    - `cny` Chinese yuan ¥  
    - `eur` Euro €  
    - `gbp` British pound £  
    - `hkd` Hong Kong dollar HK$  
    - `idr` Indonesian rupiah Rp  
    - `inr` Indian rupee ₹  
    - `jpy` Japanese yen ¥  
    - `krw` South Korean Won ₩  
    - `rub` Russian ruble ₽  
    - `mxn` Mexican peso Mex$  
    - `usd` United States dollar $  
  
Example:  
```  
coin_tracker {  
    coin = "bitcoin"  
    address = "1JCe8z4jJVNXSjohjM4i9Hh813dLCNx2Sy"  
    format = "{local_symbol}{value} {ticker}"  
    format_clicked = "{price}/{ticker}"  
}  
```  
  
    **author** tldawson@github.io  
    **donations**  0xC0FfEE9f395D72CE06F76Da710E1459A2452184e
