# Cover for 16 Spirit of the Lion: same base style, glowing lion head with radiating mane, lightning, savanna.
# Oswald title, accent bar, playlist label, TECHNO CATALOG tag), with a "forge" variant: a diagonal
# katana blade with tsuba, a rising sun circle behind it, and sparks flying from an anvil.
# Writes only the 18 cover.
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import random, math
slug,title,label,acc="18_the_last_lighthouse","The Last Lighthouse","MELODIC TECHNO","#F2B84B"
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
# Lighthouse: tower on a rock, rotating beam fanning across the sky, waves, a distant ship light
lx,ly=cx+120,cy+40
for s_,ang in ((1,-12),(-1,192)):
    for j in range(6):
        a0=math.radians(ang-6+j*2.2); r=900
        g.line([(lx,ly-170),(lx+r*math.cos(a0),ly-170+r*math.sin(a0))],fill=k(0.55-j*0.07),width=6)
w=(255,245,230)
g.polygon([(lx-34,ly+150),(lx+34,ly+150),(lx+20,ly-140),(lx-20,ly-140)],outline=w,width=6)
for yy in (ly-60,ly+40):
    g.line([(lx-28,yy),(lx+28,yy)],fill=k(0.8),width=8)
g.rectangle([lx-28,ly-200,lx+28,ly-140],outline=w,width=6)
g.ellipse([lx-16,ly-186,lx+16,ly-154],fill=k(1))
g.polygon([(lx-34,ly-200),(lx+34,ly-200),(lx,ly-236)],outline=w,width=6)
g.polygon([(lx-130,ly+210),(lx-60,ly+150),(lx+80,ly+148),(lx+170,ly+210)],outline=k(0.6),width=4)
for row in range(3):
    pts=[(x,ly+235+row*30+10*math.sin((x+row*40)/30)) for x in range(cx-380,cx+360,4)]
    g.line(pts,fill=k(0.6-row*0.15),width=3)
sx,sy=cx-160,cy-230
g.ellipse([sx-6,sy-6,sx+6,sy+6],fill=w)
for j in range(3): g.ellipse([sx-14-j*12,sy-14-j*12,sx+14+j*12,sy+14+j*12],outline=k(0.6-j*0.18),width=2)
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
