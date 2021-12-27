
    screen panel:
        zorder 110
        hbox:
            imagebutton auto "inv_%s.png" action Show('scr_inventory')
            imagebutton auto "acv_%s.png" action Show('scr_achievements')

    label start:
        scene bg
        #panel кнопок
        show screen panel
        with dissolve

        "Можно кликнуть по хреновинам в инвентаре."
        $ Achievements[0].Lock = False
        "Ачивка Получена"
        return
