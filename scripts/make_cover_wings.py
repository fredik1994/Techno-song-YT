# Cover for 10 Wings of Air. Same base style as make_assets.py / make_cover_glitch.py (dark grid,
# glow layer, left text panel, Oswald title, accent bar, playlist label, TECHNO CATALOG tag), with a
# "wings/sky" variant: a pair of feathered wings, an open cage outline, wind streams and rising feathers.
# Writes only the 10 cover.
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import random, math
slug,title,label,acc="10_wings_of_air","Wings of Air","MELODIC TECHNO","#7FB2FF"
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
# wind streams (curved lines across the sky)
for i in range(9):
    y0=80+i*70; pts=[(x, y0+28*math.sin(x/140+i)) for x in range(300,W+20,10)]
    g.line(pts,fill=k(0.18+0.04*(i%3)),width=2)
# open cage: dome + bars, door swung open on the left
for bx in range(cx-110,cx+111,28):
    if cx-110<=bx<cx-50: continue
    top=cy-60-int(60*math.cos((bx-cx)/110*math.pi/2))
    g.line([(bx,top),(bx,cy+150)],fill=k(0.35),width=3)
g.arc([cx-110,cy-180,cx+110,cy+60],180,360,fill=k(0.45),width=3)
g.line([(cx-110,cy+150),(cx+110,cy+150)],fill=k(0.45),width=4)
g.polygon([(cx-110,cy-60),(cx-200,cy-30),(cx-200,cy+180),(cx-110,cy+150)],outline=k(0.4))
# wings: feather fans on both sides, rising above the cage
for side in (-1,1):
    for j in range(11):
        ang=math.radians(200-j*9) if side<0 else math.radians(-20+j*9)
        L=330-j*14
        x0,y0=cx+side*30,cy-40
        x1=x0+L*math.cos(ang); y1=y0-abs(L*math.sin(ang))-60
        mx,my=(x0+x1)/2,(y0+y1)/2
        w=18
        g.polygon([(x0,y0),(mx-w*math.sin(ang),my+w*math.cos(ang)),(x1,y1),(mx+w*math.sin(ang),my-w*math.cos(ang))],outline=k(1-j*0.05))
        g.line([(x0,y0),(x1,y1)],fill=k(0.6),width=2)
# rising feathers / particles
for i in range(60):
    x=random.randint(560,W-20); y=random.randint(20,H-60); r=random.choice([1,2,2,3])
    g.ellipse([x-r,y-r,x+r,y+r],fill=k(random.uniform(0.4,1)))
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
