import os
from cursesmenu import *
from cursesmenu.items import *
menu = CursesMenu("Launcher")
menu_item =MenuItem("Main Menu")
command_item =CommandItem("create iso ","bash create_iso")
command_item2=CommandItem("install tools","bash install_tools")
command_item3 =CommandItem("unpack iso","bash unpack_iso")
command_item4=CommandItem("encrypt iso","bash encrypt_iso")
command_item5=CommandItem("decrypt iso ","bash decrypt_iso")
command_item6 =CommandItem("create iso ","bash")
command_item7=CommandItem("clean old file","bash clean_old_files")

menu.append_item(menu_item)
menu.append_item(command_item)
menu.append_item(command_item2)
menu.append_item(command_item3)
menu.append_item(command_item4)
menu.append_item(command_item5)
menu.append_item(command_item6)
menu.append_item(command_item7)
menu.show()