# Cover for 10 Wings of Air. Same base style as make_assets.py / make_cover_glitch.py (dark grid,
# glow layer, left text panel, Oswald title, accent bar, playlist label, TECHNO CATALOG tag), with a
# "blackout" variant: a pair of feathered wings, an open cage outline, wind streams and rising feathers.
# Writes only the 11 cover.
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import random, math
slug,title,label,acc="11_grid_down","Grid Down","PEAK-TIME TECHNO","#FF4A2E"
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
# city skyline at the bottom: most windows dark, a few still lit
x=560
while x<W:
    bw=random.randint(40,90); bh=random.randint(80,220)
    g.rectangle([x,H-bh,x+bw,H],outline=k(0.25))
    for wy in range(H-bh+12,H-10,18):
        for wx in range(x+8,x+bw-8,14):
            if random.random()<0.12: g.rectangle([wx,wy,wx+6,wy+8],fill=k(0.8))
    x+=bw+6
# power pylon (lattice tower) in the centre
top=(cx,90); bl=(cx-120,cy+200); br=(cx+120,cy+200)
g.line([top,bl],fill=k(0.9),width=4); g.line([top,br],fill=k(0.9),width=4)
for i in range(1,9):
    t=i/9; y=top[1]+t*(bl[1]-top[1]); xl=cx-120*t; xr=cx+120*t
    g.line([(xl,y),(xr,y)],fill=k(0.55),width=2)
    t2=(i+1)/9; y2=top[1]+t2*(bl[1]-top[1])
    g.line([(xl,y),(cx+120*t2,y2)],fill=k(0.4),width=2); g.line([(xr,y),(cx-120*t2,y2)],fill=k(0.4),width=2)
for ay,aw in ((150,170),(220,210)):
    g.line([(cx-aw,ay),(cx+aw,ay)],fill=k(0.9),width=4)
# power cables: left side intact, right side snapped and sparking
for ay,aw in ((150,170),(220,210)):
    g.line([(cx-aw,ay),(560,ay+60)],fill=k(0.5),width=2)
    g.line([(cx+aw,ay),(cx+aw+90,ay+50)],fill=k(0.6),width=2)
    ex,ey=cx+aw+90,ay+50
    for j in range(14):
        a=random.uniform(0,2*math.pi); L=random.randint(15,55)
        g.line([(ex,ey),(ex+L*math.cos(a),ey+L*math.sin(a))],fill=k(random.uniform(0.6,1)),width=2)
# lightning-like surge zigzag down the tower
pts=[(cx,70)]; y=70
while y<cy+150:
    y+=random.randint(25,45); pts.append((cx+random.randint(-35,35),y))
g.line(pts,fill=(255,230,200),width=3)
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
