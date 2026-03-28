# Trading Bot (Binance Futures Testnet)

This is a simple Python-based trading bot that places market and limit orders on the Binance Futures Testnet. The project focuses on clean structure, basic validation, and proper handling of API interactions.

---

## Features

* Place market and limit orders
* Supports both BUY and SELL
* Command line input using argparse
* Input validation with clear error messages
* Logs API requests, responses, and errors
* Organized code with separate modules

---

## Project Structure

trading_bot/

-bot/
--client.py
--orders.py
--validators.py
--logging_config.py

-cli.py
--requirements.txt
--README.md

---

## Setup

1. Create a virtual environment

2. Install dependencies
   pip install -r requirements.txt

3. Create a `.env` file in the root folder and add:

API_KEY=your_api_key
API_SECRET=your_api_secret

API keys are not included for security reasons.

---

## Usage

Market order:

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit order:

python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 30000

---

## Output

The program prints:

* Order request details
* Order response from the API
* Success or error message

Note: Some fields like orderId or avgPrice may appear empty due to testnet behavior.

---

## Logging

Logs are stored in `trading.log` and include:

* API requests
* API responses
* Errors

---

## Assumptions

* This project uses Binance Futures Testnet
* No real funds are involved
* API response fields may vary or be incomplete on testnet

---
