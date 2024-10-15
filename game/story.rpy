label story:

    play music pilar_men
    window hide

    show menacing as m11 zorder 10:
        xcenter 1580 ycenter 200 zoom .4
        parallel:
            ease .3 xzoom 0.9
            ease .3 xzoom 1.0
            repeat
        parallel:
            ease .2 yzoom 0.8
            ease .2 yzoom 1.0
            repeat
        parallel:
            linear 5.0 xcenter -300
            xcenter 1580
            repeat
        parallel:
            ease .5 rotate 5
            ease .5 rotate -5
            repeat
        parallel:
            ease .4 yoffset -30
            ease .4 yoffset 0
            ease .4 yoffset 30
            ease .4 yoffset 0
            repeat
    pause .5
    show menacing as m12 zorder 10:
        xcenter 1580 ycenter 200 zoom .4
        parallel:
            ease .3 xzoom 0.9
            ease .3 xzoom 1.0
            repeat
        parallel:
            ease .2 yzoom 0.8
            ease .2 yzoom 1.0
            repeat
        parallel:
            linear 5.0 xcenter -300
            xcenter 1580
            repeat
        parallel:
            ease .5 rotate 5
            ease .5 rotate -5
            repeat
        parallel:
            ease .4 yoffset -30
            ease .4 yoffset 0
            ease .4 yoffset 30
            ease .4 yoffset 0
            repeat
    pause .5
    show menacing as m13 zorder 10:
        xcenter 1580 ycenter 200 zoom .4
        parallel:
            ease .3 xzoom 0.9
            ease .3 xzoom 1.0
            repeat
        parallel:
            ease .2 yzoom 0.8
            ease .2 yzoom 1.0
            repeat
        parallel:
            linear 5.0 xcenter -300
            xcenter 1580
            repeat
        parallel:
            ease .5 rotate 5
            ease .5 rotate -5
            repeat
        parallel:
            ease .4 yoffset -30
            ease .4 yoffset 0
            ease .4 yoffset 30
            ease .4 yoffset 0
            repeat
    pause .5
    show menacing as m14 zorder 10:
        xcenter 1580 ycenter 200 zoom .4
        parallel:
            ease .3 xzoom 0.9
            ease .3 xzoom 1.0
            repeat
        parallel:
            ease .2 yzoom 0.8
            ease .2 yzoom 1.0
            repeat
        parallel:
            linear 5.0 xcenter -300
            xcenter 1580
            repeat
        parallel:
            ease .5 rotate 5
            ease .5 rotate -5
            repeat
        parallel:
            ease .4 yoffset -30
            ease .4 yoffset 0
            ease .4 yoffset 30
            ease .4 yoffset 0
            repeat
    pause .5
    show menacing as m15 zorder 10:
        xcenter 1580 ycenter 200 zoom .4
        parallel:
            ease .3 xzoom 0.9
            ease .3 xzoom 1.0
            repeat
        parallel:
            ease .2 yzoom 0.8
            ease .2 yzoom 1.0
            repeat
        parallel:
            linear 5.0 xcenter -300
            xcenter 1580
            repeat
        parallel:
            ease .5 rotate 5
            ease .5 rotate -5
            repeat
        parallel:
            ease .4 yoffset -30
            ease .4 yoffset 0
            ease .4 yoffset 30
            ease .4 yoffset 0
            repeat
    pause 2.0

    show sayori_bedroom_jojo
    show jojoyori om zorder 20 at fi(1, 1):
    with wipeleft_door
    s "Oh? You're approaching me? I thought you'd abandon me."
    show jojoyori cm at t_
    mc "I can't hang the shit out of you unless I come closer."
    show jojoyori om at f_
    s "Oh really?"
    s "Then come as close as you like."
    show jojoyori at t_
    show layer master:
        truecenter
        parallel:
            zoom 2.0 yoffset -350
            pause 1.0
            ease .5 yoffset 150 zoom 1.5
            pause 1.0
            ease .5 yoffset 0 zoom 1.0
        parallel:
            pause 1.4
            easein .25 matrixcolor HueMatrix(90) * BrightnessMatrix(0.5)
            easeout 1.0 matrixcolor HueMatrix(0) * BrightnessMatrix(0.0)


    pause 1.0
    $ renpy.music.set_volume(0.5, 0.25, "music")
    play sound flare
    show jojoyori cms
    $ renpy.music.set_volume(1.0, 0.25, "music")
    pause 1.5
    mc "SAYORI!"
    show jojoyori oms at f_
    s "[player!u]!"
    show jojoyori cms at t_
    show layer master:
        truecenter
        easeout 5.0 zoom 2.0 yoffset 300
    mc "SAYOOORIII!!"
    show jojoyori oms at f_
    s "{cps=*.3}URRRRRRYYYYYYYYYYYYYYYY!!!!{nw}"
    window hide(None)
    window auto
    play music td
    hide jojoyori
    hide m11
    hide m12
    hide m13
    hide m14
    hide m15
    show layer master
    show s_kill_bg2
    show s_kill2
    show s_kill_bg as s_kill_bg at s_kill_bg_start
    show s_kill as s_kill at s_kill_start
    pause 2.0
    mc "Ah, crap."

    stop music
    scene black
    play sound closet_close
    with wipeleft_door

    show black
    mc ""