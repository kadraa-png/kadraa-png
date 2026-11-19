"""Generates the project cards in this folder. Edit CARDS, then run: python3 assets/generate_cards.py"""
from pathlib import Path
from html import escape

OUT = Path(__file__).parent  # run from anywhere: python3 assets/generate_cards.py
OUT.mkdir(exist_ok=True)

SANS = "'Segoe UI', Ubuntu, 'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO = "'JetBrains Mono', 'Fira Code', Menlo, Consolas, monospace"

CARDS = [
    {
        "file": "transformers.svg",
        "accent": "#f34b7d", "accent2": "#ff9f43",
        "kicker": "C++ · STATIC RECOMPILATION",
        "title": "Transformers PS2 → Linux",
        "lines": ["A 2004 PlayStation 2 game, translated to native", "x86-64 code. Not an emulator."],
        "stats": [("1.6M", "instructions recompiled"), ("8 / 8", "missions playable"), ("~30 fps", "on a GTX 1050 Ti")],
    },
    {
        "file": "novka.svg",
        "accent": "#2ea043", "accent2": "#7ee787",
        "kicker": "KOTLIN · JETPACK COMPOSE",
        "title": "Novka",
        "lines": ["Offline finance app that logs card payments", "straight from your notifications."],
        "stats": [("0", "servers or trackers"), ("Any", "currency, daily rates"), ("v1.0", "released, GPL-3.0")],
    },
    {
        "file": "launcher.svg",
        "accent": "#7F52FF", "accent2": "#c084fc",
        "kicker": "KOTLIN · MATERIAL 3 EXPRESSIVE · IN PROGRESS",
        "title": "MD3 Launcher",
        "lines": ["A Pixel-style Android home screen with", "the features I wanted and couldn't find."],
        "stats": [("Vault", "fingerprint-locked apps"), ("Limits", "daily, per app"), ("Rules", "Bluetooth triggers")],
    },
    {
        "file": "yt-fetch.svg",
        "accent": "#3776AB", "accent2": "#FFD43B",
        "kicker": "PYTHON · CLI",
        "title": "yt-fetch",
        "lines": ["Bulk YouTube downloader on top of yt-dlp", "and ffmpeg, with search and dry runs."],
        "stats": [("MP3 · MP4", "best available quality"), ("Bulk", "URLs or search terms"), ("Archive", "skips duplicates")],
    },
]

W, H = 800, 400


def card(c):
    stats_svg = []
    col_w = (W - 96 + 16) / 3
    for i, (big, small) in enumerate(c["stats"]):
        x = 48 + i * col_w
        stats_svg.append(
            f'<rect x="{x:.0f}" y="262" width="{col_w - 16:.0f}" height="96" rx="14" fill="#ffffff" fill-opacity="0.04" stroke="#ffffff" stroke-opacity="0.08"/>'
            f'<text x="{x + 18:.0f}" y="306" font-family="{SANS}" font-size="30" font-weight="700" fill="url(#g)">{escape(big)}</text>'
            f'<text x="{x + 18:.0f}" y="338" font-family="{SANS}" font-size="18" fill="#8b949e">{escape(small)}</text>'
        )
    lines = "".join(
        f'<text x="48" y="{184 + i * 34}" font-family="{SANS}" font-size="24" fill="#c9d1d9">{escape(l)}</text>'
        for i, l in enumerate(c["lines"])
    )
    title_size = 44 if len(c["title"]) < 20 else 40
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{escape(c["title"])}">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{c["accent"]}"/><stop offset="1" stop-color="{c["accent2"]}"/>
    </linearGradient>
    <radialGradient id="glow" cx="0.92" cy="0.05" r="0.75">
      <stop offset="0" stop-color="{c["accent"]}" stop-opacity="0.35"/><stop offset="1" stop-color="{c["accent"]}" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="{W}" height="{H}" rx="20" fill="#0d1117"/>
  <rect width="{W}" height="{H}" rx="20" fill="url(#glow)"/>
  <rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="19.5" fill="none" stroke="#30363d"/>
  <rect x="48" y="48" width="44" height="5" rx="2.5" fill="url(#g)"/>
  <text x="48" y="86" font-family="{MONO}" font-size="17" letter-spacing="1.5" fill="{c["accent2"]}">{escape(c["kicker"])}</text>
  <text x="48" y="140" font-family="{SANS}" font-size="{title_size}" font-weight="700" fill="#f0f6fc">{escape(c["title"])}</text>
  {lines}
  {"".join(stats_svg)}
</svg>
'''


for c in CARDS:
    (OUT / c["file"]).write_text(card(c))
    print("wrote", c["file"])
