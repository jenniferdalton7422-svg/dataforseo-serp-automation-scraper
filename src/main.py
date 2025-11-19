thonpython
import json
import logging
from pathlib import Path
from api.dataforseo_client import DataForSEOClient
from processors.serp_parser import SerpParser
from processors.ai_categorizer import AICategorizer
from outputs.dashboard_exporter import DashboardExporter

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def load_settings():
 config_path = Path(__file__).parent / "config" / "settings.example.json"
 with open(config_path, "r") as f:
 return json.load(f)

def load_keywords():
 keywords_path = Path(__file__).parents[1] / "data" / "keywords.sample.txt"
 with open(keywords_path, "r") as f:
 return [k.strip() for k in f.readlines() if k.strip()]

def main():
 settings = load_settings()
 keywords = load_keywords()

 client = DataForSEOClient(
 username=settings["dataforseo_username"],
 password=settings["dataforseo_password"]
 )

 parser = SerpParser()
 categorizer = AICategorizer()
 exporter = DashboardExporter()

 all_results = []

 for kw in keywords:
 try:
 raw = client.fetch_serp(kw)
 parsed = parser.parse(kw, raw)
 categorized = categorizer.apply(parsed)
 all_results.extend(categorized)
 except Exception as e:
 logging.error(f"Failed processing '{kw}': {e}")

 exporter.export(all_results)
 logging.info("Processing complete.")

if __name__ == "__main__":
 main()