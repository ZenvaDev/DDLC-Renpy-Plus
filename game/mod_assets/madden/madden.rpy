layeredimage madden:
    at Flatten 
    always "mod_assets/madden/base.png"

    group body:
        attribute based default null
        attribute gun:
            "mod_assets/madden/base2.png"

    group head:
        attribute happ default:
            "mod_assets/madden/1.png"
        attribute mad:
            "mod_assets/madden/2.png"
        attribute ultimate default:
            "mod_assets/madden/3.png"
    group eyes:
        attribute e1 default null
        attribute e2:
            "mod_assets/madden/a.png"
        attribute e3 default:
            "mod_assets/madden/b.png"

define jm = DynamicCharacter('j_name', image='madden', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
default j_name = "???"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
