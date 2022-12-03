import numpy as np
from scipy.stats import norm

from .base import BlackScholesBase


class BlackScholesPut(BlackScholesBase):
    """
    Class to calculate (European) call option prices and Greeks with the Black-Scholes-Merton formula
    (without dividends).

    :param S: Price of underlying asset
    :param K: Strike price
    :param T: Time till expiration (in years)
    :param r: Risk-free interest rate (0.05 indicates 5%)
    :param sigma: Volatility (standard deviation) of stock (0.15 indicates 15%)
    """
    def __init__(self, S: float, K: float, T: float, r: float, sigma: float):
        super().__init__(S=S, K=K, T=T, r=r, sigma=sigma)

    def price(self):
        """ Price of a put option. """
        return norm.cdf(-self._d2) * self.K * np.exp(-self.r * self.T) - norm.cdf(-self._d1) * self.S

    def delta(self):
        return norm.cdf(self._d1) - 1

    def in_the_money(self):
        """
        Calculate probability that put option will be in the money at
        maturity.
        """
        return 1 - norm.cdf(self._d2)