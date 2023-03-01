from random import choice

import flet as ft


def main(page: ft.Page):
    #Page settings
    page.title = "SOTM"
    page.theme_mode = "dark"
    page.bgcolor = "#ddc8a9"
    #initial bgcolor == #daa520
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
    gen2_2 = "Genesis 2:2\n\nAnd on the seventh day God ended His work which He had done, and He rested on the seventh day from all His work which He had done."
    gen2_3 = "Genesis 2:3\n\nThen God blessed the seventh day and sanctified it, because in it He rested from all His work which God created and made."
    gen2_4 = "Genesis 2:4\n\nThis is the history of the heavens and the earth when thry were created, in the day that the LORD God made the earth and the heavens."
    gen2_5 = "Genesis 2;5\n\nbefore any plant of the field was in the earth and before any herb of the field had grown. For the LORD God had not caused it to rain on the earth, and there was no man to till the ground."
    gen2_6 = "Genesis 2:6\n\nbut a mist went up from the earth and watered the whole face of th ground."
    gen2_7 = "Genesis 2:7\n\nAnd the LORD God formed man of the dust of the ground, and breathed into his nostrils the breathe of life, and man became a living being."
    gen2_8 = "Genesis 2:8\n\nThe LORD God planted a garden eastward of Eden, and there He put the man whom He had formed."
    gen2_9 = "Genesis 2:9\n\nAnd out of the ground the LORD God made every tree grow that is pleasant to the sight and good for food.\nThe tree of life was also in the midst of the garden, and the tree of the knowledge of good and evil."
    gen2_10 = "Genesis 2:10\n\nNow a river went out of Eden to water the garden, and from there it parted and became four riverheads."
    gen2_11 = "Genesis 2:11\n\nThe name of the first is Pishon, it is the one which encompasses the whole land of Havilah, where there is gold."
    gen2_12 = "Genesis 2:12\n\nAnd the gold of that land is good.\nBdellium and onyx stone are there."
    gen2_13 = "Genesis 2:13\n\nThe name of the second river is Gilhon, it is the one which encompasses the land of Cush."
    gen2_14 = "Genesis 2:14\n\nThe name of the third river is Hiddekel, it is the one which goes toward the east of Assyria.\nThe fourth river is the Euphrates."
    gen2_15 = "Genesis 2:15\n\nThen the LORD God took the man and put him in te garden of Eden to tend and keep it."
    gen2_16 = "Genesis 2:16\n\nAnd the LORD God commanded the man, saying, 'Of every tree of the garden you may freely eat"
    gen2_17 = "Genesis 2:17\n\nbut of the tree of the knowledge of good and evil you shall not eat, for in the day that you eat of it you shall surely die."
    gen2_18 = "Genesis 2:18\n\nAnd the LORD said, 'It is not good that man should be alone, I will make him a helper comparable to him'."
    gen2_19 = "Genesis 2:19\n\nOut of the ground the LORD God formed every beast of the field and every bird of the air, and brought them to Adam to see what he would call them.\nAnd whatever Adam called each living creature, that was its name."
    gen2_20 = "Genesis 2:20\n\nSo Adam gave names to all cattle, to the birds of the air, and to every beast of the field.\nBut for Adam there was not a found helper comparable to him."
    gen2_21 = "Genesis 2:21\n\nAnd the LORD God caused a deep sleep to fall on Adam, and he slept, and He took one of his ribs, and closed up the flesh in its place."
    gen2_22 = "Genesis 2:22\n\nThen the rib which the LORD God taken from man He made a woman and He brought her to the man."  
    gen2_23 = "Genesis 2:23\n\nAnd Adam said:\n'This is now bone of my bones\nAnd flesh of my flesh\nShe shall be called Woman\nBecause she was taken out of Man.'"
    gen2_24 = "Genesis 2:24\n\nTherefore a man shall leave his father and mother and be joined to his wife, and they shall become one flesh."
    gen2_25 = "Genesis 2:25\n\nAnd they were both naked, the man and his wife, and were not ashamed."

    scripures = [
        gen1_1, gen1_2, gen1_3, gen1_4, gen1_5, gen1_6, gen1_7, gen1_8, gen1_9, gen1_10,
        gen1_11, gen1_12, gen1_13, gen1_14, gen1_15, gen1_16, gen1_17, gen1_18, gen1_19, gen1_20,
        gen1_21, gen1_22, gen1_23, gen1_24, gen1_25, gen1_26, gen1_27, gen1_28, gen1_29, gen1_30,
        gen1_31, 

        gen2_1, gen2_2, gen2_3, gen2_4, gen2_5, gen2_6, gen2_7, gen2_8, gen2_9, gen2_10,
        gen2_11, gen2_12, gen2_13, gen2_14, gen2_15, gen2_16, gen2_17, gen2_18, gen2_19, gen2_20,
        gen2_21, gen2_22, gen2_23, gen2_24, 25
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