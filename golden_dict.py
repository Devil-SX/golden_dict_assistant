from pathlib import Path
from datetime import datetime
import re

gd_history_path = "C:\\Users\\shuch\\AppData\\Roaming\\GoldenDict\\history"
output_dir = ".\\history"
pattern = r"\d+\s+(\w*)"

gd_history_path = Path(gd_history_path)
if not gd_history_path.exists():
    raise FileNotFoundError("GoldenDict history path not found.")
else:
    with gd_history_path.open() as f:
        history = f.read().splitlines()
        words = [re.match(pattern, line)[1] for line in history]
        words = ", ".join(words)


output_dir = Path(output_dir)
output_dir.mkdir(parents=True, exist_ok=True)
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_file = output_dir / f"gd_history_{current_time}.txt"
with output_file.open("w") as f:
    f.write(words)
