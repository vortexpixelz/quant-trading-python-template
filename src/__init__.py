"""Quantitative Trading Template Package.

A production-ready template for building quantitative trading systems.
Includes modules for strategies, backtesting, data management, and live trading.
"""

__version__ = "1.0.0"
__author__ = "Your Name"

from . import strategies
from . import data
from . import backtest
from . import utils

__all__ = ["strategies", "data", "backtest", "utils"]
