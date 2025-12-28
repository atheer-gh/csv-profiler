import json

def render_markdown(report: dict):
    md = f"## CSV Profile Report\n\n"
    md += f"- **Total Rows**: {report['rows']}\n"
    md += f"- **Total Columns**: {len(report['columns'])}\n\n"
    md += "| Column Name | Missing Values |\n"
    md += "|-------------|----------------|\n"
    for col, stats in report['columns'].items():
        md += f"| {col} | {stats['missing']} |\n"
    return md

def write_json(report: dict, output_path: str):
    with open(output_path, 'w') as f:
        json.dump(report, f, indent=4)