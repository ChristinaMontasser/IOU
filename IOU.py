import numpy as np

def txtData( Ptxt, Ttxt):
    data = [Ttxt, Ptxt]
    point = [0, 0]
    orderPair=[]
    if(not(np.any(Ptxt))):
        area1, area2 =0 ,0
        return orderPair, area1, area2
    for i in range(2):
        current =data[i]
        
        point[0]= ((current[0]-(current[2]/2)), (current[1]-(current[3]/2)))
        point[1]= ((current[0]+(current[2]/2)), (current[1]+(current[3]/2)))
        # point[2]= ((current[0]+(current[2]/2)), (current[1]-(current[3]/2)))
        # point[3]= ((current[0]-(current[2]/2)), (current[1]+(current[3]/2)))
        orderPair.append(point)
        point = [0, 0]
    #print(orderPair[0])
    area1 = (data[0][2]*data[0][3])
    area2 = (data[1][2]*data[1][3])
    return orderPair, area1, area2



def areaInter(orderPair):
    if(len(orderPair)==0):
        area_Inter=0
        return area_Inter
    x_inter1= max(orderPair[0][0][0], orderPair[1][0][0])
    y_inter1= max(orderPair[0][0][1], orderPair[1][0][1])

    x_inter2= min(orderPair[0][1][0], orderPair[1][1][0])
    y_inter2= min(orderPair[0][1][1], orderPair[1][1][1])
    
    width_inter= x_inter2- x_inter1
    height_inter=  y_inter2 -y_inter1
    # #(width_inter, height_inter)
    area_Inter =(width_inter * height_inter)
    return area_Inter

def IOU (area1, area2, area_Inter ):
    if(area_Inter==0):
        return 0
    area_union=(area1 + area2) -area_Inter
    IOU  =area_Inter/area_union
    return (IOU if IOU>0 else  0)


Pxywh1 = [0.4775,0.51625,0.73,0.5025]
Txywh1 = [0.507055,0.528219,0.804233,0.527337]
orderPair, area1, area2 =txtData(Pxywh1, Txywh1)
area_Inter = areaInter(orderPair)
print( IOU(area1, area2, area_Inter))
