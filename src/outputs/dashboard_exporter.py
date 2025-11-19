thonpython
import json
from pathlib import Path

class DashboardExporter:
 def export(self, data: list):
 out_path = Path(__file__).parents[2] / "data" / "sample_output.json"
 with open(out_path, "w") as f:
 json.dump(data, f, indent=2)