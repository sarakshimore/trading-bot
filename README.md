# Binance Futures Testnet Trading Bot

A simple Python-based trading bot for Binance USDT-M Futures Testnet/Demo trading.

This application allows users to place MARKET and LIMIT orders via CLI with proper validation, structured logging, and error handling.

---

## Features

* Place MARKET orders
* Place LIMIT orders
* BUY and SELL support
* Binance Futures Testnet/Demo support
* CLI-based order execution using argparse
* Input validation
* Structured logging
* Exception handling
* Enhanced CLI UX using Rich
* Modular project structure

---

## Bonus Implemented

Enhanced CLI UX:

* Rich formatted console output
* Improved CLI help messages
* Better validation feedback

---

## Technologies Used

* Python 3
* python-binance
* argparse
* python-dotenv
* rich

---

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading.log
│
├── cli.py
├── .env
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Requirements

* Python 3.x
* Binance Futures Testnet/Demo account
* Binance API Key & Secret

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone <your-github-repo-url>
cd trading_bot
```

### 2. Create Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Binance Futures Testnet Setup

Create Binance Futures Demo/Testnet account:

[https://demo-fapi.binance.com](https://demo-fapi.binance.com)

Generate:

* API Key
* API Secret

---

### Configure Environment Variables

Create a `.env` file in the project root:

```env
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

---

### Running the Application

#### MARKET BUY Order

```bash
python cli.py \
--symbol ETHUSDT \
--side BUY \
--type MARKET \
--quantity 0.02
```

---

#### MARKET SELL Order

```bash
python cli.py \
--symbol ETHUSDT \
--side SELL \
--type MARKET \
--quantity 0.02
```

---

#### LIMIT BUY Order

```bash
python cli.py \
--symbol ETHUSDT \
--side BUY \
--type LIMIT \
--quantity 0.02 \
--price 1500
```

---

#### LIMIT SELL Order

```bash
python cli.py \
--symbol ETHUSDT \
--side SELL \
--type LIMIT \
--quantity 0.02 \
--price 5000
```

---

## Sample Output

```text
╭──────────────────────────────╮
│ ORDER REQUEST                │
│                              │
│ Symbol      : ETHUSDT        │
│ Side        : BUY            │
│ Order Type  : MARKET         │
│ Quantity    : 0.02           │
╰──────────────────────────────╯

╭──────────────────────────────╮
│ ORDER RESPONSE               │
│                              │
│ Order ID      : 123456789    │
│ Status        : FILLED       │
│ Executed Qty  : 0.02         │
│ Avg Price     : 2500.12      │
│                              │
│ Order placed successfully │
╰──────────────────────────────╯
```
---

## Screenshots
<img width="1122" height="554" alt="Screenshot 2026-05-09 162735" src="https://github.com/user-attachments/assets/679a66bd-7b3c-4099-b750-0a27565756c5" />
<br>
<img width="1158" height="553" alt="Screenshot 2026-05-09 162808" src="https://github.com/user-attachments/assets/de35c2ec-af2d-4dfd-9744-333605f2d142" />
<br>
<img width="1232" height="541" alt="Screenshot 2026-05-09 162954" src="https://github.com/user-attachments/assets/0009c32b-0dc9-42cc-9540-b7756f9fcaf7" />
<br>
<img width="1830" height="835" alt="Screenshot 2026-05-09 165036" src="https://github.com/user-attachments/assets/60261a2c-d213-49a6-a3ac-aea643b26153" />
<br>
<img width="1827" height="811" alt="Screenshot 2026-05-09 165051" src="https://github.com/user-attachments/assets/6c6b9f27-4725-461c-84d3-e6f587d10e3c" />
<br>
<img width="1830" height="514" alt="Screenshot 2026-05-09 165014" src="https://github.com/user-attachments/assets/8ed8223a-f74b-4eed-82a3-848c307d9786" />

---

## Logging

All API requests, responses, and errors are logged to:

```text
logs/trading.log
```

Logged information includes:

* order requests
* order responses
* API errors
* validation errors

---

## Sample Logs Included

Sample trading logs are included in:

```text
logs/trading.log
```

These include:

* MARKET order logs
* LIMIT order logs

---

## Validation & Error Handling

The application validates:

* BUY/SELL side
* MARKET/LIMIT order type
* positive quantity
* required LIMIT order price

Handled exceptions include:

* invalid user input
* Binance API errors
* network/API failures

---

## Assumptions

* Binance USDT-M Futures only
* Binance Futures Demo/Testnet environment used
* User has valid API credentials
* Minimum order notional requirements depend on Binance Futures rules

---

## Notes

* MARKET orders usually return `FILLED`
* LIMIT orders may remain `NEW` until price conditions are met
* Binance Futures minimum notional requirements may apply
