import pika_lvgl as lv
import PikaStdLib as std
import evue_asset as asset

img1 = lv.img(lv.scr_act())
img1.set_src(asset.evue_designer())
img1.align(lv.ALIGN.CENTER, 0, -20)
img1.set_size(200, 200)

img2 = lv.img(lv.scr_act())
# img2.set_src(lv.SYMBOL.OK + "Accept")
img2.align_to(img1, lv.ALIGN.OUT_BOTTOM_MID, 0, 20)
std.MemChecker.now()
