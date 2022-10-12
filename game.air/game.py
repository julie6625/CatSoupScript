# -*- encoding=utf8 -*-
__author__ = "lucas"

from airtest.core.api import *


auto_setup(__file__,devices=["Android://127.0.0.1:5037/13241FDD4000VH"])


dev = connect_device("Android:///")


start_app("com.hidea.cat")
sleep(5)

number = 1
def customUsing(fiLe):
    print("--------引入" + fiLe + ".air--------")
    pathU = os.path.join("/Users/lucas/Desktop/CatSoup/"+fiLe+".air")
    using(pathU)
        
def soup():
    customUsing("ads")
    from ads import ad


    if exists(Template(r"tpl1664877771710.png", record_pos=(0.173, -0.382), resolution=(1080, 2340))):
        touch(Template(r"tpl1664877771710.png", record_pos=(0.173, -0.382), resolution=(1080, 2340)),times=15)

    if exists(Template(r"tpl1664874826775.png", record_pos=(0.012, 0.908), resolution=(1080, 2340))):
        touch(Template(r"tpl1664874826775.png", record_pos=(0.012, 0.908), resolution=(1080, 2340)))
        ad()

    if exists(Template(r"tpl1664511252246.png", record_pos=(0.056, 0.869), resolution=(1080, 2340))):
        touch(Template(r"tpl1664511252246.png", record_pos=(0.056, 0.869), resolution=(1080, 2340)))
        ad()

    if exists(Template(r"tpl1665479387871.png", record_pos=(0.427, 0.435), resolution=(1080, 2340))):
        try:
            touch(Template(r"tpl1665479387871.png", record_pos=(0.427, 0.435), resolution=(1080, 2340)))
            touch([539, 1809])
            keyevent("BACK")
        except Exception as e:
            print("異常描述: {}".format(e))
            
    if exists(Template(r"tpl1664517083833.png", record_pos=(0.446, 0.305), resolution=(1080, 2340))):
        #touch(Template(r"tpl1664511817837.png", record_pos=(-0.006, 0.206), resolution=(1080, 2340)))
        touch(Template(r"tpl1664517083833.png", record_pos=(0.446, 0.305), resolution=(1080, 2340)))
        sleep(2)
        touch(Template(r"tpl1664511817837.png", record_pos=(-0.006, 0.206), resolution=(1080, 2340)))
        sleep(1)

        ad()

        sleep(2)
        touch((646,536))

        
while(True):
    print("目前執行第"+str(number)+"次")
    while number <= 300:
    
        soup()

        print("第"+str(number)+"次已執行完畢")
        if number%10==0 or number==1 :
            touch([120,2032], duration = 30)
            touch([843, 2073])
            touch([802, 1872], duration = 30)
            keyevent("BACK")

            sleep(2)
        
        number = number + 1
    else :
        break
     
