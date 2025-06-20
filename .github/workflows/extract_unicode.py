from fontTools.ttLib import TTFont
import csv

font = TTFont("fa-solid-900.ttf")
cmap = font.getBestCmap()

with open("glyphs.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Unicode", "Glyph Name", "Character"])
    for codepoint, glyph_name in cmap.items():
        try:
            character = chr(codepoint)
        except:
            character = ""
        writer.writerow([f"{codepoint:04x}", glyph_name, character])
