import logging
import unittest
from core.algo import *


class ZI_DCT0Test(unittest.TestCase):
    def setUp(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        pass

    def tearDown(self):
        pass

    def test_should_return_overshoot(self):
        config = Config(TradeStrategy.TF, 0.01)
        dct0_runner = ZI_DCT0(self.logger, config)
        observe = dct0_runner.observe(100)
        self.assertEqual(DCEventType.UPTURN, dct0_runner.mode)
        self.assertEqual(100, dct0_runner.p_ext)
        self.assertEqual(DCEventType.OVERSHOOT, observe)
        pass

    def test_should_turn_downturn(self):
        config = Config(TradeStrategy.TF, 0.01)
        dct0_runner = ZI_DCT0(self.logger, config)
        price_series = [100, 99.9, 100.1, 99.5, 100.5, 99]
        observe = dct0_runner.observe(price_series[0])
        self.assertEqual(DCEventType.UPTURN, dct0_runner.mode)
        self.assertEqual(100, dct0_runner.p_ext)
        self.assertEqual(DCEventType.OVERSHOOT, observe)
        observe = dct0_runner.observe(price_series[1])
        self.assertEqual(DCEventType.UPTURN, dct0_runner.mode)
        self.assertEqual(100, dct0_runner.p_ext)
        self.assertEqual(DCEventType.OVERSHOOT, observe)
        observe = dct0_runner.observe(price_series[2])
        self.assertEqual(DCEventType.UPTURN, dct0_runner.mode)
        self.assertEqual(100.1, dct0_runner.p_ext)
        self.assertEqual(DCEventType.OVERSHOOT, observe)
        observe = dct0_runner.observe(price_series[3])
        self.assertEqual(DCEventType.UPTURN, dct0_runner.mode)
        self.assertEqual(100.1, dct0_runner.p_ext)
        self.assertEqual(DCEventType.OVERSHOOT, observe)
        observe = dct0_runner.observe(price_series[4])
        self.assertEqual(DCEventType.UPTURN, dct0_runner.mode)
        self.assertEqual(100.5, dct0_runner.p_ext)
        self.assertEqual(DCEventType.OVERSHOOT, observe)
        observe = dct0_runner.observe(price_series[5])
        self.assertEqual(DCEventType.DOWNTURN, dct0_runner.mode)
        self.assertEqual(99, dct0_runner.p_ext)
        self.assertEqual(DCEventType.DOWNTURN, observe)
        pass

    def test_TF_turn_downturn_should_sell(self):
        config = Config(TradeStrategy.TF, 0.01)
        dct0_runner = ZI_DCT0(self.logger, config)
        price_series = [100, 99.9, 100.1, 99.5, 100.5, 99]
        observe = dct0_runner.observe(price_series[0])
        self.assertFalse(dct0_runner.is_sell_signaled())
        self.assertFalse(dct0_runner.is_buy_signaled())
        observe = dct0_runner.observe(price_series[1])
        self.assertFalse(dct0_runner.is_sell_signaled())
        self.assertFalse(dct0_runner.is_buy_signaled())
        observe = dct0_runner.observe(price_series[2])
        self.assertFalse(dct0_runner.is_sell_signaled())
        self.assertFalse(dct0_runner.is_buy_signaled())
        observe = dct0_runner.observe(price_series[3])
        self.assertFalse(dct0_runner.is_sell_signaled())
        self.assertFalse(dct0_runner.is_buy_signaled())
        observe = dct0_runner.observe(price_series[4])
        self.assertFalse(dct0_runner.is_sell_signaled())
        self.assertFalse(dct0_runner.is_buy_signaled())
        observe = dct0_runner.observe(price_series[5])
        self.assertTrue(dct0_runner.is_sell_signaled())
        self.assertFalse(dct0_runner.is_buy_signaled())
        self.assertEqual(DCEventType.DOWNTURN, dct0_runner.mode)
        self.assertEqual(99, dct0_runner.p_ext)
        self.assertEqual(DCEventType.DOWNTURN, observe)
        pass

    def test_should_turn_upturn(self):
        config = Config(TradeStrategy.TF, 0.01, DCEventType.DOWNTURN, 1000000000.0)
        dct0_runner = ZI_DCT0(self.logger, config)
        price_series = [101, 100.9, 101.1, 100.5, 101.5, 100, 101]
        observe = dct0_runner.observe(price_series[0])
        self.assertEqual(DCEventType.DOWNTURN, dct0_runner.mode)
        self.assertEqual(101, dct0_runner.p_ext)
        self.assertEqual(DCEventType.OVERSHOOT, observe)
        observe = dct0_runner.observe(price_series[1])
        self.assertEqual(DCEventType.DOWNTURN, dct0_runner.mode)
        self.assertEqual(100.9, dct0_runner.p_ext)
        self.assertEqual(DCEventType.OVERSHOOT, observe)
        observe = dct0_runner.observe(price_series[2])
        self.assertEqual(DCEventType.DOWNTURN, dct0_runner.mode)
        self.assertEqual(100.9, dct0_runner.p_ext)
        self.assertEqual(DCEventType.OVERSHOOT, observe)
        observe = dct0_runner.observe(price_series[3])
        self.assertEqual(DCEventType.DOWNTURN, dct0_runner.mode)
        self.assertEqual(100.5, dct0_runner.p_ext)
        self.assertEqual(DCEventType.OVERSHOOT, observe)
        observe = dct0_runner.observe(price_series[4])
        self.assertEqual(DCEventType.DOWNTURN, dct0_runner.mode)
        self.assertEqual(100.5, dct0_runner.p_ext)
        self.assertEqual(DCEventType.OVERSHOOT, observe)
        observe = dct0_runner.observe(price_series[5])
        self.assertEqual(DCEventType.DOWNTURN, dct0_runner.mode)
        self.assertEqual(100, dct0_runner.p_ext)
        self.assertEqual(DCEventType.OVERSHOOT, observe)
        observe = dct0_runner.observe(price_series[6])
        self.assertEqual(DCEventType.UPTURN, dct0_runner.mode)
        self.assertEqual(101, dct0_runner.p_ext)
        self.assertEqual(DCEventType.UPTURN, observe)
        pass

    def test_TF_turn_upturn_should_buy(self):
        config = Config(TradeStrategy.TF, 0.01, DCEventType.DOWNTURN, 1000000000.0)
        dct0_runner = ZI_DCT0(self.logger, config)
        price_series = [101, 100.9, 101.1, 100.5, 101.5, 100, 101]
        observe = dct0_runner.observe(price_series[0])
        self.assertFalse(dct0_runner.is_sell_signaled())
        self.assertFalse(dct0_runner.is_buy_signaled())
        observe = dct0_runner.observe(price_series[1])
        self.assertFalse(dct0_runner.is_sell_signaled())
        self.assertFalse(dct0_runner.is_buy_signaled())
        observe = dct0_runner.observe(price_series[2])
        self.assertFalse(dct0_runner.is_sell_signaled())
        self.assertFalse(dct0_runner.is_buy_signaled())
        observe = dct0_runner.observe(price_series[3])
        self.assertFalse(dct0_runner.is_sell_signaled())
        self.assertFalse(dct0_runner.is_buy_signaled())
        observe = dct0_runner.observe(price_series[4])
        self.assertFalse(dct0_runner.is_sell_signaled())
        self.assertFalse(dct0_runner.is_buy_signaled())
        observe = dct0_runner.observe(price_series[5])
        self.assertFalse(dct0_runner.is_sell_signaled())
        self.assertFalse(dct0_runner.is_buy_signaled())
        observe = dct0_runner.observe(price_series[6])
        self.assertFalse(dct0_runner.is_sell_signaled())
        self.assertTrue(dct0_runner.is_buy_signaled())
        self.assertEqual(DCEventType.UPTURN, dct0_runner.mode)
        self.assertEqual(101, dct0_runner.p_ext)
        self.assertEqual(DCEventType.UPTURN, observe)
        pass
