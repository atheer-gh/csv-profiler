import json

def render_markdown(report):
    """Generates a Markdown table for the report (Ref: Page 84)"""
    lines = []
    lines.append("# CSV Profiling Report")
    lines.append(f"- **Total Rows**: {report['rows']}")
    lines.append("\n## Column Analysis")
    lines.append("| Column | Missing | Types |")
    lines.append("| --- | --- | --- |")
    
    for col, stats in report["columns"].items():
        types_str = ", ".join(stats["types"])
        lines.append(f"| {col} | {stats['missing']} | {types_str} |")
    
    return "\n".join(lines)

def write_json(data, filename):
    """Writes the profile report to a JSON file (Ref: Page 84)"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f" Error saving JSON: {e}")