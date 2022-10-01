import pika_lvgl as lv
import PikaStdLib as std
import evue_asset

def row_gap_anim(obj, v):
    obj.set_style_pad_row(v, 0)


def column_gap_anim(obj, v):
    obj.set_style_pad_column(v, 0)

#
# Demonstrate the effect of column and row gap style properties
#

cont = lv.obj(lv.scr_act())
cont.set_size(300, 220)
cont.center()
cont.set_flex_flow(lv.FLEX_FLOW.ROW_WRAP)

for i in range(9):
    obj = lv.obj(cont)
    obj.set_size(70, lv.SIZE.CONTENT)

    label = lv.label(obj)
    label.set_text(str(i))
    label.center()

