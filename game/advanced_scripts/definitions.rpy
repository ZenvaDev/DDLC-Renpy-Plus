init python:
    renpy.music.register_channel("ambient", "sfx", True)
    renpy.music.register_channel("ambient2", "sfx", True)
    renpy.music.register_channel("track1", "music", True)
    renpy.music.register_channel("track2", "music", True)

define config.gl2 = True
default persistent.finished = False
default persistent.cutseven = "7 - ???"
define audio.mbass = "mod_assets/madden_bass.ogg"
define audio.mbassb = "mod_assets/madden_bass_angry.ogg"
define audio.sting = "mod_assets/sting.ogg"
define audio.baby = "mod_assets/baby.mp3"
define audio.sizzle = "mod_assets/sizzle.ogg"
define audio.birds = "mod_assets/birds.ogg"
define audio.phones = "mod_assets/phones.mp3"
define audio.knock = "mod_assets/knock.ogg"
define audio.static = "mod_assets/static.ogg"
define audio.circus = "mod_assets/circus.mp3"
define audio.panning = "mod_assets/panning.ogg"
define close_eye = ImageDissolve("mod_assets/close_eye.png", 0.15, ramplen=64)
default persistent.delivery = False
default persistent.fe = False
image scan = "mod_assets/sayori/s_can.png"
image seyel = "mod_assets/sayori/s_can_l.png"
image seyer = "mod_assets/sayori/s_can_r.png"
image sayata1 = "mod_assets/sayori/sayata.png"
image sayata2 = "mod_assets/sayori/sayata2.png"
image blackzoom:
    "black"
    zoom 20
image whitezoom:
    "white"
    zoom 20
image nbaby = "mod_assets/nbaby.png"
image yt = "mod_assets/yt.png"
image preg = "mod_assets/preg.png"
image aspect = "mod_assets/fitsfetish.png"
image vhs:
    alpha .35
    "mod_assets/vhs/1.png"
    .0366666
    "mod_assets/vhs/2.png"
    .0366666
    "mod_assets/vhs/3.png"
    .0366666
    "mod_assets/vhs/4.png"
    .0366666
    "mod_assets/vhs/5.png"
    .0366666
    repeat
image sans = "mod_assets/sans.png"
image note:
    "mod_assets/note.png"
    zoom .2
image bump = "mod_assets/bump.png"
image baguette = "mod_assets/baguette.png"
image sroomz:
    "bg/sayori_bedroom.png"
    truecenter
    zoom 1.8
    xoffset 500
image sroom = "bg/sayori_bedroom.png"
image sroomf = "mod_assets/sroomf.png"
image sroom base = "bg/sayori_bedroom.png"
image bg sroomw = "mod_assets/sroomw.jpg"
image noose = "mod_assets/noose.png"
image pink = "#b59"
image lionking = "mod_assets/lk.png"
image sdrip = "mod_assets/sayori/sdrip.png"
image sroomn = "mod_assets/sroomn.png"
image mooncrawl = "mod_assets/mooncrawl.png"
image moon = "mod_assets/moon.png"
image windowcut = "mod_assets/windowcut.png"
image closetc = "mod_assets/bodies_closed.png"
image closeto = "mod_assets/monika_bodies.png"
image purple:
    "#c300ff"
image blue:
    "#2558ff"
image yellow:
    "#fbff00"
image green:
    "#06ac00"
image red:
    "#b30000"
image rainbow:
    zoom 7
    block:
        "red" with Dissolve(1, alpha=True)
        1
        "purple" with Dissolve(1, alpha=True)
        1
        "blue" with Dissolve(1, alpha=True)
        1
        "yellow" with Dissolve(1, alpha=True)
        1
        "green" with Dissolve(1, alpha=True)
        1
        repeat
transform peek_left:
    subpixel True xanchor 0.5 yanchor 0.5 ypos 350 xpos -100 zoom 0.8 alpha .9
    ease .25 rotate 50 xpos 100
    on hide:
        ease .25 rotate 0 xpos -100















