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

#include "PikaMain.h"
#include <stdio.h>
#include <stdlib.h>

PikaObj *__pikaMain;
PikaObj *pikaScriptInit(void){
    __platform_printf("======[pikascript packages installed]======\r\n");
    pks_printVersion();
    __platform_printf("PikaStdLib==latest\r\n");
    __platform_printf("===========================================\r\n");
    __pikaMain = newRootObj("pikaMain", New_PikaMain);
    extern unsigned char pikaModules_py_a[];
    obj_linkLibrary(__pikaMain, pikaModules_py_a);
#if PIKA_INIT_STRING_ENABLE
    obj_run(__pikaMain,
            "import pika_lvgl as lv\n"
            "class DataBinding:\n"
            "    _inner_ = []\n"
            "    def __init__(self, data):\n"
            "        _bindings_ = {}\n"
            "        self._inner_.append(_bindings_)\n"
            "        self._inner_.append(data)\n"
            "        # self._inner_[0] = _bindings\n"
            "        # self._inner_[1] = data\n"
            "    def __getattr__(self, name):\n"
            "        data = self._inner_[1]\n"
            "        return data[name]\n"
            "    def __setattr__(self, name, value):\n"
            "        _bindings_ = self._inner_[0]\n"
            "        if name in _bindings_:\n"
            "            bindings = _bindings_[name]\n"
            "            for binding in bindings:\n"
            "                element = binding['element']\n"
            "                attr = binding['attr']\n"
            "                _name = attr.replace(\"-\", \"_\")\n"
            "                funcName = \"set_%s\" % _name\n"
            "                if hasattr(element, funcName):\n"
            "                    func = getattr(element, funcName)\n"
            "                    func(value)\n"
            "                else:\n"
            "                    if hasattr(element, \"obj\") and element.obj:\n"
            "                        setattr(element.obj, _name, value)\n"
            "    def set_binding_value(self, element, attr, key):\n"
            "        _bindings_ = self._inner_[0]\n"
            "        if key not in _bindings_:\n"
            "            _bindings_[key] = []\n"
            "        _bindings_[key].append({\n"
            "            \"element\": element,\n"
            "            \"attr\": attr\n"
            "        })\n"
            "_data = {\n"
            "    'a': 10,\n"
            "    'b': 100\n"
            "}\n"
            "data = DataBinding(_data)\n"
            "class Binding:\n"
            "    def set_value(self, value):\n"
            "        print('set value =', value)\n"
            "binding = Binding()\n"
            "data.set_binding_value(binding, 'value', 'a')\n"
            "data.a = 20\n"
            "\n");
#else 
    obj_runModule(__pikaMain, "main");
#endif
    return __pikaMain;
}

