# -*- encoding=utf8 -*-
__author__ = "lucas"

from airtest.core.api import *

auto_setup(__file__)
count = 0
def customUsing(fiLe):
    print("--------引入" + fiLe + ".air--------")
    pathU = os.path.join("/Users/lucas/Desktop/CatSoup/"+fiLe+".air")
    using(pathU)
def treasure(): #daily treasure and diamond 
    customUsing("ads")
    from ads import ad
    
    try:
        #diamond
        touch([998, 298])
        touch([639, 669])
#         if exists():
#             touch([257, 1797])
#             ad()
        
        keyevent("BACK")
        
        #treasure
        for count in range(3):

            touch([1010, 1766])
            touch([537, 915])
            if exists(Template(r"tpl1665996686087.png", rgb=True, record_pos=(-0.144, 0.454), resolution=(1080, 2340))):
                break
            else:
                ad()
                touch([393, 1698])
                sleep(65)
        keyevent("BACK")
        keyevent("BACK")
            

    except Exception as e:
        print("異常描述: {}".format(e))
        
# treasure()