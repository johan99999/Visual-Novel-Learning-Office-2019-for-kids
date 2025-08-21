# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Ewing")
define pov = Character("[povname]")



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg first

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show ewing normal

    # These display lines of dialogue.

    e "Halo."
    e "Kenalin, aku Ewing."
    python:
        povname = renpy.input("Nama kamu siapa?", length=32)
        povname = povname.strip()

        if not povname:
            povname = "Tanpa Nama"
    e "[povname], senang mengenalmu!"
    e "oh iya, [povname], apa kamu tahu kita mau ngapain?"
    menu:
        "Belajar Microsoft Office":
            scene bg introduction
            show ewing normal
            e "Benar sekali!, Kita akan belajar aplikasi Microsoft Office, mulai dari Word untuk mengolah teks, Powerpoint untuk membuat presentasi, dan juga Excel untuk mengolah data!"
        "Nggak tahu":
            scene bg introduction
            show ewing normal
            e "Jadi begini, Kita akan belajar aplikasi Microsoft Office, mulai dari Word untuk mengolah teks, Powerpoint untuk membuat presentasi, dan juga Excel untuk mengolah data!"
            scene bg hint1
            show ewing normal
    e "oke, sebelum kita mulai, pastikan dulu kamu udah buka aplikasinya yah, agar kamu bisa langsung mencoba, agar tidak bingung, gunakan kombinasi di keyboard alt + tab, agar bisa berpindah antar aplikasi ya!"
    scene bg first
    show ewing normal
    e "Nah, kamu mau belajar apa dulu nih?"
    menu :
        "Microsoft Word":
            #jump word
            return
        "Microsoft Powerpoint":
            #jump ppt
            return
        "Microsoft Excel":
            #jump excel
            return



    # This ends the game.

    return
