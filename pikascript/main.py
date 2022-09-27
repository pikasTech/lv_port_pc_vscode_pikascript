import pika_lvgl
import PikaStdLib as std
nodes = dict({})
nodes.update({'widget0':{"type":"div","attributes":{"class":"container","style":{"width":240,"height":240,"margin":0,"padding":0,"border-radius":0,"border-width":0,"border-color":"red","background-color":37864}},"nodes":[{"type":"text","attributes":{"font-size":"30","class":"result-text","style":{"top":5,"left":5,"width":220,"text-align":"right","height":30,"color":"white","text-overflow":"longbreak","border-width":0,"border-color":"red","background-color":"transparent"}},"nodes":[],"bindings":[{"attrName":"text","key":"result","isText":True}],"events":[],"value":"0","widgetName":"widget1"},{"type":"div","attributes":{"class":"key-wrapper","onclick":"onclick","style":{"width":60,"height":50,"border-width":0,"border-color":"red","background-color":"transparent","top":40,"left":10}},"nodes":[{"type":"text","attributes":{"font-size":"30","class":"key","style":{"left":0,"top":0,"width":50,"height":40,"margin":0,"padding":0,"color":"white","font-size":30,"text-align":"center","background-color":"transparent"}},"nodes":[],"bindings":[],"events":[],"value":"1","widgetName":"widget3"}],"bindings":[],"events":[{"onclick":"onclick"}],"widgetName":"widget2"},{"type":"div","attributes":{"class":"key-wrapper","onclick":"onclick","style":{"width":60,"height":50,"border-width":0,"border-color":"red","background-color":"transparent","top":40,"left":60}},"nodes":[{"type":"text","attributes":{"font-size":"30","class":"key","style":{"left":0,"top":0,"width":50,"height":40,"margin":0,"padding":0,"color":"white","font-size":30,"text-align":"center","background-color":"transparent"}},"nodes":[],"bindings":[],"events":[],"value":"2","widgetName":"widget5"}],"bindings":[],"events":[{"onclick":"onclick"}],"widgetName":"widget4"},{"type":"div","attributes":{"class":"key-wrapper","onclick":"onclick","style":{"width":60,"height":50,"border-width":0,"border-color":"red","background-color":"transparent","top":40,"left":110}},"nodes":[{"type":"text","attributes":{"font-size":"30","class":"key","style":{"left":0,"top":0,"width":50,"height":40,"margin":0,"padding":0,"color":"white","font-size":30,"text-align":"center","background-color":"transparent"}},"nodes":[],"bindings":[],"events":[],"value":"3","widgetName":"widget7"}],"bindings":[],"events":[{"onclick":"onclick"}],"widgetName":"widget6"},{"type":"div","attributes":{"class":"key-wrapper","onclick":"onclick","style":{"width":60,"height":50,"border-width":0,"border-color":"red","background-color":"transparent","top":40,"left":160}},"nodes":[{"type":"text","attributes":{"font-size":"30","class":"key","style":{"left":0,"top":0,"width":50,"height":40,"margin":0,"padding":0,"color":"white","font-size":30,"text-align":"center","background-color":"transparent"}},"nodes":[],"bindings":[],"events":[],"value":"+","widgetName":"widget9"}],"bindings":[],"events":[{"onclick":"onclick"}],"widgetName":"widget8"}],"bindings":[],"events":[],"widgetName":"widget0"}})
nodes.update({'widget1':{"type":"text","attributes":{"font-size":"30","class":"result-text","style":{"top":5,"left":5,"width":220,"text-align":"right","height":30,"color":"white","text-overflow":"longbreak","border-width":0,"border-color":"red","background-color":"transparent"}},"nodes":[],"bindings":[{"attrName":"text","key":"result","isText":True}],"events":[],"value":"0","widgetName":"widget1"}})
nodes.update({'widget2':{"type":"div","attributes":{"class":"key-wrapper","onclick":"onclick","style":{"width":60,"height":50,"border-width":0,"border-color":"red","background-color":"transparent","top":40,"left":10}},"nodes":[{"type":"text","attributes":{"font-size":"30","class":"key","style":{"left":0,"top":0,"width":50,"height":40,"margin":0,"padding":0,"color":"white","font-size":30,"text-align":"center","background-color":"transparent"}},"nodes":[],"bindings":[],"events":[],"value":"1","widgetName":"widget3"}],"bindings":[],"events":[{"onclick":"onclick"}],"widgetName":"widget2"}})
nodes.update({'widget3':{"type":"text","attributes":{"font-size":"30","class":"key","style":{"left":0,"top":0,"width":50,"height":40,"margin":0,"padding":0,"color":"white","font-size":30,"text-align":"center","background-color":"transparent"}},"nodes":[],"bindings":[],"events":[],"value":"1","widgetName":"widget3"}})
nodes.update({'widget4':{"type":"div","attributes":{"class":"key-wrapper","onclick":"onclick","style":{"width":60,"height":50,"border-width":0,"border-color":"red","background-color":"transparent","top":40,"left":60}},"nodes":[{"type":"text","attributes":{"font-size":"30","class":"key","style":{"left":0,"top":0,"width":50,"height":40,"margin":0,"padding":0,"color":"white","font-size":30,"text-align":"center","background-color":"transparent"}},"nodes":[],"bindings":[],"events":[],"value":"2","widgetName":"widget5"}],"bindings":[],"events":[{"onclick":"onclick"}],"widgetName":"widget4"}})
nodes.update({'widget5':{"type":"text","attributes":{"font-size":"30","class":"key","style":{"left":0,"top":0,"width":50,"height":40,"margin":0,"padding":0,"color":"white","font-size":30,"text-align":"center","background-color":"transparent"}},"nodes":[],"bindings":[],"events":[],"value":"2","widgetName":"widget5"}})
nodes.update({'widget6':{"type":"div","attributes":{"class":"key-wrapper","onclick":"onclick","style":{"width":60,"height":50,"border-width":0,"border-color":"red","background-color":"transparent","top":40,"left":110}},"nodes":[{"type":"text","attributes":{"font-size":"30","class":"key","style":{"left":0,"top":0,"width":50,"height":40,"margin":0,"padding":0,"color":"white","font-size":30,"text-align":"center","background-color":"transparent"}},"nodes":[],"bindings":[],"events":[],"value":"3","widgetName":"widget7"}],"bindings":[],"events":[{"onclick":"onclick"}],"widgetName":"widget6"}})
nodes.update({'widget7':{"type":"text","attributes":{"font-size":"30","class":"key","style":{"left":0,"top":0,"width":50,"height":40,"margin":0,"padding":0,"color":"white","font-size":30,"text-align":"center","background-color":"transparent"}},"nodes":[],"bindings":[],"events":[],"value":"3","widgetName":"widget7"}})
nodes.update({'widget8':{"type":"div","attributes":{"class":"key-wrapper","onclick":"onclick","style":{"width":60,"height":50,"border-width":0,"border-color":"red","background-color":"transparent","top":40,"left":160}},"nodes":[{"type":"text","attributes":{"font-size":"30","class":"key","style":{"left":0,"top":0,"width":50,"height":40,"margin":0,"padding":0,"color":"white","font-size":30,"text-align":"center","background-color":"transparent"}},"nodes":[],"bindings":[],"events":[],"value":"+","widgetName":"widget9"}],"bindings":[],"events":[{"onclick":"onclick"}],"widgetName":"widget8"}})
nodes.update({'widget9':{"type":"text","attributes":{"font-size":"30","class":"key","style":{"left":0,"top":0,"width":50,"height":40,"margin":0,"padding":0,"color":"white","font-size":30,"text-align":"center","background-color":"transparent"}},"nodes":[],"bindings":[],"events":[],"value":"+","widgetName":"widget9"}})
print(nodes)
std.MemChecker.now()
del nodes
std.MemChecker.now()