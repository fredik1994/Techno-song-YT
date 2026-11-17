# Cover for 14 Lands Beyond (sail variant): same base style, a sailboat heading to a golden horizon sun with wave lines.
# Oswald title, accent bar, playlist label, TECHNO CATALOG tag), with a "forge" variant: a diagonal
# katana blade with tsuba, a rising sun circle behind it, and sparks flying from an anvil.
# Writes only the 12 cover.
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import random, math
slug,title,label,acc="14_lands_beyond","Lands Beyond","EUPHORIC TECHNO","#FFC23D"
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
# golden horizon sun with rays, layered wave lines, a small sailboat (and tiny fleet) sailing toward it
g.ellipse([cx-120,cy-150,cx+120,cy+90],outline=k(1),width=8)
for i in range(18):
    a=math.radians(180+i*10)
    g.line([(cx+140*math.cos(a),cy-30+140*math.sin(a)),(cx+300*math.cos(a),cy-30+300*math.sin(a))],fill=k(0.45),width=3)
g.line([(cx-330,cy+40),(cx+330,cy+40)],fill=(255,240,210),width=4)
for j,y in enumerate(range(cy+70,H,34)):
    pts=[(x,y+8*math.sin(x/40+j)) for x in range(cx-340,cx+341,8)]
    g.line(pts,fill=k(0.25+0.08*j),width=3)
bx,by=cx-150,cy+150
g.polygon([(bx-70,by),(bx+70,by),(bx+45,by+28),(bx-45,by+28)],outline=(255,245,230),width=4)
g.line([(bx,by),(bx,by-150)],fill=(255,245,230),width=4)
g.polygon([(bx+4,by-145),(bx+4,by-10),(bx+85,by-10)],outline=k(1),width=4)
g.polygon([(bx-4,by-120),(bx-4,by-10),(bx-60,by-10)],outline=k(0.8),width=4)
for ox,oy,sc in [(110,40,0.35),(200,10,0.25),(270,30,0.2)]:
    x0,y0=cx+ox-60,cy+90+oy
    g.line([(x0,y0),(x0,y0-int(120*sc))],fill=k(0.7),width=2)
    g.polygon([(x0+2,y0-int(115*sc)),(x0+2,y0),(x0+int(60*sc),y0)],outline=k(0.7),width=2)
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
