# Cover for 22 Aurora Gate: same base style (dark grid, Oswald title, accent bar, playlist label,
# TECHNO CATALOG tag), distinct motif: flowing green aurora curtains over a polar horizon forming an open
# arch/gate, a pole star above, icy ground line and two small figures walking toward the gate. Writes only the 22 cover.
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import random, math
slug,title,label,acc="22_aurora_gate","Aurora Gate","EUPHORIC TECHNO","#3DFFB0"
F="/usr/share/fonts/truetype/sand-box/google/Oswald/Oswald-VariableFont_wght.ttf"
def font(sz,w=700):
    f=ImageFont.truetype(F,sz)
    try: f.set_variation_by_axes([w])
    except Exception: pass
    return f
c=tuple(int(acc[i:i+2],16) for i in (1,3,5))
def k(f,col=c): return tuple(int(v*f) for v in col)
W,H=1280,720; random.seed(slug)
img=Image.new("RGB",(W,H),(8,8,12)); d=ImageDraw.Draw(img)
for x in range(0,W,40): d.line([(x,0),(x,H)],fill=(18,18,26))
for y in range(0,H,40): d.line([(0,y),(W,y)],fill=(18,18,26))
glow=Image.new("RGB",(W,H),(0,0,0)); g=ImageDraw.Draw(glow)
cx=1000; base=560; violet=(150,90,255)
# aurora curtains: vertical streaks along two arching ribbons forming a gate
for side in (-1,1):
    for i in range(160):
        t=i/159
        x=cx+side*(60+t*230)+math.sin(t*9+side)*18
        top=110+ (1-math.sin(t*math.pi*0.5+0.2))*40 + math.sin(t*14)*25
        L=random.randint(120,300)
        col=c if random.random()>0.25 else violet
        g.line([(x,top),(x+random.uniform(-6,6),top+L)],fill=k(random.uniform(0.25,0.8),col),width=random.choice((2,3,4)))
# arch top ribbon
for i in range(120):
    a=math.pi+i/119*math.pi
    x=cx+120*math.cos(a); y=230+90*math.sin(a)
    g.line([(x,y),(x,y+random.randint(40,110))],fill=k(random.uniform(0.3,0.9)),width=3)
# pole star
sx,sy=cx,95; w=(235,255,248)
g.ellipse([sx-7,sy-7,sx+7,sy+7],fill=w)
for a in (0,math.pi/2,math.pi/4,-math.pi/4):
    Lr=40 if a in (0,math.pi/2) else 18
    g.line([(sx-Lr*math.cos(a),sy-Lr*math.sin(a)),(sx+Lr*math.cos(a),sy+Lr*math.sin(a))],fill=w,width=2)
# stars
for _ in range(90):
    x=random.randint(560,W-10); y=random.randint(20,420); r=random.choice((1,1,2))
    g.ellipse([x-r,y-r,x+r,y+r],fill=(170,190,200))
# icy horizon
g.line([(560,base),(W,base)],fill=k(0.9),width=3)
for j in range(6): g.line([(600+j*20,base+12+j*14),(W-40-j*20,base+12+j*14)],fill=k(0.35-j*0.05),width=2)
img=ImageChops.add(img,glow.filter(ImageFilter.GaussianBlur(10)))
img=ImageChops.add(img,glow.point(lambda v:int(v*0.7)))
d=ImageDraw.Draw(img)
# two small walking figures toward the gate (duet)
for fx,h in ((cx-28,46),(cx+12,40)):
    d.ellipse([fx-6,base-h-12,fx+6,base-h],fill=(10,12,16))
    d.polygon([(fx-9,base),(fx+9,base),(fx+5,base-h),(fx-5,base-h)],fill=(10,12,16))
ov=Image.new("L",(W,H),0); od=ImageDraw.Draw(ov)
for x in range(W): od.line([(x,0),(x,H)],fill=int(max(0,200-x*0.25)))
img=Image.composite(Image.new("RGB",(W,H),(5,5,8)),img,ov)
d=ImageDraw.Draw(img)
sz=150
while True:
    f=font(sz); bb=d.textbbox((0,0),title.upper(),font=f)
    if bb[2]-bb[0]<=700 or sz<60: break
    sz-=6
d.rectangle([80,250,92,250+sz+20],fill=c)
d.text((115,240),title.upper(),font=f,fill=(245,245,250))
d.text((118,270+sz),label,font=font(42,400),fill=c)
d.text((W-260,40),"TECHNO CATALOG",font=font(28,400),fill=(120,120,135))
img.save(f"{slug}.cover.png"); print("ok",sz)
