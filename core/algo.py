import logging
from enum import Enum


class DCEventType(Enum):
    UPTURN = 1
    DOWNTURN = 2
    OVERSHOOT = 3


class TradeMethod(Enum):
    TF = 1
    CT = 2


class Config:
    def __init__(self, trade_method, delta_p, mode=None, p_ext=None):
        self.trade_method = trade_method
        self.delta_p = delta_p
        if mode is None and p_ext is None:
            if trade_method == TradeMethod.TF:
                self.mode = DCEventType.UPTURN
                self.p_ext = 1000000000.0
            else:
                self.mode = DCEventType.DOWNTURN
                self.p_ext = 0.0
        else:
            self.mode = mode
            self.p_ext = p_ext


config = None
logger = None


class Position:
    def __init__(self, price):
        self.price = price


def config_log(log_level):
    global logger
    logging.basicConfig(level=log_level)
    logger = logging.getLogger(__name__)


def zi_dct0(p_t):
    global config, logger
    if config is None:
        logger.error('No configuration')
        return
    if config.mode == DCEventType.UPTURN:
        if p_t <= config.p_ext * (1.0 - config.delta_p):
            logger.debug('p_ext={} p_t={}'.format(config.p_ext, p_t))
            config.mode = DCEventType.DOWNTURN
            config.p_ext = p_t
            return config.mode
        else:
            config.p_ext = max([config.p_ext, p_t])
            logger.debug('p_ext={} p_t={}'.format(config.p_ext, p_t))
            return DCEventType.OVERSHOOT

    else:  # mode is DOWNTURN
        if p_t >= config.p_ext * (1.0 + config.delta_p):
            logger.debug('p_ext={} p_t={}'.format(config.p_ext, p_t))
            config.mode = DCEventType.UPTURN
            config.p_ext = p_t
            return config.mode
        else:
            config.p_ext = min([config.p_ext, p_t])
            logger.debug('p_ext={} p_t={}'.format(config.p_ext, p_t))
            return DCEventType.OVERSHOOT


def is_buy_signaled(event_type, trade_method):
    buy_signaled = (trade_method == TradeMethod.TF and DCEventType.UPTURN == event_type) or (
            trade_method == TradeMethod.CT and DCEventType.DOWNTURN == event_type)
    return buy_signaled


def is_sell_signaled(event_type, trade_method):
    sell_signaled = (trade_method == TradeMethod.TF and DCEventType.DOWNTURN == event_type) or (
            trade_method == TradeMethod.CT and DCEventType.UPTURN == event_type)
    return sell_signaled
