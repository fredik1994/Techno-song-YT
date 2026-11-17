# Cover for 16 Spirit of the Lion: same base style, glowing lion head with radiating mane, lightning, savanna.
# Oswald title, accent bar, playlist label, TECHNO CATALOG tag), with a "forge" variant: a diagonal
# katana blade with tsuba, a rising sun circle behind it, and sparks flying from an anvil.
# Writes only the 12 cover.
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import random, math
slug,title,label,acc="16_spirit_of_the_lion","Spirit of the Lion","AFRO TECHNO","#F0B030"
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
# Spirit of the Lion: lion head in profile with radiating mane, lightning bolt, savanna horizon with acacia, rain
for i in range(70):
    rx,ry=random.randint(cx-340,cx+340),random.randint(20,H-60)
    g.line([(rx,ry),(rx-8,ry+26)],fill=k(random.uniform(0.15,0.4)),width=1)
g.line([(cx-360,cy+230),(cx+360,cy+230)],fill=k(0.6),width=3)
ax=cx+250; g.line([(ax,cy+230),(ax,cy+150)],fill=k(0.7),width=5)
g.arc([ax-80,cy+110,ax+80,cy+180],180,360,fill=k(0.7),width=5)
g.line([(cx+150,30),(cx+110,120),(cx+150,120),(cx+100,230)],fill=(255,245,220),width=5)
hx,hy=cx-40,cy+10
for a in range(0,360,12):
    r1=95; r2=180+25*math.sin(a*3*math.pi/180)
    t=math.radians(a)
    g.line([(hx+r1*math.cos(t),hy+r1*math.sin(t)),(hx+r2*math.cos(t),hy+r2*math.sin(t))],fill=k(0.55+0.4*random.random()),width=4)
g.ellipse([hx-95,hy-95,hx+95,hy+95],outline=k(1),width=6)
face=[(hx-40,hy-60),(hx+40,hy-60),(hx+60,hy),(hx+30,hy+70),(hx,hy+85),(hx-30,hy+70),(hx-60,hy)]
g.polygon(face,outline=(255,240,215))
g.line(face+[face[0]],fill=(255,240,215),width=4)
for ex in (-28,28): g.ellipse([hx+ex-9,hy-22,hx+ex+9,hy-10],outline=(255,240,215),width=3)
g.polygon([(hx-14,hy+30),(hx+14,hy+30),(hx,hy+44)],fill=(255,240,215))
g.line([(hx,hy+44),(hx,hy+58)],fill=(255,240,215),width=3)
for ex in (-62,62): g.ellipse([hx+ex-18,hy-95,hx+ex+18,hy-60],outline=(255,240,215),width=3)
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