transform shake:
    dizzy(1.5, 0.01)

transform anxiety:
    truecenter
    subpixel True
    zoom 1.2
    parallel:
        block:
            rotate 0
            ease 5 rotate 3
            time 1
            ease 5 rotate -3
            ease 5 rotate 0
            repeat
    parallel:
        block:
            dizzy(.8, 2.0)












image sayori 1a = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/ab.png")
image sayori 1b = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/bb.png")
image sayori 1c = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/cb.png")
image sayori 1d = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/db.png")
image sayori 1e = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/eb.png")
image sayori 1f = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/fb.png")
image sayori 1g = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/gb.png")
image sayori 1h = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/hb.png")
image sayori 1i = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/ib.png")
image sayori 1j = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/jb.png")
image sayori 1k = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/kb.png")
image sayori 1l = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/lb.png")
image sayori 1m = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/mb.png")
image sayori 1n = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/nb.png")
image sayori 1o = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/ob.png")
image sayori 1p = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/pb.png")
image sayori 1q = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/qb.png")
image sayori 1r = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/rb.png")
image sayori 1s = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/sb.png")
image sayori 1t = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/tb.png")
image sayori 1u = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/ub.png")
image sayori 1v = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/vb.png")
image sayori 1w = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/wb.png")
image sayori 1x = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/xb.png")
image sayori 1y = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/yb.png")

image sayori 2 = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/ab.png")
image sayori 2a = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/ab.png")
image sayori 2b = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/bb.png")
image sayori 2c = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/cb.png")
image sayori 2d = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/db.png")
image sayori 2e = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/eb.png")
image sayori 2f = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/fb.png")
image sayori 2g = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/gb.png")
image sayori 2h = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/hb.png")
image sayori 2i = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/ib.png")
image sayori 2j = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/jb.png")
image sayori 2k = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/kb.png")
image sayori 2l = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/lb.png")
image sayori 2m = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/mb.png")
image sayori 2n = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/nb.png")
image sayori 2o = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/ob.png")
image sayori 2p = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/pb.png")
image sayori 2q = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/qb.png")
image sayori 2r = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/rb.png")
image sayori 2s = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/sb.png")
image sayori 2t = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/tb.png")
image sayori 2u = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/ub.png")
image sayori 2v = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/vb.png")
image sayori 2w = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/wb.png")
image sayori 2x = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/xb.png")
image sayori 2y = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/yb.png")




image sayori 1ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 1bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 1bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 1bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 1be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 1bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 1bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 1bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 1bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 1bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 1bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 1bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 1bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 1bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 1bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 1bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 1bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 1br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 1bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 1bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 1bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 1bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 1bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 1bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 1by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 2ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 2bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 2bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 2bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 2be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 2bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 2bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 2bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 2bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 2bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 2bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 2bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 2bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 2bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 2bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 2bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 2bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 2br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 2bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 2bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 2bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 2bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 2bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 2bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 2by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

image sayori 3ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 3bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 3bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 3bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 3be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 3bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 3bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 3bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 3bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 3bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 3bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 3bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 3bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 3bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 3bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 3bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 3bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 3br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 3bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 3bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 3bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 3bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 3bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 3bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 3by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 4ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 4bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 4bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 4bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 4be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 4bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 4bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 4bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 4bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 4bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 4bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 4bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 4bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 4bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 4bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 4bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 4bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 4br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 4bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 4bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 4bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 4bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 4bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 4bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 4by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")










define persistent.demo = False
define persistent.steam = ("steamapps" in config.basedir.lower())

define config.developer = True

python early:
    import singleton
    me = singleton.SingleInstance()

