# 🚀 Quantitative Trading Python Template

> Production-ready template for quantitative finance projects. Options strategies, market-making, HFT backtesting, and live trading.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

## 📋 Table of Contents

- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Key Features](#key-features)
- [Recommended Libraries](#recommended-libraries)
- [Usage Examples](#usage-examples)
- [Configuration](#configuration)
- [Contributing](#contributing)

## 🎯 Quick Start

### Use This Template

1. Click "Use this template" button above
2. Create a new repository from this template
3. Clone your new repository

### Setup Environment

```bash
# Clone your repository
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys
```

## 📁 Project Structure

```
quant-trading-python-template/
├── src/
│   ├── __init__.py           # Package initialization
│   ├── strategies/           # Trading strategies
│   │   ├── __init__.py
│   │   ├── options.py        # Options strategies
│   │   └── market_making.py  # Market-making logic
│   ├── data/                 # Data management
│   │   ├── __init__.py
│   │   ├── fetchers.py       # Data API integrations
│   │   └── storage.py        # Database models
│   ├── backtest/             # Backtesting engine
│   │   ├── __init__.py
│   │   ├── engine.py
│   │   └── metrics.py
│   └── utils/                # Utilities
│       ├── __init__.py
│       ├── greeks.py         # Options Greeks calculator
│       └── risk.py           # Risk management
├── notebooks/                # Jupyter notebooks for analysis
├── tests/                    # Unit and integration tests
├── config/                   # Configuration files
├── data/                     # Raw and processed data
├── requirements.txt          # Python dependencies
├── .env.example              # Environment variables template
└── README.md
```

## ✨ Key Features

### Options Trading
- **Greeks Calculation**: Black-Scholes, Implied Volatility
- **Strategy Builders**: Vertical spreads, Iron condors, Butterflies
- **Risk Analysis**: Position Greeks, P&L scenarios

### Market Making
- **Order Book Simulation**: Real-time spread management
- **Inventory Control**: Position limits and rebalancing
- **Latency Optimization**: Async order execution

### Backtesting
- **Vectorized Engine**: NumPy/Pandas-powered speed
- **Walk-Forward Analysis**: Robust strategy validation
- **Performance Metrics**: Sharpe, Sortino, Max Drawdown

### Live Trading
- **Multi-Broker Support**: Interactive Brokers, Tradier API
- **Paper Trading**: Risk-free strategy testing
- **WebSocket Feeds**: Real-time market data

## 📚 Recommended Libraries

### Python Repositories for Quantitative Finance

#### Options Strategies Focus

| Repository | Stars | Description | Key Features | Best For |
|------------|-------|-------------|--------------|----------|
| [FinRL](https://github.com/AI4Finance-Foundation/FinRL_Podracer) | ~8,000+ | Deep reinforcement learning library for automated trading | - Options trading with DRL agents<br>- Training-testing-trading pipeline<br>- Multiple environments & benchmarks<br>- NeurIPS 2020 featured | Options strategies using machine learning, portfolio optimization |
| [PyOptionTrader](https://github.com/ldt9/PyOptionTrader) | 64 | Interactive Brokers options trader | - Built on ib_insync<br>- Live options trading<br>- py_vollib for Greeks<br>- Asyncio support | Live options execution, Interactive Brokers integration |
| [OptionStrategy](https://github.com/LorenzoAusiello/OptionStrategy-Python-Package) | N/A | User-friendly option strategy package | - Common strategies simplified<br>- P&L profiles<br>- Greeks via Black-Scholes<br>- Yahoo Finance integration | Quick strategy evaluation, educational purposes |
| [optionlab](https://github.com/rgaveiga/optionlab) | 417 | Lightweight options evaluation library | - Profit/loss profiles<br>- Greeks calculation<br>- Probability of profit<br>- Strategy optimization | Strategy backtesting, risk analysis |
| [gs-quant](https://github.com/goldmansachs/gs-quant) | 6,700+ | Goldman Sachs quantitative toolkit | - 25+ years experience<br>- Derivative structuring<br>- Risk management<br>- Professional grade | Institutional-grade derivatives, portfolio risk |

#### Market-Making & Crypto Trading

| Repository | Stars | Description | Key Features | Best For |
|------------|-------|-------------|--------------|----------|
| [hftbacktest](https://github.com/nkaz001/hftbacktest) | 2,800+ | High-frequency trading backtester (Python + Rust) | - Limit order book simulation<br>- Queue position tracking<br>- Full tick data support<br>- Binance/Bybit examples | Market-making strategies, HFT backtesting, crypto futures |
| [freqtrade](https://github.com/freqtrade/freqtrade) | 28,000+ | Open-source crypto trading bot | - Multiple exchanges<br>- Strategy optimization<br>- Backtesting & live trading<br>- Community-driven | Crypto algorithmic trading, automated strategies |
| [vectorbt](https://blog.quantinsti.com/python-trading-library/) | 4,000+ | High-performance backtesting framework | - NumPy/Pandas optimization<br>- Large-scale data handling<br>- Portfolio analysis<br>- Technical indicators | Quantitative research, portfolio optimization |

## 🔧 Configuration

### Environment Variables (.env)

```env
# Data APIs
TRADIER_API_KEY=your_key_here
POLYGON_API_KEY=your_key_here

# Interactive Brokers
IB_ACCOUNT=your_account
IB_GATEWAY_HOST=127.0.0.1
IB_GATEWAY_PORT=4001

# Database
DATABASE_URL=postgresql://user:password@localhost/trading

# Risk Limits
MAX_POSITION_SIZE=10000
MAX_DAILY_LOSS=5000
```

## 🎓 Usage Examples

### Options Strategy Backtest

```python
from src.strategies.options import IronCondor
from src.backtest.engine import BacktestEngine

# Initialize strategy
strategy = IronCondor(
    underlying="SPY",
    dte_target=45,
    width=10,
    delta_target=0.30
)

# Run backtest
engine = BacktestEngine(strategy)
results = engine.run(
    start_date="2023-01-01",
    end_date="2024-01-01"
)

print(results.summary())
```

### Live Market-Making Bot

```python
from src.strategies.market_making import SimpleMarketMaker
from src.data.fetchers import BinanceWebSocket

# Initialize market maker
mm = SimpleMarketMaker(
    symbol="BTCUSDT",
    spread_bps=5,
    position_limit=1.0
)

# Connect to live feed
feed = BinanceWebSocket(symbols=["BTCUSDT"])
feed.on_book_update(mm.on_market_data)
feed.start()
```

## 🧪 Testing

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest --cov=src tests/

# Run specific test module
pytest tests/test_options.py
```

## 📊 Performance Monitoring

The template includes built-in metrics tracking:

- **Sharpe Ratio**: Risk-adjusted returns
- **Max Drawdown**: Peak-to-trough decline
- **Win Rate**: Percentage of profitable trades
- **Profit Factor**: Gross profit / gross loss
- **Greeks Exposure**: Portfolio delta, gamma, theta, vega

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

**This template is for educational and research purposes only. Trading financial instruments involves substantial risk of loss. Past performance is not indicative of future results. Always conduct thorough research and consider seeking advice from a licensed financial advisor before trading.**

## 📞 Support

For questions or issues:
- Open an issue on GitHub
- Check existing discussions
- Review the documentation

---

**Happy Trading! 📈**
