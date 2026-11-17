# Cover for 14 Silk Road: same base style, camel caravan on dunes under a crescent moon.
# Oswald title, accent bar, playlist label, TECHNO CATALOG tag), with a "forge" variant: a diagonal
# katana blade with tsuba, a rising sun circle behind it, and sparks flying from an anvil.
# Writes only the 12 cover.
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import random, math
slug,title,label,acc="15_silk_road","Silk Road","ETHNIC TECHNO","#E8A04A"
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
# Silk Road: crescent moon and stars over layered dunes, a caravan of camels walking along the ridge, a winding road
g.ellipse([cx+80,cy-260,cx+200,cy-140],outline=k(1),width=6)
g.ellipse([cx+110,cy-275,cx+225,cy-160],fill=(0,0,0))
for i in range(40):
    sx,sy=random.randint(cx-330,cx+330),random.randint(30,cy-60)
    r=random.choice([1,1,2,3]); g.ellipse([sx-r,sy-r,sx+r,sy+r],fill=k(random.uniform(0.4,1)))
for j,(amp,base) in enumerate([(40,cy+20),(55,cy+110),(70,cy+210)]):
    pts=[(x,base-amp*math.sin((x-cx)/(160+40*j)+j)) for x in range(cx-360,cx+361,6)]
    g.line(pts,fill=k(0.35+0.25*j),width=4)
def ridge(x): return cy+20-40*math.sin((x-cx)/160)
for n in range(5):
    x=cx-90+n*78; y=ridge(x)-6; s=1-0.08*n
    g.line([(x-28*s,y),(x-28*s,y-34*s)],fill=(255,240,215),width=3)
    g.line([(x+22*s,y),(x+22*s,y-34*s)],fill=(255,240,215),width=3)
    g.arc([x-36*s,y-70*s,x+10*s,y-26*s],180,360,fill=(255,240,215),width=3)
    g.arc([x-6*s,y-66*s,x+30*s,y-30*s],180,360,fill=(255,240,215),width=3)
    g.line([(x+28*s,y-46*s),(x+44*s,y-74*s)],fill=(255,240,215),width=3)
    g.ellipse([x+40*s,y-82*s,x+54*s,y-70*s],outline=(255,240,215),width=3)
    g.ellipse([x-6,y-26*s,x+2,y-18*s],outline=k(1),width=2)
road=[(cx-60+90*math.sin(t/30),H-10-t*1.4) for t in range(0,200,4)]
g.line(road,fill=k(0.9),width=5)
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
