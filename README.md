# coin_tracker  
  
Display information about coin balances, prices, and percent change in price. Designed for [i3status](https://github.com/i3/i3status) using [py3status](https://github.com/ultrabug/py3status).  
  
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
    - `bitcoin` Bitcoin BTC  
    - `bitcrystals` BitCrystals BCY  
    - `counterparty` Counterparty XCP  
    - `databits` Databits DTB  
    - `digibyte` DigiByte DGB  
    - `digixdao` DigixDAO DGD  
    - `dogecoin` Dogecoin DOGE  
    - `ethereum` Ethereum ETH  
    - `firstblood` FirstBlood 1ST  
    - `foldingcoin` FoldingCoin FLDC  
    - `funfair` FunFair FUN  
    - `gnosis-gno` Gnosis GNO  
    - `golem-network-tokens` Golem GNT  
    - `guppy` Matchpool GUP  
    - `iconomi` Iconomi ICONOMI  
    - `melon` Melon MLN  
    - `pepe-cash` Pepecash PEPECASH  
    - `pluton` Pluton PLU  
    - `rare-pepe-party` Rare Pepe Party RAREPEPEPRTY  
    - `rlc` iExec RLC  
    - `round` Round ROUND  
    - `singulardtv` SingularDTV SINGLS  
    - `storjcoin-x` Storjcoin-X SJCX  
    - `swarm-city` Swarm City SWT  
    - `tokencard` TokenCard TKN  
    - `waves` Waves WAVES  
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
    **donations**  0x00d50ABE465e6309066FfDeDeFb0aE6a708FEe6a    
