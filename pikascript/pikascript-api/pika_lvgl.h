/*
 * [Warning!] This file is auto-generated by pika compiler.
 * Do not edit it manually.
 * The source code is *.pyi file.
 * More details: 
 * English Doc:
 * https://pikadoc.readthedocs.io/en/latest/PikaScript%20%E6%A8%A1%E5%9D%97%E6%A6%82%E8%BF%B0.html
 * Chinese Doc:
 * https://pikadoc.readthedocs.io/zh/latest/PikaScript%20%E6%A8%A1%E5%9D%97%E6%A6%82%E8%BF%B0.html
 */

#ifndef __pika_lvgl__H
#define __pika_lvgl__H
#include <stdio.h>
#include <stdlib.h>
#include "PikaObj.h"

PikaObj *New_pika_lvgl(Args *args);

Arg* pika_lvgl_ALIGN(PikaObj *self);
Arg* pika_lvgl_ANIM(PikaObj *self);
Arg* pika_lvgl_EVENT(PikaObj *self);
Arg* pika_lvgl_OPA(PikaObj *self);
Arg* pika_lvgl_PALETTE(PikaObj *self);
Arg* pika_lvgl_STATE(PikaObj *self);
Arg* pika_lvgl_TEXT_DECOR(PikaObj *self);
void pika_lvgl___init__(PikaObj *self);
Arg* pika_lvgl_arc(PikaObj *self);
Arg* pika_lvgl_bar(PikaObj *self);
Arg* pika_lvgl_btn(PikaObj *self);
Arg* pika_lvgl_checkbox(PikaObj *self);
Arg* pika_lvgl_dropdown(PikaObj *self);
PikaObj* pika_lvgl_indev_get_act(PikaObj *self);
Arg* pika_lvgl_indev_t(PikaObj *self);
Arg* pika_lvgl_label(PikaObj *self);
PikaObj* pika_lvgl_lv_color_hex(PikaObj *self, int64_t hex);
Arg* pika_lvgl_lv_color_t(PikaObj *self);
Arg* pika_lvgl_lv_event(PikaObj *self);
Arg* pika_lvgl_lv_obj(PikaObj *self);
Arg* pika_lvgl_lv_timer_t(PikaObj *self);
PikaObj* pika_lvgl_obj(PikaObj *self, PikaObj* parent);
PikaObj* pika_lvgl_palette_lighten(PikaObj *self, int p, int lvl);
PikaObj* pika_lvgl_palette_main(PikaObj *self, int p);
Arg* pika_lvgl_point_t(PikaObj *self);
Arg* pika_lvgl_roller(PikaObj *self);
PikaObj* pika_lvgl_scr_act(PikaObj *self);
Arg* pika_lvgl_slider(PikaObj *self);
Arg* pika_lvgl_style_t(PikaObj *self);
Arg* pika_lvgl_switch(PikaObj *self);
Arg* pika_lvgl_table(PikaObj *self);
Arg* pika_lvgl_textarea(PikaObj *self);
PikaObj* pika_lvgl_timer_create_basic(PikaObj *self);

#endif
