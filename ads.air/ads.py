# -*- encoding=utf8 -*-
__author__ = "lucas"

from airtest.core.api import *

auto_setup(__file__)

def ad():
    try:
        if exists(Template(r"tpl1664874935491.png", record_pos=(0.124, 0.171), resolution=(1080, 2340))):
            touch(Template(r"tpl1664874935491.png", record_pos=(0.124, 0.171), resolution=(1080, 2340)))
        
        if exists( Template(r"tpl1665480534403.png", record_pos=(0.007, 0.437), resolution=(1080, 2340))):
            touch( Template(r"tpl1665480534403.png", record_pos=(0.007, 0.437), resolution=(1080, 2340)))
        
        if exists(Template(r"tpl1664511404901.png", record_pos=(0.124, 0.171), resolution=(1080, 2340))):
            touch(Template(r"tpl1664511404901.png", record_pos=(0.124, 0.171), resolution=(1080, 2340)))
        if exists(Template(r"tpl1665572725934.png", record_pos=(0.023, 0.208), resolution=(1080, 2340))):
            sleep(15)
        else:
            sleep(60)
            keyevent("BACK")
                
        if exists(Template(r"tpl1665570375325.png", record_pos=(0.004, -0.021), resolution=(1080, 2340))):
            keyevent("BACK")

#         if wait(Template(r"tpl1664512025277.png", record_pos=(0.427, -0.891), resolution=(1080, 2340))):
#             touch(Template(r"tpl1664512047580.png", record_pos=(0.427, -0.886), resolution=(1080, 2340)))
#         elif exists(Template(r"tpl1664519942680.png", record_pos=(0.406, -0.747), resolution=(1080, 2340))):
#             touch(Template(r"tpl1664519942680.png", record_pos=(0.406, -0.747), resolution=(1080, 2340)))
#         elif exists(Template(r"tpl1664795178504.png", record_pos=(-0.433, -0.887), resolution=(1080, 2340))):
#             touch(Template(r"tpl1664795178504.png", record_pos=(-0.433, -0.887), resolution=(1080, 2340)))    
#             sleep(1)
#             touch(Template(r"tpl1664795260912.png", record_pos=(-0.429, -0.885), resolution=(1080, 2340)))

#         else :
#             touch((79,209))
    except Exception as e:
        print("異常描述: {}".format(e))
