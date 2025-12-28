import typer
from csv_profiler.io import read_csv_rows
from csv_profiler.profile import Profiler
from csv_profiler.render import render_markdown, write_json

app = typer.Typer()

@app.command()
def profile(
    file_path: str = typer.Argument(..., help="Path to the CSV file"),
    output_json: str = typer.Option("report.json", help="Output JSON filename")
):
    """
    Compute the profile of a CSV file.
    """
    
    rows = read_csv_rows(file_path)
    
    if not rows:
        print("Error: Could not read rows from the file.")
        return

    
    profiler = Profiler(rows)
    report = profiler.get_profile()

    
    print(render_markdown(report))
    write_json(report, output_json)
    print(f"\nSuccess! Report saved to {output_json}")

if __name__ == "__main__":
    app()




    
 