# Cover for 16 Spirit of the Lion: same base style, glowing lion head with radiating mane, lightning, savanna.
# Oswald title, accent bar, playlist label, TECHNO CATALOG tag), with a "forge" variant: a diagonal
# katana blade with tsuba, a rising sun circle behind it, and sparks flying from an anvil.
# Writes only the 12 cover.
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import random, math
slug,title,label,acc="17_tuning_fork","Tuning Fork","HIGH-TECH MINIMAL","#36E0C8"
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
# Tuning Fork: a two-prong tuning fork, concentric sound rings, a wine glass resonating, sine wave across
fx,fy=cx+140,cy-10
for r in range(60,330,34):
    g.ellipse([fx-r,fy-r,fx+r,fy+r],outline=k(max(0.12,0.75-r/450)),width=2)
pts=[(x,cy+250+22*math.sin((x-cx)/38)) for x in range(cx-360,cx+360,4)]
g.line(pts,fill=k(0.55),width=3)
w=(255,245,230)
g.line([(fx-40,fy-170),(fx-40,fy+40)],fill=w,width=12)
g.line([(fx+40,fy-170),(fx+40,fy+40)],fill=w,width=12)
g.arc([fx-46,fy,fx+46,fy+90],0,180,fill=w,width=12)
g.line([(fx,fy+90),(fx,fy+250)],fill=w,width=12)
g.ellipse([fx-14,fy+240,fx+14,fy+264],fill=w)
for s in (-1,1):
    for j in range(3):
        x0=fx+s*(70+j*26); g.arc([x0-20,fy-150,x0+20,fy-40],(-60 if s>0 else 120),(60 if s>0 else 240),fill=k(1-j*0.25),width=4)
gx,gy=cx-60,cy+190
g.arc([gx-55,gy-120,gx+55,gy],0,180,fill=k(1),width=5)
g.line([(gx-55,gy-60),(gx+55,gy-60)],fill=k(0.6),width=2)
g.line([(gx,gy),(gx,gy+90)],fill=k(1),width=5)
g.line([(gx-40,gy+92),(gx+40,gy+92)],fill=k(1),width=5)
for j in range(3):
    g.arc([gx-75-j*18,gy-140-j*18,gx+75+j*18,gy+20+j*18],230,310,fill=k(0.8-j*0.2),width=3)
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
