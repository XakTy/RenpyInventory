init python:
    class Achievement(object):

        def __init__(self, Name, Description, Image):
            self.Name = Name
            self.Description = Description
            self.Image = Image
            self.Lock = True
        
        def Show(self):
            if(self.Lock == False):
                renpy.show_screen("scr_use", self)
            else:
                pass

        def Avatar(self):
            myImage = self.Image + ".png"
            if(renpy.loadable(myImage)):
                if(self.Lock):
                    return im.Grayscale(myImage)
                return myImage
            else:
                return "ss.jpg"

    Achievements = []
    Achievements.append(Achievement("Первый взлёт","Как-то её там начала свое первое прохождение","Fly"))

init:
    screen scr_achievements:
        modal True
        zorder 111
        frame:
            xmargin 0 ymargin 0
            xpadding 0 ypadding 0
            align (.0, .0)
            background "font" # фон инвентаря
            xmaximum 9999 xminimum 0
            vbox:
                button:
                    textbutton _("Закрыть") xpos 1700 ypos 30 action [Hide("scr_achievements"),Hide("scr_use")]
                viewport id "box":
                    mousewheel True
                    draggable True
                    pagekeys True
                    # заполняем ячейки
                    vbox:
                        for y in range(0, 3):
                            text "" #пробелы между иконками по вертикали
                            hbox:
                                for x in range(0, 5):
                                    text " " #пробелы между иконками по горизонтали
                                    # индекс ячейки
                                    $ i = x + y
                                    button:
                                        xpos 60
                                        text(" ")
                                        idle_background "icon.png" xmaximum 150 ymaximum 135
                                        hover_background "icon_hover.png"
                                        xmargin 0 ymargin 0
                                        xpadding 0 ypadding 0
                                        # кликабельны только очертания предмета, не пустота
                                        focus_mask True
                                        # размеры предмета
                                        if i < len(Achievements):
                                            add Achievements[i].Avatar() size(90,90) xpos 38 ypos 38 # картинка предмета
                                            action Function(Achievements[i].Show)
                                        else:
                                            add "icon.png" 