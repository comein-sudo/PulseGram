from PIL import Image, ImageOps
from pathlib import Path

root = Path("TMessagesProj/src/main/res")
logo = Image.open("pulsegram.png").convert("RGBA")

sizes = {
    "mipmap-mdpi": 48,
    "mipmap-hdpi": 72,
    "mipmap-xhdpi": 96,
    "mipmap-xxhdpi": 144,
    "mipmap-xxxhdpi": 192,
}

for folder, size in sizes.items():
    d = root / folder
    icon = ImageOps.fit(logo, (size, size), method=Image.Resampling.LANCZOS)
    icon.save(d / "ic_launcher.png")
    icon.save(d / "ic_launcher_round.png")

adaptive_sizes = {
    "mipmap-mdpi": 108,
    "mipmap-hdpi": 162,
    "mipmap-xhdpi": 216,
    "mipmap-xxhdpi": 324,
    "mipmap-xxxhdpi": 432,
}

for folder, size in adaptive_sizes.items():
    d = root / folder
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    margin = round(size * 0.18)
    inner = ImageOps.contain(logo, (size - 2 * margin, size - 2 * margin), method=Image.Resampling.LANCZOS)
    canvas.alpha_composite(inner, ((size - inner.width) // 2, (size - inner.height) // 2))
    for name in ("icon_foreground.png", "icon_foreground_round.png", "icon_foreground_sa.png"):
        canvas.save(d / name)

print("Иконки Pulsegram обновлены")
