import pika_lvgl as lv
import PikaStdLib
mem = PikaStdLib.MemChecker()


widget0 = lv.obj(lv.scr_act())
widget0.set_width(240)
widget0.set_height(240)
style = lv.style_t()
style.init()
style.set_bg_color(lv.lv_color_hex(37864))
widget0.add_style(style, 0)
style = lv.style_t()
style.init()
widget0.add_style(style, 0)
widget1 = lv.label(widget0)
widget1.set_pos(5, widget1.get_y())
widget1.set_pos(widget1.get_x(), 10)
widget1.set_width(220)
widget1.set_height(30)
style = lv.style_t()
style.init()
style.set_bg_opa(lv.OPA.TRANSP)
widget1.add_style(style, 0)
widget1.set_text('hello qqq')
style = lv.style_t()
style.init()
widget1.add_style(style, 0)


# user code
print("write python code here")
