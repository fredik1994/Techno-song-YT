# Cover for 16 Spirit of the Lion: same base style, glowing lion head with radiating mane, lightning, savanna.
# Oswald title, accent bar, playlist label, TECHNO CATALOG tag), with a "forge" variant: a diagonal
# katana blade with tsuba, a rising sun circle behind it, and sparks flying from an anvil.
# Writes only the 19 cover (fire walk: ember path in perspective, footprints, flames, sparks).
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import random, math
slug,title,label,acc="19_fire_walker","Fire Walker","PEAK-TIME TECHNO","#FF6A2B"
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
# Fire walk: ember path in perspective, glowing footprints walking forward, flames on the sides, sparks
w=(255,240,220)
top=(cx,cy-200); 
for i in range(14):
    t=i/13; y=cy-200+t*560; half=20+t*260
    g.line([(cx-half,y),(cx+half,y)],fill=k(0.25+0.45*t),width=2)
g.line([(cx-20,cy-200),(cx-280,cy+360)],fill=k(0.9),width=4)
g.line([(cx+20,cy-200),(cx+280,cy+360)],fill=k(0.9),width=4)
for _ in range(260):
    t=random.random()**0.7; y=cy-200+t*560; half=20+t*260
    x=cx+random.uniform(-half,half); r=1+t*4
    g.ellipse([x-r,y-r*0.6,x+r,y+r*0.6],fill=k(random.uniform(0.4,1)))
for i in range(5):
    t=0.15+i*0.18; y=cy-200+t*560; s=0.4+t*1.1; side=-1 if i%2 else 1
    x=cx+side*28*s
    g.ellipse([x-12*s,y-26*s,x+12*s,y+18*s],fill=w)
    for tt in range(5):
        g.ellipse([x-12*s+tt*5*s,y-38*s,x-7*s+tt*5*s,y-31*s],fill=w)
for side in (-1,1):
    for j in range(3):
        bx=cx+side*(330+j*40); by=cy+340-j*110; hgt=200-j*40; wd=60-j*12
        for layer,(sc,f) in enumerate(((1,0.95),(0.6,0.75))):
            pts=[]
            for q in range(41):
                u=q/40; yy=by-u*hgt*sc
                ww=wd*sc*math.sin(math.pi*min(1,u*1.15))*(1-u)**0.4
                pts.append((bx+ww+side*8*math.sin(u*9),yy))
            for q in range(40,-1,-1):
                u=q/40; yy=by-u*hgt*sc
                ww=wd*sc*math.sin(math.pi*min(1,u*1.15))*(1-u)**0.4
                pts.append((bx-ww+side*8*math.sin(u*9),yy))
            if layer==0: g.polygon(pts,outline=k(f),width=4)
            else: g.polygon(pts,fill=k(f-j*0.15))
for _ in range(70):
    x=random.uniform(cx-340,cx+340); y=random.uniform(cy-330,cy+200); r=random.uniform(1,3)
    g.ellipse([x-r,y-r,x+r,y+r],fill=(255,200,120))
img=ImageChops.add(img,glow.filter(ImageFilter.GaussianBlur(10)))
img=ImageChops.add(img,glow.point(lambda v:int(v*0.7)))
ov=Image.new("L",(W,H),0); od=ImageDraw.Draw(ov)
for x in range(W): od.line([(x,0),(x,H)],fill=int(max(0,200-x*0.25)))
img=Image.composite(Image.new("RGB",(W,H),(5,5,8)),img,ov)
d=ImageDraw.Draw(img)
sz=150
while True:
    f=font(sz); bb=d.textbbox((0,0),title.upper(),font=f)
    if bb[2]-bb[0]<=860 or sz<60: break
    sz-=6
d.rectangle([80,250,92,250+sz+20],fill=c)
d.text((115,240),title.upper(),font=f,fill=(245,245,250))
d.text((118,270+sz),label,font=font(42,400),fill=c)
d.text((W-260,40),"TECHNO CATALOG",font=font(28,400),fill=(120,120,135))
img.save(f"{slug}.cover.png"); print("ok",sz)
