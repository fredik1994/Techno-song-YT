from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random, math
songs = [
 ("01_quantum_fox","Quantum Fox","High-Tech Minimal","#00E5FF","#hightechminimal","#minimaltechno",
  "A playful, glitchy minimal track about standing at a fork in reality and picking the braver path. Clicky micro-percussion, a rubbery offbeat bass and a half-whispered female vocal chase each other through two drops."),
 ("02_northern_compass","Northern Compass","Melodic Techno","#7FB2FF","#melodictechno","#deeptechno",
  "Spin me around, blindfold me twice - the needle still finds the north. An icy, cinematic melodic techno journey about the compass that always points to the exit: come and pass."),
 ("03_thunder_call","Thunder Call","Peak-Time Techno","#FF3B3B","#peaktimetechno","#warehousetechno",
  "A storm-warning for the sleeping city. Rumbling kicks, thunder toms and a commanding female chant build from ominous calm into full main-stage energy: wake up."),
 ("04_ronin","Ronin (No Master)","Japanese Techno","#FF2E63","#japanesetechno","#samurai",
  "No lord, no banner - only the road and the sword he chose to carry. Taiko drums, shakuhachi and a stoic chanted vocal tell the story of a ronin who walks free."),
 ("05_puppet_masters","Puppet Masters","Dark Techno","#B026FF","#darktechno","#hypnotictechno",
  "Feel that tug at your wrist? That's not you. Hypnotic dark techno with creaking strings and a menacing whisper - until the puppet looks up, sees the strings, and cuts them."),
 ("06_phoenix_protocol","Phoenix Protocol","Euphoric Techno","#FF8C1A","#euphorictechno","#festivaltechno",
  "Let the name, the job and the mask burn to grey - then rise. A soaring euphoric techno anthem about letting go and being reborn from the ashes."),
 ("07_land_of_fire","Land of Fire","Ethnic Techno","#FFC233","#ethnictechno","#middleeasterntechno",
  "Fire in the dark, fire in the blood - nobody gave it, nobody can take it. Tar and kamancha melodies, frame drums and a deep mugham-style vocal meet a hypnotic driving kick."),
 ("08_shamans_drum","Shaman's Drum","Afro Techno","#2EE59D","#afrotechno","#afrohouse",
  "Sit in the circle, close your eyes - the drum is talking. Djembe, talking drum and kalimba weave a ritual, trance-inducing groove with call-and-response chants."),
]
F="/usr/share/fonts/truetype/sand-box/google/Oswald/Oswald-VariableFont_wght.ttf"
def font(sz, w=700):
    f=ImageFont.truetype(F, sz)
    try: f.set_variation_by_axes([w])
    except Exception: pass
    return f
def hexrgb(h): return tuple(int(h[i:i+2],16) for i in (1,3,5))
for slug,title,pl,acc,t1,t2,desc in songs:
    W,H=1280,720; c=hexrgb(acc); random.seed(slug)
    img=Image.new("RGB",(W,H),(8,8,12)); d=ImageDraw.Draw(img)
    # grid
    for x in range(0,W,40): d.line([(x,0),(x,H)],fill=(18,18,26))
    for y in range(0,H,40): d.line([(0,y),(W,y)],fill=(18,18,26))
    # glow layer: concentric rings + waveform
    glow=Image.new("RGB",(W,H),(0,0,0)); g=ImageDraw.Draw(glow)
    cx,cy=930,330
    for r in range(60,520,38):
        g.ellipse([cx-r,cy-r,cx+r,cy+r],outline=tuple(int(v*max(0.15,1-r/560)) for v in c),width=3)
    pts=[]
    for x in range(0,W,6):
        a=40*math.sin(x/37.0+random.random()*0.3)*math.sin(x/211.0)+random.uniform(-14,14)
        pts.append((x,600+a))
    g.line(pts,fill=c,width=3)
    for i in range(70):
        x=random.randint(0,W); h=random.randint(4,90)
        g.rectangle([x,690-h,x+4,690],fill=tuple(int(v*0.5) for v in c))
    img=Image.composite(img,img,Image.new("L",(W,H),255))
    blurred=glow.filter(ImageFilter.GaussianBlur(10))
    from PIL import ImageChops
    img=ImageChops.add(img,blurred); img=ImageChops.add(img,glow.point(lambda v:int(v*0.7)))
    # dark left panel for text
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
    d.text((118,270+sz),pl.upper()+" TECHNO" if not pl.endswith("Techno") else pl.upper(),font=font(42,400),fill=c)
    d.text((W-260,40),"TECHNO CATALOG",font=font(28,400),fill=(120,120,135))
    img.save(f"{slug}.cover.png")
    ttl=f"{title} | {pl if pl.endswith('Techno') else pl+' Techno'}"
    open(f"{slug}.title.txt","w").write(ttl+"\n")
    tag="#"+pl.replace("-","").replace(" ","").lower()
    tags=" ".join(dict.fromkeys(["#techno",t1,t2,"#sunoai","#aimusic"]))
    open(f"{slug}.desc.txt","w").write(f"{title} - {pl if pl.endswith('Techno') else pl+' Techno'}\n\n{desc}\n\nMade with Suno AI.\n\n{tags}\n")
print("ok")
