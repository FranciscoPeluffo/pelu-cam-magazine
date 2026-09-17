import os
from PIL import Image

SRC = r'C:\Users\Franp\Downloads\#3263 - Francisco Peluffo - FotoLibro Rectangular Vertical 20x27cm'
DST = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'images', 'fotolibro')
os.makedirs(DST, exist_ok=True)

MAX_W = 1400
QUALITY = 82

def convert(src_name, dst_name):
    im = Image.open(os.path.join(SRC, src_name)).convert('RGB')
    if im.width > MAX_W:
        ratio = MAX_W / im.width
        im = im.resize((MAX_W, round(im.height * ratio)), Image.LANCZOS)
    out_path = os.path.join(DST, dst_name)
    im.save(out_path, 'JPEG', quality=QUALITY, optimize=True)
    return os.path.getsize(out_path)

total = 0
total += convert('TAPA.png', 'page-00-tapa.jpg')
for i in range(2, 42):
    total += convert(f'{i}.png', f'page-{i-1:02d}.jpg')
total += convert('CONTRATAPA.png', 'page-41-contratapa.jpg')

print('Total pages:', 42)
print('Total size MB:', round(total / 1024 / 1024, 2))
