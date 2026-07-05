from pathlib import Path
import pandas as pd

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

performance_path = BASE_DIR / "data" / "processed" / "scheme_performance_cleaned.csv"

performance = pd.read_csv(performance_path)

def recommend_funds(risk_appetite):
    """
    Recommend top 3 funds based on risk appetite and Sharpe ratio.
    """

    filtered = performance[
        performance["risk_grade"].str.lower() == risk_appetite.lower()
    ]

    if filtered.empty:
        print(f"No funds found for risk grade: {risk_appetite}")
        return

    recommendations = (
        filtered.sort_values("sharpe_ratio", ascending=False)
        .head(3)[
            [
                "scheme_name",
                "fund_house",
                "category",
                "sharpe_ratio",
                "return_3yr_pct",
                "aum_crore",
            ]
        ]
    )

    print("\nTop 3 Recommended Funds\n")
    print(recommendations.to_string(index=False))


if __name__ == "__main__":
    risk = input("Enter Risk Appetite (Low / Moderate / High): ")
    recommend_funds(risk)