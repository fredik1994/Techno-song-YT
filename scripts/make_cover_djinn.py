# Cover for 23 Desert Djinn: same base style, sand vortex djinn over a well of gold.
# Oswald title, accent bar, playlist label, TECHNO CATALOG tag), with a "forge" variant: a diagonal
# katana blade with tsuba, a rising sun circle behind it, and sparks flying from an anvil.
# Writes only the 12 cover.
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import random, math
slug,title,label,acc="23_desert_djinn","Desert Djinn","ETHNIC TECHNO","#D9A441"
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
# Desert Djinn: a swirling sand vortex rising into a smoky djinn figure with two glowing eyes, a well of gold below, falling sand grains
for i in range(14):
    r=40+i*16; yy=cy+200-i*28
    g.ellipse([cx-r,yy-10-i,cx+r,yy+10+i],outline=k(0.3+0.05*i),width=3)
# smoky body: spiral
pts=[]
for t in range(0,720,6):
    a=math.radians(t); rr=20+t*0.22
    pts.append((cx+rr*math.cos(a)*0.9, cy-60-t*0.25+rr*math.sin(a)*0.3))
g.line(pts,fill=k(0.8),width=3)
# head and eyes
g.ellipse([cx-70,cy-300,cx+70,cy-170],outline=k(1),width=5)
for ex in (-28,28):
    g.ellipse([cx+ex-10,cy-250,cx+ex+10,cy-232],fill=(255,240,215))
# arms open
g.arc([cx-220,cy-200,cx-40,cy-40],200,320,fill=k(0.9),width=5)
g.arc([cx+40,cy-200,cx+220,cy-40],220,340,fill=k(0.9),width=5)
# well of gold
g.ellipse([cx-110,cy+250,cx+110,cy+300],outline=(255,215,120),width=6)
g.ellipse([cx-80,cy+258,cx+80,cy+292],fill=(140,100,30))
for i in range(70):
    sx=random.randint(cx-330,cx+330); sy=random.randint(20,H-20); r=random.choice([1,1,2])
    g.ellipse([sx-r,sy-r,sx+r,sy+r],fill=k(random.uniform(0.3,0.9)))
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
