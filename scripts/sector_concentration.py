from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


# --------------------------------------------------
# 1. PROJECT PATHS
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

portfolio_path = (
    BASE_DIR / "data" / "raw" / "09_portfolio_holdings.csv"
)

fund_master_path = (
    BASE_DIR / "data" / "raw" / "01_fund_master.csv"
)

output_path = (
    BASE_DIR / "data" / "processed" / "sector_hhi.csv"
)

chart_path = (
    BASE_DIR / "reports" / "sector_hhi_chart.png"
)


# --------------------------------------------------
# 2. LOAD DATASETS
# --------------------------------------------------

portfolio = pd.read_csv(portfolio_path)
fund_master = pd.read_csv(fund_master_path)


# --------------------------------------------------
# 3. CALCULATE TOTAL WEIGHT OF EACH SECTOR
# --------------------------------------------------

sector_weights = (
    portfolio
    .groupby(["amfi_code", "sector"])["weight_pct"]
    .sum()
    .reset_index()
)


# --------------------------------------------------
# 4. SQUARE EACH SECTOR WEIGHT
# --------------------------------------------------

sector_weights["weight_squared"] = (
    sector_weights["weight_pct"] ** 2
)


# --------------------------------------------------
# 5. CALCULATE HHI FOR EACH FUND
# --------------------------------------------------

sector_hhi = (
    sector_weights
    .groupby("amfi_code")["weight_squared"]
    .sum()
    .reset_index(name="sector_hhi")
)


# --------------------------------------------------
# 6. CLASSIFY CONCENTRATION LEVEL
# --------------------------------------------------

def classify_concentration(hhi):
    if hhi < 1500:
        return "Diversified"
    elif hhi <= 2500:
        return "Moderately Concentrated"
    else:
        return "Highly Concentrated"


sector_hhi["concentration_level"] = (
    sector_hhi["sector_hhi"]
    .apply(classify_concentration)
)


# --------------------------------------------------
# 7. ADD FUND DETAILS
# --------------------------------------------------

fund_info = fund_master[
    [
        "amfi_code",
        "scheme_name",
        "fund_house",
    ]
]

sector_hhi = sector_hhi.merge(
    fund_info,
    on="amfi_code",
    how="left",
)


# --------------------------------------------------
# 8. REORDER AND SORT RESULTS
# --------------------------------------------------

sector_hhi = sector_hhi[
    [
        "amfi_code",
        "scheme_name",
        "fund_house",
        "sector_hhi",
        "concentration_level",
    ]
]

sector_hhi = sector_hhi.sort_values(
    "sector_hhi",
    ascending=False,
)


# --------------------------------------------------
# 9. DISPLAY FINAL RESULTS
# --------------------------------------------------

print("\nSECTOR CONCENTRATION ANALYSIS")
print("-" * 80)

print(
    sector_hhi.head(10).to_string(index=False)
)


# --------------------------------------------------
# 10. SAVE RESULTS TO CSV
# --------------------------------------------------

output_path.parent.mkdir(
    parents=True,
    exist_ok=True,
)

sector_hhi.to_csv(
    output_path,
    index=False,
)

print(
    f"\nSector HHI report saved to:\n{output_path}"
)


# --------------------------------------------------
# 11. CREATE HHI CHART
# --------------------------------------------------

top_10 = sector_hhi.head(10)

plt.figure(figsize=(12, 7))

plt.barh(
    top_10["scheme_name"],
    top_10["sector_hhi"],
)

plt.xlabel("Sector HHI")
plt.ylabel("Fund")
plt.title(
    "Top 10 Mutual Funds by Sector Concentration"
)

plt.gca().invert_yaxis()

plt.tight_layout()


# --------------------------------------------------
# 12. SAVE CHART
# --------------------------------------------------

chart_path.parent.mkdir(
    parents=True,
    exist_ok=True,
)

plt.savefig(
    chart_path,
    dpi=300,
    bbox_inches="tight",
)

plt.show()

print(
    f"\nChart saved to:\n{chart_path}"
)