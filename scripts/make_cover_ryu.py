# Cover for 20 Ryu (Dragon): same base style (dark grid, Oswald title, accent bar, playlist label,
# TECHNO CATALOG tag), distinct motif: a water dragon spiralling up out of a still lake toward a full moon,
# ripples on the mirror lake and falling droplets. Writes only the 20 cover.
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import random, math
slug,title,label,acc="20_ryu","Ryū (Dragon)","JAPANESE TECHNO","#4FD1C5"
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
cx,cy=1010,380
w=(240,250,255)
# moon
mx,my=cx+120,cy-170
g.ellipse([mx-70,my-70,mx+70,my+70],outline=w,width=5)
for j in range(3): g.ellipse([mx-86-j*16,my-86-j*16,mx+86+j*16,my+86+j*16],outline=k(0.5-j*0.15),width=2)
# lake surface + ripples
ly=cy+220
g.line([(cx-420,ly),(cx+340,ly)],fill=k(0.7),width=3)
for j in range(4):
    rw=120+j*70; rh=14+j*6
    g.ellipse([cx-40-rw,ly-rh,cx-40+rw,ly+rh],outline=k(0.75-j*0.16),width=3)
# dragon body: a spiral rising from the water
pts=[]
for i in range(220):
    t=i/219
    ang=t*3.4*math.pi
    r=120*(1-t*0.55)
    x=cx-40+r*math.sin(ang)+t*40
    y=ly-t*420
    pts.append((x,y))
for j,wd in enumerate((26,14)):
    g.line(pts,fill=k(1.0) if j==0 else w,width=wd,joint="curve")
# scales/spines
for i in range(10,210,12):
    x,y=pts[i]; x2,y2=pts[i+2]
    a=math.atan2(y2-y,x2-x)-math.pi/2
    g.line([(x,y),(x+26*math.cos(a),y+26*math.sin(a))],fill=k(0.8),width=4)
# head
hx,hy=pts[-1]
g.polygon([(hx-10,hy+10),(hx+70,hy-20),(hx+40,hy+22)],outline=w,width=5)
g.ellipse([hx+30,hy-8,hx+40,hy+2],fill=k(1))
g.line([(hx+10,hy-6),(hx-20,hy-50)],fill=w,width=4)
g.line([(hx+20,hy-10),(hx+5,hy-60)],fill=w,width=4)
g.line([(hx+66,hy-14),(hx+120,hy-40)],fill=k(0.8),width=3)
g.line([(hx+60,hy+4),(hx+118,hy+20)],fill=k(0.8),width=3)
# droplets
for _ in range(40):
    x=random.randint(cx-300,cx+260); y=random.randint(cy-200,ly-10)
    r=random.choice((2,3,4)); g.ellipse([x-r,y-r,x+r,y+r],fill=k(random.uniform(0.4,1)))
img=ImageChops.add(img,glow.filter(ImageFilter.GaussianBlur(10)))
img=ImageChops.add(img,glow.point(lambda v:int(v*0.7)))
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
