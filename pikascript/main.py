import pika_lvgl as lv
import evue_asset
import PikaStdLib as std

try:
    f = open('../logo.png', 'rb')
    png_data = f.read(-1)
except:
    print("Could not find img_cogwheel_argb.png")
    exit()

img_cogwheel_argb = lv.img_dsc_t({
    'data_size': len(png_data),
    'data': png_data
})

img1 = lv.img(lv.scr_act())
img1.set_src(img_cogwheel_argb)
img1.align(lv.ALIGN.TOP_LEFT, 20, 20)
img1.set_size(200, 50)

std.MemChecker.now()


