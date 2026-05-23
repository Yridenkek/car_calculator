from pathlib import Path
import html

def generate_report(data: dict) -> str:
    template_path = Path(__file__).parent / "report_template.html"
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()
    for key, value in data.items():
        template = template.replace(f"{{{{{key}}}}}", html.escape(str(value)))
    return template