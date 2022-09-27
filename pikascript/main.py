import pika_lvgl as lv
import PikaStdLib
mem = PikaStdLib.MemChecker()

class DataBinding:
    _inner_ = []
    def __init__(self, data):
        _bindings_ = {}
        self._inner_.append(_bindings_)
        self._inner_.append(data)

    def __getattr__(self, name):
        data = self._inner_[1]
        return data[name]

    def __setattr__(self, name, value):
        _bindings_ = self._inner_[0]
        if name in _bindings_:
            bindings = _bindings_[name]
            for binding in bindings:
                element = binding['element']
                attr = binding['attr']
                _name = attr.replace("-", "_")
                funcName = "set_%s" % _name
                if attr is 'text':
                    value = str(value)
                if hasattr(element, funcName):
                    element.func = getattr(element, funcName)
                    element.func(value)
                else:
                    if hasattr(element, "obj") and element.obj:
                        setattr(element.obj, _name, value)

    def set_binding_value(self, element, attr, key):
        _bindings_ = self._inner_[0]
        if key not in _bindings_:
            _bindings_[key] = []

        _bindings_[key].append({
            "element": element,
            "attr": attr
        })


data = {"clickcount":0,"result":"","count":0}
data = DataBinding(data)

widget0 = lv.obj(lv.scr_act())
style = lv.style_t()
style.init()
widget0.set_width(240)
widget0.set_height(240)
style.set_bg_color(lv.lv_color_hex(37864))
widget0.add_style(style, 0)
widget1 = lv.label(widget0)
style = lv.style_t()
style.init()
widget1.set_x(5)
widget1.set_y(10)
widget1.set_width(220)
widget1.set_height(30)
style.set_bg_opa(lv.OPA.TRANSP)
widget1.set_text('0')
widget1.add_style(style, 0)
data.set_binding_value(widget1, 'text', 'count')


# user code
def onclick(e):
    print('fsdf')
    data.count = data.count + 1

widget1.add_event_cb(onclick, lv.EVENT.ALL, 0)
