#!/usr/bin/env python3
"""
Build script: scans all .py solution files and produces docs/data.js
Run this whenever you add/edit solutions, then push to GitHub.
"""

import os
import json
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(ROOT, "docs")

CATEGORY_ORDER = [
    "1.Arrays_and_Hashing",
    "2.Two_Pointers",
    "3.Sliding_Window",
    "4.Stack",
    "5.Binary_Search",
    "6.Linked_List",
    "7.Trees",
    "8.Tries",
    "9.Heap",
    "10.Backtracking",
    "11.Graphs",
    "12.Advanced_Graphs",
    "13.Dynamic_Programming",
    "14.Intervals",
    "15.Math_and_Geometry",
    "16.Bit_Manipulation",
]

CATEGORY_ICONS = {
    "Arrays_and_Hashing": "grid_view",
    "Two_Pointers": "compare_arrows",
    "Sliding_Window": "swap_horiz",
    "Stack": "layers",
    "Binary_Search": "search",
    "Linked_List": "link",
    "Trees": "account_tree",
    "Tries": "text_fields",
    "Heap": "filter_list",
    "Backtracking": "undo",
    "Graphs": "hub",
    "Advanced_Graphs": "polyline",
    "Dynamic_Programming": "grid_on",
    "Intervals": "date_range",
    "Math_and_Geometry": "functions",
    "Bit_Manipulation": "memory",
}


def parse_problem(filepath):
    """Extract metadata from a solution file's docstring."""
    with open(filepath, "r") as f:
        content = f.read()

    # Extract LeetCode number from docstring (e.g. "217. Contains Duplicate")
    num_match = re.search(r'(\d+)\.\s', content)
    lc_number = int(num_match.group(1)) if num_match else 0

    # Extract URL
    url_match = re.search(r'https://leetcode\.com/problems/[^\s/]+/?', content)
    url = url_match.group(0) if url_match else ""

    # Extract Key Intuition
    intuition_match = re.search(
        r'Key Intuition:\s*\n(.*?)(?=\nComplexity|\nTime|\n\n)',
        content, re.DOTALL
    )
    intuition = ""
    if intuition_match:
        lines = intuition_match.group(1).strip().split("\n")
        intuition = " ".join(l.strip() for l in lines)

    # Extract complexities
    time_match = re.search(r'Time:\s*(.+)', content)
    space_match = re.search(r'Space:\s*(.+)', content)
    time_c = time_match.group(1).strip() if time_match else ""
    space_c = space_match.group(1).strip() if space_match else ""

    filename = os.path.basename(filepath)
    title = filename.replace(".py", "").replace("_", " ")

    return {
        "number": lc_number,
        "title": title,
        "url": url,
        "intuition": intuition,
        "time": time_c,
        "space": space_c,
        "code": content,
        "filename": filename,
    }


def build():
    os.makedirs(DOCS, exist_ok=True)
    categories = []

    for cat_dir in CATEGORY_ORDER:
        cat_path = os.path.join(ROOT, cat_dir)
        if not os.path.isdir(cat_path):
            continue

        # Clean category name
        cat_name = re.sub(r'^\d+\.', '', cat_dir).replace("_", " ")
        cat_key = re.sub(r'^\d+\.', '', cat_dir)
        icon = CATEGORY_ICONS.get(cat_key, "code")

        problems = []
        for fname in sorted(os.listdir(cat_path)):
            if fname.endswith(".py"):
                fpath = os.path.join(cat_path, fname)
                problems.append(parse_problem(fpath))

        problems.sort(key=lambda p: p["number"])
        categories.append({
            "name": cat_name,
            "icon": icon,
            "problems": problems,
        })

    data_js = "const PROBLEMS_DATA = " + json.dumps(categories, indent=2) + ";\n"
    out_path = os.path.join(DOCS, "data.js")
    with open(out_path, "w") as f:
        f.write(data_js)

    total = sum(len(c["problems"]) for c in categories)
    print(f"✅  Built {total} problems across {len(categories)} categories → docs/data.js")


if __name__ == "__main__":
    build()
