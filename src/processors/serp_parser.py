thonpython
import tldextract

class SerpParser:
 def parse(self, keyword: str, raw: dict):
 results = []
 items = raw.get("items", [])

 for item in items:
 results.append({
 "keyword": keyword,
 "rank": item.get("rank_group"),
 "title": item.get("title"),
 "url": item.get("url"),
 "snippet": item.get("description"),
 "domain": tldextract.extract(item.get("url")).registered_domain,
 "serp_type": item.get("type")
 })
 return results