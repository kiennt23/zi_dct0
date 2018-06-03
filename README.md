# ZI DCT0

This is a Python implementation for the ZI DCT0 trading algorithm. The explanation of the algorithm is beyond the scope of this documentation.
Use at your own risk.

**Source code** [https://github.com/kiennt23/zi_dct0](url)

## Install
Use pip to install the library
```commandline
pip install zi_dct0
```

## Usage
First setup log config  
```python
    LOG_LEVEL = logging.INFO
    core.algo.config_log(LOG_LEVEL)
```
Then setup trade method
```python
    trade_method = TradeMethod.TF
    core.algo.config_trade_method(trade_method)
```
Set LAMBDA (delta price)
```python
    core.algo.delta_p = LAMBDA
```

After setup all the configuration, then run the calculation
```python
    event_type = core.algo.zi_dct0(p_t)
```
whether `p_t` is the price at time *t*

from `event_type` we conclude if is a buy/sell signal `core.algo.is_buy_signaled(event_type, trade_method)` or `core.algo.is_sell_signaled(event_type, trade_method)`

