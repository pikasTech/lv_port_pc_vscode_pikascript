import pika_lvgl as lv
import PikaStdLib

import pika_lvgl as lv
import PikaStdLib
mem = PikaStdLib.MemChecker()


def event_cb_1(evt:lv.lv_event):
    print(evt.get_target().get_id())
    print('mem used now: %0.2f kB' % (mem.getNow()))


def event_cb_2(evt:lv.lv_event):
    print(evt.get_target().get_id())
    print('mem used now: %0.2f kB' % (mem.getNow()))


btn1 = lv.btn(lv.scr_act())
btn1.align(lv.ALIGN.TOP_MID, 0, 10)
btn2 = lv.btn(lv.scr_act())
btn2.align(lv.ALIGN.TOP_MID, 0, 50)
btn1.set_id('id:btn1')
btn1.add_event_cb(event_cb_1, lv.EVENT.CLICKED, 0)
btn2.set_id('id:btn2')
btn2.add_event_cb(event_cb_2, lv.EVENT.CLICKED, 0)

print('mem used max: %0.2f kB' % (mem.getMax()))
print('mem used now: %0.2f kB' % (mem.getNow()))
