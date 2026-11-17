# Cover for 21 Moon Eats the Sun: same base style (dark grid, Oswald title, accent bar, playlist label,
# TECHNO CATALOG tag), distinct motif: a total solar eclipse (black moon disc over a blazing corona ring),
# corona rays, a diamond-ring flash, ritual frame-drum circles below and a flock of birds. Writes only the 21 cover.
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import random, math
slug,title,label,acc="21_moon_eats_the_sun","Moon Eats the Sun","DARK TECHNO","#FF8A1F"
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
cx,cy=1030,300; R=118; w=(255,245,225)
# corona rays
for i in range(72):
    a=i/72*2*math.pi+random.uniform(-0.03,0.03)
    L=R+random.randint(30,150)
    g.line([(cx+(R+6)*math.cos(a),cy+(R+6)*math.sin(a)),(cx+L*math.cos(a),cy+L*math.sin(a))],fill=k(random.uniform(0.35,0.9)),width=random.choice((2,3,4)))
for j in range(3): g.ellipse([cx-R-8-j*22,cy-R-8-j*22,cx+R+8+j*22,cy+R+8+j*22],outline=k(0.7-j*0.2),width=3)
g.ellipse([cx-R-4,cy-R-4,cx+R+4,cy+R+4],outline=w,width=8)
# diamond ring flash
fx,fy=cx+R*math.cos(-0.7),cy+R*math.sin(-0.7)
g.ellipse([fx-16,fy-16,fx+16,fy+16],fill=w)
for a in (0,math.pi/2,math.pi/4,-math.pi/4):
    g.line([(fx-60*math.cos(a),fy-60*math.sin(a)),(fx+60*math.cos(a),fy+60*math.sin(a))],fill=w,width=3)
# ritual drum circles below
gy=640
for j,(dx,r) in enumerate(((-260,48),(-120,62),(40,70),(200,56),(320,42))):
    x=cx+dx; g.ellipse([x-r,gy-r*0.35,x+r,gy+r*0.35],outline=k(0.8),width=3)
    g.ellipse([x-r*0.55,gy-r*0.2,x+r*0.55,gy+r*0.2],outline=k(0.45),width=2)
# birds (simple v shapes)
for _ in range(14):
    x=random.randint(cx-380,cx+300); y=random.randint(470,580); s=random.randint(8,16)
    g.line([(x-s,y-s*0.5),(x,y),(x+s,y-s*0.5)],fill=k(0.6),width=2)
img=ImageChops.add(img,glow.filter(ImageFilter.GaussianBlur(12)))
img=ImageChops.add(img,glow.point(lambda v:int(v*0.75)))
d=ImageDraw.Draw(img)
d.ellipse([cx-R,cy-R,cx+R,cy+R],fill=(4,4,6))  # the moon disc
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
