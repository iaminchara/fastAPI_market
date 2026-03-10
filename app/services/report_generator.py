from datetime import datetime

def generate_markdown(sector, analysis):

    report = f"""
# Market Analysis Report

**Sector:** {sector}

**Date:** {datetime.now()}

---

## AI Market Insights

{analysis}

---

## Conclusion

This report was generated automatically using AI market analysis.
"""

    return report