init python:
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['hide_windows'].append('mouseup_3')
    config.keymap['self_voicing'] = []
    config.keymap['clipboard_voicing'] = []
    config.keymap['toggle_skip'] = []
    renpy.music.register_channel("music_poem", mixer="music", tight=True)


    def get_pos(channel='music'):
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0


    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)


    def delete_character(name):
        import os
        if renpy.android:
            try: os.remove(os.path.realpath("/sdcard/Android/data/"+package_name+"/characters/") + name + ".chr")
            except: pass
        else:
            try: os.remove(config.basedir + "/characters/" + name + ".chr")
            except: pass


    def restore_all_characters():
        if renpy.android:
            try: file(os.path.realpath("/sdcard/Android/data/"+package_name+"/characters/monika.chr"))
            except: open(os.path.realpath("/sdcard/Android/data/"+package_name+"/characters/monika.chr"), "wb").write(renpy.file("monika.chr").read())
            try: file(os.path.realpath("/sdcard/Android/data/"+package_name+"/characters/natsuki.chr"))
            except: open(os.path.realpath("/sdcard/Android/data/"+package_name+"/characters/natsuki.chr"), "wb").write(renpy.file("natsuki.chr").read())
            try: file(os.path.realpath("/sdcard/Android/data/"+package_name+"/characters/yuri.chr"))
            except: open(os.path.realpath("/sdcard/Android/data/"+package_name+"/characters/yuri.chr"), "wb").write(renpy.file("yuri.chr").read())
            try: file(os.path.realpath("/sdcard/Android/data/"+package_name+"/characters/sayori.chr"))
            except: open(os.path.realpath("/sdcard/Android/data/"+package_name+"/characters/sayori.chr"), "wb").write(renpy.file("sayori.chr").read())
        else:
            try: renpy.file("../characters/monika.chr")
            except: open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
            try: renpy.file("../characters/natsuki.chr")
            except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
            try: renpy.file("../characters/yuri.chr")
            except: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
            try: renpy.file("../characters/sayori.chr")
            except: open(config.basedir + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())


    def restore_relevant_characters():
        restore_all_characters()
        if persistent.playthrough == 1 or persistent.playthrough == 2:
            delete_character("sayori")
        elif persistent.playthrough == 3:
            delete_character("sayori")
            delete_character("natsuki")
            delete_character("yuri")
        elif persistent.playthrough == 4:
            delete_character("monika")


    def pause(time=None):
        
        if not time:
            
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            
            return
        if time <= 0: return
        
        renpy.pause(time)









define audio.t1 = "mod_assets/sweden_acoustic.ogg"
define audio.t2 = "<loop 4.499>bgm/2.ogg"
define audio.t2g = "bgm/2g.ogg"
define audio.t2g2 = "<from 4.499 loop 4.499>bgm/2.ogg"
define audio.t2g3 = "<loop 4.492>bgm/2g2.ogg"
define audio.t3 = "<loop 4.618>bgm/3.ogg"
define audio.t3g = "<to 15.255>bgm/3g.ogg"
define audio.t3g2 = "<from 15.255 loop 4.618>bgm/3.ogg"
define audio.t3g3 = "<loop 4.618>bgm/3g2.ogg"
define audio.t3m = "<loop 4.618>bgm/3.ogg"
define audio.t4 = "<loop 19.451>bgm/4.ogg"
define audio.t4g = "<loop 1.000>bgm/4g.ogg"
define audio.t5 = "<loop 4.444>bgm/5.ogg"

define audio.tmonika = "<loop 4.444>bgm/5_monika.ogg"
define audio.tsayori = "<loop 4.444>bgm/5_sayori.ogg"
define audio.tnatsuki = "<loop 4.444>bgm/5_natsuki.ogg"
define audio.tyuri = "<loop 4.444>bgm/5_yuri.ogg"

