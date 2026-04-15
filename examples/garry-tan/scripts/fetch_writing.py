#!/usr/bin/env python3
"""
Fetch Garry Tan's long-form writing from YC blog and personal site.

Sources:
- ycombinator.com/blog/author/garry/ — author archive, HTML paginated
- garry.posterous.com (historical, via archive.org Wayback)
- garrytan.substack.com (if present)
- medium.com/@garrytan (if present)

Output: data/writing/<slug>.md with frontmatter.
"""

from __future__ import annotations

import pathlib
import re
import sys
import time
import urllib.request
from html.parser import HTMLParser

UA = "Mozilla/5.0 (compatible; soul-garrytan/1.0; +https://github.com/aaronjmars/soul.md)"
OUT = pathlib.Path(__file__).parent.parent / "data" / "writing"
OUT.mkdir(parents=True, exist_ok=True)

YC_AUTHOR_URL = "https://www.ycombinator.com/blog/author/garry/"
WAYBACK_CDX = (
    "https://web.archive.org/cdx/search/cdx?url=garry.posterous.com/*"
    "&output=json&collapse=urlkey&fl=timestamp,original&filter=statuscode:200"
)


def _fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def _slug(s: str, n: int = 80) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:n]


class _TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.skip = 0
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "nav", "footer"}:
            self.skip += 1

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "nav", "footer"} and self.skip > 0:
            self.skip -= 1

    def handle_data(self, data: str) -> None:
        if self.skip == 0 and data.strip():
            self.parts.append(data.strip())


def _extract(html: str) -> str:
    p = _TextExtractor()
    p.feed(html)
    return "\n\n".join(p.parts)


def fetch_yc() -> int:
    html = _fetch(YC_AUTHOR_URL)
    links = sorted(set(re.findall(r'href="(/blog/[^"]+)"', html)))
    n = 0
    for path in links:
        if path in {"/blog/", "/blog/author/garry/"}:
            continue
        url = f"https://www.ycombinator.com{path}"
        page = _fetch(url)
        title_match = re.search(r"<title>([^<]+)</title>", page)
        title = title_match.group(1).strip() if title_match else path
        body = _extract(page)
        slug = _slug(path.rstrip("/").rsplit("/", 1)[-1])
        (OUT / f"yc_{slug}.md").write_text(
            f"---\nsource: ycombinator.com/blog\ntitle: {title}\nurl: {url}\n---\n\n{body}\n",
            encoding="utf-8",
        )
        n += 1
        time.sleep(0.5)
    return n


def fetch_wayback_posterous() -> int:
    import json as _json

    try:
        raw = _fetch(WAYBACK_CDX)
    except Exception as exc:  # noqa: BLE001
        sys.stderr.write(f"wayback fetch failed: {exc}\n")
        return 0
    rows = _json.loads(raw)[1:]  # skip header
    seen: set[str] = set()
    n = 0
    for ts, original in rows:
        if original in seen or original.endswith("/"):
            continue
        seen.add(original)
        try:
            page = _fetch(f"https://web.archive.org/web/{ts}id_/{original}")
        except Exception:
            continue
        title_match = re.search(r"<title>([^<]+)</title>", page)
        title = title_match.group(1).strip() if title_match else original
        body = _extract(page)
        if len(body) < 400:
            continue
        slug = _slug(original.rsplit("/", 1)[-1] or ts)
        (OUT / f"posterous_{slug}.md").write_text(
            f"---\nsource: garry.posterous.com (via wayback)\ntitle: {title}\nurl: {original}\nwayback_ts: {ts}\n---\n\n{body}\n",
            encoding="utf-8",
        )
        n += 1
        time.sleep(0.4)
    return n


def main() -> None:
    total = 0
    total += fetch_yc()
    total += fetch_wayback_posterous()
    print(f"wrote {total} long-form pieces → {OUT}")


if __name__ == "__main__":
    main()
