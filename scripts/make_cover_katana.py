# Cover for 12 Katana. Same base style as make_cover_grid.py (dark grid, glow layer, left text panel,
# Oswald title, accent bar, playlist label, TECHNO CATALOG tag), with a "forge" variant: a diagonal
# katana blade with tsuba, a rising sun circle behind it, and sparks flying from an anvil.
# Writes only the 12 cover.
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import random, math
slug,title,label,acc="12_katana","Katana","JAPANESE TECHNO","#E8323C"
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
# rising sun circle with rays
g.ellipse([cx-190,cy-190,cx+190,cy+190],outline=k(0.6),width=4)
for i in range(16):
    a=i*math.pi/8; g.line([(cx+200*math.cos(a),cy+200*math.sin(a)),(cx+300*math.cos(a),cy+300*math.sin(a))],fill=k(0.25),width=3)
# katana: diagonal blade, tsuba and wrapped handle
ang=math.radians(-35); ux,uy=math.cos(ang),math.sin(ang)
px,py=-uy,ux
bx,by=cx-60*ux,cy-60*uy
tip=(bx+330*ux,by+330*uy)
g.polygon([(bx+6*px,by+6*py),(tip[0]+2*px,tip[1]+2*py),tip,(bx-6*px,by-6*py)],fill=(255,240,225))
g.line([(bx,by),tip],fill=k(1),width=1)
g.ellipse([bx-26,by-26,bx+26,by+26],outline=k(0.9),width=5)
hx,hy=bx-150*ux,by-150*uy
g.line([(bx,by),(hx,hy)],fill=k(0.7),width=14)
for t in range(10,150,16):
    x0,y0=bx-t*ux,by-t*uy
    g.line([(x0+8*px,y0+8*py),(x0-8*ux-8*px,y0-8*uy-8*py)],fill=k(0.35),width=3)
# anvil at the bottom with sparks
ax,ay=cx-40,cy+250
g.polygon([(ax-120,ay),(ax+120,ay),(ax+70,ay+30),(ax+50,ay+80),(ax-50,ay+80),(ax-70,ay+30)],outline=k(0.6))
for j in range(40):
    a=random.uniform(-math.pi,0); L=random.randint(20,140)
    g.line([(ax,ay),(ax+L*math.cos(a),ay+L*math.sin(a))],fill=k(random.uniform(0.5,1)),width=2)
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
