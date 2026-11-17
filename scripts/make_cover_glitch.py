# Cover for 09 Glitch in the System. Same base style as make_assets.py (dark grid, glow layer,
# left text panel, Oswald title, accent bar, playlist label, TECHNO CATALOG tag), but with a
# "glitch" variant: concentric squares, a square-wave line, displaced slices and RGB split.
# Writes only the 09 cover, so the 01-08 assets are untouched.
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import random
slug,title,pl,acc="09_glitch_in_the_system","Glitch in the System","High-Tech Minimal","#00E5FF"
F="/usr/share/fonts/truetype/sand-box/google/Oswald/Oswald-VariableFont_wght.ttf"
def font(sz,w=700):
    f=ImageFont.truetype(F,sz)
    try: f.set_variation_by_axes([w])
    except Exception: pass
    return f
c=tuple(int(acc[i:i+2],16) for i in (1,3,5))
W,H=1280,720; random.seed(slug)
img=Image.new("RGB",(W,H),(8,8,12)); d=ImageDraw.Draw(img)
for x in range(0,W,40): d.line([(x,0),(x,H)],fill=(18,18,26))
for y in range(0,H,40): d.line([(0,y),(W,y)],fill=(18,18,26))
glow=Image.new("RGB",(W,H),(0,0,0)); g=ImageDraw.Draw(glow)
cx,cy=930,330
for r in range(50,520,38):
    k=max(0.15,1-r/560)
    g.rectangle([cx-r,cy-r,cx+r,cy+r],outline=tuple(int(v*k) for v in c),width=3)
# square-wave (stepped) line instead of the sine waveform
pts=[]; x=0; y=600
while x<W:
    seg=random.choice([12,18,24,36,48])
    pts += [(x,y),(x+seg,y)]
    x+=seg; y=600+random.choice([-44,-28,-14,0,14,28,44])
g.line(pts,fill=c,width=3)
# click/bit blocks
for i in range(70):
    x=random.randint(0,W); h=random.choice([6,12,24,48,72])
    g.rectangle([x,690-h,x+random.choice([4,8,12]),690],fill=tuple(int(v*0.5) for v in c))
img=ImageChops.add(img,glow.filter(ImageFilter.GaussianBlur(10)))
img=ImageChops.add(img,glow.point(lambda v:int(v*0.7)))
# glitch: horizontal slice displacement on the art (right side)
for i in range(14):
    y0=random.randint(0,H-30); hh=random.randint(4,26); dx=random.randint(-70,70)
    band=img.crop((0,y0,W,y0+hh)); img.paste(band,(dx,y0))
# RGB channel split on the art
r_,g_,b_=img.split()
img=Image.merge("RGB",(ImageChops.offset(r_,6,0),g_,ImageChops.offset(b_,-6,0)))
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
# subtle cyan/red ghost behind the title for the glitch feel
d.text((115-4,240),title.upper(),font=f,fill=(0,90,110))
d.text((115+4,240),title.upper(),font=f,fill=(110,20,40))
d.text((115,240),title.upper(),font=f,fill=(245,245,250))
d.text((118,270+sz),pl.upper()+" TECHNO",font=font(42,400),fill=c)
d.text((W-260,40),"TECHNO CATALOG",font=font(28,400),fill=(120,120,135))
img.save(f"{slug}.cover.png"); print("ok",sz)
