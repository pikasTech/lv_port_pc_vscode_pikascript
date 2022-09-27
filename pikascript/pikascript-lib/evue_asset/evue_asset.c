#include "evue_asset_evue_designer.h"
#include "lvgl.h"

void evue_asset_evue_designer___init__(PikaObj *self){
    extern const lv_img_dsc_t asset_evue_designer;
    obj_setStruct(self, "img_dsc", asset_evue_designer);
}
