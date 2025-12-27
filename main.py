import typer
import time
from typing import Optional
from csv_profiler.io import read_csv_rows
from csv_profiler.profile import Profiler
from csv_profiler.render import render_markdown, write_json

app = typer.Typer()

@app.command()
def profile(
    file_path: str = typer.Argument(..., help="Path to the CSV file"),
    output_json: str = typer.Option("report.json", help="Output JSON filename"),
    threshold: float = typer.Option(0.5, help="Failure threshold")
):
    """
    Compute the profile of a CSV file.
    """
    
    start_time = time.time()
    
    
    rows = read_csv_rows(file_path)
    if not rows:
        return

    
    profiler = Profiler(rows)
    report = profiler.get_profile()

    
    total_rows = report["rows"]
    for col, stats in report["columns"].items():
        if stats["missing"] / total_rows > threshold:
            print(f"Error: Column {col} exceeds missing threshold")
            raise typer.Exit(code=1)

    
    print(render_markdown(report))
    write_json(report, output_json)

    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.4f}s")

if __name__ == "__main__":
    app()





    
 