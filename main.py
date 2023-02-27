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

    scripures = [
        gen1_1, gen1_2, gen1_3, gen1_4, gen1_5, gen1_6, gen1_7, gen1_8, gen1_9, gen1_10,
        gen1_11, gen1_12
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