define audio.t5b = "<loop 4.444>bgm/5.ogg"
define audio.t5c = "<loop 4.444>bgm/5.ogg"
define audio.t6 = "<loop 10.893>bgm/6.ogg"
define audio.t6g = "<loop 10.893>bgm/6g.ogg"
define audio.t6r = "<to 39.817 loop 0>bgm/6r.ogg"
define audio.t6s = "<loop 43.572>bgm/6s.ogg"
define audio.t7 = "<loop 2.291>bgm/7.ogg"
define audio.t7a = "<loop 4.316 to 12.453>bgm/7.ogg"
define audio.t7g = "<loop 31.880>bgm/7g.ogg"
define audio.t8 = "<loop 9.938>bgm/8.ogg"
define audio.t9 = "<loop 3.172>bgm/9.ogg"
define audio.t9g = "<loop 1.532>bgm/9g.ogg"
define audio.t10 = "<loop 5.861>bgm/10.ogg"
define audio.t10y = "<loop 0>bgm/10-yuri.ogg"
define audio.td = "<loop 36.782>bgm/d.ogg"
define audio.shot = "mod_assets/shot.ogg"
define audio.m1 = "<loop 0>bgm/m1.ogg"
define audio.mend = "<loop 6.424>bgm/monika-end.ogg"

define audio.ghostmenu = "<loop 0>bgm/ghostmenu.ogg"
define audio.g1 = "<loop 0>bgm/g1.ogg"
define audio.g2 = "<loop 0>bgm/g2.ogg"
define audio.hb = "<loop 0>bgm/heartbeat.ogg"

define audio.opend = "sfx/closet-open.ogg"
define audio.closed = "sfx/closet-close.ogg"
define audio.page_turn = "sfx/pageflip.ogg"
define audio.fall = "sfx/fall.ogg"






image black = "#000000"
image dark = "#000000e4"
image darkred = "#110000c8"
image white = "#ffffff"
image splash = "bg/splash.png"
image end:
    truecenter
    "gui/end.png"
image bg residential_day = "bg/residential.png"
image bg class_day = "bg/class.png"
image bg corridor = "bg/corridor.png"
image bg club_day = "bg/club.png"
image bg club_day2:
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg/club-skill.png"
image bg closet = "bg/closet.png"
image bg bedroom = "bg/bedroom.png"
image bg sroom = "bg/sayori_bedroom.png"
image bg house = "bg/house.png"
image bg kitchen = "bg/kitchen.png"

image bg notebook = "bg/notebook.png"
image bg notebook-glitch = "bg/notebook-glitch.png"

image bg glitch = LiveTile("bg/glitch.jpg")

image glitch_color:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.7
        linear 0.45 alpha 0



image glitch_color2:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.7
        linear 0.45 alpha 0


image natsuki mouth = LiveComposite((960, 960), (0, 0), "natsuki/0.png", (390, 340), "n_rects_mouth", (480, 334), "n_rects_mouth")

image n_rects_mouth:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    size (20, 25)

image n_moving_mouth:
    "images/natsuki/mouth.png"
    pos (615, 305)
    xanchor 0.5 yanchor 0.5
    parallel:
        choice:
            ease 0.10 yzoom 0.2
        choice:
            ease 0.05 yzoom 0.2
        choice:
            ease 0.075 yzoom 0.2
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        pass
        choice:
            ease 0.10 yzoom 1
        choice:
            ease 0.05 yzoom 1
        choice:
            ease 0.075 yzoom 1
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        repeat
    parallel:
        choice:
            0.2
        choice:
            0.4
        choice:
            0.6
        ease 0.2 xzoom 0.4
        ease 0.2 xzoom 0.8
        repeat

image natsuki_ghost_blood:
    "#00000000"
    "natsuki/ghost_blood.png" with ImageDissolve("images/menu/wipedown.png", 80.0, ramplen=4, alpha=True)
    pos (620,320) zoom 0.80

image natsuki ghost_base:
    "natsuki/ghost1.png"
image natsuki ghost1:
    "natsuki 11"
    "natsuki ghost_base" with Dissolve(20.0, alpha=True)
image natsuki ghost2 = Image("natsuki/ghost2.png")
image natsuki ghost3 = Image("natsuki/ghost3.png")
image natsuki ghost4:
    "natsuki ghost3"
    parallel:
        easeout 0.25 zoom 4.5 yoffset 1200
    parallel:
        ease 0.025 xoffset -20
        ease 0.025 xoffset 20
        repeat
    0.25
    "black"
