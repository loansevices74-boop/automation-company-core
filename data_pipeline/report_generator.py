import pandas as pd

def generate_summary(report_path):
    df = pd.read_csv(report_path)
    summary = {
        "rows": len(df),
        "columns": list(df.columns),
        "sample": df.head(5).to_dict()
    }
    return summary

if __name__ == "__main__":
    summary = generate_summary("reports/daily_report.csv")
    print("Report Summary:", summary)