import json
from pathlib import Path

def render_markdown(report: dict) -> str:
    """
    Creates a nice-looking Markdown report with a table.
    
    """
    md = "# CSV Profiler Report\n\n"
    md += f"- **Total Rows**: {report['row_count']}\n"
    md += f"- **Total Columns**: {report['col_count']}\n\n"
    
    
    md += "## Column Summary\n\n"
    md += "| Column Name | Type | Missing | Min | Max | Mean |\n"
    md += "|-------------|------|---------|-----|-----|------|\n"
    
    for col, stats in report['columns'].items():
        col_type = stats.get('type', 'Unknown')
        missing = stats.get('missing', 0)
        
        c_min = stats.get('min', '-')
        c_max = stats.get('max', '-')
        
        mean = stats.get('mean', '-')
        if isinstance(mean, float):
            mean = f"{mean:.2f}"
            
        md += f"| {col} | {col_type} | {missing} | {c_min} | {c_max} | {mean} |\n"
        
    return md

def save_report_json(report: dict, output_path: str | Path):
    """
    Saves the report dictionary as a JSON file (Day 1 Task 5).
    """
    path = Path(output_path)
    
    path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=4)

def save_report_md(markdown_text: str, output_path: str | Path):
    """
    Saves the Markdown string to a file.
    """
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(markdown_text)