image natsuki glitch1:
    "natsuki/glitch1.png"
    zoom 1.25
    block:
        yoffset 300 xoffset 100 ytile 2
        linear 0.15 yoffset 200
        repeat
    time 0.75
    yoffset 0 zoom 1 xoffset 0 ytile 1
    "natsuki 4e"

image natsuki scream = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/scream.png")
image natsuki vomit = "natsuki/vomit.png"

image n_blackeyes = "images/natsuki/blackeyes.png"
image n_eye = "images/natsuki/eye.png"





image y_glitch_head:
    "images/yuri/za.png"
    0.15
    "images/yuri/zb.png"
    0.15
    "images/yuri/zc.png"
    0.15
    "images/yuri/zd.png"
    0.15
    repeat

image yuri stab_1 = "yuri/stab/1.png"
image yuri stab_2 = "yuri/stab/2.png"
image yuri stab_3 = "yuri/stab/3.png"
image yuri stab_4 = "yuri/stab/4.png"
image yuri stab_5 = "yuri/stab/5.png"
image yuri stab_6 = LiveComposite((960,960), (0, 0), "yuri/stab/6-mask.png", (0, 0), "yuri stab_6_eyes", (0, 0), "yuri/stab/6.png")

image yuri stab_6_eyes:
    "yuri/stab/6-eyes.png"
    subpixel True
    parallel:
        choice:
            xoffset 0.5
        choice:
            xoffset 0
        choice:
            xoffset -0.5
        0.2
        repeat
    parallel:
        choice:
            yoffset 0.5
        choice:
            yoffset 0
        choice:
            yoffset -0.5
        0.2
        repeat
    parallel:
        2.05
        easeout 1.0 yoffset -15
        linear 10 yoffset -15


image yuri oneeye = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/oneeye.png", (0, 0), "yuri oneeye2")
image yuri oneeye2:
    "yuri/oneeye2.png"
    subpixel True
    pause 5.0
    linear 60 xoffset -50 yoffset 20

image yuri glitch:
    "yuri/glitch1.png"
    pause 0.1
    "yuri/glitch2.png"
    pause 0.1
    "yuri/glitch3.png"
    pause 0.1
    "yuri/glitch4.png"
    pause 0.1
    "yuri/glitch5.png"
    pause 0.1
    repeat
image yuri glitch2:
    "yuri/0a.png"
    pause 0.1
    "yuri/0b.png"
    pause 0.5
    "yuri/0a.png"
    pause 0.3
    "yuri/0b.png"
    pause 0.3
    "yuri 1"

image yuri eyes = LiveComposite((1280, 720), (0, 0), "yuri/eyes1.png", (0, 0), "yuripupils")

image yuri eyes_base = "yuri/eyes1.png"

image yuripupils:
    "yuri/eyes2.png"
    yuripupils_move

image yuri cuts = "yuri/cuts.png"

image yuri dragon:
    "yuri 3"
    0.25
    parallel:
        "yuri/dragon1.png"
        0.01
        "yuri/dragon2.png"
        0.01
        repeat
    parallel:
        0.01
        choice:
            xoffset -1
            xoffset -2
            xoffset -5
            xoffset -6
            xoffset -9
            xoffset -10
        0.01
        xoffset 0
        repeat
    time 0.55
    xoffset 0
    "yuri 3"



image monika g1:
    "monika/g1.png"
    xoffset 35 yoffset 55
    parallel:
        zoom 1.00
        linear 0.10 zoom 1.03
        repeat
    parallel:
        xoffset 35
        0.20
        xoffset 0
        0.05
        xoffset -10
        0.05
        xoffset 0
        0.05
        xoffset -80
        0.05
        repeat
    time 1.25
    xoffset 0 yoffset 0 zoom 1.00
    "monika 3"

image monika g2:
    block:
        choice:
            "monika/g2.png"
        choice:
            "monika/g3.png"
        choice:
            "monika/g4.png"
    block:
        choice:
            pause 0.05
        choice:
            pause 0.1
        choice:
            pause 0.15
        choice:
            pause 0.2
    repeat








