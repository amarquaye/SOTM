from random import choice

import flet as ft


def main(page: ft.Page):
    #Page settings
    page.title = "SOTM"
    page.theme_mode = "dark"
    page.bgcolor = "#daa520"
    #initial bgcolor === #ffd700
    page.padding = 30
    page.auto_scroll = True
    #page.scroll = "HIDDEN"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.fonts = {
        "DaddyTimeMono" : "fonts/DaddyTimeMono.ttf"
    }

    #Data Set for scriptures
    gen1_1 = "Genesis 1:1\n\nIn the beginning God created the Heavens and the Earth."
    gen1_2 = "Genesis 1:2\n\nThe earth was without form, and void, and darkness was on the face of the deep.\nAnd the Spirit of God was hovering over the face of the waters."
    gen1_3 = "Genesis 1:3\n\nThen God said, 'Let there be light', and there was light."
    gen1_4 = "Genesis 1:4\n\nAnd God saw the light, that it was good, and God divided the light from the darkness."
    gen1_5 = "Genesis 1:5\n\nGod called the light Day, and the darkness He called Night.\nSo the evening and the morning were the first day."
    gen1_6 = "Genesis 1:6\n\nThen God said, 'Let there be a firmament in the mist of the waters, and let it divide the waters from the waters."
    gen1_7 = "Genesis 1:7\n\nThus God made the firmament, and divided the waters which were under the firmament from the waters which were above the firmament, and it was so."
    gen1_8 = "Genesis 1:8\n\nAnd God called the firmament above Heaven.\nSo the eveinig and the morining were the second day."
    gen1_9 = "Genesis 1:9\n\nThen God said, 'Let the waters under the heavens be gathered together into one place, and let the dry land appear', and it was so."
    gen1_10 = "Genesis 1:10\n\nAnd God called the dry land Earth, and all the gathering together of the waters He called Seas.\nAnd God saw that it was good."
    gen1_11 = "Genesis 1:11\n\nThen God said, 'Let the earth bring forth grass, the herb that yields seed, and the fruit tree that yields fruit according to its kind, whose seed is in itself, on the earth', and it was so."
    gen1_12 = "Genesis 1:12\n\nAnd the earth brought forth grass, the herb that yields seed according to its kind, and the tree that yields fruit, whose seed is in itself according to its kind.\nAnd God saw that it was good."
    gen1_13 = "Genesis 1:13\n\nSo the evening and the morning were the third day."
    gen1_14 = "Genesis 1:14\n\nThen God said, 'Let there be lights in the firmament of the heavens to divide the day from the night, and let them be for signs and seasons, and for days and years'."
    gen1_15 = "Genesis 1:15\n\n'and let them be for lights in the firmament of the heavens to give light on the earth', and it was so."
    gen1_16 = "Genesis 1:16\n\nThen God made two great lights: the greater light to rule the day and the lesser light to rule the night. He made the stars also."
    gen1_17 = "Genesis 1:17\n\nGod set them in the firmament of the heavens to give light on the earth."
    gen1_18 = "Genesis 1:18\n\nand to rule over the day and over the night, and to divide the light from the darkness. And God saw that it was good."
    gen1_19 = "Genesis 1:19\n\nSo the eveining and the morining were the fourth day."
    gen1_20 = "Genesis 1:20\n\nThen God said, 'Let the waters abound with the abundance of living creatures, and let birds fly above the earth across the face of the firmament of the heavens'."
    gen1_21 = "Genesis 1:21\n\nSo God created great sea creatures and every livivng thing that moves, with which the waters abounded, according to their kind, and every winged bird according to its kind.\nAnd God saw that it was good."
    gen1_22 = "Genesis 1:22\n\nAnd God blessed them, saying, 'Be fruitful and multiply, and fill the waters in the seas, and let birds multiply on the earth'."
    gen1_23 = "Genesis 1:23\n\nSo the evening and the morning were the fifth day."
    gen1_24 = "Genesis 1:24\n\nThen God said, 'Let the earth bring forth the living creatures according to its kind: cattle and creeping thing and beast of the earth, each according to its kind', and it was so."
    gen1_25 = "Genesis 1:25\n\nAnd God made the beast of the earth according to its kind, cattle according to its kind, and everything that creeps on the earth according to its kind.\nAnd God saw that it was good."
    gen1_26 = "Genesis 1:26\n\nThen God said, 'Let Us make man in Our image, according to Our likeness, let them have dominion over the fish of the sea, over the birds of the air, and over the cattle, over all the earth and over every creeping thing that creeps on the earth'."
    gen1_27 = "Genesis 1:27\n\nSo God created man in His own image, in the image of God He created him, male and female He created them."
    gen1_28 = "Genesis 1:28\n\nThen God blessed them, and said to them, 'Be fruitful and multiply, fill the earth and subdue it, have dominion over the fish of the sea, over the birds of the air, and over every living thing that moves on the earth'."
    gen1_29 = "Genesis 1:29\n\nAnd God said, 'See I have given you every herb that yields seed which is on the face of all the earth, and every tree whose fruit yields seed, to you it shall be for food."
    gen1_30 = "Genesis 1:30\n\n'Also to every beast of the earth, to every bird of the air, and to everything that creeps on the earth, in which there is life, I have given every green herb for food', and it was so."
    gen1_31 = "Genesis 1:31\n\nThen God saw everything that He made, and indeed it was very good.\nSo the evening and the morning were the sixth day."
    
    gen2_1 = "Genesis 2:1\n\nThus the heavens and the earth, and all the host of them, were finished."

    scripures = [
        gen1_1, gen1_2, gen1_3, gen1_4, gen1_5, gen1_6, gen1_7, gen1_8, gen1_9, gen1_10,
        gen1_11, gen1_12, gen1_13, gen1_14, gen1_15, gen1_16, gen1_17, gen1_18, gen1_19, gen1_20,
        gen1_21, gen1_22, gen1_23, gen1_24, gen1_25, gen1_26, gen1_27, gen1_28, gen1_29, gen1_30,
        gen1_31,

        gen2_1
    ]
    
    txt1 = ft.Text(size=12, font_family="DaddyTimeMono", weight="bold", color="#E481FA")
    
    txt1.value = choice(scripures)
    page.update()
       

    page.add(
        ft.Card(
        content=ft.Container(
        txt1, padding=35
        )
        )
    )
    

ft.app(target=main, view=ft.WEB_BROWSER,assets_dir="assets")