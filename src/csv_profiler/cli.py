import typer
import time
from pathlib import Path
from csv_profiler.io import read_csv_rows
from csv_profiler.profiling import profile_rows # تأكد أن الملف اسمه profiling.py
from csv_profiler.render import render_markdown, save_report_json, save_report_md

app = typer.Typer()

@app.command()
def profile(
    input_file: str = typer.Argument(..., help="Path to the CSV file you want to check"),
    output_dir: str = typer.Option("outputs", help="Folder to save the reports")
):
    start_time = time.time()
    
    # تحويل النصوص إلى مسارات (Path objects)
    input_path = Path(input_file)
    output_path = Path(output_dir)

    # إنشاء مجلد المخرجات إذا لم يكن موجوداً
    output_path.mkdir(parents=True, exist_ok=True)

    if not input_path.exists():
        typer.secho(f"Error: File not found at {input_file}", fg=typer.colors.RED)
        raise typer.Exit(1)

    typer.echo(f"Processing: {input_file}...")

    try:
        rows = read_csv_rows(input_path)
        report = profile_rows(rows)
        md_text = render_markdown(report)
        
        # حفظ التقارير
        save_report_json(report, output_path / "report.json")
        save_report_md(md_text, output_path / "report.md")
        
        duration = round(time.time() - start_time, 4)
        typer.secho(f"Done! Reports saved in '{output_dir}' folder ({duration}s)", fg=typer.colors.GREEN)
        
    except Exception as e:
        typer.secho(f"An error occurred: {e}", fg=typer.colors.RED)
        raise typer.Exit(1)

if __name__ == "__main__":
    app()