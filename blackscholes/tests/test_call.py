import numpy as np


from blackscholes import BlackScholesCall, BlackScholesPut


class TestBlackScholesCall:
    test_S = 55.  # Asset price of 55
    test_K = 50.  # Strike price of 50
    test_T = 1.  # 1 year to maturity
    test_r = 0.0025  # 0.25% risk-free rate
    test_sigma = 0.15  # 15% vol
    call = BlackScholesCall(S=test_S, K=test_K, T=test_T, r=test_r, sigma=test_sigma)

    def test_delta(self):
        call_delta = self.call.delta()
        np.testing.assert_almost_equal(call_delta, 0.766407808509462, decimal=6)

        # Due to put-call parity, Call delta - Put delta should be 1.
        put = BlackScholesPut(S=self.test_S, K=self.test_K, T=self.test_T,
                              r=self.test_r, sigma=self.test_sigma)
        assert call_delta - put.delta() == 1.


