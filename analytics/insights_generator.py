import yaml

def generate_insights(summaries, config):
    with open(config['insights_output'], "w") as f:
        for summary in summaries:
            f.write(summary + "\n")
    print("Insights generated and saved.")

if __name__ == "__main__":
    with open("analytics/config.yml") as f:
        config = yaml.safe_load(f)
    summaries = [
        "Client growth trend: steady increase in active users.",
        "Revenue trend: consistent weekly inflow.",
        "Community feedback: positive sentiment overall."
    ]
    generate_insights(summaries, config)