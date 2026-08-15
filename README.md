# Anticipating Our AGI Future — course website

Static site for the Fall 2026 course at Columbia. No frameworks, no dependencies —
just Python 3 (already on macOS) rendering one HTML file.

## Editing

**Almost everything you want to change lives in [`content.py`](content.py).** It is a
plain Python file of lists and dicts: the description, the outline, the readings,
grading, logistics. Then rebuild:

```bash
python3 build.py
```

That rewrites `index.html`. To preview while editing:

```bash
python3 build.py --serve
```

and open <http://localhost:8000>.

### Common edits

| I want to…                 | Do this in `content.py`                                                   |
| -------------------------- | ------------------------------------------------------------------------- |
| Fix the meeting time/room  | Edit `FACTS`                                                              |
| Change the banner at top   | Edit `NOTICES` (or set it to `[]` to hide)                                |
| Add a reading              | Add an entry to `READINGS` with a short key, then list that key in a session's `readings` |
| Add or reorder a topic     | Edit `UNITS` → `sessions`                                                 |
| Put real dates on the weeks| Add `"date": "2026-09-09"` to a session; the left column switches from "Week N" to the date automatically |
| Announce a guest speaker   | Add a `("Name", "Affiliation", "When")` tuple to `SPEAKERS`               |
| Post slides or notes       | Add `"links": [("Slides", "assets/wk1.pdf")]` to a session                |

Text fields accept a little Markdown: `[text](url)`, `**bold**`, `*italic*`, `` `code` ``.

Visual styling is in [`assets/style.css`](assets/style.css); the page skeleton is the
template at the bottom of [`build.py`](build.py). Light and dark mode are both handled.

## Publishing to GitHub Pages

Free, and no build step runs on GitHub's side — `index.html` is committed, so Pages
just serves it.

1. Create an empty repo on the GitHub account you want (e.g. `agi-future`). Do not
   add a README from the web UI; this repo already has one.
2. Push:

   ```bash
   git remote add origin https://github.com/<username>/agi-future.git
   git branch -M main
   git push -u origin main
   ```

3. On GitHub: **Settings → Pages → Source: Deploy from a branch → `main` / `(root)`**.
4. The site appears at `https://<username>.github.io/agi-future/` within a minute or two.

If you'd rather have it at `https://<username>.github.io/` with no path, name the repo
`<username>.github.io` instead — nothing else changes.

After the first setup, updating the site is:

```bash
python3 build.py && git add -A && git commit -m "update" && git push
```

`.nojekyll` is present so GitHub serves the files as-is instead of running Jekyll.
