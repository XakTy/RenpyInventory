init python:

    class Inventory(object):

        def __init__(self):
            self.items = []
            self.SizeInventory = 10
        
        def AddItem(self, item):
            if(len(self.items) < self.SizeInventory):
                self.items.append(item)

        def RemoveItem(self, item):
            self.items.remove(item)

    inventory = Inventory()

    class Item(object):
        def __init__(self, Name = "None1", Description = "None2", Image = "pot12"):
            self.Name = Name
            self.Description = Description
            self.Image = Image
        
        def Show(self):
            renpy.show_screen("scr_use", self)

        def Use(self):
            inventory.RemoveItem(self)

        def Avatar(self):
            myImage = self.Image + ".png"
            if(renpy.loadable(myImage)):
                return myImage
            else:
                return "ss.jpg"

    class ClickItem(Item):
        def Use(self):
            print("Hellow")
        

    inventory.AddItem(ClickItem("Зелье","Особенное зелье","pot9"))
    inventory.AddItem(Item("Ручка","Особенная ручка","sss"))
    inventory.AddItem(Item("Ручка","Не оч особенная","pot11"))
    inventory.AddItem(Item("Ручка","Средняя","pot10"))


init:
# сам экран инвентаря
    screen scr_inventory:
        zorder 111
        modal True
        frame:
            xmargin 0 ymargin 0
            xpadding 0 ypadding 0
            align (.0, .0)
            background "font" # фон инвентаря
            xmaximum 9999 xminimum -9999
            vbox:
                button:
                    textbutton _("Закрыть") xpos 1700 ypos 30 action [Hide("scr_inventory"),Hide("scr_use")]
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
                                    $ i = x + y * 5
                                    # если не за грницами списка предметов
                                    # if i < len(inventory.items):
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
                                        minimum (15, 15)
                                        maximum (30, 30)
                                        if i < len(inventory.items):
                                            add inventory.items[i].Avatar() size(90,90) xpos 38 ypos 38 # картинка предмета
                                            action Function(inventory.items[i].Show) # Это ждет нажатия
                                        else:
                                            add "icon.png" 
    screen scr_use(item):
        zorder 112
        frame:
            background "font2"
            xpos 1000 ypos 79
            xminimum 0
            has vbox:
                xalign .5
            text " "
            add item.Avatar() xpos 300 size (420,420)
            text item.Name xpos -20 ypos 135 size 55 xsize 200 ysize 200
            text item.Description xpos -20 ypos 145 xsize 600 ysize 400
            text " "
            if(type(item) is Item):
                hbox:
                    xminimum 500
                    textbutton _("Применить") xpos 650 ypos 250  action [item.Use, [Hide("scr_use")]]
                text " "