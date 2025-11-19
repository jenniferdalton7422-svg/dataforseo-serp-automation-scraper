thonpython
class AICategorizer:
 def apply(self, records: list):
 for r in records:
 title = (r.get("title") or "").lower()
 if "review" in title or "best" in title:
 r["ai_category"] = "Review / Comparison"
 elif "tool" in title or "software" in title:
 r["ai_category"] = "Software"
 else:
 r["ai_category"] = "General"
 return records