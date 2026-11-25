"""template.html + data/ -> ../DTA_Wortvektoren.html (one self-contained file)."""
from pathlib import Path

HERE = Path(__file__).parent
page = (HERE / "template.html").read_text(encoding="utf-8")
page = page.replace("/*META*/", (HERE / "data/meta.json").read_text(encoding="utf-8").replace("</", r"<\/"))
page = page.replace("/*VECTORS*/", (HERE / "data/vectors.b64").read_text(encoding="utf-8"))
out = HERE.parent / "DTA_Wortvektoren.html"
out.write_text(page, encoding="utf-8")
print(out, out.stat().st_size // 1024, "KB")