define narrator = Character(ctc="ctc", ctc_position="fixed")
define mc = DynamicCharacter('player', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define s = DynamicCharacter('s_name', image='sayori', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define m = DynamicCharacter('m_name', image='monika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define n = DynamicCharacter('n_name', image='natsuki', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define y = DynamicCharacter('y_name', image='yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define ny = Character('Nat & Yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define mcn = DynamicCharacter('mcnname', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define a = DynamicCharacter('a_name', image ='ava', what_prefix='"{font=mod_assets/wingding.ttf}', what_suffix='{/font}"', ctc="ctc", ctc_position="fixed")
image ava ngelion = "mod_assets/ava.png"
default _dismiss_pause = True
default a_name = "{font=mod_assets/wingding.ttf}Ava"
default mcnname = "[player]&Natsuki"
define ss = Character("Sayori", what_prefix="''", what_suffix="''", what_text_align=1.0)







default persistent.playername = ""
default player = persistent.playername
default persistent.playthrough = 0
default persistent.yuri_kill = 0
default persistent.seen_eyes = None
default persistent.seen_sticker = None
default persistent.ghost_menu = None
default persistent.seen_ghost_menu = None
default seen_eyes_this_chapter = False
default persistent.anticheat = 0
default persistent.clear = [False, False, False, False, False, False, False, False, False, False]
default persistent.special_poems = None
default persistent.clearall = None
default persistent.menu_bg_m = None
default persistent.first_load = None
default persistent.first_poem = None
default persistent.seen_colors_poem = None
default persistent.monika_back = None


default in_sayori_kill = None
default in_yuri_kill = None
default anticheat = 0
define config.mouse = None
default allow_skipping = True
default basedir = config.basedir
default chapter = 0
default currentpos = 0
default faint_effect = None




default s_name = "Sayori"
default m_name = "Monika"
default n_name = "Natsuki"
default y_name = "Yuri"






default n_poemappeal = [0, 0, 0]
default s_poemappeal = [0, 0, 0]
default y_poemappeal = [0, 0, 0]
default m_poemappeal = [0, 0, 0]


default poemwinner = ['sayori', 'sayori', 'sayori']


default s_readpoem = False
default n_readpoem = False
default y_readpoem = False
default m_readpoem = False


default poemsread = 0



default n_appeal = 0
default s_appeal = 0
default y_appeal = 0
default m_appeal = 0


default n_exclusivewatched = False
default y_exclusivewatched = False


default y_gave = False
default y_ranaway = False


default n_read3 = False
default y_read3 = False


default ch1_choice = "sayori"

default n_poemearly = False


default help_sayori = None
default help_monika = None


default ch4_scene = "yuri"
default ch4_name = "Yuri"


default sayori_confess = True


default natsuki_23 = None




image blank_sprite:
    "images/sayori/a.png"
    alpha 0.0


image bathroom = "mod_assets/bg/bathroom.png"
image green_screen = "#00b140"
image sayori_bedroom_night = "mod_assets/bg/sayori_bedroom_night.png"
image detroit = "mod_assets/bg/detroit.png"
image sayori_bedroom_jojo = "mod_assets/bg/sayori_bedroom_jojo.png"
image sayori_bedroom_finale = "mod_assets/bg/sayori_bedroom_finale.png"


image cg_pipe = "mod_assets/cg/pipecg.png"
image cg_bath = "mod_assets/cg/bathtub_yuri.png"
image cg_moni = "mod_assets/cg/monikill.png"
image cg_ball = "mod_assets/cg/fear_him_adore_him.png"
image cg_ging = "mod_assets/cg/ginger.png"
image cg_bodc = "mod_assets/cg/bodies_closed.png"
image cg_bodo = "mod_assets/cg/bodies_open.png"
image cg_dol1 = "mod_assets/cg/doll.png"
image cg_dol2 = "mod_assets/cg/no_doll.png"
image cg_dol3 = "mod_assets/cg/big_doll.png"
image cg_dol4 = "mod_assets/cg/scare_doll.png"


define audio.d_rev = "<loop 0.0>mod_assets/bgm/d_rev.ogg"
define audio.lobby_time = "<loop 0.0>mod_assets/bgm/lobby_time.ogg"
define audio.heavy_rain = "<loop 4.500>mod_assets/bgm/heavy_rain.ogg"
define audio.nfl = "<loop 4.500>mod_assets/bgm/nfl_cbs_earrape_whydididothistomyself.ogg"
define audio.vibrator = "<loop 4.500>mod_assets/bgm/vibrator.ogg"
define audio.birds = "<loop 0.0>mod_assets/bgm/birds.ogg"
define audio.t_doll = "<loop 0.0>mod_assets/bgm/doll.ogg"
define audio.film_static = "<loop 0.0>mod_assets/bgm/film_static.ogg"
define audio.pilar_men = "<loop 3.818>mod_assets/bgm/pilar_men.ogg"


define audio.door_slam = "mod_assets/sfx/door_slam.ogg"
define audio.laugh_1 = "mod_assets/sfx/laugh_1.ogg"
define audio.laugh_2 = "mod_assets/sfx/laugh_2.ogg"
define audio.laugh_3 = "mod_assets/sfx/laugh_3.ogg"
define audio.dream_in = "mod_assets/sfx/dream_in.ogg"
define audio.dream_out = "mod_assets/sfx/dream_out.ogg"
define audio.flare = "mod_assets/sfx/flare.ogg"
define audio.glitch_scream = "mod_assets/sfx/glitch_scream.ogg"


image ad_1 = "mod_assets/vfx/ad_1.png"
image ad_2 = "mod_assets/vfx/ad_2.png"
image ad_3 = "mod_assets/vfx/ad_3.png"
image rain_1:
    alpha 0.0 zoom .8
    "mod_assets/vfx/rain.png"
    parallel:
        linear .3 xcenter 620 ycenter 460
        xcenter 660 ycenter 260
        repeat
    parallel:
        easein .05 alpha .4
        .2
        easeout .05 alpha 0.0
        repeat
image rain_2:
    alpha 0.0 zoom .8
    .1
    xoffset 200
    "mod_assets/vfx/rain.png"
    parallel:
        linear .3 xcenter 620 ycenter 460
        xcenter 660 ycenter 260
        repeat
    parallel:
        easein .05 alpha .4
        .2
        easeout .05 alpha 0.0
        repeat
image rain_3:
    alpha 0.0 zoom .8
    .2
    xoffset -200
    "mod_assets/vfx/rain.png"
    parallel:
        linear .3 xcenter 620 ycenter 460
        xcenter 660 ycenter 260
        repeat
    parallel:
        easein .05 alpha .4
        .2
        easeout .05 alpha 0.0
        repeat
image doll_static:
    "mod_assets/vfx/doll_noise_1.png"
    0.02
    "mod_assets/vfx/doll_noise_2.png"
    0.02
    "mod_assets/vfx/doll_noise_3.png"
    0.02
    repeat
image menacing = "mod_assets/vfx/menacing.png"
image mod_end = "mod_assets/vfx/end.png"


image ropu_kun = "mod_assets/props/noose.png"
image chair = "mod_assets/props/chair.png"
image skill = "mod_assets/props/s_kill.png"
image chair_kill = "mod_assets/props/chair_kill.png"


image ski_natsuki = "mod_assets/sprites/ski_natsuki.png"
image ski_yuri = "mod_assets/sprites/ski_yuri.png"
image jojoyori cm = "mod_assets/sprites/jojo_sayori_cm.png"
image jojoyori cms = "mod_assets/sprites/jojo_sayori_cms.png"
image jojoyori om = "mod_assets/sprites/jojo_sayori_om.png"
image jojoyori oms = "mod_assets/sprites/jojo_sayori_oms.png"


define audio.closet_open = "sfx/closet-open.ogg"
define audio.closet_close = "sfx/closet-close.ogg"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
