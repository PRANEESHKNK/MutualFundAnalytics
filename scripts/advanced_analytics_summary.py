from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

performance = pd.read_csv(
    BASE_DIR / "data" / "processed" / "scheme_performance_cleaned.csv"
)

transactions = pd.read_csv(
    BASE_DIR / "data" / "processed" / "investor_transactions_cleaned.csv"
)

sector_hhi = pd.read_csv(
    BASE_DIR / "data" / "processed" / "sector_hhi.csv"
)


# 1. Best risk-adjusted fund
best_sharpe = performance.loc[
    performance["sharpe_ratio"].idxmax()
]

print("1. BEST RISK-ADJUSTED FUND")
print("Fund:", best_sharpe["scheme_name"])
print("Sharpe Ratio:", best_sharpe["sharpe_ratio"])
print("3-Year Return:", best_sharpe["return_3yr_pct"], "%")


# 2. Highest 3-year return
best_return = performance.loc[
    performance["return_3yr_pct"].idxmax()
]

print("\n2. HIGHEST 3-YEAR RETURN")
print("Fund:", best_return["scheme_name"])
print("3-Year Return:", best_return["return_3yr_pct"], "%")
print("Risk Grade:", best_return["risk_grade"])


# 3. Highest sector concentration
highest_hhi = sector_hhi.loc[
    sector_hhi["sector_hhi"].idxmax()
]

print("\n3. HIGHEST SECTOR CONCENTRATION")
print("Fund:", highest_hhi["scheme_name"])
print("Sector HHI:", round(highest_hhi["sector_hhi"], 2))
print("Concentration Level:", highest_hhi["concentration_level"])


# 4. Age group with highest average investment
age_investment = (
    transactions
    .groupby("age_group")["amount_inr"]
    .mean()
    .sort_values(ascending=False)
)

print("\n4. HIGHEST AVERAGE INVESTMENT BY AGE GROUP")
print("Age Group:", age_investment.index[0])
print("Average Transaction Amount:", round(age_investment.iloc[0], 2))


# 5. State with highest total investment
state_investment = (
    transactions
    .groupby("state")["amount_inr"]
    .sum()
    .sort_values(ascending=False)
)

print("\n5. HIGHEST INVESTMENT BY STATE")
print("State:", state_investment.index[0])
print("Total Transaction Amount:", round(state_investment.iloc[0], 2))