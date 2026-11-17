# Cover for 13 Labyrinth Mind (maze variant). Same base style as make_cover_grid.py (dark grid, glow layer, left text panel,
# Oswald title, accent bar, playlist label, TECHNO CATALOG tag), with a "forge" variant: a diagonal
# katana blade with tsuba, a rising sun circle behind it, and sparks flying from an anvil.
# Writes only the 12 cover.
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import random, math
slug,title,label,acc="13_labyrinth_mind","Labyrinth Mind","DARK TECHNO","#B026FF"
F="/usr/share/fonts/truetype/sand-box/google/Oswald/Oswald-VariableFont_wght.ttf"
def font(sz,w=700):
    f=ImageFont.truetype(F,sz)
    try: f.set_variation_by_axes([w])
    except Exception: pass
    return f
c=tuple(int(acc[i:i+2],16) for i in (1,3,5))
def k(f): return tuple(int(v*f) for v in c)
W,H=1280,720; random.seed(slug)
img=Image.new("RGB",(W,H),(8,8,12)); d=ImageDraw.Draw(img)
for x in range(0,W,40): d.line([(x,0),(x,H)],fill=(18,18,26))
for y in range(0,H,40): d.line([(0,y),(W,y)],fill=(18,18,26))
glow=Image.new("RGB",(W,H),(0,0,0)); g=ImageDraw.Draw(glow)
cx,cy=930,360
# labyrinth: concentric circular maze rings with gaps, a glowing exit gap at the top, horns at the center
for r in range(40,300,36):
    gap=random.uniform(0,360)
    g.arc([cx-r,cy-r,cx+r,cy+r],start=gap+18,end=gap+360-18,fill=k(0.35+0.5*(r/300)),width=5)
    # radial walls
    for _ in range(2):
        a=math.radians(random.uniform(0,360))
        g.line([(cx+r*math.cos(a),cy+r*math.sin(a)),(cx+(r+36)*math.cos(a),cy+(r+36)*math.sin(a))],fill=k(0.4),width=4)
g.arc([cx-292,cy-292,cx+292,cy+292],start=255,end=285,fill=(255,245,230),width=8)
# bull horns in the center
g.arc([cx-60,cy-50,cx-4,cy+20],start=180,end=300,fill=k(1),width=6)
g.arc([cx+4,cy-50,cx+60,cy+20],start=240,end=360,fill=k(1),width=6)
g.ellipse([cx-8,cy-8,cx+8,cy+8],fill=(255,240,230))
img=ImageChops.add(img,glow.filter(ImageFilter.GaussianBlur(10)))
img=ImageChops.add(img,glow.point(lambda v:int(v*0.7)))
ov=Image.new("L",(W,H),0); od=ImageDraw.Draw(ov)
for x in range(W): od.line([(x,0),(x,H)],fill=int(max(0,200-x*0.25)))
img=Image.composite(Image.new("RGB",(W,H),(5,5,8)),img,ov)
d=ImageDraw.Draw(img)
sz=150
while True:
    f=font(sz); bb=d.textbbox((0,0),title.upper(),font=f)
    if bb[2]-bb[0]<=1120 or sz<60: break
    sz-=6
d.rectangle([80,250,92,250+sz+20],fill=c)
d.text((115,240),title.upper(),font=f,fill=(245,245,250))
d.text((118,270+sz),label,font=font(42,400),fill=c)
d.text((W-260,40),"TECHNO CATALOG",font=font(28,400),fill=(120,120,135))
img.save(f"{slug}.cover.png"); print("ok",sz)
