from pathlib import Path

dirs = {
    ".png" : "IMAGES",
    ".jpg" : "IMAGES",
    ".jpeg" : "IMAGES",
    ".gif" : "IMAGES",
    ".mp4" : "VIDEO",
    ".mov" : "VIDEO",
    ".zip" : "ARCHIVES",
    ".pdf" : "DOCUMENTS",
    ".txt" : "DOCUMENTS",
    ".json" : "DOCUMENTS",
    ".docx" : "DOCUMENTS",
    ".dotx" : "DOCUMENTS",
    ".odt" : "DOCUMENTS",
    ".py" : "PROGRAMMES",
}

tri_dirs = Path.home() / "Documents"

files = [f for f in tri_dirs.iterdir() if f.is_file()]
for f in files:
    out_dir = tri_dirs / dirs.get(f.suffix, "AUTRES")
    out_dir.mkdir(exist_ok=True)
    f.rename(out_dir/f.name)
