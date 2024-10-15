


transform falldown:
    subpixel True
    on hide:
        easeout 0.25 yalign -20.0

define wipeleft_door = MultipleTransition([
    False, ImageDissolve("images/menu/wipeleft.png", 0.35, ramplen=64),
    Solid("#000"), Pause(0.141),
    Solid("#000"), ImageDissolve("images/menu/wipeleft.png", 0.35, ramplen=64),
    True])
transform floating:
    truecenter
    zoom 0.6
    block:
        ease 3 yoffset 25
        ease 3 yoffset -25
        repeat







transform tcommon(x=640, z=0.80):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.00 alpha 1.00

    on replace:
        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.00
        parallel:
            easein .15 yoffset 0 ypos 1.03

transform tinstant(x=640, z=0.80):
    xcenter x yoffset 0 zoom z*1.00 alpha 1.00 yanchor 1.0 ypos 1.03


transform focus(x=640, z=0.80):
    yanchor 1.0 ypos 1.03 subpixel True

    on show:
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.05 alpha 1.00
        yanchor 1.0 ypos 1.03
    on replace:
        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.05
        parallel:
            easein .15 yoffset 0

transform splashtext:
    rotate 336
    parallel:
        ease .4 xzoom 1.2
        ease .4 xzoom 1.0
        repeat


