import requests
from datetime import datetime

# SETTINGS (EDIT THIS)
initial_investment = 100
btc_owned = 0.00179372  # <<< REPLACE WITH YOUR REAL BTC AMOUNT
charity_percentage = 0.10

# Get BTC price
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=gbp"
data = requests.get(url).json()
btc_price = data["bitcoin"]["gbp"]

# Calculate values
portfolio_value = btc_owned * btc_price
profit = portfolio_value - initial_investment

# Charity rule
if profit > 20:
    daily_charity = (profit * charity_percentage) / 365
else:
    daily_charity = 0

# Log data
with open("charity_log.txt", "a") as f:
    f.write(f"{datetime.now()} | Value: £{portfolio_value:.2f} | Profit: £{profit:.2f} | Daily Charity: £{daily_charity:.4f}\n")

print("Bot ran successfully")
