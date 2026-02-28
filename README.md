# 🧠 Blind 75 — LeetCode Solutions

A curated collection of **75 LeetCode problems** organized by pattern, with optimal Python solutions, complexity analysis, alternative approaches, and key intuitions.

## 🌐 Live Site

**[View the solutions →](https://<your-username>.github.io/Neetcode_blind75/)**

## 📁 Structure

```
├── 1.Arrays_and_Hashing/
├── 2.Two_Pointers/
├── 3.Sliding_Window/
├── 4.Stack/
├── 5.Binary_Search/
├── 6.Linked_List/
├── 7.Trees/
├── 8.Tries/
├── 9.Heap/
├── 10.Backtracking/
├── 11.Graphs/
├── 12.Advanced_Graphs/
├── 13.Dynamic_Programming/
├── 14.Intervals/
├── 15.Math_and_Geometry/
├── 16.Bit_Manipulation/
├── docs/              ← GitHub Pages site
│   ├── index.html
│   └── data.js        ← auto-generated
└── build_site.py      ← site generator
```

## 🚀 Deploying to GitHub Pages

### 1. Create a GitHub repository

```bash
cd Neetcode_blind75
git init
git add .
git commit -m "Initial commit: Blind 75 solutions + site"
git branch -M main
git remote add origin https://github.com/<your-username>/Neetcode_blind75.git
git push -u origin main
```

### 2. Enable GitHub Pages

1. Go to your repo on GitHub → **Settings** → **Pages**
2. Under **Source**, select **Deploy from a branch**
3. Branch: `main`, Folder: `/docs`
4. Click **Save**
5. Your site will be live at `https://<your-username>.github.io/Neetcode_blind75/`

### 3. Updating solutions

After editing or adding `.py` files:

```bash
python3 build_site.py     # re-generates docs/data.js
git add . && git commit -m "Update solutions"
git push
```

The site auto-updates within a minute.

## 📖 What each solution includes

| Section | Description |
|---|---|
| **Key Intuition** | 1-2 sentence "aha!" moment |
| **Optimal Solution** | Clean, idiomatic Python 3 |
| **Complexity** | Explicit Big-O for Time & Space |
| **Alternative** | Secondary approach with trade-offs |

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|---|---|
| `Ctrl+K` / `⌘+K` | Focus search bar |

---

Built for interview prep 💪