transform sink(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .5 ypos 1.06


transform hop(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .1 yoffset -20
    easeout .1 yoffset 0

transform hopfocus(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.05 alpha 1.00 subpixel True
    easein .1 yoffset -21
    easeout .1 yoffset 0


transform dip(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 yoffset 25
    easeout .25 yoffset 0


transform panic(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    parallel:
        ease 1.2 yoffset 25
        ease 1.2 yoffset 0
        repeat
    parallel:
        easein .3 xoffset 20
        ease .6 xoffset -20
        easeout .3 xoffset 0
        repeat


transform leftin(x=640, z=0.80):
    xcenter -300 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 xcenter x

transform rightin(x=640, z=0.80):
    xcenter 2000 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 xcenter x


transform thide(z=0.80):
    subpixel True
    transform_anchor True

    on hide:
        easein .25 zoom z*0.95 alpha 0.00 yoffset -20
transform lhide:
    subpixel True
    on hide:
        easeout .25 xcenter -300

transform rhide:
    subpixel True
    on hide:
        easeout .25 xcenter 2000


transform t41:
    tcommon(200)
transform t42:
    tcommon(493)
transform t43:
    tcommon(786)
transform t44:
    tcommon(1080)
transform t31:
    tcommon(240)
transform t32:
    tcommon(640)
transform t33:
    tcommon(1040)
transform t21:
    tcommon(400)
transform t22:
    tcommon(880)
transform t11:
    tcommon(640)


transform i41:
    tinstant(200)
transform i42:
    tinstant(493)
transform i43:
    tinstant(786)
transform i44:
    tinstant(1080)
transform i31:
    tinstant(240)
transform i32:
    tinstant(640)
transform i33:
    tinstant(1040)
transform i21:
    tinstant(400)
transform i22:
    tinstant(880)
transform i11:
    tinstant(640)


transform f41:
    focus(200)
transform f42:
    focus(493)
transform f43:
    focus(786)
transform f44:
    focus(1080)
transform f31:
    focus(240)
transform f32:
    focus(640)
transform f33:
    focus(1040)
transform f21:
    focus(400)
transform f22:
    focus(880)
transform f11:
    focus(640)


transform s41:
    sink(200)
transform s42:
    sink(493)
transform s43:
    sink(786)
transform s44:
    sink(1080)
transform s31:
    sink(240)
transform s32:
    sink(640)
transform s33:
    sink(1040)
transform s21:
    sink(400)
transform s22:
    sink(880)
transform s11:
    sink(640)


transform h41:
    hop(200)
transform h42:
    hop(493)
transform h43:
    hop(786)
transform h44:
    hop(1080)
transform h31:
    hop(240)
transform h32:
    hop(640)
transform h33:
    hop(1040)
transform h21:
    hop(400)
transform h22:
    hop(880)
transform h11:
    hop(640)


transform hf41:
    hopfocus(200)
transform hf42:
    hopfocus(493)
transform hf43:
    hopfocus(786)
transform hf44:
    hopfocus(1080)
transform hf31:
    hopfocus(240)
transform hf32:
    hopfocus(640)
transform hf33:
    hopfocus(1040)
transform hf21:
    hopfocus(400)
transform hf22:
    hopfocus(880)
transform hf11:
    hopfocus(640)


transform d41:
    dip(200)
transform d42:
    dip(493)
transform d43:
    dip(786)
transform d44:
    dip(1080)
transform d31:
    dip(240)
transform d32:
    dip(640)
transform d33:
    dip(1040)
transform d21:
    dip(400)
transform d22:
    dip(880)
transform d11:
    dip(640)


transform l41:
    leftin(200)
transform l42:
    leftin(493)
transform l43:
    leftin(786)
transform l44:
    leftin(1080)
transform l31:
    leftin(240)
transform l32:
    leftin(640)
transform l33:
    leftin(1040)
transform l21:
    leftin(400)
transform l22:
    leftin(880)
transform l11:
    leftin(640)


transform face(z=0.80, y=500):
    subpixel True
    xcenter 640
    yanchor 1.0 ypos 1.03
    yoffset y
    zoom z*2.00


transform cgfade:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.5 alpha 0.0


transform n_cg2_wiggle:
    subpixel True
    xoffset 0
    easein 0.15 xoffset 20
    easeout 0.15 xoffset 0
    easein 0.15 xoffset -15
    easeout 0.15 xoffset 0
    easein 0.15 xoffset 10
    easeout 0.15 xoffset 0
    easein 0.15 xoffset -5
    ease 0.15 xoffset 0

transform n_cg2_wiggle_loop:
    n_cg2_wiggle
    1.0
    repeat


transform n_cg2_zoom:
    subpixel True
    truecenter
    xoffset 0
    easeout 0.20 zoom 2.5 xoffset 200


define dissolve = Dissolve(0.25)


define dissolve_cg = Dissolve(0.75)
define dissolve_scene = Dissolve(1.0)


define dissolve_scene_full = MultipleTransition([
    False, Dissolve(1.0),
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])



define dissolve_scene_half = MultipleTransition([
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])


define close_eyes = MultipleTransition([
    False, Dissolve(0.5),
    Solid("#000"), Pause(0.25),
    True])


define open_eyes = MultipleTransition([
    False, Dissolve(0.5),
    True])


define trueblack = MultipleTransition([
    Solid("#000"), Pause(0.25),
    Solid("#000")
    ])


define wipeleft = ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64)


define wipeleft_scene = MultipleTransition([
    False, ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64),
    True])

define tpause = Pause(0.25)


image noise:
    truecenter
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    xzoom -1
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    yzoom -1
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    xzoom 1
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    yzoom 1
    repeat


transform noise_alpha:
    alpha 0.25


transform noisefade(t=0):
    alpha 0.0
    t
    linear 5.0 alpha 0.40


image vignette:
    truecenter
    "images/bg/vignette.png"


transform vignettefade(t=0):
    alpha 0.0
    t
    linear 25.0 alpha 1.00


transform vignetteflicker(t=0):
    alpha 0.0
    t + 2.030
    parallel:
        alpha 1.00
        linear 0.2 alpha 0.8
        0.1
        alpha 0.7
        linear 0.1 alpha 1.00
        alpha 0.0
        1.19
        repeat
    parallel:
        easeout 20 zoom 3.0

transform layerflicker(t=0):
    truecenter
    t + 2.030
    parallel:
        zoom 1.05
        linear 0.2 zoom 1.04
        0.1
        zoom 1.035
        linear 0.1 zoom 1.05
        zoom 1.0
        1.19
        repeat
    parallel:
        easeout_bounce 0.3 xalign 0.6
        easeout_bounce 0.3 xalign 0.4
        repeat


transform rewind:
    truecenter
    zoom 1.20
    parallel:
        easeout_bounce 0.2 xalign 0.55
        easeout_bounce 0.2 xalign 0.45
        repeat
    parallel:
        easeout_bounce 0.33 yalign 0.55
        easeout_bounce 0.33 yalign 0.45
        repeat


transform heartbeat:
    heartbeat2(1)

transform heartbeat2(m):
    truecenter
    parallel:
        0.144
        zoom 1.00 + 0.07 * m
        easein 0.250 zoom 1.00 + 0.04 * m
        easeout 0.269 zoom 1.00 + 0.07 * m
        zoom 1.00
        1.479
        repeat
    parallel:
        easeout_bounce 0.3 xalign 0.5 + 0.02 * m
        easeout_bounce 0.3 xalign 0.5 - 0.02 * m
        repeat


transform yuripupils_move:
    function yuripupils_function

init python:
    def yuripupils_function(trans, st, at):
        trans.xoffset = -1 + random.random() * 9 - 4
        trans.yoffset = 3 + random.random() * 6 - 3
        return random.random() * 1.2 + 0.3


transform malpha(a=1.00):
    i11
    alpha a




init python:
    renpy.register_shader("example.vhs_like", variables="""
    uniform sampler2D tex0;
    attribute vec2 a_tex_coord;
    varying vec2 v_tex_coord;
    uniform float u_time;
    """, vertex_300="""
        v_tex_coord = a_tex_coord;
    """, fragment_300="""
        const float range = 0.05;
        const float noiseQuality = 64.0;
        const float noiseIntensity = 0.003;
        const float offsetIntensity = 0.02;
        const float colorOffsetIntensity = 1.3;

        #define rand(co) fract(sin(dot(co.xy ,vec2(12.9898,78.233))) * 43758.5453)

        vec2 uv = v_tex_coord;

        for (float i = 0.0; i < 0.71; i += 0.1313)
        {
            float d = mod(u_time * i, 1.7);
            float o = sin(1.0 - tan(u_time * 0.24 * i));
            o *= offsetIntensity;
            float edge0 = (d - range);
            float edge1 = (d + range);

            float x = smoothstep(edge0, d, uv.y) * o;
            x -= smoothstep(d, edge1, uv.y) * o;

            uv.x += x;
        }

        float uvY = uv.y;
        uvY *= noiseQuality;
        uvY = float(int(uvY)) * (1.0 / noiseQuality);
        float noise = rand(vec2(u_time * 0.0001, uvY));
        uv.x += noise * noiseIntensity;

        vec2 offsetR = vec2(0.006 * sin(u_time), 0.0) * colorOffsetIntensity;
        vec2 offsetG = vec2(0.0073 * (cos(u_time * 0.97)), 0.0) * colorOffsetIntensity;

        float r = texture2D(tex0, uv + offsetR).r;
        float g = texture2D(tex0, uv + offsetG).g;
        float b = texture2D(tex0, uv).b;

        vec4 tex = vec4(r, g, b, texture2D(tex0, uv).a);
        gl_FragColor = tex;
    """)

transform test_shader:
    mesh True
    shader "example.vhs_like"









transform master_camera(x_1=640, y_1=360, z_1=1.0, x_2=640, y_2=600, z_2=2.0, t=1.0):
    subpixel True zoom z_1 xcenter x_1 ycenter y_1
    ease t zoom z_2 xcenter x_2 ypos y_2

transform night_filter:
    matrixcolor SaturationMatrix(0.8) * BrightnessMatrix(-0.1) * TintMatrix((115, 115, 165))


transform t(t=1, p=1):
    on show:
        subpixel True xanchor .5 yanchor .5
        zoom .65 alpha 0.0 xcenter math.ceil(((1280/t)*p) - (1280/(2*t))) ycenter 400
        easein .25 zoom .8 alpha 1.0 ycenter 360 rotate 0
    on replace:
        ease .25 zoom .8 alpha 1.0 xcenter math.ceil(((1280/t)*p) - (1280/(2*t))) ycenter 360 rotate 0
    on hide:
        easeout .25 zoom .65 alpha 0.0 ycenter 400

transform f(t=1, p=1):
    on show:
        subpixel True xanchor .5 yanchor .5
        zoom .65 alpha 0.0 xcenter math.ceil(((1280/t)*p) - (1280/(2*t))) ycenter 400
        easein .25 zoom .875 alpha 1.0 ycenter 360 rotate 0
    on replace:
        ease .25 zoom .875 alpha 1.0 xcenter math.ceil(((1280/t)*p) - (1280/(2*t))) ycenter 360 rotate 0
    on hide:
        easeout .25 zoom .65 alpha 0.0 ycenter 400

transform i(t=1, p=1):
    on show:
        subpixel True
        zoom .8 alpha 1.0 xcenter math.ceil(((1280/t)*p) - (1280/(2*t))) ycenter 360 rotate 0
    on replace:
        zoom .8 alpha 1.0 xcenter math.ceil(((1280/t)*p) - (1280/(2*t))) ycenter 360 rotate 0
    on hide:
        alpha 0.0

transform fi(t=1, p=1):
    on show:
        subpixel True
        zoom .875 alpha 1.0 xcenter math.ceil(((1280/t)*p) - (1280/(2*t))) ycenter 360 rotate 0
    on replace:
        zoom .875 alpha 1.0 xcenter math.ceil(((1280/t)*p) - (1280/(2*t))) ycenter 360 rotate 0
    on hide:
        alpha 0.0

transform h(t=1, p=1):
    on show:
        subpixel True xanchor .5 yanchor .5
        zoom .8 alpha 1.0 xcenter math.ceil(((1280/t)*p) - (1280/(2*t))) ycenter 360 rotate 0
        ease .125 yoffset -25
        ease .125 yoffset 0
    on replace:
        ease .125 yoffset -25 zoom .8 alpha 1.0 xcenter math.ceil(((1280/t)*p) - (1280/(2*t))) ycenter 360 rotate 0
        ease .125 yoffset 0
    on hide:
        easeout .25 zoom .65 alpha 0.0 ycenter 400

transform hf(t=1, p=1):
    on show:
        subpixel True xanchor .5 yanchor .5
        zoom .875 alpha 1.0 xcenter math.ceil(((1280/t)*p) - (1280/(2*t))) ycenter 360 rotate 0
        ease .125 yoffset -25
        ease .125 yoffset 0
    on replace:
        ease .125 yoffset -25 zoom .875 alpha 1.0 xcenter math.ceil(((1280/t)*p) - (1280/(2*t))) ycenter 360 rotate 0
        ease .125 yoffset 0
    on hide:
        easeout .25 zoom .65 alpha 0.0 ycenter 400

transform l(t=1, p=1):
    on show:
        subpixel True xanchor .5 yanchor .5
        zoom .8 alpha 1.0 xcenter -300 ycenter 360
        easein .25 xcenter math.ceil(((1280/t)*p) - (1280/(2*t))) rotate 0
    on replace:
        ease .25 zoom .8 alpha 1.0 xcenter math.ceil(((1280/t)*p) - (1280/(2*t))) ycenter 360 rotate 0
    on hide:
        easeout .25 xcenter -300

transform lf(t=1, p=1):
    on show:
        subpixel True xanchor .5 yanchor .5
        zoom .875 alpha 1.0 xcenter -300 ycenter 360
        easein .25 xcenter math.ceil(((1280/t)*p) - (1280/(2*t))) rotate 0
    on replace:
        ease .25 zoom .875 alpha 1.0 xcenter math.ceil(((1280/t)*p) - (1280/(2*t))) ycenter 360 rotate 0
    on hide:
        easeout .25 xcenter -300

transform r(t=1, p=1):
    on show:
        subpixel True xanchor .5 yanchor .5
        zoom .8 alpha 1.0 xcenter 1580 ycenter 360
        easein .25 xcenter math.ceil(((1280/t)*p) - (1280/(2*t))) rotate 0
    on replace:
        ease .25 zoom .8 alpha 1.0 xcenter math.ceil(((1280/t)*p) - (1280/(2*t))) ycenter 360 rotate 0
    on hide:
        easeout .25 xcenter 1580

transform rf(t=1, p=1):
    on show:
        subpixel True xanchor .5 yanchor .5
        zoom .875 alpha 1.0 xcenter 1580 ycenter 360
        easein .25 xcenter math.ceil(((1280/t)*p) - (1280/(2*t))) rotate 0
    on replace:
        ease .25 zoom .875 alpha 1.0 xcenter math.ceil(((1280/t)*p) - (1280/(2*t))) ycenter 360 rotate 0
    on hide:
        easeout .25 xcenter 1580

transform f_:
    ease .25 zoom .875

transform t_:
    ease .25 zoom .8

transform h_:
    ease .125 yoffset -25
    ease .125 yoffset 0

define dream = ImageDissolve("mod_assets/transitions/dream.png", 3.0, ramplen=64)

define tpause = Pause(0.25)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
