import pandas as pd
import matplotlib.pyplot as plt

class CreditDataAnalyzer:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)

    def show_head(self):
        print("First 5 rows:")
        print(self.df.head())

    def show_info(self):
        print("\nBasic Info:")
        print(self.df.info())

    def describe_numeric(self):
        print("\nStatistical Summary:")
        print(self.df.describe())

    def count_risk_levels(self):
        print("\nCount of Risk levels:")
        print(self.df["Risk"].value_counts())

    def check_missing_values(self):
        print("\nMissing Values in Each Column:")
        print(self.df.isnull().sum())

    def filter_high_credit(self, threshold=10000):
        print(f"\nPeople with credit amount greater than {threshold}:")
        print(self.df[self.df["Credit amount"] > threshold][["Credit amount", "Risk"]].head())

    def plot_risk_distribution(self):
        print("\nShowing bar plot of risk distribution:")
        self.df["Risk"].value_counts().plot(kind="bar", title="Risk Distribution", color=["green", "red"])
        plt.xlabel("Risk Level")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    analyzer = CreditDataAnalyzer("C:/Users/91749/Downloads/german_credit_risk.csv")
    analyzer.show_head()
    analyzer.show_info()
    analyzer.describe_numeric()
    analyzer.count_risk_levels()
    analyzer.check_missing_values()
    analyzer.filter_high_credit(threshold=10000)
    analyzer.plot_risk_distribution()
