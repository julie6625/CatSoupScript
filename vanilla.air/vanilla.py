# -*- encoding=utf8 -*-
__author__ = "lucas"

from airtest.core.api import *

auto_setup(__file__)
count = 0
def customUsing(fiLe):
    print("--------引入" + fiLe + ".air--------")
    pathU = os.path.join("/Users/lucas/Desktop/CatSoup/"+fiLe+".air")
    using(pathU)
def treasure(): #vanilla and library
    customUsing("ads")
    from ads import ad
    
    try:
        #vanilla

        
        keyevent("BACK")
        
        #library

            

    except Exception as e:
        print("異常描述: {}".format(e))
        
# treasure()