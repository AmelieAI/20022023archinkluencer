
import uuid
import time
import tempfile
import ifcopenshell

#import numpy as np
#from shapely.geometry import Point, Polygon, LineString, MultiLineString
#from shapely import affinity
#import geopandas as gpd
#import matplotlib.pyplot as plt
import math, random
import sqlite3



#from signal import signal, SIGPIPE, SIG_DFL




def main():

    #signal(SIGPIPE, SIG_DFL)
    db_path = '/Users/ameliehofer/PycharmProjects/djangoProject/db.sqlite3'
    db_connection = sqlite3.connect(db_path)
    db_cursor = db_connection.cursor()

    db_cursor.execute('SELECT name FROM Archinkluencer_modeldataifc;')
    data = db_cursor.fetchall()
    DimensionsNot = []
    Dimensions = []
    AlgoInt = []
    for all in data:
        #print(all)
        for value in all:
            #print(value)
            try:
                val = float(value)
                #print(val)
                Dimensions.append(val)
            except:
                pass

    db_cursor.execute('SELECT length FROM Archinkluencer_modeldataifc;')
    data = db_cursor.fetchall()
    DimensionLength = []
    for all in data:
        # print(all)
        for value in all:
            # print(value)
            try:
                val = float(value)
                # print(val)
                DimensionLength.append(val)
            except:
                pass

    #print(DimensionLength)
    db_cursor.execute('SELECT doorpos FROM Archinkluencer_modeldataifc;')
    data = db_cursor.fetchall()
    DimensionDoor = []
    for all in data:
        # print(all)
        for value in all:
            # print(value)
            try:
                val = float(value)
                # print(val)
                DimensionDoor.append(val)
            except:
                pass


    """
    if len(DimensionLength) == 40:
        db_cursor.execute('DELETE from Archinkluencer_modeldataifc where wallname')
        db_cursor.execute('DELETE from Archinkluencer_modeldataifc where name')
        db_cursor.execute('DELETE from Archinkluencer_modeldataifc where length')
        db_cursor.execute('DELETE from Archinkluencer_modeldataifc where doorpos')
        db_cursor.execute('DELETE from Archinkluencer_modeldataifc where algo')
        db_connection.commit()
        print("Record deleted successfully")

    if len(DimensionLength) == 0:
        roomWidth = 5.0
        roomLength = 5.0
        posDoor = 1.2
        wallselwc = 3.0
        wallselsink = 6.0
       
        db_cursor.execute(
            'INSERT INTO Archinkluencer_modeldataifc ( id, created_at, name,done, door, wallname, wallname_wc , doorpos, length) VALUES ( 1, 2023-02-08, 5.0, 0,0, 3,  8, 1.2, 5.0)')
        db_cursor.execute(
            'INSERT INTO Archinkluencer_modeldataifc ( id, created_at, name,done, door, wallname, wallname_wc , doorpos, length) VALUES ( 2, 2023-02-08, 5.0, 0,0, 3,  8, 1.2, 5.0)')
        db_cursor.execute(
            'INSERT INTO Archinkluencer_modeldataifc ( id, created_at, name,done, door, wallname, wallname_wc , doorpos, length) VALUES ( 3, 2023-02-08, 5.0, 0,0, 3,  8, 1.2, 5.0)')
        db_cursor.execute(
            'INSERT INTO Archinkluencer_modeldataifc ( id, created_at, name,done, door, wallname, wallname_wc , doorpos, length) VALUES ( 4, 2023-02-08, 5.0, 0,0, 3,  8, 1.2, 5.0)')
        db_cursor.execute(
            'INSERT INTO Archinkluencer_modeldataifc ( id, created_at, name,done, door, wallname, wallname_wc , doorpos, length) VALUES ( 5, 2023-02-08, 5.0, 0,0, 8,  8, 1.2, 5.0)')
        
    #print(DimensionDoor)

    # klo value  1,2,3,4
    # wb value 5,6,7,8
    else:"""

    roomWidth= DimensionLength[-1]
    print("breite", roomWidth)
    roomLength = Dimensions[-1]
    print("länge", roomLength)
    posDoor = DimensionDoor[-1]
    print("door", posDoor)

    # print(roomLength+roomWidth)



    db_cursor.execute('SELECT wallname FROM Archinkluencer_modeldataifc;')
    data = db_cursor.fetchall()
    DimensionsFurnitureNot = []
    DimensionsFurniture = []
    for all in data:
        # print(all)
        for value in all:
            # print(value)
            try:
                val = float(value)
                # print(val)
                if val == 10 or val == 20:
                    AlgoInt.append(val)
                else:
                    DimensionsFurniture.append(val)
            except:
                pass

    print(DimensionsFurniture)

    # klo value  1,2,3,4
    #wb value 5,6,7,8
    wallselwc = DimensionsFurniture[-2]
    wallselsink = DimensionsFurniture[-1]

    algo = AlgoInt[-1]
    print("selected Algo: ", algo)


    print("walls", wallselwc, wallselsink)

    if wallselwc not in range(1,5):
        print("error")
        listlen = len(DimensionsFurniture)
        while wallselwc not in range(1,5):
            listlen = listlen -1
            val =  DimensionsFurniture[listlen]
            if val in range(1,5):
                wallselwc = val
                break
    print("walls2", wallselwc, wallselsink)



    if wallselsink not in range(5,9):
        print("sink position error!")
        listlen = len(DimensionsFurniture)
        while wallselsink not in range(5,9):
            listlen = listlen - 1
            val = DimensionsFurniture[listlen]
            if val in range(5,9):
                wallselsink = val
                break




    #db_connection.close()
#jetzt kann ich den algorithmus starten...
# optionen: X beide an einer Wand x
#           X beide an einer Wand y
#           klo an anderer wand wie wb aber beide x (1,3)
#           klo an anderer Wand wie wb aber beide y (2,4)
#           klo an x und wb an y
#           klo an y und wb an x


    # ORIGIN
    O = 0., 0., 0.
    X = 1., 0., 0.
    Y = 0., 1., 0.
    Z = 0., 0., 1.

    # INPUT USER
    global t, l, b

    t = 0.2  # halbe Dicke der Wand-> insgesamt t*2
    l = float(roomLength) + 2 * t  # 7.0 + 2 * t  # width der Wand x
    b = float(roomWidth) + 2 * t  # 3.0 + 2 * t  # height der zweiten Wand y
    print("roomsettings t,l,b: ", t, l, b)
    # -------------------ifc WALLS--------------------------------------
    # Punkte für Polyline
    point_0 = (0., 0.)  # Startpoint Line 1 -> Ursprung O, endpoint Line  4
    point_1 = (l, 0.)  # Endpoint Line 1, new startpoint Line 2
    point_2 = (l, b)  # Endpoint Line 2, new startpoint Line 3
    point_3 = (0., b)  # Endpoint Line 3, new startpoint Line 4

    points_line = [point_0, point_1, point_2, point_3]

    # Rectangle
    # ergeben sich in Abhängigkeit zum Ursprung,
    # der Ursprung ist jeweils der Endpunkt der vorangegangenen Polyline der Wand!!!
    # Lenght horizontal
    global point_6, point_8, point_10, point_7
    point_4 = (-t, -t)
    point_5 = ((l + t), -t)
    point_6 = ((l - t), t)
    point_7 = (t, t)

    # Width vertical
    point_4 = (-t, -t)
    point_7 = (t, t)
    point_8 = (t, (b - t))
    point_9 = (-t, (b + t))

    point_10 = ((l - t), (b - t))
    point_11 = ((l + t), (b + t))

    points_rect = [point_4, point_5, point_6, point_7, point_8, point_9, point_10, point_11]

    summe_x = (point_7[0] + point_8[0] + point_10[0] + point_6[0]) / 4
    summe_y = (point_7[1] + point_8[1] + point_10[1] + point_6[1]) / 4


    # ------------------------
    # wc position
    rotate = 1.0


    #x = 0.5 #1.6  # (2*t)+0.1 #(2*t) #
    #y = 2 * t #b - 2 * t  # 2 * t #2 * t     #b-2 * t #1.2 -2 * t
    z = 0.08
    ValuesX = []

    #wc_point_center = (x, y, z)

    # -----sink position--------
    # wall 1


    zs = 0.67
    ValuesXS = []
    #print(xs)

    #Wand_02 = 2 * t + 0.075
    #input = Wand_02

    # door input:
    door_width = 0.9
    door_heigth = 2.1

    # Abstand der Türöffnung zur Raumecke
    position_door = float(posDoor) + 0.2
    print("position door: ",position_door)


    position_door_end = door_width + position_door
    pos_x = 0.0
    pos_y = 0.0


    point_list_opening_extrusion_area = [(position_door + pos_x, t + pos_y), (position_door + pos_x, -t + pos_y),
                                         (position_door_end + pos_x, -t + pos_y),
                                         (position_door_end + pos_x, t + pos_y)]



    # -------------------------------------------------------------------------------------
    # .........................ifc Toilet......................................................................................
    # ---------------------------------------------------------------------------------------------------------------------
    # Points for Toilet Geom

    # M = (0,0) dann ist Toilette ganz an der Wand, ohne Abstand.
    # M = (1,0) dann ist Toilette im Abstand 1m von Innenkante Wand orthogonal zum Klo, weg.

    # ---------------WC--------------------

    wc_point_0 = (0. - 0.2, 0. + 0.2)
    wc_point_1 = (0. + 0.2, 0. + 0.2)
    wc_point_2 = (0. + 0.2, 0. - 0.2)
    wc_point_3 = (0. - 0.2, 0. - 0.2)
    wc_point_4 = (0. + 0., 0. - 0.4)
    wc_point_5 = (0. + 0., 0. - 0.2)
    wc_point_6 = (0. + 0.173, 0. - 0.3)
    wc_point_7 = (0. + 0.1, 0. - 0.373)
    wc_point_8 = (0. - 0.173, 0. - 0.3)
    wc_point_9 = (0. - 0.1, 0. - 0.373)

    wc_point_10 = (0.3, 0.173)
    wc_point_11 = (0.373, 0.1)
    wc_point_12 = (0.4, 0.)
    wc_point_13 = (0.373, -0.1)
    wc_point_14 = (0.3, -0.173)

    wc_point_15 = (0.173, 0.3)
    wc_point_16 = (0.1, 0.373)
    wc_point_17 = (0.0, 0.4)

    #wand 1
    wc_point_out_1 = (-0.2, 0.4)
    wc_point_out_2 = (0.2, 0.4)
    wc_point_out_3 = (0.2, -0.2)
    wc_point_out_4 = (-0.2, -0.2)

    #wand 3
    wc_point_out_1_3 = (0.2, -0.4)
    wc_point_out_2_3 = (-0.2, -0.4)
    wc_point_out_3_3 = (-0.2, 0.2)
    wc_point_out_4_3 = (0.2, 0.2)

    #wand 2
    wc_point_out_1_2 = (0.4, 0.2)
    wc_point_out_2_2 = (0.4, -0.2)
    wc_point_out_3_2 = (-0.2, -0.2)
    wc_point_out_4_2 = (-0.2, 0.2)

    #wand 4
    wc_point_out_1_4 = (-0.4, -0.2)
    wc_point_out_2_4 = (-0.4, 0.2)
    wc_point_out_3_4 = (0.2, 0.2)
    wc_point_out_4_4 = (0.2, -0.2)


    #wand 1
    sink_point_out_1 = (-0.3, 0.275)
    sink_point_out_2 = (0.3, 0.275)
    sink_point_out_3 = (0.3, -0.275)
    sink_point_out_4 = (-0.3, -0.275)

    #wand 3
    sink_point_out_1_3 = (0.3, -0.275)
    sink_point_out_2_3 = (-0.3,- 0.275)
    sink_point_out_3_3 = (-0.3, 0.275)
    sink_point_out_4_3 = (0.3, 0.275)

    #wand 2
    sink_point_out_1_2 = ( 0.275, 0.3)
    sink_point_out_2_2 = (0.275, -0.3)
    sink_point_out_3_2 = (-0.275, -0.3)
    sink_point_out_4_2 = (-0.275, 0.3)

    #wand 4
    sink_point_out_1_4 = ( -0.275, -0.3)
    sink_point_out_2_4 = (- 0.275, 0.3)
    sink_point_out_3_4 = ( 0.275, 0.3)
    sink_point_out_4_4 = (0.275, -0.3)

#-------------ALGORITHMUS---------------------
    # ,, (0, 0.4), (-0.173, 0.373), (-0.1, 0.3)

    # wc_point_list = [wc_point_0, wc_point_1, wc_point_2, wc_point_3,
    # wc_point_4, wc_point_5, wc_point_6,wc_point_7,wc_point_8,wc_point_9]

    # --------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------
    # --------------------------POSITION ALGORITHM------------------------------------
    # --------------------------------------------------------------------------------
    def linie(p1, p2):
        A = (p1[1] - p2[1])
        B = (p2[0] - p1[0])
        C = (p1[0] * p2[1] - p2[0] * p1[1])

        return A, B, -C

    def schnittpunkt(L1, L2):
        D = L1[0] * L2[1] - L1[1] * L2[0]
        Dx = L1[2] * L2[1] - L1[1] * L2[2]
        Dy = L1[0] * L2[2] - L1[2] * L2[0]
        if D != 0:
            x = Dx / D
            y = Dy / D
            return x, y
        else:
            return False

    def PointInPolygon(x_value, y_value, min_X, max_X, min_Y, max_Y):
        if x_value >= min_X and y_value >= min_Y and x_value <= max_X and y_value <= max_Y:
            #print( "ERGEBNISVGL", x_value, min_X, y_value, min_Y, "max ",x_value, max_X, y_value, max_Y )
            return True
        else:
            #print("ERGEBNISVGL", x_value, min_X, y_value, min_Y, "max ", x_value, max_X, y_value, max_Y)
            return False

        # ich gebe statisches Door Polygon ein (Liste mit Lines) und möchte alle Obj2 Lines auf Intersections testen:


    def AllIntersections(StaticObjList, Obj1List):
        IntersectionPoints = []
        for i in range(len(Obj1List)):
            for linesStatic in StaticObjList:
                # print("Linestat ", linesStatic)
                R = schnittpunkt(linesStatic, Obj1List[i])

                if R != False:
                    IntersectionPoints.append(R)

        return IntersectionPoints

    def IntersectionsInsidePoly(IntersectionPoints, min_X_obj1, max_X_obj1, min_Y_obj1, max_Y_obj1):
        IntersectionPointsInside = []
        for r in IntersectionPoints:
            Obj1Int = PointInPolygon(r[0], r[1], min_X_obj1, max_X_obj1, min_Y_obj1, max_Y_obj1)
            if Obj1Int == True:
                IntersectionPointsInside.append(r)
                # print("      INTERSECTIONPOINTS INSIDE POLY:",r)

        return IntersectionPointsInside

        # sind alle Eckpunkte von Obj1 in der Area von ObjStatic? -> Input Eckpunkte Obj, min max Obj Static

    def PolyContainsPoly(Obj1Points, min_X_objStat, max_X_objStat, min_Y_objStat, max_Y_objStat):
        Obj1InsideObjStaticList = []
        Obj1InsideObjStaticListFalse = []
        for pts in Obj1Points:
            Obj1InsideObjStatic = PointInPolygon(pts[0], pts[1], min_X_objStat, max_X_objStat, min_Y_objStat,
                                                 max_Y_objStat)
            # alle Puunkte in PolyStatic:
            if Obj1InsideObjStatic == True:
                Obj1InsideObjStaticList.append(Obj1InsideObjStatic)

            # nicht alle Punkte in PolyStatic
            else:
                Obj1InsideObjStaticListFalse.append(Obj1InsideObjStatic)

        if len(Obj1InsideObjStaticList) == 4:
            set = None
            #print(len(Obj1InsideObjStaticList), "None")
            # print("Poly contains Poly")
            return set, None

        elif len(Obj1InsideObjStaticListFalse) == 4:
            set = True
            # print(len(Obj1InsideObjStaticListFalse), "True")
            # print("No intersections, no containing")
            return set, True

        else:
            set = False
            # print("Some intersections detected")
            #print(len(Obj1InsideObjStaticListFalse), "False")
            return set, False

    def PositionChecking(StaticObjList, Obj1List,
                         min_X_obj1, max_X_obj1, min_Y_obj1, max_Y_obj1,
                         Obj1Points, min_X_objStat, max_X_objStat, min_Y_objStat, max_Y_objStat):
        IntersectionPoints = AllIntersections(StaticObjList, Obj1List)
        IntersectionsInsidePoly(IntersectionPoints, min_X_obj1, max_X_obj1, min_Y_obj1, max_Y_obj1)
        return PolyContainsPoly(Obj1Points, min_X_objStat, max_X_objStat, min_Y_objStat, max_Y_objStat)

        # ---------------
        # ---------------

    summe_x = (point_7[0] + point_8[0] + point_10[0] + point_6[0]) / 4
    summe_y = (point_7[1] + point_8[1] + point_10[1] + point_6[1]) / 4

    def Distance(IntersectionPoint, vert1):
        d1 = math.sqrt((IntersectionPoint[0] - vert1[0]) ** 2 + (IntersectionPoint[1] - vert1[1]) ** 2)
        print("distance= ", d1)
        return d1

    # ----------Room-----------

    def InputPoints(pt_1, pt_2, pt_3, pt_4):
        roomAA = (pt_1[0], pt_1[1])
        roomBB = (pt_2[0], pt_2[1])
        roomCC = (pt_3[0], pt_3[1])
        roomDD = (pt_4[0], pt_4[1])

        roomAreaPoints_X = []
        roomAreaPoints_X.append(roomAA[0])
        roomAreaPoints_X.append(roomBB[0])
        roomAreaPoints_X.append(roomCC[0])
        roomAreaPoints_X.append(roomDD[0])

        # print(doorAreaPoints_X)
        min_X_room = min(roomAreaPoints_X)
        # print(min_X_door)
        max_X_room = max(roomAreaPoints_X)
        # print(max_X_door)

        roomAreaPoints_Y = []
        roomAreaPoints_Y.append(roomAA[1])
        roomAreaPoints_Y.append(roomBB[1])
        roomAreaPoints_Y.append(roomCC[1])
        roomAreaPoints_Y.append(roomDD[1])

        # print(doorAreaPoints_Y)
        min_Y_room = min(roomAreaPoints_Y)
        # print(min_Y_door)
        max_Y_room = max(roomAreaPoints_Y)
        # print(max_Y_door)

        RoomAreaPoints = []
        RoomAreaPoints.append(roomAA)
        RoomAreaPoints.append(roomBB)
        RoomAreaPoints.append(roomCC)
        RoomAreaPoints.append(roomDD)

        # ------door lines ---------------
        RoomPoly = []
        RoomLineAB = linie(roomAA, roomBB)
        RoomLineAD = linie(roomAA, roomDD)
        RoomLineBC = linie(roomBB, roomCC)
        RoomLineDC = linie(roomDD, roomCC)

        RoomPoly.append(RoomLineAB)
        RoomPoly.append(RoomLineAD)
        RoomPoly.append(RoomLineBC)
        RoomPoly.append(RoomLineDC)

        return "min_X_: ", min_X_room, "max_X_: ", max_X_room, "min_Y_: ", min_Y_room, "max_Y_: ", max_Y_room, "AreaPoints: ", RoomAreaPoints, "Poly: ", RoomPoly

    room = InputPoints(point_8, point_10, point_6, point_7)
    # print("room;", room)

    # wall1
    door = InputPoints(
        ((point_list_opening_extrusion_area[0][0] - 0.2), (point_list_opening_extrusion_area[0][1] + 1.2)),
        ((point_list_opening_extrusion_area[0][0] + 1.3), (point_list_opening_extrusion_area[0][1] + 1.2)),
        ((point_list_opening_extrusion_area[0][0] + 1.3), (point_list_opening_extrusion_area[0][1])),
        ((point_list_opening_extrusion_area[0][0] - 0.2), point_list_opening_extrusion_area[0][1]))
    print("door;", door)

    # print("      ", WcCheck2)

    def PositionWcX(x, y, point_10, wc_1, wc_2, wc_3, wc_4):
        # ------------Check 1----------------

        room = InputPoints(point_8, point_10, point_6, point_7)
        # print("room;", room)

        # wall1
        door = InputPoints(
            ((point_list_opening_extrusion_area[0][0] - 0.2), (point_list_opening_extrusion_area[0][1] + 1.2)),
            ((point_list_opening_extrusion_area[0][0] + 1.3), (point_list_opening_extrusion_area[0][1] + 1.2)),
            ((point_list_opening_extrusion_area[0][0] + 1.3), (point_list_opening_extrusion_area[0][1])),
            ((point_list_opening_extrusion_area[0][0] - 0.2), point_list_opening_extrusion_area[0][1]))
        # print("door", door)

        # ------------------------------------------

        # wc and door Wall 1
        XPosPositionsWc = []
        XNotPositionsWc = []
        WcOutDoor = []
        ValuesX = []

        XContainsPositionsWc = []

        while x < point_10[0]:
            if x != point_10[0]:
                x = x + 0.2
                ValuesX.append(x)
            elif x == point_10[0]:
                break

        for valuesX in ValuesX:
            #print(valuesX)
            x = valuesX

            wc1 = (wc_1[0] + x, wc_1[1] + y)  # (1.1 + x, 0.2 + y)
            wc2 = (wc_2[0] + x, wc_2[1] + y)  # (1.1 + x, -0.5 + y)
            wc3 = (wc_3[0] + x, wc_3[1] + y)  # (-1.1 + x, -0.5 + y)
            wc4 = (wc_4[0] + x, wc_4[1] + y)  # (-1.1 + x, 0.2 + y)
            wc = InputPoints(wc1, wc2, wc3, wc4)


            WcCheck = PositionChecking(door[11], wc[11],
                                       wc[1], wc[3], wc[5], wc[7],
                                       wc[9], door[1], door[3], door[5], door[7])
            #print("WcCheck", WcCheck)
            if algo == 10:
                if WcCheck[-1] == True:
                    # print(x, "position")
                    # XPosPositionsWc.append(x)
                    if wallselwc == 1:
                        XPosPositionsWc.append(x)
                        wc1 = (wc_point_out_1[0] + x, wc_point_out_1[1] + y)
                        wc2 = (wc_point_out_2[0] + x, wc_point_out_2[1] + y)
                        wc3 = (wc_point_out_3[0] + x, wc_point_out_3[1] + y)
                        wc4 = (wc_point_out_4[0] + x, wc_point_out_4[1] + y)
                        wcOut = InputPoints(wc1, wc2, wc3, wc4)

                        DoorWcOutline = PositionChecking(door[11], wcOut[11],
                                                         wcOut[1], wcOut[3], wcOut[5], wcOut[7],
                                                         wcOut[9], door[1], door[3], door[5],
                                                         door[7])  # wcOut[1], wcOut[3], wcOut[5], wcOut[7]
                        # print("      DoorWcOutline", DoorWcOutline)
                        if DoorWcOutline[-1] == None:
                            # print("    position contains", x)
                            XPosPositionsWc.remove(x)
                    else:
                        XPosPositionsWc.append(x)

            if algo == 20:
                if WcCheck[-1] == False or WcCheck[-1] == None or WcCheck[-1] == True:
                    # print(x, "position not")
                    # WcOut darf nicht in der Area Door liegen.
                    if wallselwc == 1:
                       # XNotPositionsWc.append(x)
                        wc1 = (wc_point_out_1[0] + x, wc_point_out_1[1] + y)
                        wc2 = (wc_point_out_2[0] + x, wc_point_out_2[1] + y)
                        wc3 = (wc_point_out_3[0] + x, wc_point_out_3[1] + y)
                        wc4 = (wc_point_out_4[0] + x, wc_point_out_4[1] + y)
                        wcOut = InputPoints(wc1, wc2, wc3, wc4)

                        DoorWcOutline = PositionChecking(door[11], wcOut[11],
                                                         wcOut[1], wcOut[3], wcOut[5], wcOut[7],
                                                         wcOut[9], door[1], door[3], door[5],
                                                         door[7])  # wcOut[1], wcOut[3], wcOut[5], wcOut[7]
                        #print("      DoorWcOutline", DoorWcOutline)
                        if DoorWcOutline[-1] == True:
                            # print("    position contains", x)
                            XNotPositionsWc.append(x)

                    if wallselwc == 3:
                        XNotPositionsWc.append(x)
                        wc1 = (wc_point_out_1_3[0] + x, wc_point_out_1_3[1] + y)
                        wc2 = (wc_point_out_2_3[0] + x, wc_point_out_2_3[1] + y)
                        wc3 = (wc_point_out_3_3[0] + x, wc_point_out_3_3[1] + y)
                        wc4 = (wc_point_out_4_3[0] + x, wc_point_out_4_3[1] + y)
                        wcOut = InputPoints(wc1, wc2, wc3, wc4)

                        DoorWcOutline = PositionChecking(door[11], wcOut[11],
                                                         wcOut[1], wcOut[3], wcOut[5], wcOut[7],
                                                         wcOut[9], door[1], door[3], door[5],
                                                         door[7])  # wcOut[1], wcOut[3], wcOut[5], wcOut[7]
                        # print("      DoorWcOutline", DoorWcOutline)
                        if DoorWcOutline[-1] == True:
                            # print("    position contains", x)
                            XNotPositionsWc.append(x)

        #print("Pos Wc", XPosPositionsWc)
        #print("NotPos Wc", XNotPositionsWc)
        # print("ContPos Wc", XContainsPositions)

        # ------------------------------------------
        # ------------Check 2----------------
        XPosPositionsRoomandWc = []
        roomParams = []
        if algo == 10:
            #print("XPosPositionsWc", XPosPositionsWc)
            for xposwc in XPosPositionsWc:
                x = xposwc

                wc1 = (wc_1[0] + x, wc_1[1] + y)  # (1.1 + x, 0.2 + y)
                wc2 = (wc_2[0] + x, wc_2[1] + y)  # (1.1 + x, -0.5 + y)
                wc3 = (wc_3[0] + x, wc_3[1] + y)  # (-1.1 + x, -0.5 + y)
                wc4 = (wc_4[0] + x, wc_4[1] + y)  # (-1.1 + x, 0.2 + y)
                wc = InputPoints(wc1, wc2, wc3, wc4)
                #print(wc1,wc2,wc3,wc4)
                RoomWCCheck = PositionChecking(room[11], wc[11],
                                                 wc[1], wc[3], wc[5], wc[7],
                                                 wc[9], room[1], room[3], room[5], room[7])
                #print("wCrrii", RoomWCCheck, x)
                if RoomWCCheck[-1] == None:
                    # XSNotPositions.append()
                    # print(xs, "position")
                    XPosPositionsRoomandWc.append(x)

        if algo == 20:
            for xposwc in XNotPositionsWc:
                x = xposwc

                wc1 = (wc_1[0] + x, wc_1[1] + y)  # (1.1 + x, 0.2 + y)
                wc2 = (wc_2[0] + x, wc_2[1] + y)  # (1.1 + x, -0.5 + y)
                wc3 = (wc_3[0] + x, wc_3[1] + y)  # (-1.1 + x, -0.5 + y)
                wc4 = (wc_4[0] + x, wc_4[1] + y)  # (-1.1 + x, 0.2 + y)
                wc = InputPoints(wc1, wc2, wc3, wc4)
                # print(wc1,wc2,wc3,wc4)
                RoomWCCheck = PositionChecking(room[11], wc[11],
                                               wc[1], wc[3], wc[5], wc[7],
                                               wc[9], room[1], room[3], room[5], room[7])
                # print("wCrrii", RoomWCCheck)
                if RoomWCCheck[-1] == None:
                    # XSNotPositions.append()
                    # print(xs, "position")
                    XPosPositionsRoomandWc.append(x)
        #print("XPosPositionsRoomandWc", XPosPositionsRoomandWc)
        return XPosPositionsRoomandWc

    #freies ys
    def PositionSinkY(xs, ys, pt_1, pt_2, pt_3, pt_4):
        # sink and door Wall 1
        YSPosPositions = []
        YSNotPositions = []
        YSContainsPositions = []
        ValuesYS = []

        room = InputPoints(point_8, point_10, point_6, point_7)
        # print("room;", room)

        # wall1
        door = InputPoints(
            ((point_list_opening_extrusion_area[0][0] - 0.2), (point_list_opening_extrusion_area[0][1] + 1.2)),
            ((point_list_opening_extrusion_area[0][0] + 1.3), (point_list_opening_extrusion_area[0][1] + 1.2)),
            ((point_list_opening_extrusion_area[0][0] + 1.3), (point_list_opening_extrusion_area[0][1])),
            ((point_list_opening_extrusion_area[0][0] - 0.2), point_list_opening_extrusion_area[0][1]))
        # print("door", door)
        while ys < point_10[1]:
            if ys != point_10[1]:
                ys = ys + 0.2
                ValuesYS.append(ys)
            elif ys == point_10[1]:
                break

        for values in ValuesYS:
            #print(values)
            ys = values

            pt1 = (pt_1[0] + xs, pt_1[1] + ys)  # (-0.45 + xs, 0.275 + ys)
            pt2 = (pt_2[0] + xs, pt_2[1] + ys)  # (0.45 + xs, 0.275 + ys)
            pt3 = (pt_3[0] + xs, pt_3[1] + ys)  # (0.45 + xs, -0.275 + ys)
            pt4 = (pt_4[0] + xs, pt_4[1] + ys)  # (-0.45 + xs, -0.275 + ys)
            sink = InputPoints(pt1, pt2, pt3, pt4)

            SinkCheck = PositionChecking(door[11], sink[11],
                                         sink[1], sink[3], sink[5], sink[7],
                                         sink[9], door[1], door[3], door[5], door[7])
            #print("Hellp, ", SinkCheck)
            #if algo == 10:
            if SinkCheck[-1] == True:
                # XSNotPositions.append()
                # print(xs, "position")
                YSPosPositions.append(ys)
            #if algo == 20:
            if SinkCheck[-1] == False or SinkCheck[-1] == None or SinkCheck[-1] == True:
                #print(xs, "position not")
                if wallselsink ==  6:
                    pt1 = (sink_point_out_1_2[0] + xs, sink_point_out_1_2[1] + ys)
                    pt2 = (sink_point_out_2_2[0] + xs, sink_point_out_2_2[1] + ys)
                    pt3 = (sink_point_out_3_2[0] + xs, sink_point_out_3_2[1] + ys)
                    pt4 = (sink_point_out_4_2[0] + xs, sink_point_out_4_2[1] + ys)
                    sinkout = InputPoints(pt1, pt2, pt3, pt4)

                    DoorSinkOutline = PositionChecking(door[11], sinkout[11],
                                                     sinkout[1], sinkout[3], sinkout[5], sinkout[7],
                                                     sinkout[9], door[1], door[3], door[5],
                                                     door[7])
                    #print("      DoorSinkOutline", DoorSinkOutline)
                    if DoorSinkOutline[-1] == True:
                        # print("    position contains", x)
                        YSNotPositions.append(ys)

                if wallselsink ==  8:
                    pt1 = (sink_point_out_1_4[0] + xs, sink_point_out_1_4[1] + ys)
                    pt2 = (sink_point_out_2_4[0] + xs, sink_point_out_2_4[1] + ys)
                    pt3 = (sink_point_out_3_4[0] + xs, sink_point_out_3_4[1] + ys)
                    pt4 = (sink_point_out_4_4[0] + xs, sink_point_out_4_4[1] + ys)
                    sinkout = InputPoints(pt1, pt2, pt3, pt4)

                    DoorSinkOutline = PositionChecking(door[11], sinkout[11],
                                                     sinkout[1], sinkout[3], sinkout[5], sinkout[7],
                                                     sinkout[9], door[1], door[3], door[5],
                                                     door[7])
                    #print("      DoorSinkOutline", DoorSinkOutline)
                    if DoorSinkOutline[-1] == True:
                        # print("    position contains", x)
                        YSNotPositions.append(ys)



        #print("Pos sink", YSPosPositions)
        #print("NotPos sink", YSNotPositions)
        # print("ContPos sink", XSContainsPositions)
        # ------------------------------------------

        YSPosPositionsRoomandSink = []
        roomParams = []
        if algo == 10:
            for posSink in YSPosPositions:
                ys = posSink

                pt1 = (pt_1[0] + xs, pt_1[1] + ys)  # (-0.45 + xs, 0.275 + ys)
                pt2 = (pt_2[0] + xs, pt_2[1] + ys)  # (0.45 + xs, 0.275 + ys)
                pt3 = (pt_3[0] + xs, pt_3[1] + ys)  # (0.45 + xs, -0.275 + ys)
                pt4 = (pt_4[0] + xs, pt_4[1] + ys)  # (-0.45 + xs, -0.275 + ys)
                sink = InputPoints(pt1, pt2, pt3, pt4)
                """
                if  pt1[0] > point_8[0] and pt2[0] < point_10[0] :
                        YSPosPositionsRoomandSink.append(ys)
                        roomParams.append(YSPosPositionsRoomandSink)
                        #print("          ", XPosPositionsRoomandWc)
                elif pt1[0] < point_10[0] and pt2[0] > point_10[0]:
                    YSPosPositionsRoomandSink.append(ys)
                    roomParams.append(YSPosPositionsRoomandSink)
                """
                RoomSinkCheck = PositionChecking(room[11], sink[11],
                                                 sink[1], sink[3], sink[5], sink[7],
                                                 sink[9], room[1], room[3], room[5], room[7])
                #print(RoomSinkCheck)
                if RoomSinkCheck[-1] == None:
                    # print(xs, "position contains")
                    YSPosPositionsRoomandSink.append(ys)
                    roomParams.append(YSPosPositionsRoomandSink)

        if algo == 20:
            for posSink in YSNotPositions:
                ys = posSink

                pt1 = (pt_1[0] + xs, pt_1[1] + ys)  # (-0.45 + xs, 0.275 + ys)
                pt2 = (pt_2[0] + xs, pt_2[1] + ys)  # (0.45 + xs, 0.275 + ys)
                pt3 = (pt_3[0] + xs, pt_3[1] + ys)  # (0.45 + xs, -0.275 + ys)
                pt4 = (pt_4[0] + xs, pt_4[1] + ys)  # (-0.45 + xs, -0.275 + ys)
                sink = InputPoints(pt1, pt2, pt3, pt4)

                RoomSinkCheck = PositionChecking(room[11], sink[11],
                                                 sink[1], sink[3], sink[5], sink[7],
                                                 sink[9], room[1], room[3], room[5], room[7])
                # print(RoomSinkCheck)
                if RoomSinkCheck[-1] == None:
                    # print(xs, "position contains")
                    YSPosPositionsRoomandSink.append(ys)
                    roomParams.append(YSPosPositionsRoomandSink)

        return YSPosPositionsRoomandSink

    def PositionWcY(x, y, point_10, wc_1, wc_2, wc_3, wc_4):
        YPosPositionsWc = []
        YNotPositionsWc = []
        YContainsPositionsWc = []
        ValuesY = []

        while y < point_10[1]:
            if y != point_10[1]:
                y = y + 0.2
                ValuesY.append(y)
            elif y == point_10[1]:
                break

        for valuesY in ValuesY:
            # print(values)
            y = valuesY

            # wall2

            wc1 = (wc_1[0] + x, wc_1[1] + y)
            wc2 = (wc_2[0] + x, wc_2[1] + y)
            wc3 = (wc_3[0] + x, wc_3[1] + y)
            wc4 = (wc_4[0] + x, wc_4[1] + y)
            wc = InputPoints(wc1, wc2, wc3, wc4)

            WcCheck = PositionChecking(door[11], wc[11],
                                       wc[1], wc[3], wc[5], wc[7],
                                       wc[9], door[1], door[3], door[5], door[7])
            if algo == 10:
                if WcCheck[-1] == True:
                    # print(x, "position")
                    YPosPositionsWc.append(y)

            if algo == 20:
                if WcCheck[-1] == False or WcCheck[-1] == None or WcCheck[-1] ==True :
                    # print(x, "position not")
                    # WcOut darf nicht in der Area Door liegen.
                    if wallselwc == 2:
                        # XNotPositionsWc.append(x)
                        wc1 = (wc_point_out_1_2[0] + x, wc_point_out_1_2[1] + y)
                        wc2 = (wc_point_out_2_2[0] + x, wc_point_out_2_2[1] + y)
                        wc3 = (wc_point_out_3_2[0] + x, wc_point_out_3_2[1] + y)
                        wc4 = (wc_point_out_4_2[0] + x, wc_point_out_4_2[1] + y)
                        wcOut = InputPoints(wc1, wc2, wc3, wc4)

                        DoorWcOutline = PositionChecking(door[11], wcOut[11],
                                                         wcOut[1], wcOut[3], wcOut[5], wcOut[7],
                                                         wcOut[9], door[1], door[3], door[5],
                                                         door[7])  # wcOut[1], wcOut[3], wcOut[5], wcOut[7]
                        # print("      DoorWcOutline", DoorWcOutline)
                        if DoorWcOutline[-1] == True:
                            # print("    position contains", x)
                            YNotPositionsWc.append(y)

                    if wallselwc == 4:
                        #YNotPositionsWc.append(y)
                        wc1 = (wc_point_out_1_4[0] + x, wc_point_out_1_4[1] + y)
                        wc2 = (wc_point_out_2_4[0] + x, wc_point_out_2_4[1] + y)
                        wc3 = (wc_point_out_3_4[0] + x, wc_point_out_3_4[1] + y)
                        wc4 = (wc_point_out_4_4[0] + x, wc_point_out_4_4[1] + y)
                        wcOut = InputPoints(wc1, wc2, wc3, wc4)

                        DoorWcOutline = PositionChecking(door[11], wcOut[11],
                                                         wcOut[1], wcOut[3], wcOut[5], wcOut[7],
                                                         wcOut[9], door[1], door[3], door[5],
                                                         door[7])  # wcOut[1], wcOut[3], wcOut[5], wcOut[7]
                        # print("      DoorWcOutline", DoorWcOutline)
                        if DoorWcOutline[-1] == True:
                            # print("    position contains", x)
                            YNotPositionsWc.append(y)



        #print("Pos Wc", YPosPositionsWc)
        #print("NotPos Wc", YNotPositionsWc)
        # print("ContPos Wc", XContainsPositions)

        # ------------------------------------------

        # ------------------------------------------
        # ------------Check 2----------------
        YPosPositionsRoomandWc = []
        roomParams = []
        if algo == 10:
            for yposwc in YPosPositionsWc:
                y = yposwc

                wc1 = (wc_1[0] + x, wc_1[1] + y)  # (1.1 + x, 0.2 + y)
                wc2 = (wc_2[0] + x, wc_2[1] + y)  # (1.1 + x, -0.5 + y)
                wc3 = (wc_3[0] + x, wc_3[1] + y)  # (-1.1 + x, -0.5 + y)
                wc4 = (wc_4[0] + x, wc_4[1] + y)  # (-1.1 + x, 0.2 + y)
                wc = InputPoints(wc1, wc2, wc3, wc4)

                RoomWCCheck = PositionChecking(room[11], wc[11],
                                                 wc[1], wc[3], wc[5], wc[7],
                                                 wc[9], room[1], room[3], room[5], room[7])
                #print("wCrrii", RoomWCCheck)
                if RoomWCCheck[-1] == None:
                    # XSNotPositions.append()
                    # print(xs, "position")
                    YPosPositionsRoomandWc.append(y)
        if algo == 20:
            for yposwc in YNotPositionsWc:
                y = yposwc

                wc1 = (wc_1[0] + x, wc_1[1] + y)  # (1.1 + x, 0.2 + y)
                wc2 = (wc_2[0] + x, wc_2[1] + y)  # (1.1 + x, -0.5 + y)
                wc3 = (wc_3[0] + x, wc_3[1] + y)  # (-1.1 + x, -0.5 + y)
                wc4 = (wc_4[0] + x, wc_4[1] + y)  # (-1.1 + x, 0.2 + y)
                wc = InputPoints(wc1, wc2, wc3, wc4)

                RoomWCCheck = PositionChecking(room[11], wc[11],
                                               wc[1], wc[3], wc[5], wc[7],
                                               wc[9], room[1], room[3], room[5], room[7])
                # print("wCrrii", RoomWCCheck)
                if RoomWCCheck[-1] == None:
                    # XSNotPositions.append()
                    # print(xs, "position")
                    YPosPositionsRoomandWc.append(y)


        return YPosPositionsRoomandWc

    def PositionSinkX(xs, ys, pt_1, pt_2, pt_3, pt_4):
        # ------------Check 1----------------
        # sink and door Wall 1
        XSPosPositions = []
        XSNotPositions = []
        XSContainsPositions = []

        room = InputPoints(point_8, point_10, point_6, point_7)
        print("room;", room)

        # wall1
        door = InputPoints(
            ((point_list_opening_extrusion_area[0][0] - 0.2), (point_list_opening_extrusion_area[0][1] + 1.2)),
            ((point_list_opening_extrusion_area[0][0] + 1.3), (point_list_opening_extrusion_area[0][1] + 1.2)),
            ((point_list_opening_extrusion_area[0][0] + 1.3), (point_list_opening_extrusion_area[0][1])),
            ((point_list_opening_extrusion_area[0][0] - 0.2), point_list_opening_extrusion_area[0][1]))
        # print("door", door)
        while xs < point_10[0]:
            if xs != point_10[0]:
                xs = xs + 0.2
                ValuesXS.append(xs)
            elif xs == point_10[0]:
                break

        for values in ValuesXS:
            # print(values)
            xs = values

            pt1 = (pt_1[0] + xs, pt_1[1] + ys)  # (-0.45 + xs, 0.275 + ys)
            pt2 = (pt_2[0] + xs, pt_2[1] + ys)  # (0.45 + xs, 0.275 + ys)
            pt3 = (pt_3[0] + xs, pt_3[1] + ys)  # (0.45 + xs, -0.275 + ys)
            pt4 = (pt_4[0] + xs, pt_4[1] + ys)  # (-0.45 + xs, -0.275 + ys)
            sink = InputPoints(pt1, pt2, pt3, pt4)

            SinkCheck = PositionChecking(door[11], sink[11],
                                         sink[1], sink[3], sink[5], sink[7],
                                         sink[9], door[1], door[3], door[5], door[7])
            if algo == 10:
                if SinkCheck[-1] == True:
                    # XSNotPositions.append()
                    # print(xs, "position")
                    XSPosPositions.append(xs)

            if algo == 20:
                if SinkCheck[-1] == False or SinkCheck[-1] == None or SinkCheck[-1] == True:
                    # print(xs, "position not")
                    if wallselsink == 5:
                        pt1 = (sink_point_out_1[0] + xs, sink_point_out_1[1] + ys)
                        pt2 = (sink_point_out_2[0] + xs, sink_point_out_2[1] + ys)
                        pt3 = (sink_point_out_3[0] + xs, sink_point_out_3[1] + ys)
                        pt4 = (sink_point_out_4[0] + xs, sink_point_out_4[1] + ys)
                        sinkout = InputPoints(pt1, pt2, pt3, pt4)

                        DoorSinkOutline = PositionChecking(door[11], sinkout[11],
                                                           sinkout[1], sinkout[3], sinkout[5], sinkout[7],
                                                           sinkout[9], door[1], door[3], door[5],
                                                           door[7])
                        # print("      DoorSinkOutline", DoorSinkOutline)
                        if DoorSinkOutline[-1] == True:
                            # print("    position contains", x)
                            XSNotPositions.append(xs)

                    if wallselsink == 7:
                        pt1 = (sink_point_out_1_3[0] + xs, sink_point_out_1_3[1] + ys)
                        pt2 = (sink_point_out_2_3[0] + xs, sink_point_out_2_3[1] + ys)
                        pt3 = (sink_point_out_3_3[0] + xs, sink_point_out_3_3[1] + ys)
                        pt4 = (sink_point_out_4_3[0] + xs, sink_point_out_4_3[1] + ys)
                        sinkout = InputPoints(pt1, pt2, pt3, pt4)

                        DoorSinkOutline = PositionChecking(door[11], sinkout[11],
                                                           sinkout[1], sinkout[3], sinkout[5], sinkout[7],
                                                           sinkout[9], door[1], door[3], door[5],
                                                           door[7])
                        # print("      DoorSinkOutline", DoorSinkOutline)
                        if DoorSinkOutline[-1] == True:
                            # print("    position contains", x)
                            XSNotPositions.append(xs)

        print("Pos sinkX", XSPosPositions)
        # print("NotPos sink", XSNotPositions)
        # print("ContPos sink", XSContainsPositions)
        # ------------------------------------------
        XSPosPositionsRoomandSink = []
        roomParams = []
        if algo == 10:
            for posSink in XSPosPositions:
                xs = posSink
                #print(posSink)
                pt1 = (pt_1[0] + xs, pt_1[1] + ys)  # (-0.45 + xs, 0.275 + ys)
                pt2 = (pt_2[0] + xs, pt_2[1] + ys)  # (0.45 + xs, 0.275 + ys)
                pt3 = (pt_3[0] + xs, pt_3[1] + ys)  # (0.45 + xs, -0.275 + ys)
                pt4 = (pt_4[0] + xs, pt_4[1] + ys)  # (-0.45 + xs, -0.275 + ys)
                sink = InputPoints(pt1, pt2, pt3, pt4)
                #print(pt1,pt2,pt3,pt4)

                RoomSinkCheck = PositionChecking(room[11], sink[11],
                                                 sink[1], sink[3], sink[5], sink[7],
                                                 sink[9], room[1], room[3], room[5], room[7])
                #print(RoomSinkCheck)

                if RoomSinkCheck[-1] == None:
                    # print(xs, "position contains")
                    XSPosPositionsRoomandSink.append(xs)
                    roomParams.append(XSPosPositionsRoomandSink)

        if algo == 20:
            for posSink in XSNotPositions:
                xs = posSink
                # print(posSink)
                pt1 = (pt_1[0] + xs, pt_1[1] + ys)  # (-0.45 + xs, 0.275 + ys)
                pt2 = (pt_2[0] + xs, pt_2[1] + ys)  # (0.45 + xs, 0.275 + ys)
                pt3 = (pt_3[0] + xs, pt_3[1] + ys)  # (0.45 + xs, -0.275 + ys)
                pt4 = (pt_4[0] + xs, pt_4[1] + ys)  # (-0.45 + xs, -0.275 + ys)
                sink = InputPoints(pt1, pt2, pt3, pt4)
                # print(pt1,pt2,pt3,pt4)

                RoomSinkCheck = PositionChecking(room[11], sink[11],
                                                 sink[1], sink[3], sink[5], sink[7],
                                                 sink[9], room[1], room[3], room[5], room[7])
                # print(RoomSinkCheck)

                if RoomSinkCheck[-1] == None:
                    # print(xs, "position contains")
                    XSPosPositionsRoomandSink.append(xs)
                    roomParams.append(XSPosPositionsRoomandSink)

        return XSPosPositionsRoomandSink

        # ------------------------------------------

        # wc and door Wall 1

    def WCXandSinkY(xs, y, Sink, Klo, pt_1, pt_2, pt_3, pt_4, wc_1, wc_2, wc_3, wc_4, wc_point_out_1,
                    wc_point_out_2, wc_point_out_3, wc_point_out_4,
                    sink_point_out_1, sink_point_out_2, sink_point_out_3,sink_point_out_4):
        XValues = []
        YSValues = []
        XMoveValues = []
        YSMoveValues = []
        Positions = []

        for xpos in Klo:
            for yspos in Sink:
                x = xpos
                #print(AlgoInt)
                # wall2
                wc1 = (wc_1[0] + x, wc_1[1] + y)
                wc2 = (wc_2[0] + x, wc_2[1] + y)
                wc3 = (wc_3[0] + x, wc_3[1] + y)
                wc4 = (wc_4[0] + x, wc_4[1] + y)
                wc = InputPoints(wc1, wc2, wc3, wc4)

                # ---------------------------------

                ys = yspos
                pt1 = (pt_1[0] + xs, pt_1[1] + ys)  # (-0.45 + xs, 0.275 + ys)
                pt2 = (pt_2[0] + xs, pt_2[1] + ys)  # (0.45 + xs, 0.275 + ys)
                pt3 = (pt_3[0] + xs, pt_3[1] + ys)  # (0.45 + xs, -0.275 + ys)
                pt4 = (pt_4[0] + xs, pt_4[1] + ys)  # (-0.45 + xs, -0.275 + ys)
                sink = InputPoints(pt1, pt2, pt3, pt4)

                # ----------------------------
                wc1 = (wc_point_out_1[0] + x, wc_point_out_1[1] + y)
                wc2 = (wc_point_out_2[0] + x, wc_point_out_2[1] + y)
                wc3 = (wc_point_out_3[0] + x, wc_point_out_3[1] + y)
                wc4 = (wc_point_out_4[0] + x, wc_point_out_4[1] + y)
                wcOut = InputPoints(wc1, wc2, wc3, wc4)
                # ----------------------------
                pt1 = (sink_point_out_1[0] + xs, sink_point_out_1[1] + ys)  # (-0.45 + xs, 0.275 + ys)
                pt2 = (sink_point_out_2[0] + xs, sink_point_out_2[1] + ys)  # (0.45 + xs, 0.275 + ys)
                pt3 = (sink_point_out_3[0] + xs, sink_point_out_3[1] + ys)  # (0.45 + xs, -0.275 + ys)
                pt4 = (sink_point_out_4[0] + xs, sink_point_out_4[1] + ys)  # (-0.45 + xs, -0.275 + ys)
                sinkout = InputPoints(pt1, pt2, pt3, pt4)
                # ----------------------------
                if algo == 10:
                    SinkWCCheckUpdate = PositionChecking(wc[11], sink[11],
                                                         sink[1], sink[3], sink[5], sink[7],
                                                         sink[9], wc[1], wc[3], wc[5], wc[7])
                    #print("""Ddd""",SinkWCCheckUpdate )

                    #print("WCSNK",SinkWCCheckUpdate)
                    if SinkWCCheckUpdate[-1] == True:
                        # print(xs, "position", x)
                        XValues.append(x)
                        YSValues.append(ys)
                        Positions.append(YSValues)
                        Positions.append(XValues)
                        # print(Positions, "Positions")"""

                if algo == 20:

                        SinkWcOutline = PositionChecking(sink[11], wcOut[11],
                                                         wcOut[1], wcOut[3], wcOut[5], wcOut[7],
                                                         wcOut[9], sink[1], sink[3], sink[5],
                                                         sink[7])  # wcOut[1], wcOut[3], wcOut[5], wcOut[7]
                        #print("      SnkWcOutline", SinkWcOutline)


                        WcSinkOutline = PositionChecking(sinkout[11], wc[11],
                                                         wc[1], wc[3], wc[5], wc[7],
                                                         wc[9], sinkout[1], sinkout[3], sinkout[5],
                                                         sinkout[7])
                        #print("      SnkWcOutline", WcSinkOutline)

                        if SinkWcOutline[-1] == True and WcSinkOutline[-1] == True :
                            # print("WCSNK", SinkWcOutline)
                            # print(xs, "position", x)
                            XValues.append(x)
                            YSValues.append(ys)
                            Positions.append(YSValues)
                            Positions.append(XValues)


                        # print(Positions, "Positions")"""
        if algo == 10:
            coords = random.randint(0, len(Positions[0]))
            print(coords)
            coordsx = coords + 1
            print(coordsx)

            ys = Positions[0][coords]
            x = Positions[1][coordsx]
            if ys == None or x == None:
                print("Error positioning not possible")
            else:
                print("sink position: ", ys)
                print("wc position: ", x)
                print("number of possible solutions: ", len(Positions[0]))

        if algo == 20:
            ys = min(Positions[0])
            x = min(Positions[1])
            print("sink position: ", ys)
            print("wc position: ", x)


        return ys, x, Positions

    def WCYandSinkX(x, ys, Sink, Klo, pt_1, pt_2, pt_3, pt_4, wc_1, wc_2, wc_3, wc_4, wc_point_out_1,
                    wc_point_out_2, wc_point_out_3, wc_point_out_4,
                    sink_point_out_1, sink_point_out_2, sink_point_out_3,sink_point_out_4):
        XValues = []
        YSValues = []
        Positions = []
        for xspos in Sink:
            for ypos in Klo:
                xs = xspos
                y = ypos
                # wall2
                wc1 = (wc_1[0] + x, wc_1[1] + y)
                wc2 = (wc_2[0] + x, wc_2[1] + y)
                wc3 = (wc_3[0] + x, wc_3[1] + y)
                wc4 = (wc_4[0] + x, wc_4[1] + y)
                wc = InputPoints(wc1, wc2, wc3, wc4)
                # ---------------------------------
                pt1 = (pt_1[0] + xs, pt_1[1] + ys)  # (-0.45 + xs, 0.275 + ys)
                pt2 = (pt_2[0] + xs, pt_2[1] + ys)  # (0.45 + xs, 0.275 + ys)
                pt3 = (pt_3[0] + xs, pt_3[1] + ys)  # (0.45 + xs, -0.275 + ys)
                pt4 = (pt_4[0] + xs, pt_4[1] + ys)  # (-0.45 + xs, -0.275 + ys)
                sink = InputPoints(pt1, pt2, pt3, pt4)
                # ----------------------------

                wc1 = (wc_point_out_1[0] + x, wc_point_out_1[1] + y)
                wc2 = (wc_point_out_2[0] + x, wc_point_out_2[1] + y)
                wc3 = (wc_point_out_3[0] + x, wc_point_out_3[1] + y)
                wc4 = (wc_point_out_4[0] + x, wc_point_out_4[1] + y)
                wcOut = InputPoints(wc1, wc2, wc3, wc4)
                # ----------------------------
                pt1 = (sink_point_out_1[0] + xs, sink_point_out_1[1] + ys)  # (-0.45 + xs, 0.275 + ys)
                pt2 = (sink_point_out_2[0] + xs, sink_point_out_2[1] + ys)  # (0.45 + xs, 0.275 + ys)
                pt3 = (sink_point_out_3[0] + xs, sink_point_out_3[1] + ys)  # (0.45 + xs, -0.275 + ys)
                pt4 = (sink_point_out_4[0] + xs, sink_point_out_4[1] + ys)  # (-0.45 + xs, -0.275 + ys)
                sinkout = InputPoints(pt1, pt2, pt3, pt4)
                # ----------------------------
                if algo == 10:
                    SinkWCCheckUpdate = PositionChecking(wc[11], sink[11],
                                                         sink[1], sink[3], sink[5], sink[7],
                                                         sink[9], wc[1], wc[3], wc[5], wc[7])

                    # print(SinkWCCheckUpdate)
                    if SinkWCCheckUpdate[-1] == True:
                        # print(xs, "position", x)
                        XValues.append(xs)
                        YSValues.append(y)
                        Positions.append(YSValues)
                        Positions.append(XValues)
                        # print(Positions, "Positions")
                if algo == 20:

                        SinkWcOutline = PositionChecking(sink[11], wcOut[11],
                                                         wcOut[1], wcOut[3], wcOut[5], wcOut[7],
                                                         wcOut[9], sink[1], sink[3], sink[5],
                                                         sink[7])  # wcOut[1], wcOut[3], wcOut[5], wcOut[7]
                        #print("      SnkWcOutline", SinkWcOutline)


                        WcSinkOutline = PositionChecking(sinkout[11], wc[11],
                                                         wc[1], wc[3], wc[5], wc[7],
                                                         wc[9], sinkout[1], sinkout[3], sinkout[5],
                                                         sinkout[7])
                        #print("      SnkWcOutline", WcSinkOutline)

                        if SinkWcOutline[-1] == True and WcSinkOutline[-1] == True :
                            # print("WCSNK", SinkWcOutline)
                            # print(xs, "position", x)
                            XValues.append(xs)
                            YSValues.append(y)
                            Positions.append(YSValues)
                            Positions.append(XValues)

        if algo == 10:
            coords = random.randint(0, len(Positions[0]))
            print(coords)
            coordsx = coords + 1
            print(coordsx)

            y = Positions[0][coords]
            xs = Positions[1][coordsx]
            if y == None or xs == None:
                print("Error positioning not possible")
            else:
                print("sink position: ", xs)
                print("wc position: ", y)
                print("number of possible solutions: ", len(Positions[0]))
        if algo == 20:
            coords = random.randint(0, len(Positions[0]))
            print(coords)
            coordsx = coords + 1
            print(coordsx)

            y = Positions[0][coords]
            xs = Positions[1][coordsx]
            if y == None or xs == None:
                print("Error positioning not possible")
            else:
                print("sink position: ", xs)
                print("wc position: ", y)
                print("number of possible solutions: ", len(Positions[0]))
            """     
            y = min(Positions[0])
            xs = min(Positions[1])
            print("sink position: ", xs)
            print("wc position: ", y)"""

        return y, xs, Positions

    def WCXandSinkX(ys, y, Sink, Klo, pt_1, pt_2, pt_3, pt_4, wc_1, wc_2, wc_3, wc_4, wc_point_out_1,
                    wc_point_out_2, wc_point_out_3, wc_point_out_4,
                    sink_point_out_1, sink_point_out_2, sink_point_out_3,sink_point_out_4):
        XValues = []
        YSValues = []
        Positions = []
        for xpos in Klo:
            for xspos in Sink:
                x = xpos
                # wall2
                wc1 = (wc_1[0] + x, wc_1[1] + y)
                wc2 = (wc_2[0] + x, wc_2[1] + y)
                wc3 = (wc_3[0] + x, wc_3[1] + y)
                wc4 = (wc_4[0] + x, wc_4[1] + y)
                wc = InputPoints(wc1, wc2, wc3, wc4)
                # ---------------------------------
                xs = xspos
                pt1 = (pt_1[0] + xs, pt_1[1] + ys)  # (-0.45 + xs, 0.275 + ys)
                pt2 = (pt_2[0] + xs, pt_2[1] + ys)  # (0.45 + xs, 0.275 + ys)
                pt3 = (pt_3[0] + xs, pt_3[1] + ys)  # (0.45 + xs, -0.275 + ys)
                pt4 = (pt_4[0] + xs, pt_4[1] + ys)  # (-0.45 + xs, -0.275 + ys)
                sink = InputPoints(pt1, pt2, pt3, pt4)
                # ----------------------------
                wc1 = (wc_point_out_1[0] + x, wc_point_out_1[1] + y)
                wc2 = (wc_point_out_2[0] + x, wc_point_out_2[1] + y)
                wc3 = (wc_point_out_3[0] + x, wc_point_out_3[1] + y)
                wc4 = (wc_point_out_4[0] + x, wc_point_out_4[1] + y)
                wcOut = InputPoints(wc1, wc2, wc3, wc4)
                # ----------------------------
                pt1 = (sink_point_out_1[0] + xs, sink_point_out_1[1] + ys)  # (-0.45 + xs, 0.275 + ys)
                pt2 = (sink_point_out_2[0] + xs, sink_point_out_2[1] + ys)  # (0.45 + xs, 0.275 + ys)
                pt3 = (sink_point_out_3[0] + xs, sink_point_out_3[1] + ys)  # (0.45 + xs, -0.275 + ys)
                pt4 = (sink_point_out_4[0] + xs, sink_point_out_4[1] + ys)  # (-0.45 + xs, -0.275 + ys)
                sinkout = InputPoints(pt1, pt2, pt3, pt4)
                # ----------------------------
                if algo == 10:

                    SinkWCCheckUpdate = PositionChecking(wc[11], sink[11],
                                                         sink[1], sink[3], sink[5], sink[7],
                                                         sink[9], wc[1], wc[3], wc[5], wc[7])

                    #print(SinkWCCheckUpdate, xs, x)
                    if SinkWCCheckUpdate[-1] == True:
                        # print(xs, "position", x)
                        XValues.append(x)
                        YSValues.append(xs)
                        Positions.append(YSValues)
                        Positions.append(XValues)
                        #print(Positions, "Positions")
                if algo == 20:

                    SinkWcOutline = PositionChecking(sink[11], wcOut[11],
                                                     wcOut[1], wcOut[3], wcOut[5], wcOut[7],
                                                     wcOut[9], sink[1], sink[3], sink[5],
                                                     sink[7])  # wcOut[1], wcOut[3], wcOut[5], wcOut[7]
                    # print("      SnkWcOutline", SinkWcOutline)

                    WcSinkOutline = PositionChecking(sinkout[11], wc[11],
                                                     wc[1], wc[3], wc[5], wc[7],
                                                     wc[9], sinkout[1], sinkout[3], sinkout[5],
                                                     sinkout[7])
                    # print("      SnkWcOutline", WcSinkOutline)

                    if SinkWcOutline[-1] == True and WcSinkOutline[-1] == True:
                        # print("WCSNK", SinkWcOutline)
                        # print(xs, "position", x)
                        XValues.append(x)
                        YSValues.append(xs)
                        Positions.append(YSValues)
                        Positions.append(XValues)

        if algo == 10:
            coords = random.randint(0, (len(Positions[0])-1))
            print(coords)
            coordsx = coords + 1
            print(coordsx)

            xs = Positions[0][coords]
            x = Positions[1][coordsx]
            if xs == None or x == None:
                print("Error positioning not possible")
            else:
                print("sink position: ", xs)
                print("wc position: ", x)
                print("number of possible solutions: ", len(Positions[0]))

        if algo == 20:
            xs = min(Positions[0])
            x = min(Positions[1])
            print("sink position: ", xs)
            print("wc position: ", x)
        return xs, x, Positions

    def WCYandSinkY(x, xs, Sink, Klo, pt_1, pt_2, pt_3, pt_4, wc_1, wc_2, wc_3, wc_4, wc_point_out_1,
                    wc_point_out_2, wc_point_out_3, wc_point_out_4,
                    sink_point_out_1, sink_point_out_2, sink_point_out_3,sink_point_out_4):
        XValues = []
        YSValues = []
        Positions = []
        for yspos in Sink:
            for ypos in Klo:
                ys = yspos
                y = ypos
                # wall2
                wc1 = (wc_1[0] + x, wc_1[1] + y)
                wc2 = (wc_2[0] + x, wc_2[1] + y)
                wc3 = (wc_3[0] + x, wc_3[1] + y)
                wc4 = (wc_4[0] + x, wc_4[1] + y)
                wc = InputPoints(wc1, wc2, wc3, wc4)
                # ---------------------------------
                pt1 = (pt_1[0] + xs, pt_1[1] + ys)  # (-0.45 + xs, 0.275 + ys)
                pt2 = (pt_2[0] + xs, pt_2[1] + ys)  # (0.45 + xs, 0.275 + ys)
                pt3 = (pt_3[0] + xs, pt_3[1] + ys)  # (0.45 + xs, -0.275 + ys)
                pt4 = (pt_4[0] + xs, pt_4[1] + ys)  # (-0.45 + xs, -0.275 + ys)
                sink = InputPoints(pt1, pt2, pt3, pt4)
                # ----------------------------
                wc1 = (wc_point_out_1[0] + x, wc_point_out_1[1] + y)
                wc2 = (wc_point_out_2[0] + x, wc_point_out_2[1] + y)
                wc3 = (wc_point_out_3[0] + x, wc_point_out_3[1] + y)
                wc4 = (wc_point_out_4[0] + x, wc_point_out_4[1] + y)
                wcOut = InputPoints(wc1, wc2, wc3, wc4)
                # ----------------------------
                pt1 = (sink_point_out_1[0] + xs, sink_point_out_1[1] + ys)  # (-0.45 + xs, 0.275 + ys)
                pt2 = (sink_point_out_2[0] + xs, sink_point_out_2[1] + ys)  # (0.45 + xs, 0.275 + ys)
                pt3 = (sink_point_out_3[0] + xs, sink_point_out_3[1] + ys)  # (0.45 + xs, -0.275 + ys)
                pt4 = (sink_point_out_4[0] + xs, sink_point_out_4[1] + ys)  # (-0.45 + xs, -0.275 + ys)
                sinkout = InputPoints(pt1, pt2, pt3, pt4)
                # ----------------------------
                if algo == 10:
                    SinkWCCheckUpdate = PositionChecking(wc[11], sink[11],
                                                         sink[1], sink[3], sink[5], sink[7],
                                                         sink[9], wc[1], wc[3], wc[5], wc[7])

                    # print(SinkWCCheckUpdate)
                    if SinkWCCheckUpdate[-1] == True:
                        # print(xs, "position", x)
                        XValues.append(ys)
                        YSValues.append(y)
                        Positions.append(YSValues)
                        Positions.append(XValues)
                        # print(Positions, "Positions")
                if algo == 20:

                    SinkWcOutline = PositionChecking(sink[11], wcOut[11],
                                                     wcOut[1], wcOut[3], wcOut[5], wcOut[7],
                                                     wcOut[9], sink[1], sink[3], sink[5],
                                                     sink[7])  # wcOut[1], wcOut[3], wcOut[5], wcOut[7]
                    # print("      SnkWcOutline", SinkWcOutline)

                    WcSinkOutline = PositionChecking(sinkout[11], wc[11],
                                                     wc[1], wc[3], wc[5], wc[7],
                                                     wc[9], sinkout[1], sinkout[3], sinkout[5],
                                                     sinkout[7])
                    # print("      SnkWcOutline", WcSinkOutline)

                    if SinkWcOutline[-1] == True and WcSinkOutline[-1] == True:
                        # print("WCSNK", SinkWcOutline)
                        # print(xs, "position", x)
                        XValues.append(ys)
                        YSValues.append(y)
                        Positions.append(YSValues)
                        Positions.append(XValues)

        if algo == 10 :
            coords = random.randint(0, len(Positions[0]))
            print(coords)
            coordsx = coords + 1
            print(coordsx)

            y = Positions[0][coords]
            ys = Positions[1][coordsx]
            if y == None or ys == None:
                print("Error positioning not possible")
            else:
                print("sink position: ", ys)
                print("wc position: ", y)
                print("number of possible solutions: ", len(Positions[0]))

        if algo == 20:
            print(20)
            """
            y = min(Positions[0])
            ys = min(Positions[1])
            print("sink position: ", ys)
            print("wc position: ", y)"""
        return y, ys, Positions

    #-----------MOVEAREA ALGORITHMUS-------------
    def MoveareaWCX(x , y, xm, ym, xs, ys, sink_point_out_1, sink_point_out_2, sink_point_out_3, sink_point_out_4):
        ValuesXM = []
        PosMoveAreaRoom = []
        PosMoveArea = []
        room = InputPoints(point_8, point_10, point_6, point_7)
        while xm < point_10[0]:
            if xm != point_10[0]:
                xm = xm + 0.2
                ValuesXM.append(xm)
            elif xm == point_10[0]:
                break

        for valuesxm in ValuesXM:
            xm = valuesxm

            moveAA = (0.75 + xm, 0.75 + ym)
            moveBB = (0.75 + xm, -0.75 + ym)
            moveCC = (-0.75 + xm, -0.75 + ym)
            moveDD = (-0.75 + xm, 0.75 + ym)
            #print("MOVE", moveAA, moveBB, moveCC, moveDD)
            move = InputPoints(moveAA, moveBB, moveCC, moveDD)

            moveandroom = PositionChecking(room[11], move[11],
                                           move[1], move[3], move[5], move[7],
                                           move[9], room[1], room[3], room[5], room[7])
            #print("      moveandroom", moveandroom, xm)
            if moveandroom[-1] == None:
                PosMoveAreaRoom.append(xm)
            #print(PosMoveAreaRoom)

        for valuesXM in PosMoveAreaRoom:
            #print(valuesX)
            xm = valuesXM
            if wallselwc == 1:
                wc1 = (wc_point_out_1[0] + x, wc_point_out_1[1] + y)
                wc2 = (wc_point_out_2[0] + x, wc_point_out_2[1] + y)
                wc3 = (wc_point_out_3[0] + x, wc_point_out_3[1] + y)
                wc4 = (wc_point_out_4[0] + x, wc_point_out_4[1] + y)
                #print("WCOUT",wc1,wc2,wc3,wc4)
                wcOut = InputPoints(wc1, wc2, wc3, wc4)

            if wallselwc == 3:
                wc1 = (wc_point_out_1_3[0] + x, wc_point_out_1_3[1] + y)
                wc2 = (wc_point_out_2_3[0] + x, wc_point_out_2_3[1] + y)
                wc3 = (wc_point_out_3_3[0] + x, wc_point_out_3_3[1] + y)
                wc4 = (wc_point_out_4_3[0] + x, wc_point_out_4_3[1] + y)
                #print("WCOUT",wc1,wc2,wc3,wc4)
                wcOut = InputPoints(wc1, wc2, wc3, wc4)

            moveAA = (0.75 + xm, 0.75 + ym  )
            moveBB = (0.75 + xm, -0.75 + ym)
            moveCC = (-0.75 + xm, -0.75 + ym )
            moveDD = (-0.75 + xm, 0.75 + ym )
            #print("MOVE", moveAA, moveBB, moveCC, moveDD)

            wcOutListX = [moveAA[0], moveBB[0], moveCC[0], moveDD[0]]
            wcOutListY = [moveAA[1], moveBB[1], moveCC[1], moveDD[1]]
            maxX = max(wcOutListX)
            maxY = max(wcOutListY)
            minX = min(wcOutListX)
            minY = min(wcOutListY)

            poi1 = PointInPolygon(wc1[0],wc1[1], minX, maxX, minY, maxY)
            poi2 = PointInPolygon(wc2[0], wc2[1], minX, maxX, minY, maxY)
            #print(poi1, poi2)

            if poi1 == True and poi2 == True:
                PosMoveArea.append(xm)

            move = InputPoints(moveAA, moveBB, moveCC, moveDD)

            # wenn Punkte von move == punkte von wcOut bei gleichbleibendem y Wert
            moveanddoor = PositionChecking(door[11], move[11],
                                         move[1], move[3], move[5], move[7],
                                         move[9], door[1], door[3],door[5], door[7])
            #print("moveandwcc", moveanddoor)
            if moveanddoor[-1] == False:
                if xm in PosMoveArea:
                    PosMoveArea.append(xm)

            pt1 = (sink_point_out_1[0] + xs, sink_point_out_1[1] + ys)  # (-0.45 + xs, 0.275 + ys)
            pt2 = (sink_point_out_2[0] + xs, sink_point_out_2[1] + ys)  # (0.45 + xs, 0.275 + ys)
            pt3 = (sink_point_out_3[0] + xs, sink_point_out_3[1] + ys)  # (0.45 + xs, -0.275 + ys)
            pt4 = (sink_point_out_4[0] + xs, sink_point_out_4[1] + ys)  # (-0.45 + xs, -0.275 + ys)
            sinkout = InputPoints(pt1, pt2, pt3, pt4)


            moveandsink = PositionChecking(sinkout[11], move[11],
                                           move[1], move[3], move[5], move[7],
                                           move[9], sinkout[1], sinkout[3], sinkout[5], sinkout[7])
            #print("moveandsink", moveandsink)
            if moveandsink[-1] == False or moveandsink[-1] == None:
                if xm in PosMoveArea:
                    PosMoveArea.remove(xm)

        #print(PosMoveArea)
        if len(PosMoveArea) == 0:
            return False
        else:
            return PosMoveArea


    def MoveareaSinkX(x, y, xms, yms, xs, ys, wc_point_out1, wc_point_out2,wc_point_out3, wc_point_out4):
        ValuesXM = []
        PosMoveAreaRoom = []
        PosMoveArea = []
        PosMoveAreaLast = []
        room = InputPoints(point_8, point_10, point_6, point_7)
        while xms < point_10[0]:
            if xms != point_10[0]:
                xms = xms + 0.2
                ValuesXM.append(xms)
            elif xms == point_10[0]:
                break

        for valuesxms in ValuesXM:
            xms = valuesxms

            moveAA = (0.75 + xms, 0.75 + yms)
            moveBB = (0.75 + xms, -0.75 + yms)
            moveCC = (-0.75 + xms, -0.75 + yms)
            moveDD = (-0.75 + xms, 0.75 + yms)
            #print("MOVE", moveAA, moveBB, moveCC, moveDD)
            move = InputPoints(moveAA, moveBB, moveCC, moveDD)

            moveandroom = PositionChecking(room[11], move[11],
                                           move[1], move[3], move[5], move[7],
                                           move[9], room[1], room[3], room[5], room[7])
            #print("      moveandroom", moveandroom, xms)
            if moveandroom[-1] == None:
                PosMoveAreaRoom.append(xms)
            #print(PosMoveAreaRoom)
        for valuesXMS in PosMoveAreaRoom:
            xms = valuesXMS
            if wallselsink == 7:
                pt1 = (sink_point_out_1_3[0] + xs, sink_point_out_1_3[1] + ys)  # (-0.45 + xs, 0.275 + ys)
                pt2 = (sink_point_out_2_3[0] + xs, sink_point_out_2_3[1] + ys)  # (0.45 + xs, 0.275 + ys)
                pt3 = (sink_point_out_3_3[0] + xs, sink_point_out_3_3[1] + ys)  # (0.45 + xs, -0.275 + ys)
                pt4 = (sink_point_out_4_3[0] + xs, sink_point_out_4_3[1] + ys)  # (-0.45 + xs, -0.275 + ys)
                sinkout = InputPoints(pt1, pt2, pt3, pt4)

            if wallselsink == 5:
                pt1 = (sink_point_out_1[0] + xs, sink_point_out_1[1] + ys)  # (-0.45 + xs, 0.275 + ys)
                pt2 = (sink_point_out_2[0] + xs, sink_point_out_2[1] + ys)  # (0.45 + xs, 0.275 + ys)
                pt3 = (sink_point_out_3[0] + xs, sink_point_out_3[1] + ys)  # (0.45 + xs, -0.275 + ys)
                pt4 = (sink_point_out_4[0] + xs, sink_point_out_4[1] + ys)  # (-0.45 + xs, -0.275 + ys)
                sinkout = InputPoints(pt1, pt2, pt3, pt4)
            #print("           ",pt1, pt2, pt3, pt4)


            moveAA = (0.75 + xms, 0.75 + yms)
            moveBB = (0.75 + xms, -0.75 + yms)
            moveCC = (-0.75 + xms, -0.75 + yms)
            moveDD = (-0.75 + xms, 0.75 + yms)
            #print("MOVE", moveAA, moveBB, moveCC, moveDD)


            wcOutListX = [moveAA[0], moveBB[0], moveCC[0], moveDD[0]]
            wcOutListY = [moveAA[1], moveBB[1], moveCC[1], moveDD[1]]
            maxX = max(wcOutListX)
            maxY = max(wcOutListY)
            minX = min(wcOutListX)
            minY = min(wcOutListY)


            poi1 = PointInPolygon(pt1[0], pt1[1], minX, maxX, minY, maxY)
            poi2 = PointInPolygon(pt2[0], pt2[1], minX, maxX, minY, maxY)
            #print(poi1, poi2)

            if poi1 == True and poi2 == True:
                PosMoveArea.append(xms)

            move = InputPoints(moveAA, moveBB, moveCC, moveDD)

            # wenn Punkte von move == punkte von wcOut bei gleichbleibendem y Wert
            moveanddoor = PositionChecking(door[11], move[11],
                                           move[1], move[3], move[5], move[7],
                                           move[9], door[1], door[3], door[5], door[7])
            # print("moveandwcc", moveanddoor)
            if moveanddoor[-1] == False:
                if xms in PosMoveArea:
                    PosMoveArea.append(xms)


            wc1 = (wc_point_out1[0] + x, wc_point_out1[1] + y)
            wc2 = (wc_point_out2[0] + x, wc_point_out2[1] + y)
            wc3 = (wc_point_out3[0] + x, wc_point_out3[1] + y)
            wc4 = (wc_point_out4[0] + x, wc_point_out4[1] + y)
            #print("WCOUT2", wc1, wc2, wc3, wc4)
            wcOut = InputPoints(wc1, wc2, wc3, wc4)


            moveandWC = PositionChecking(move[11], wcOut[11],
                                           wcOut[1], wcOut[3], wcOut[5], wcOut[7],
                                           wcOut[9], move[1], move[3], move[5], move[7])
            #print("moveandWC", moveandWC, xms)
            if moveandWC[-1] == True:
                PosMoveAreaLast.append(xms)
            if moveandWC[-1] == False or moveandWC[-1] == None:
                for val in PosMoveArea:
                    if xms == val:
                        PosMoveArea.remove(val)

        print("PosMoveAreaLast", PosMoveAreaLast)
        print("PosMoveArea2", PosMoveArea)
        for values in PosMoveArea:
            if values not in PosMoveAreaLast:
                PosMoveArea.remove(values)
        print("PosMoveArea2", PosMoveArea)
        print("xms", xms)
        if len(PosMoveArea) == 0:
            return False
        else:
            return PosMoveArea


    def MoveareaWCXPosition(x, y, xm, ym, xs, ys, sink_point_out_1, sink_point_out_2, sink_point_out_3,
                            sink_point_out_4, beide, numb):
        PositionMoveWc = MoveareaWCX(x, y, xm, ym, xs, ys, sink_point_out_1, sink_point_out_2, sink_point_out_3,
                                     sink_point_out_4)

        if PositionMoveWc == False:
            return False

        else:
            max = len(PositionMoveWc)
            coordsXM = random.randint(0, (max - 1))
            print(coordsXM)
            xm = PositionMoveWc[coordsXM]

            if xm == None:
                print("Error positioning not possible")
            else:
                print("Movearea position xm: ", xm)
                print("number of possible solutions: ", len(PositionMoveWc))
            return xm

    def MoveareaSinkXPosition(x, y, xms, yms, xs, ys, wc_point_out1, wc_point_out2, wc_point_out3,
                              wc_point_out4, beide, numb):

        PositionMoveSink = MoveareaSinkX(x, y, xms, yms, xs, ys, wc_point_out1, wc_point_out2, wc_point_out3,
                                         wc_point_out4)

        if PositionMoveSink == False:
            return False

        else:
            max = len(PositionMoveSink)
            coordsXMS = random.randint(0, (max-1 ))
            print(coordsXMS)
            xms = PositionMoveSink[coordsXMS]

            if xms == None:
                print("Error positioning not possible")
            else:
                print("Movearea position xms: ", xms)
                print("number of possible solutions: ", len(PositionMoveSink))

            return xms
    def MoveareaWCY(x , y, xm, ym, xs, ys, sink_point_out_1, sink_point_out_2, sink_point_out_3, sink_point_out_4):
        ValuesYM = []
        PosMoveAreaRoom = []
        PosMoveArea = []
        PosMoveAreaDel = []
        PosMoveAreaLast = []
        room = InputPoints(point_8, point_10, point_6, point_7)
        while ym < point_10[1]:
            if ym != point_10[1]:
                ym = ym + 0.2
                ValuesYM.append(ym)
            elif ym == point_10[1]:
                break

        for valuesym in ValuesYM:
            ym = valuesym

            moveAA = (0.75 + xm, 0.75 + ym)
            moveBB = (0.75 + xm, -0.75 + ym)
            moveCC = (-0.75 + xm, -0.75 + ym)
            moveDD = (-0.75 + xm, 0.75 + ym)
            #print("MOVE", moveAA, moveBB, moveCC, moveDD)
            move = InputPoints(moveAA, moveBB, moveCC, moveDD)

            moveandroom = PositionChecking(room[11], move[11],
                                           move[1], move[3], move[5], move[7],
                                           move[9], room[1], room[3], room[5], room[7])
            #print("      moveandroom", moveandroom, xm)
            if moveandroom[-1] == None:
                PosMoveAreaRoom.append(ym)
            #print(PosMoveAreaRoom)

        for valuesYM in PosMoveAreaRoom:
            #print(valuesX)
            ym = valuesYM

            if wallselwc == 2:
                wc1 = (wc_point_out_1_2[0] + x, wc_point_out_1_2[1] + y)
                wc2 = (wc_point_out_2_2[0] + x, wc_point_out_2_2[1] + y)
                wc3 = (wc_point_out_3_2[0] + x, wc_point_out_3_2[1] + y)
                wc4 = (wc_point_out_4_2[0] + x, wc_point_out_4_2[1] + y)
                #print("WCOUT",wc1,wc2,wc3,wc4)
                wcOut = InputPoints(wc1, wc2, wc3, wc4)

            if wallselwc == 4:
                wc1 = (wc_point_out_1_4[0] + x, wc_point_out_1_4[1] + y)
                wc2 = (wc_point_out_2_4[0] + x, wc_point_out_2_4[1] + y)
                wc3 = (wc_point_out_3_4[0] + x, wc_point_out_3_4[1] + y)
                wc4 = (wc_point_out_4_4[0] + x, wc_point_out_4_4[1] + y)
                #print("WCOUT",wc1,wc2,wc3,wc4)
                wcOut = InputPoints(wc1, wc2, wc3, wc4)
            #print("xx", xm)

            moveAA = (0.75 + xm, 0.75 + ym )
            moveBB = (0.75 + xm, -0.75 + ym)
            moveCC = (-0.75 + xm, -0.75 + ym )
            moveDD = (-0.75 + xm, 0.75 + ym )
            #print("MOVE", moveAA, moveBB, moveCC, moveDD)
            move = InputPoints(moveAA, moveBB, moveCC, moveDD)

            wcOutListX = [moveAA[0], moveBB[0], moveCC[0], moveDD[0]]
            wcOutListY = [moveAA[1], moveBB[1], moveCC[1], moveDD[1]]
            maxX = max(wcOutListX)
            maxY = max(wcOutListY)
            minX = min(wcOutListX)
            minY = min(wcOutListY)

            poi1 = PointInPolygon(wc1[0], wc1[1], minX, maxX, minY, maxY)
            poi2 = PointInPolygon(wc2[0], wc2[1], minX, maxX, minY, maxY)
            # print(poi1, poi2)

            if poi1 == True and poi2 == True:
                PosMoveArea.append(ym)

            # wenn Punkte von move == punkte von wcOut bei gleichbleibendem y Wert
            moveanddoor = PositionChecking(door[11], move[11],
                                         move[1], move[3], move[5], move[7],
                                         move[9], door[1], door[3],door[5], door[7])
            #print("moveandwcc", moveanddoor)
            if moveanddoor[-1] == False:
                if ym in PosMoveArea:
                    PosMoveArea.append(ym)

            pt1 = (sink_point_out_1[0] + xs, sink_point_out_1[1] + ys)  # (-0.45 + xs, 0.275 + ys)
            pt2 = (sink_point_out_2[0] + xs, sink_point_out_2[1] + ys)  # (0.45 + xs, 0.275 + ys)
            pt3 = (sink_point_out_3[0] + xs, sink_point_out_3[1] + ys)  # (0.45 + xs, -0.275 + ys)
            pt4 = (sink_point_out_4[0] + xs, sink_point_out_4[1] + ys)  # (-0.45 + xs, -0.275 + ys)
            sinkout = InputPoints(pt1, pt2, pt3, pt4)


            moveandsink = PositionChecking(sinkout[11], move[11],
                                           move[1], move[3], move[5], move[7],
                                           move[9], sinkout[1], sinkout[3], sinkout[5], sinkout[7])
            #print("moveandsink", moveandsink)
            if moveandsink[-1] == True:
                PosMoveAreaLast.append(ym)


            if moveandsink[-1] == False or moveandsink[-1] == None:
                #if ym in PosMoveArea:
                PosMoveAreaDel.append(ym)

        print("PosMoveAreaLast", PosMoveAreaLast)

        #print("PosMoveAreaDel", PosMoveAreaDel)
        print("PosMoveArea", PosMoveArea)


        for values in PosMoveArea:
            if values not in PosMoveAreaLast:
                PosMoveArea.remove(values)
        #print("PosMoveArea2", PosMoveArea)

        #for value in PosMoveAreaDel:
            #if ym == value:
                #print("FAlse")
                #return False


        if len(PosMoveArea) == 0:
            return False
        else:
            return PosMoveArea, y


    def MoveareaWCYPosition(x, y, xm, ym, xs, ys, sink_point_out_1, sink_point_out_2, sink_point_out_3,
                            sink_point_out_4, beide, numb):

        PositionMoveWc = MoveareaWCY(x, y, xm, ym, xs, ys, sink_point_out_1, sink_point_out_2, sink_point_out_3,
                                     sink_point_out_4)

        if PositionMoveWc == False:
            return False

        else:
            #print("hell0",len(PositionMoveWc))
            max = len(PositionMoveWc)
            coordsXM = random.randint(0, (max-1))

            ym = PositionMoveWc[0][coordsXM]

            if ym == None:
                print("Error positioning not possible")
            else:
                print("Movearea position ym: ", ym)
                print("number of possible solutions: ", len(PositionMoveWc))
            return ym

    def MoveareaSinkY(x, y, xms, yms, xs, ys, wc_point_out1, wc_point_out2,wc_point_out3, wc_point_out4):
        ValuesXM = []
        PosMoveAreaRoom = []
        PosMoveArea = []
        room = InputPoints(point_8, point_10, point_6, point_7)
        while yms < point_10[1]:
            if yms != point_10[1]:
                yms = yms + 0.2
                ValuesXM.append(yms)
            elif yms == point_10[1]:
                break

        for valuesxms in ValuesXM:
            yms = valuesxms

            moveAA = (0.75 + xms, 0.75 + yms)
            moveBB = (0.75 + xms, -0.75 + yms)
            moveCC = (-0.75 + xms, -0.75 + yms)
            moveDD = (-0.75 + xms, 0.75 + yms)
            #print("MOVE", moveAA, moveBB, moveCC, moveDD)
            move = InputPoints(moveAA, moveBB, moveCC, moveDD)

            moveandroom = PositionChecking(room[11], move[11],
                                           move[1], move[3], move[5], move[7],
                                           move[9], room[1], room[3], room[5], room[7])
            #print("      moveandroom", moveandroom, yms)
            if moveandroom[-1] == None:
                PosMoveAreaRoom.append(yms)
            #print(PosMoveAreaRoom)
        for valuesXMS in PosMoveAreaRoom:
            yms = valuesXMS
            if wallselsink == 6:
                pt1 = (sink_point_out_1_2[0] + xs, sink_point_out_1_2[1] + ys)  # (-0.45 + xs, 0.275 + ys)
                pt2 = (sink_point_out_2_2[0] + xs, sink_point_out_2_2[1] + ys)  # (0.45 + xs, 0.275 + ys)
                pt3 = (sink_point_out_3_2[0] + xs, sink_point_out_3_2[1] + ys)  # (0.45 + xs, -0.275 + ys)
                pt4 = (sink_point_out_4_2[0] + xs, sink_point_out_4_2[1] + ys)  # (-0.45 + xs, -0.275 + ys)
                sinkout = InputPoints(pt1, pt2, pt3, pt4)

            if wallselsink == 8:
                pt1 = (sink_point_out_1_4[0] + xs, sink_point_out_1_4[1] + ys)  # (-0.45 + xs, 0.275 + ys)
                pt2 = (sink_point_out_2_4[0] + xs, sink_point_out_2_4[1] + ys)  # (0.45 + xs, 0.275 + ys)
                pt3 = (sink_point_out_3_4[0] + xs, sink_point_out_3_4[1] + ys)  # (0.45 + xs, -0.275 + ys)
                pt4 = (sink_point_out_4_4[0] + xs, sink_point_out_4_4[1] + ys)  # (-0.45 + xs, -0.275 + ys)
                sinkout = InputPoints(pt1, pt2, pt3, pt4)
                #print(pt1, pt2, pt3, pt4)


            moveAA = (0.75 + xms, 0.75 + yms)
            moveBB = (0.75 + xms, -0.75 + yms)
            moveCC = (-0.75 + xms, -0.75 + yms)
            moveDD = (-0.75 + xms, 0.75 + yms)
            #print("MOVE", moveAA, moveBB, moveCC, moveDD)
            move = InputPoints(moveAA, moveBB, moveCC, moveDD)

            wc1 = (wc_point_out1[0] + x, wc_point_out1[1] + y)
            wc2 = (wc_point_out2[0] + x, wc_point_out2[1] + y)
            wc3 = (wc_point_out3[0] + x, wc_point_out3[1] + y)
            wc4 = (wc_point_out4[0] + x, wc_point_out4[1] + y)
            #print("WCOUT2", wc1, wc2, wc3, wc4)
            wcOut = InputPoints(wc1, wc2, wc3, wc4)

            moveandWC = PositionChecking(wcOut[11], move[11],
                                           move[1], move[3], move[5], move[7],
                                           move[9], wcOut[1], wcOut[3], wcOut[5], wcOut[7])
            # print("moveandsink", moveandsink)
            if moveandWC[-1] == False or moveandWC[-1] == None:
                if yms in PosMoveArea:
                    PosMoveArea.remove(yms)

            wcOutListX = [moveAA[0], moveBB[0], moveCC[0], moveDD[0]]
            wcOutListY = [moveAA[1], moveBB[1], moveCC[1], moveDD[1]]
            maxX = max(wcOutListX)
            maxY = max(wcOutListY)
            minX = min(wcOutListX)
            minY = min(wcOutListY)


            poi1 = PointInPolygon(pt1[0], pt1[1], minX, maxX, minY, maxY)
            poi2 = PointInPolygon(pt2[0], pt2[1], minX, maxX, minY, maxY)
            #print(poi1, poi2)

            if poi1 == True and poi2 == True:
                PosMoveArea.append(yms)



            # wenn Punkte von move == punkte von wcOut bei gleichbleibendem y Wert
            moveanddoor = PositionChecking(door[11], move[11],
                                           move[1], move[3], move[5], move[7],
                                           move[9], door[1], door[3], door[5], door[7])
            # print("moveandwcc", moveanddoor)
            if moveanddoor[-1] == False:
                if yms in PosMoveArea:
                    PosMoveArea.append(yms)


            wc1 = (wc_point_out1[0] + x, wc_point_out1[1] + y)
            wc2 = (wc_point_out2[0] + x, wc_point_out2[1] + y)
            wc3 = (wc_point_out3[0] + x, wc_point_out3[1] + y)
            wc4 = (wc_point_out4[0] + x, wc_point_out4[1] + y)
            #print("WCOUT2", wc1, wc2, wc3, wc4)
            wcOut = InputPoints(wc1, wc2, wc3, wc4)


            moveandWC = PositionChecking(wcOut[11], move[11],
                                           move[1], move[3], move[5], move[7],
                                           move[9], wcOut[1], wcOut[3], wcOut[5], wcOut[7])
            # print("moveandsink", moveandsink)
            if moveandWC[-1] == False or moveandWC[-1] == None:
                if yms in PosMoveArea:
                    PosMoveArea.remove(yms)

        #print("PosMoveArea2", PosMoveArea)
        if len(PosMoveArea) == 0:
            return False
        else:
            return PosMoveArea, ys

    def MoveareaSinkYPosition(x, y, xms, yms, xs, ys, wc_point_out1, wc_point_out2,wc_point_out3, wc_point_out4, beide, numb):

        PositionMoveSink = MoveareaSinkY(x, y, xms, yms, xs, ys, wc_point_out1, wc_point_out2,wc_point_out3, wc_point_out4)
        #print("gello snk y", (PositionMoveSink))

        if PositionMoveSink == False:
            return False

        else:
            max = len(PositionMoveSink)
            coordsXM = random.randint(0, (max-1))

            yms = PositionMoveSink[0][coordsXM]

            if yms == None:
                print("Error positioning not possible")
            else:
                print("Movearea position yms: ", yms)
                print("number of possible solutions: ", len(PositionMoveSink))
                return yms #False

    # Alle an einer Wand:
    if wallselwc == 1 and wallselsink == 5:
        # klo +sink  auf x achse Wand 1
        x = 0.1
        y = 2 * t

        xs = 0.1
        ys = 2 * t + 0.075

        Klo = PositionWcX(x, y, point_6, (- 1.1, 0.5), (1.1, 0.5), (1.1, - 0.2), (- 1.1, - 0.2))
        print(Klo, "Klo")
        Sink = PositionSinkX(xs, ys, (-0.45, 0.275), (0.45, 0.275), (0.45, -0.275), (-0.45, -0.275))
        print(Sink, "Sink")

        beide = WCXandSinkX(ys, y, Sink, Klo, (0.45, -0.275), (-0.45, -0.275), (-0.45, 0.275), (0.45, 0.275),
                            (- 1.1, 0.5), (1.1, 0.5), (1.1, - 0.2), (- 1.1, - 0.2), wc_point_out_1,
                    wc_point_out_2, wc_point_out_3, wc_point_out_4,
                    sink_point_out_1, sink_point_out_2, sink_point_out_3,sink_point_out_4)

        #print("b 8", beide)
        xs = beide[0]
        x = beide[1]
        # --------------------------------------------------------
        ym = y + 1.15
        xm = 0.1
        xm = MoveareaWCXPosition(x, y, xm, ym, xs, ys, sink_point_out_1, sink_point_out_2, sink_point_out_3, sink_point_out_4, beide, 1)

        while xm == False:
            # print(beide[-1][0])
            # print("Error2", len(beide[-1][0]))
            for values in beide[-1][1]:
                if values == x:
                    beide[-1][1].remove(values)
            # print("Error3", len(beide[-1][0]))
            x = float(min(beide[-1][1]))

            xm = MoveareaWCXPosition(x, y, xm, ym, xs, ys, sink_point_out_1, sink_point_out_2, sink_point_out_3, sink_point_out_4, beide, 1)

            if xm != False:
                print("wc position New: ", x)
                break
        # --------------------------------------------------------
        yms = ys + 1.025
        xms = 0.1
        xms = MoveareaSinkXPosition(x, y, xms, yms, xs, ys, wc_point_out_1, wc_point_out_2, wc_point_out_3,wc_point_out_4, beide, 0)

        while xms == False:
            # print(beide[-1][0])
            # print("Error2", len(beide[-1][0]))
            for values in beide[-1][0]:
                if values == xs:
                    beide[-1][0].remove(values)
            print("Error3", len(beide[-1][0]))
            xs = min(beide[-1][0])

            xms = MoveareaSinkXPosition(x, y, xms, yms, xs, ys, wc_point_out_1, wc_point_out_2, wc_point_out_3,
                                        wc_point_out_4, beide, 0)
            if xms != False:
                print("sink position New: ", xs)
                break

    if wallselwc == 3 and wallselsink == 7:
        #klo +sink auf x achse Wand 3
        x = 0.1
        y = b - 2 * t

        xs = 0.1
        ys = b - 2 * t - 0.075

        Sink = PositionSinkX(xs, ys, (0.45, -0.275), (-0.45, -0.275), (-0.45, 0.275), (0.45, 0.275))
        print(Sink, "Sink")
        Klo = PositionWcX(x, y, point_10, (1.1, - 0.5), (- 1.1, - 0.5), (- 1.1, 0.2), (1.1, 0.2))
        print(Klo, "Klo")

        beide = WCXandSinkX(ys, y, Sink, Klo, (0.45, -0.275), (-0.45, -0.275), (-0.45, 0.275), (0.45, 0.275),
                            (1.1, - 0.5), (- 1.1, - 0.5), (- 1.1, 0.2), (1.1, 0.2), wc_point_out_1_3,
                    wc_point_out_2_3, wc_point_out_3_3, wc_point_out_4_3,
                    sink_point_out_1_3, sink_point_out_2_3, sink_point_out_3_3,sink_point_out_4_3)

        print("b 8", beide)
        xs = beide[0]
        x = beide[1]

        # --------------------------------------------------------
        ym = y - 1.15
        xm = 0.1
        xm = MoveareaWCXPosition(x, y, xm, ym, xs, ys, sink_point_out_1_3, sink_point_out_2_3, sink_point_out_3_3,
                                   sink_point_out_4_3, beide, 1)

        while xm == False:
            # print(beide[-1][0])
            # print("Error2", len(beide[-1][0]))
            for values in beide[-1][1]:
                if values == x:
                    beide[-1][1].remove(values)
            # print("Error3", len(beide[-1][0]))
            x = float(min(beide[-1][1]))

            xm = MoveareaWCXPosition(x, y, xm, ym, xs, ys, sink_point_out_1_3, sink_point_out_2_3, sink_point_out_3_3,
                                     sink_point_out_4_3, beide, 1)
            if xm != False:
                print("wc position New: ", x)
                break

        yms = y - 1.1
        xms = 0.1
        xms = MoveareaSinkXPosition(x, y, xms, yms, xs, ys, wc_point_out_1_3, wc_point_out_2_3, wc_point_out_3_3,
                                         wc_point_out_4_3, beide, 0)
        while xms == False:
            # print(beide[-1][0])
            # print("Error2", len(beide[-1][0]))
            for values in beide[-1][0]:
                if values == xs:
                    beide[-1][0].remove(values)
            # print("Error3", len(beide[-1][0]))
            xs = float(min(beide[-1][0]))

            xms = MoveareaSinkXPosition(x, y, xms, yms, xs, ys, wc_point_out_1_3, wc_point_out_2_3, wc_point_out_3_3,
                                        wc_point_out_4_3, beide, 0)
            if xms != False:
                print("sink position New: ", xs)
                break

    if wallselwc == 2 and wallselsink == 6:
        # klo +sink auf y achse Wand 2
        x = 2 * t
        y = 0.1


        xs = float(2 * t + 0.075)
        ys = 0.1

        Sink = PositionSinkY(xs, ys, (0.275, 0.45), (0.275, -0.45), (-0.275, -0.45), (-0.275, 0.45))
        print(Sink, "Sink")

        Klo = PositionWcY(x, y, point_10, (0.5, 1.1), (0.5, -1.1), (-0.2, -1.1), (- 0.2, 1.1))
        print(Klo, "Klo")

        beide = WCYandSinkY(xs, x, Sink, Klo, (0.275, 0.45), (0.275, -0.45), (-0.275, -0.45), (-0.275, 0.45),
                            (0.5, 1.1), (0.5, -1.1), (-0.2, -1.1), (- 0.2, 1.1), wc_point_out_1_2,
                    wc_point_out_2_2, wc_point_out_3_2, wc_point_out_4_2,
                    sink_point_out_1_2, sink_point_out_2_2, sink_point_out_3_2,sink_point_out_4_2)

        #print("b", beide)
        y = beide[0]
        ys = beide[1]


        # --------------------------------------------------------
        ym = 0.1
        xm = x + 1.15
        ym = MoveareaWCYPosition(x, y, xm, ym, xs, ys, sink_point_out_1_2, sink_point_out_2_2, sink_point_out_3_2,
                            sink_point_out_4_2, beide, 0)


        while ym == False:
            # print(beide[-1][0])
            # print("Error2", len(beide[-1][0]))
            for values in beide[-1][0]:
                if values == y:
                    beide[-1][0].remove(values)
            # print("Error3", len(beide[-1][0]))
            y = float(min(beide[-1][0]))

            ym = MoveareaWCYPosition(x, y, xm, ym, xs, ys, sink_point_out_1_2, sink_point_out_2_2, sink_point_out_3_2,
                                     sink_point_out_4_2, beide, 0)



            if ym != False:
                print("wc position New: ", y)
                break


        # --------------------------------------------------------
        xms = xs + 1.025
        yms = 0.1
        yms = MoveareaSinkYPosition(x, y, xms, yms, xs, ys, wc_point_out_1_2, wc_point_out_2_2, wc_point_out_3_2, wc_point_out_4_2, beide, 1)

        while yms == False:
            # print(beide[-1][0])
            # print("Error2", len(beide[-1][0]))
            for values in beide[-1][1]:
                if values == ys:
                    beide[-1][1].remove(values)
            # print("Error3", len(beide[-1][0]))
            ys = float(min(beide[-1][1]))

            yms = MoveareaSinkYPosition(x, y, xms, yms, xs, ys, wc_point_out_1_2, wc_point_out_2_2, wc_point_out_3_2, wc_point_out_4_2, beide, 1)


            if yms != False:
                print("sink position New: ", ys)
                break



    if wallselwc == 4 and wallselsink == 8:
        #klo +sink auf y achse Wand 4
        x = l - 2 * t
        y = 0.1

        xs = l - 2 * t - 0.075
        ys = 0.1

        Sink = PositionSinkY(xs, ys, (-0.275, -0.45), (-0.275, 0.45), (0.275, 0.45), (0.275, -0.45))
        print(Sink, "Sink")

        Klo = PositionWcY(x, y, point_10, (-0.5, -1.1), (-0.5, 1.1), (0.2, 1.1), (0.2, -1.1))
        print(Klo, "Klo")

        beide = WCYandSinkY(xs, x, Sink, Klo, (-0.275, -0.45), (-0.275, 0.45), (0.275, 0.45), (0.275, -0.45),
                            (-0.5, -1.1), (-0.5, 1.1), (0.2, 1.1), (0.2, -1.1), wc_point_out_1_4,
                    wc_point_out_2_4, wc_point_out_3_4, wc_point_out_4_4,
                    sink_point_out_1_4, sink_point_out_2_4, sink_point_out_3_4,sink_point_out_4_4)

        #print("b", beide)
        y = beide[0]
        ys = beide[1]

        # --------------------------------------------------------
        ym = 0.1
        xm = x - 1.15
        ym = MoveareaWCYPosition(x, y, xm, ym, xs, ys, sink_point_out_1_4, sink_point_out_2_4, sink_point_out_3_4,
                                 sink_point_out_4_4, beide, 0)

        while ym == False:
            # print(beide[-1][0])
            # print("Error2", len(beide[-1][0]))
            for values in beide[-1][0]:
                if values == y:
                    beide[-1][0].remove(values)
            # print("Error3", len(beide[-1][0]))
            y = float(min(beide[-1][0]))

            ym = MoveareaWCYPosition(x, y, xm, ym, xs, ys, sink_point_out_1_4, sink_point_out_2_4, sink_point_out_3_4,
                                     sink_point_out_4_4, beide, 0)
            if ym != False:
                print("wc position New: ", y)
                break
        # --------------------------------------------------------
        xms = xs - 1.025
        yms = 0.1
        yms = MoveareaSinkYPosition(x, y, xms, yms, xs, ys, wc_point_out_1_4, wc_point_out_2_4, wc_point_out_3_4,
                                    wc_point_out_4_4, beide, 1)
        while yms == False:
            # print(beide[-1][0])
            # print("Error2", len(beide[-1][0]))
            for values in beide[-1][1]:
                if values == ys:
                    beide[-1][1].remove(values)
            # print("Error3", len(beide[-1][0]))
            ys = float(min(beide[-1][1]))

            yms = MoveareaSinkYPosition(x, y, xms, yms, xs, ys, wc_point_out_1_4, wc_point_out_2_4, wc_point_out_3_4,
                                        wc_point_out_4_4, beide, 1)

            if yms != False:
                print("sink position New: ", ys)
                break


    # klo an Wand 1, rotierendes WB:
    if wallselwc == 1 and wallselsink == 6:
        x = 0.1
        y = 2 * t

        xs = float(2 * t + 0.075)
        ys = 0.1

        Sink = PositionSinkY(xs, ys, (0.275, 0.45), (0.275, -0.45), (-0.275, -0.45), (-0.275, 0.45))
        print(Sink, "Sink")

        Klo = PositionWcX(x, y, point_6,(- 1.1, 0.5), (1.1, 0.5), (1.1, - 0.2), (- 1.1, - 0.2))
        print(Klo, "Klo")
        #--------------------------------------------------------

        beide = WCXandSinkY(xs, y, Sink, Klo, (0.275, 0.45), (0.275, -0.45), (-0.275, -0.45), (-0.275, 0.45), (- 1.1, 0.5), (1.1, 0.5), (1.1, - 0.2), (- 1.1, - 0.2), wc_point_out_1,wc_point_out_2, wc_point_out_3,wc_point_out_4, sink_point_out_1_2, sink_point_out_2_2,sink_point_out_3_2,sink_point_out_4_2 )

        #print("b", beide)
        ys =beide[0]
        x = beide[1]
        #--------------------------------------------------------
        ym = y + 1.15
        xm = 0.1
        xm = MoveareaWCXPosition(x, y, xm, ym, xs, ys, sink_point_out_1_2, sink_point_out_2_2, sink_point_out_3_2, sink_point_out_4_2, beide, 1)
        while xm == False:
            # print(beide[-1][0])
            # print("Error2", len(beide[-1][0]))
            for values in beide[-1][1]:
                if values == x:
                    beide[-1][1].remove(values)
            # print("Error3", len(beide[-1][0]))
            x = float(min(beide[-1][1]))

            xm = MoveareaWCXPosition(x, y, xm, ym, xs, ys, sink_point_out_1_2, sink_point_out_2_2, sink_point_out_3_2,
                                     sink_point_out_4_2, beide, 1)
            if xm != False:
                print("wc position New: ", x)
                break
        # --------------------------------------------------------
        xms = xs + 1.025
        yms = 0.1
        yms = MoveareaSinkYPosition(x, y, xms, yms, xs, ys, wc_point_out_1, wc_point_out_2, wc_point_out_3, wc_point_out_4, beide, 0)
        while yms == False:
            #print(beide[-1][0])
            #print("Error2", len(beide[-1][0]))
            for values in beide[-1][0]:
                if values == ys:
                    beide[-1][0].remove(values)
            #print("Error3", len(beide[-1][0]))
            ys = float(min(beide[-1][0]))

            yms = MoveareaSinkYPosition(x, y, xms, yms, xs, ys, wc_point_out_1, wc_point_out_2, wc_point_out_3, wc_point_out_4, beide, 0)
            if yms != False:
                print("sink position New: ", ys)
                break

    if wallselwc == 1 and wallselsink==8 :
        x = 0.1
        y = 2 * t

        xs = l - 2 * t - 0.075
        ys =0.1


        Sink = PositionSinkY(xs, ys, (-0.275, -0.45), (-0.275, 0.45), (0.275, 0.45), (0.275, -0.45))
        print(Sink, "Sink")


        Klo = PositionWcX(x, y, point_6, (- 1.1, 0.5), (1.1, 0.5), (1.1, - 0.2), (- 1.1, - 0.2))
        print(Klo, "Klo")

        # --------------------------------------------------------

        beide = WCXandSinkY(xs, y, Sink, Klo, (-0.275, -0.45), (-0.275, 0.45), (0.275, 0.45), (0.275, -0.45), (- 1.1, 0.5), (1.1, 0.5), (1.1, - 0.2), (- 1.1, - 0.2),  wc_point_out_1,wc_point_out_2, wc_point_out_3,wc_point_out_4, sink_point_out_1_4, sink_point_out_2_4,sink_point_out_3_4,sink_point_out_4_4)

        #print("b", beide)
        ys = beide[0]
        x = beide[1]
        #--------------------------------------------------------
        ym = y + 1.15
        xm = 0.1
        xm = MoveareaWCXPosition(x, y, xm, ym, xs, ys, sink_point_out_1_4, sink_point_out_2_4, sink_point_out_3_4, sink_point_out_4_4, beide, 1)

        while xm == False:
            #print(beide[-1][0])
            #print("Error2", len(beide[-1][0]))
            for values in beide[-1][1]:
                if values == x:
                    beide[-1][1].remove(values)
            #print("Error3", len(beide[-1][0]))
            x = float(min(beide[-1][1]))

            xm = MoveareaWCXPosition(x, y, xm, ym, xs, ys, sink_point_out_1_4, sink_point_out_2_4, sink_point_out_3_4, sink_point_out_4_4, beide, 1)

            if xm != False:
                print("wc position New: ", x)
                break
        #------------------------------------------

        xms = xs - 1.025
        yms = 0.1
        yms = MoveareaSinkYPosition(x, y, xms, yms, xs, ys, wc_point_out_1, wc_point_out_2, wc_point_out_3,
                                    wc_point_out_4, beide, 0)

        while yms == False:
            #print(beide[-1][0])
            #print("Error2", len(beide[-1][0]))
            for values in beide[-1][0]:
                if values == ys:
                    beide[-1][0].remove(values)
            #print("Error3", len(beide[-1][0]))
            ys = float(min(beide[-1][0]))

            yms = MoveareaSinkYPosition(x, y, xms, yms, xs, ys, wc_point_out_1, wc_point_out_2, wc_point_out_3,
                                    wc_point_out_4, beide, 0)
            if yms != False:
                print("sink position New: ", ys)
                break

    if wallselwc == 1 and wallselsink==7:
        x = 0.1
        y = 2 * t

        xs = 0.1
        ys = float(b - 2 * t - 0.075)

        Klo = PositionWcX(x, y, point_6, (- 1.1, 0.5), (1.1, 0.5), (1.1, - 0.2), (- 1.1, - 0.2))
        print(Klo, "Klo")

        Sink = PositionSinkX(xs, ys,(0.45, -0.275), (-0.45, -0.275), (-0.45, 0.275), (0.45, 0.275) )
        print(Sink, "Sink")


        beide = WCXandSinkX(ys, y, Sink, Klo, (0.45, -0.275), (-0.45, -0.275), (-0.45, 0.275), (0.45, 0.275), (- 1.1, 0.5), (1.1, 0.5), (1.1, - 0.2), (- 1.1, - 0.2), wc_point_out_1,
                    wc_point_out_2, wc_point_out_3, wc_point_out_4,
                    sink_point_out_1_3, sink_point_out_2_3, sink_point_out_3_3,sink_point_out_4_3)

        #print("b 8", beide)
        xs =beide[0]
        x = beide[1]

        #--------------------------------------------------------
        ym = y + 1.15
        xm = 0.1
        xm = MoveareaWCXPosition(x, y, xm, ym, xs, ys, sink_point_out_1_3, sink_point_out_2_3, sink_point_out_3_3, sink_point_out_4_3, beide, 1)
        while xm == False:
            # print(beide[-1][0])
            # print("Error2", len(beide[-1][0]))
            for values in beide[-1][1]:
                if values == x:
                    beide[-1][1].remove(values)
            # print("Error3", len(beide[-1][0]))
            x = float(min(beide[-1][1]))

            xm = MoveareaWCXPosition(x, y, xm, ym, xs, ys, sink_point_out_1_3, sink_point_out_2_3, sink_point_out_3_3,
                                     sink_point_out_4_3, beide, 1)

            if xm != False:
                print("wc position New: ", x)
                break

        #--------------------------------------------------------
        yms = ys - 1.0
        xms = 0.1
        xms = MoveareaSinkXPosition(x, y, xms, yms, xs, ys, wc_point_out_1, wc_point_out_2, wc_point_out_3,
                                         wc_point_out_4, beide, 0)
        while xms == False:
            # print(beide[-1][0])
            # print("Error2", len(beide[-1][0]))
            for values in beide[-1][0]:
                if values == xs:
                    beide[-1][0].remove(values)
            # print("Error3", len(beide[-1][0]))
            xs = float(min(beide[-1][0]))

            xms = MoveareaSinkXPosition(x, y, xms, yms, xs, ys, wc_point_out_1, wc_point_out_2, wc_point_out_3,
                                        wc_point_out_4, beide, 0)
            if xms != False:
                print("sink position New: ", xs)
                break


    #klo an wand 2, WB rotierend:
    if wallselwc == 2 and wallselsink == 5:
        x = 2 * t
        y = 0.1

        xs = 0.1
        ys = 2 * t + 0.075

        Sink = PositionSinkX(xs, ys, (-0.45, 0.275), (0.45, 0.275), (0.45, -0.275), (-0.45, -0.275))
        print(Sink, "Sink")
        Klo = PositionWcY(x, y, point_10, (0.5, 1.1), (0.5, -1.1), (-0.2, -1.1), (- 0.2, 1.1))
        print(Klo, "Klo")

        beide = WCYandSinkX(x, ys, Sink, Klo, (-0.45, 0.275), (0.45, 0.275), (0.45, -0.275), (-0.45, -0.275),(0.5, 1.1), (0.5, -1.1), (-0.2, -1.1), (- 0.2, 1.1),
                            wc_point_out_1_2,wc_point_out_2_2, wc_point_out_3_2, wc_point_out_4_2,
                            sink_point_out_1, sink_point_out_2, sink_point_out_3,sink_point_out_4 )

        #print("b", beide)
        y = beide[0]
        xs = beide[1]

        ym = 0.1
        xm = x + 1.15
        ym = MoveareaWCYPosition(x, y, xm, ym, xs, ys, sink_point_out_1, sink_point_out_2, sink_point_out_3,
                            sink_point_out_4, beide, 0)
        print("    ",ym)
        while ym == False:
            # print(beide[-1][0])
            # print("Error2", len(beide[-1][0]))
            for values in beide[-1][0]:
                if values == y:
                    beide[-1][0].remove(values)
            # print("Error3", len(beide[-1][0]))
            y = float(min(beide[-1][0]))

            ym = MoveareaWCYPosition(x, y, xm, ym, xs, ys, sink_point_out_1, sink_point_out_2, sink_point_out_3,
                                     sink_point_out_4, beide, 0)
            if ym != False:
                print("wc position New: ", y)
                break
        # --------------------------------------------------------
        yms = ys + 1.025
        xms = 0.1
        xms = MoveareaSinkXPosition(x, y, xms, yms, xs, ys, wc_point_out_1_2, wc_point_out_2_2, wc_point_out_3_2,wc_point_out_4_2,beide, 1)
        print("    ", xms)
        while xms == False:
            # print(beide[-1][0])
            # print("Error2", len(beide[-1][0]))
            for values in beide[-1][1]:
                if values == xs:
                    beide[-1][1].remove(values)
            # print("Error3", len(beide[-1][0]))
            xs = float(min(beide[-1][1]))

            xms = MoveareaSinkXPosition(x, y, xms, yms, xs, ys, wc_point_out_1_2, wc_point_out_2_2, wc_point_out_3_2,
                                        wc_point_out_4_2, beide, 1)

            if xms != False:
                print("sink position New: ", xs)
                break

    if wallselwc == 2 and wallselsink == 7:
        x = 2 * t
        y = 0.1

        xs = 0.1
        ys = float(b - 2 * t - 0.075)

        Sink = PositionSinkX(xs, ys, (0.45, -0.275), (-0.45, -0.275), (-0.45, 0.275), (0.45, 0.275))
        print(Sink, "Sink")

        Klo = PositionWcY(x, y, point_10, (0.5, 1.1), (0.5, -1.1), (-0.2, -1.1), (- 0.2, 1.1))
        print(Klo, "Klo")

        # --------------------------------------------------------

        beide = WCYandSinkX(x, ys, Sink, Klo,(0.45, -0.275), (-0.45, -0.275), (-0.45, 0.275), (0.45, 0.275), (0.5, 1.1), (0.5, -1.1), (-0.2, -1.1), (- 0.2, 1.1),
                            wc_point_out_1_2,wc_point_out_2_2, wc_point_out_3_2, wc_point_out_4_2,
                            sink_point_out_1_3, sink_point_out_2_3, sink_point_out_3_3,sink_point_out_4_3)

        #print("b", beide)
        y = beide[0]
        xs = beide[1]

        # wenn bei algo 20 der kleinste Wert nicht geht, weil movearea  mit sink intersected, lösche ihn und nimm den nächsten wert.
        ym = 0.1
        xm = x + 1.15
        ym = MoveareaWCYPosition(x, y, xm, ym, xs, ys, sink_point_out_1_3, sink_point_out_2_3, sink_point_out_3_3,
                                 sink_point_out_4_3, beide, 0)

        while ym == False:
            # print(beide[-1][0])
            # print("Error2", len(beide[-1][0]))
            for values in beide[-1][0]:
                if values == y:
                    beide[-1][0].remove(values)
            # print("Error3", len(beide[-1][0]))
            y = float(min(beide[-1][0]))

            ym = MoveareaWCYPosition(x, y, xm, ym, xs, ys, sink_point_out_1_3, sink_point_out_2_3, sink_point_out_3_3,
                                     sink_point_out_4_3, beide, 0)
            if ym != False:
                print("wc position New: ", y)
                break
        # --------------------------------------------------------
        yms = ys - 1.0
        xms = 0.1
        xms = MoveareaSinkXPosition(x, y, xms, yms, xs, ys, wc_point_out_1_2, wc_point_out_2_2, wc_point_out_3_2,
                                    wc_point_out_4_2, beide, 1)

        if xms == False:
            # print(beide[-1][0])
            # print("Error2", len(beide[-1][0]))
            for values in beide[-1][1]:
                if values == xs:
                    beide[-1][1].remove(values)
            # print("Error3", len(beide[-1][0]))
            xs = float(min(beide[-1][1]))

            xms = MoveareaSinkXPosition(x, y, xms, yms, xs, ys, wc_point_out_1_2, wc_point_out_2_2, wc_point_out_3_2,
                                        wc_point_out_4_2, beide, 1)
            print(xms)
        if xms != False:
            print("sink position New: ", xs)

                #break

    if wallselwc == 2 and wallselsink == 8:
        x = 2 * t
        y = 0.1

        xs = l - 2 * t - 0.075
        ys = 0.1

        Sink = PositionSinkY(xs, ys, (-0.275, -0.45), (-0.275, 0.45), (0.275, 0.45), (0.275, -0.45))
        print(Sink, "Sink")

        Klo = PositionWcY(x, y, point_10, (0.5, 1.1), (0.5, -1.1), (-0.2, -1.1), (- 0.2, 1.1))
        print(Klo, "Klo")

        # --------------------------------------------------------

        beide = WCYandSinkY(xs, x, Sink, Klo,(-0.275, -0.45), (-0.275, 0.45), (0.275, 0.45), (0.275, -0.45), (0.5, 1.1), (0.5, -1.1), (-0.2, -1.1), (- 0.2, 1.1) ,
                            wc_point_out_1_2,wc_point_out_2_2, wc_point_out_3_2, wc_point_out_4_2,
                            sink_point_out_1_4, sink_point_out_2_4, sink_point_out_3_4,sink_point_out_4_4)

        #print("b", beide)
        y = beide[0]
        ys = beide[1]

        # --------------------------------------------------------
        ym = 0.1
        xm = x + 1.15
        ym = MoveareaWCYPosition(x, y, xm, ym, xs, ys, sink_point_out_1_4, sink_point_out_2_4, sink_point_out_3_4,
                                 sink_point_out_4_4, beide, 0)
        while ym == False:
            # print(beide[-1][0])
            # print("Error2", len(beide[-1][0]))
            for values in beide[-1][0]:
                if values == y:
                    beide[-1][0].remove(values)
            # print("Error3", len(beide[-1][0]))
            y = float(min(beide[-1][0]))

            ym = MoveareaWCYPosition(x, y, xm, ym, xs, ys, sink_point_out_1_4, sink_point_out_2_4, sink_point_out_3_4,
                                     sink_point_out_4_4, beide, 0)
            if ym != False:
                print("wc position New: ", y)
                break
        # --------------------------------------------------------
        xms = xs - 1.025
        yms = 0.1
        yms = MoveareaSinkYPosition(x, y, xms, yms, xs, ys, wc_point_out_1_2, wc_point_out_2_2, wc_point_out_3_2,
                                    wc_point_out_4_2, beide, 1)
        while yms == False:
            #print(beide[-1][0])
            #print("Error2", len(beide[-1][0]))
            for values in beide[-1][1]:
                if values == ys:
                    beide[-1][1].remove(values)
            #print("Error3", len(beide[-1][0]))
            ys = float(min(beide[-1][1]))

            yms = MoveareaSinkYPosition(x, y, xms, yms, xs, ys, wc_point_out_1_2, wc_point_out_2_2, wc_point_out_3_2,
                                        wc_point_out_4_2, beide, 1)
            if yms != False:
                print("sink position New: ", ys)
                break

    #klo an wand 3, WB rotierend:
    if wallselwc == 3 and wallselsink == 5:
        x = 0.1
        y = b - 2 * t

        xs = 0.1
        ys = 2 * t + 0.075

        Sink = PositionSinkX(xs, ys, (-0.45, 0.275), (0.45, 0.275), (0.45, -0.275), (-0.45, -0.275))
        print(Sink, "Sink")

        Klo = PositionWcX(x, y, point_10,  (1.1, - 0.5), (- 1.1, - 0.5), (- 1.1, 0.2), (1.1, 0.2))
        print(Klo, "Klo")

        beide = WCXandSinkX(ys, y, Sink, Klo, (-0.45, 0.275), (0.45, 0.275), (0.45, -0.275), (-0.45, -0.275),(1.1, - 0.5), (- 1.1, - 0.5), (- 1.1, 0.2), (1.1, 0.2),
                            wc_point_out_1_3, wc_point_out_2_3, wc_point_out_3_3, wc_point_out_4_3,
                            sink_point_out_1, sink_point_out_2, sink_point_out_3, sink_point_out_4)

        #print("b", beide)
        xs = beide[0]
        x = beide[1]

        # --------------------------------------------------------
        ym = y - 1.15
        xm = 0.1
        xm = MoveareaWCXPosition(x, y, xm, ym, xs, ys, sink_point_out_1, sink_point_out_2, sink_point_out_3,
                                   sink_point_out_4, beide, 1)
        while xm == False:
            # print(beide[-1][0])
            # print("Error2", len(beide[-1][0]))
            for values in beide[-1][1]:
                if values == x:
                    beide[-1][1].remove(values)
            # print("Error3", len(beide[-1][0]))
            x = float(min(beide[-1][1]))

            xm = MoveareaWCXPosition(x, y, xm, ym, xs, ys, sink_point_out_1, sink_point_out_2, sink_point_out_3,
                                     sink_point_out_4, beide, 1)

            if xm != False:
                print("wc position New: ", x)
                break
        # --------------------------------------------------------
        yms = ys + 1.025
        xms = 0.1
        xms = MoveareaSinkXPosition(x, y, xms, yms, xs, ys, wc_point_out_1_3, wc_point_out_2_3, wc_point_out_3_3,wc_point_out_4_3,beide, 0)

        while xms == False:
            # print(beide[-1][0])
            # print("Error2", len(beide[-1][0]))
            for values in beide[-1][0]:
                if values == xs:
                    beide[-1][0].remove(values)
            # print("Error3", len(beide[-1][0]))
            xs = float(min(beide[-1][0]))

            xms = MoveareaSinkXPosition(x, y, xms, yms, xs, ys, wc_point_out_1_3, wc_point_out_2_3, wc_point_out_3_3,
                                        wc_point_out_4_3, beide, 0)
            if xms != False:
                print("sink position New: ", xs)
                break

    if wallselwc == 3 and wallselsink == 8:
        x = 0.1
        y = float(b - 2 * t)

        xs = l - 2 * t - 0.075
        ys = 0.1

        Sink = PositionSinkY(xs, ys, (-0.275, -0.45), (-0.275, 0.45), (0.275, 0.45), (0.275, -0.45))
        print(Sink, "Sink")

        Klo = PositionWcX(x, y, point_6, (- 1.1, - 0.5), (1.1, - 0.5), (1.1, 0.2), (- 1.1, 0.2))
        print(Klo, "Klo")

        beide = WCXandSinkY(xs, y, Sink, Klo, (-0.275, -0.45), (-0.275, 0.45), (0.275, 0.45), (0.275, -0.45),(- 1.1, - 0.5), (1.1, - 0.5), (1.1, 0.2), (- 1.1, 0.2),  wc_point_out_1_3,wc_point_out_2_3, wc_point_out_3_3,wc_point_out_4_3, sink_point_out_1_4, sink_point_out_2_4,sink_point_out_3_4,sink_point_out_4_4)

        print("b", beide)
        ys = beide[0]
        x = beide[1]

        # --------------------------------------------------------
        ym = y - 1.15
        xm = 0.1
        xm = MoveareaWCXPosition(x, y, xm, ym, xs, ys, sink_point_out_1_4, sink_point_out_2_4, sink_point_out_3_4,
                                   sink_point_out_4_4, beide, 1)
        while xm == False:
            # print(beide[-1][0])
            # print("Error2", len(beide[-1][0]))
            for values in beide[-1][1]:
                if values == x:
                    beide[-1][1].remove(values)
            # print("Error3", len(beide[-1][0]))
            x = float(min(beide[-1][1]))

            xm = MoveareaWCXPosition(x, y, xm, ym, xs, ys, sink_point_out_1_4, sink_point_out_2_4, sink_point_out_3_4,
                                     sink_point_out_4_4, beide, 1)

            if xm != False:
                print("wc position New: ", x)
                break
        # --------------------------------------------------------
        xms = xs - 1.025
        yms = 0.1
        yms = MoveareaSinkYPosition(x, y, xms, yms, xs, ys, wc_point_out_1_3, wc_point_out_2_3, wc_point_out_3_3,
                                    wc_point_out_4_3, beide, 0)

        while yms == False:
            #print(beide[-1][0])
            #print("Error2", len(beide[-1][0]))
            for values in beide[-1][0]:
                if values == ys:
                    beide[-1][0].remove(values)
            #print("Error3", len(beide[-1][0]))
            ys = float(min(beide[-1][0]))

            yms = MoveareaSinkYPosition(x, y, xms, yms, xs, ys, wc_point_out_1_3, wc_point_out_2_3, wc_point_out_3_3,
                                        wc_point_out_4_3, beide, 0)
            if yms != False:
                print("sink position New: ", ys)
                break

    if wallselwc == 3 and wallselsink == 6:
        x = 0.1
        y = float(b - 2 * t)

        xs = float(2 * t + 0.075)
        ys = 0.1

        Sink = PositionSinkY(xs, ys, (0.275, 0.45), (0.275, -0.45), (-0.275, -0.45), (-0.275, 0.45))
        print(Sink, "Sink")

        Klo = PositionWcX(x, y, point_6, (- 1.1, - 0.5), (1.1, - 0.5), (1.1, 0.2), (- 1.1, 0.2))
        print(Klo, "Klo")

        beide = WCXandSinkY(xs, y, Sink, Klo, (0.275, 0.45), (0.275, -0.45), (-0.275, -0.45), (-0.275, 0.45),(- 1.1, - 0.5), (1.1, - 0.5), (1.1, 0.2), (- 1.1, 0.2),  wc_point_out_1_3,wc_point_out_2_3, wc_point_out_3_3,wc_point_out_4_3, sink_point_out_1_2, sink_point_out_2_2,sink_point_out_3_2,sink_point_out_4_2)

        print("b", beide)
        ys = beide[0]
        x = beide[1]

        # --------------------------------------------------------
        ym = y - 1.15
        xm = 0.1
        xm = MoveareaWCXPosition(x, y, xm, ym, xs, ys, sink_point_out_1_2, sink_point_out_2_2, sink_point_out_3_2,
                                   sink_point_out_4_2, beide, 1)
        while xm == False:
            # print(beide[-1][0])
            # print("Error2", len(beide[-1][0]))
            for values in beide[-1][1]:
                if values == x:
                    beide[-1][1].remove(values)
            # print("Error3", len(beide[-1][0]))
            x = float(min(beide[-1][1]))

            xm = MoveareaWCXPosition(x, y, xm, ym, xs, ys, sink_point_out_1_2, sink_point_out_2_2, sink_point_out_3_2,
                                     sink_point_out_4_2, beide, 1)

            if xm != False:
                print("wc position New: ", x)
                break
        # --------------------------------------------------------
        xms = xs + 1.025
        yms = 0.1
        yms = MoveareaSinkYPosition(x, y, xms, yms, xs, ys, wc_point_out_1_3, wc_point_out_2_3, wc_point_out_3_3, wc_point_out_4_3, beide, 0)

        while yms == False:
            # print(beide[-1][0])
            # print("Error2", len(beide[-1][0]))
            for values in beide[-1][0]:
                if values == ys:
                    beide[-1][0].remove(values)
            # print("Error3", len(beide[-1][0]))
            ys = float(min(beide[-1][0]))

            yms = MoveareaSinkYPosition(x, y, xms, yms, xs, ys, wc_point_out_1_3, wc_point_out_2_3, wc_point_out_3_3,
                                        wc_point_out_4_3, beide, 0)

            if yms != False:
                print("sink position New: ", ys)
                break

    #klo an wand 4, WB rotierend:
    if wallselwc == 4 and wallselsink == 5:
        x = l - 2 * t
        y = 0.1

        xs = 0.1
        ys = 2 * t + 0.075

        Sink = PositionSinkX(xs, ys, (-0.45, 0.275), (0.45, 0.275), (0.45, -0.275), (-0.45, -0.275))
        print(Sink, "Sink")
        Klo = PositionWcY(x, y, point_10, (-0.5, -1.1), (-0.5, 1.1), (0.2, 1.1), (0.2, -1.1))

        print(Klo, "Klo")

        beide = WCYandSinkX(x, ys, Sink, Klo, (-0.45, 0.275), (0.45, 0.275), (0.45, -0.275), (-0.45, -0.275),
                            (-0.5, -1.1), (-0.5, 1.1), (0.2, 1.1), (0.2, -1.1),
                            wc_point_out_1_4,wc_point_out_2_4, wc_point_out_3_4, wc_point_out_4_4,
                            sink_point_out_1, sink_point_out_2, sink_point_out_3,sink_point_out_4)

        #print("b", beide)
        y = beide[0]
        xs = beide[1]

        # --------------------------------------------------------
        ym = 0.1
        xm = x - 1.15
        ym = MoveareaWCYPosition(x, y, xm, ym, xs, ys, sink_point_out_1, sink_point_out_2, sink_point_out_3,
                                 sink_point_out_4, beide, 0)
        while ym == False:
            # print(beide[-1][0])
            # print("Error2", len(beide[-1][0]))
            for values in beide[-1][0]:
                if values == y:
                    beide[-1][0].remove(values)
            # print("Error3", len(beide[-1][0]))
            y = float(min(beide[-1][0]))
            ym = MoveareaWCYPosition(x, y, xm, ym, xs, ys, sink_point_out_1, sink_point_out_2, sink_point_out_3,
                                     sink_point_out_4, beide, 0)
            if ym != False:
                print("wc position New: ", y)
                break
        # --------------------------------------------------------
        yms = ys + 1.025
        xms = 0.1
        xms = MoveareaSinkXPosition(x, y, xms, yms, xs, ys, wc_point_out_1_4, wc_point_out_2_4, wc_point_out_3_4,wc_point_out_4_4, beide, 1)

        while xms == False:
            # print(beide[-1][0])
            # print("Error2", len(beide[-1][0]))
            for values in beide[-1][1]:
                if values == xs:
                    beide[-1][1].remove(values)
            # print("Error3", len(beide[-1][0]))
            xs = float(min(beide[-1][1]))

            xms = MoveareaSinkXPosition(x, y, xms, yms, xs, ys, wc_point_out_1_4, wc_point_out_2_4, wc_point_out_3_4,
                                        wc_point_out_4_4, beide, 1)

            if xms != False:
                print("sink position New: ", xs)
                break
    if wallselwc == 4 and wallselsink == 6:
        x = l - 2 * t
        y = 0.1

        xs = float(2 * t + 0.075)
        ys = 0.1

        Sink = PositionSinkY(xs, ys, (0.275, 0.45), (0.275, -0.45), (-0.275, -0.45), (-0.275, 0.45))
        print(Sink, "Sink")

        Klo = PositionWcY(x, y, point_10, (-0.5, -1.1), (-0.5, 1.1), (0.2, 1.1), (0.2, -1.1))
        print(Klo, "Klo")

        beide = WCYandSinkY(xs, x, Sink, Klo, (0.275, 0.45), (0.275, -0.45), (-0.275, -0.45), (-0.275, 0.45),
                            (-0.5, -1.1), (-0.5, 1.1), (0.2, 1.1), (0.2, -1.1), wc_point_out_1_4,wc_point_out_2_4, wc_point_out_3_4, wc_point_out_4_4,
                            sink_point_out_1_2, sink_point_out_2_2, sink_point_out_3_2,sink_point_out_4_2)

        #print("b", beide)
        y = beide[0]
        ys = beide[1]

        # --------------------------------------------------------
        ym = 0.1
        xm = x - 1.15
        ym = MoveareaWCYPosition(x, y, xm, ym, xs, ys, sink_point_out_1_2, sink_point_out_2_2, sink_point_out_3_2,
                                 sink_point_out_4_2, beide, 0)
        while ym == False:
            # print(beide[-1][0])
            # print("Error2", len(beide[-1][0]))
            for values in beide[-1][0]:
                if values == y:
                    beide[-1][0].remove(values)
            # print("Error3", len(beide[-1][0]))
            y = float(min(beide[-1][0]))
            ym = MoveareaWCYPosition(x, y, xm, ym, xs, ys, sink_point_out_1_2, sink_point_out_2_2, sink_point_out_3_2,
                                     sink_point_out_4_2, beide, 0)
            if ym != False:
                print("wc position New: ", y)
                break
        # --------------------------------------------------------
        xms = xs + 1.025
        yms = 0.1
        yms = MoveareaSinkYPosition(x, y, xms, yms, xs, ys, wc_point_out_1_4, wc_point_out_2_4, wc_point_out_3_4, wc_point_out_4_4, beide, 1)

        while yms == False:
            # print(beide[-1][0])
            # print("Error2", len(beide[-1][0]))
            for values in beide[-1][1]:
                if values == ys:
                    beide[-1][1].remove(values)
            # print("Error3", len(beide[-1][0]))
            ys = float(min(beide[-1][1]))

            yms = MoveareaSinkYPosition(x, y, xms, yms, xs, ys, wc_point_out_1_4, wc_point_out_2_4, wc_point_out_3_4,
                                        wc_point_out_4_4, beide, 1)

            if yms != False:
                print("sink position New: ", ys)
                break

    if wallselwc == 4 and wallselsink == 7:
        x = l - 2 * t
        y = 0.1

        xs = 0.1
        ys = float(b - 2 * t - 0.075)

        Sink = PositionSinkX(xs, ys, (0.45, -0.275), (-0.45, -0.275), (-0.45, 0.275), (0.45, 0.275))
        print(Sink, "Sink")

        Klo = PositionWcY(x, y, point_10, (-0.5, -1.1), (-0.5, 1.1), (0.2, 1.1), (0.2, -1.1))
        print(Klo, "Klo")

        beide = WCYandSinkX(x, ys, Sink, Klo,(0.45, -0.275), (-0.45, -0.275), (-0.45, 0.275), (0.45, 0.275),
                            (-0.5, -1.1), (-0.5, 1.1), (0.2, 1.1), (0.2, -1.1), wc_point_out_1_4,wc_point_out_2_4, wc_point_out_3_4, wc_point_out_4_4,
                            sink_point_out_1_3, sink_point_out_2_3, sink_point_out_3_3,sink_point_out_4_3)

        #print("b", beide)
        y = beide[0]
        xs = beide[1]
        # --------------------------------------------------------
        ym = 0.1
        xm = x - 1.15
        ym = MoveareaWCYPosition(x, y, xm, ym, xs, ys, sink_point_out_1_3, sink_point_out_2_3, sink_point_out_3_3,
                                 sink_point_out_4_3, beide, 0)
        while ym == False:
            # print(beide[-1][0])
            # print("Error2", len(beide[-1][0]))
            for values in beide[-1][0]:
                if values == y:
                    beide[-1][0].remove(values)
            # print("Error3", len(beide[-1][0]))
            y = float(min(beide[-1][0]))
            ym = MoveareaWCYPosition(x, y, xm, ym, xs, ys, sink_point_out_1_3, sink_point_out_2_3, sink_point_out_3_3,
                                     sink_point_out_4_3, beide, 0)
            if ym != False:
                print("wc position New: ", y)
                break
        # --------------------------------------------------------
        yms = ys - 1.0
        xms = 0.1
        xms = MoveareaSinkXPosition(x, y, xms, yms, xs, ys, wc_point_out_1_4, wc_point_out_2_4, wc_point_out_3_4,
                                    wc_point_out_4_4, beide, 1)
        while xms == False:
            # print(beide[-1][0])
            # print("Error2", len(beide[-1][0]))
            for values in beide[-1][1]:
                if values == xs:
                    beide[-1][1].remove(values)
            # print("Error3", len(beide[-1][0]))
            xs = float(min(beide[-1][1]))
            xms = MoveareaSinkXPosition(x, y, xms, yms, xs, ys, wc_point_out_1_4, wc_point_out_2_4, wc_point_out_3_4,
                                        wc_point_out_4_4, beide, 1)

            if xms != False:
                print("sink position New: ", xs)
                break


#-------------IFC-------------------------------

    #-------------------------------------------------------------------------------------------------------------


    # ------------------------------------------------------------------------------------------------------------
    # HELPER FUNCTIONS

    # Creates an IfcAxis2Placement3D from Location, Axis and RefDirection specified as Python tuples
    def create_ifcaxis2placement(ifcfile, point=O, dir1=Z, dir2=X):
        point = ifcfile.createIfcCartesianPoint(point)
        dir1 = ifcfile.createIfcDirection(dir1)
        dir2 = ifcfile.createIfcDirection(dir2)
        axis2placement = ifcfile.createIfcAxis2Placement3D(point, dir1, dir2)
        return axis2placement

    # Creates an IfcLocalPlacement from Location, Axis and RefDirection, specified as Python tuples, and relative placement
    # Object coordinates in relation to World Coordinates
    def create_ifclocalplacement(ifcfile, point=O, dir1=Z, dir2=X, relative_to=None):
        axis2placement = create_ifcaxis2placement(ifcfile, point, dir1, dir2)
        ifclocalplacement2 = ifcfile.createIfcLocalPlacement(relative_to, axis2placement)
        return ifclocalplacement2

    # Creates an IfcPolyLine from a list of points, specified as Python tuples
    def create_ifcpolyline(ifcfile, point_list):
        ifcpts = []  # Point_List
        for point in point_list:
            point = ifcfile.createIfcCartesianPoint(point)
            ifcpts.append(point)
        polyline = ifcfile.createIfcPolyLine(ifcpts)
        return polyline

    # Creates an IfcExtrudedAreaSolid from a list of points, specified as Python tuples
    def create_ifcextrudedareasolid(ifcfile, rect_list, ifcaxis2placement, extrude_dir, extrusion):
        polyline = create_ifcpolyline(ifcfile, rect_list)
        ifcclosedprofile = ifcfile.createIfcArbitraryClosedProfileDef("AREA", None, polyline)
        ifcdir = ifcfile.createIfcDirection(extrude_dir)
        ifcextrudedareasolid = ifcfile.createIfcExtrudedAreaSolid(ifcclosedprofile, ifcaxis2placement, ifcdir,
                                                                  extrusion)
        return ifcextrudedareasolid

    def create_ifcline(ifcfile, point, dirV):
        point = ifcfile.createIfcCartesianPoint(point)
        ifcdir = ifcfile.createIfcDirection(dirV)
        line = ifcfile.createIfcLine(point, ifcdir)
        return line

    create_guid = lambda: ifcopenshell.guid.compress(uuid.uuid1().hex)

    # ------------------------------------------------------------------------------------------------------------
    # IFC TEMPLATE

    timestamp = time.time()
    timestring = time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(timestamp))
    creator = "Amelie Hofer"
    organization = "icd, Uni Stuttgart"
    application, application_version = "IfcOpenShell", "0.7.0"
    project_globalid, project_name = create_guid(), "IFC"

    # ------------------------------------------------------------------------------------------------------------
    # FILE EXPORT/IMPORT
    # import module
    from datetime import datetime

    # get current date and time
    current_datetime = datetime.now()
    # print("Current date & time : ", current_datetime)
    timestr = str(current_datetime)

    #filename = "../scripts/archinkluencer001A_"+timestr+".ifc"
    filename = "/Users/ameliehofer/PycharmProjects/djangoProject/Archinkluencer/static/archinkluencer002.ifc"
    filename_area = "/Users/ameliehofer/PycharmProjects/djangoProject/Archinkluencer/static/area2.ifc"

    # ------------------------------------------------------------------------------------------------------------
    # TEMPLATE IFC FILE STEP-FORMAT, ENTITIES FOR AN IFCPROJECT

    template = """ISO-10303-21;
    HEADER;
    FILE_DESCRIPTION(('ViewDefinition [CoordinationView]'),'2;1');
    FILE_NAME('%(filename)s','%(timestring)s',('%(creator)s'),('%(organization)s'),'%(application)s','%(application)s','');
    FILE_SCHEMA(('IFC4'));
    ENDSEC;
    DATA;
    #1=IFCPERSON($,$,'%(creator)s',$,$,$,$,$);
    #2=IFCORGANIZATION($,'%(organization)s',$,$,$);
    #3=IFCPERSONANDORGANIZATION(#1,#2,$);
    #4=IFCAPPLICATION(#2,'%(application_version)s','%(application)s','');
    #5=IFCOWNERHISTORY(#3,#4,$,.ADDED.,$,#3,#4,%(timestamp)s);
    #6=IFCDIRECTION((1.,0.,0.));
    #7=IFCDIRECTION((0.,0.,1.));
    #8=IFCCARTESIANPOINT((0.,0.,0.));
    #9=IFCAXIS2PLACEMENT3D(#8,#7,#6);
    #10=IFCDIRECTION((0.,1.,0.));
    #11=IFCGEOMETRICREPRESENTATIONCONTEXT($,'Model',3,1.E-05,#9,#10);
    #12=IFCDIMENSIONALEXPONENTS(0,0,0,0,0,0,0);
    #13=IFCSIUNIT(*,.LENGTHUNIT.,$,.METRE.);
    #14=IFCSIUNIT(*,.AREAUNIT.,$,.SQUARE_METRE.);
    #15=IFCSIUNIT(*,.VOLUMEUNIT.,$,.CUBIC_METRE.);
    #16=IFCSIUNIT(*,.PLANEANGLEUNIT.,$,.RADIAN.);
    #17=IFCMEASUREWITHUNIT(IFCPLANEANGLEMEASURE(0.017453292519943295),#16);
    #18=IFCCONVERSIONBASEDUNIT(#12,.PLANEANGLEUNIT.,'DEGREE',#17);
    #19=IFCUNITASSIGNMENT((#13,#14,#15,#18));
    #20=IFCPROJECT('%(project_globalid)s',#5,'%(project_name)s',$,$,$,$,(#11),#19);
    ENDSEC;
    END-ISO-10303-21;
    """ % locals()

    # ------------------------------------------------------------------------------------------------------------
    # TEMPLATE FILE WRITING
    temp_handle, temp_filename = tempfile.mkstemp(suffix=".ifc")
    with open(temp_filename, "w") as f:
        f.write(template)

    temp2_handle, temp2_filename = tempfile.mkstemp(suffix=".ifc")
    with open(temp2_filename, "w") as f:
        f.write(template)

    # ------------------------------------------------------------------------------------------------------------
    # VARIABLES AND REFERENCES TO INSTANCES DEFINED IN THE TEMPLATE

    ifcfile = ifcopenshell.open(temp_filename)
    owner_history = ifcfile.by_type("IfcOwnerHistory")[0]
    project = ifcfile.by_type("IfcProject")[0]
    context = ifcfile.by_type("IfcGeometricRepresentationContext")[0]

    # ------------------------------------------------------------------------------------------------------------
    # IFC HIERARCHY

    site_placement = create_ifclocalplacement(ifcfile)
    site = ifcfile.createIfcSite(create_guid(), owner_history, "Site", None, None, site_placement, None, None,
                                 "ELEMENT",
                                 None, None, None, None, None)

    building_placement = create_ifclocalplacement(ifcfile, relative_to=site_placement)
    building = ifcfile.createIfcBuilding(create_guid(), owner_history, 'Building', None, None, building_placement, None,
                                         None, "ELEMENT", None, None, None)

    storey_placement = create_ifclocalplacement(ifcfile, relative_to=building_placement)
    elevation = 0.0
    building_storey = ifcfile.createIfcBuildingStorey(create_guid(), owner_history, 'Storey', None, None,
                                                      storey_placement,
                                                      None, None, "ELEMENT", elevation)

    container_storey = ifcfile.createIfcRelAggregates(create_guid(), owner_history, "Building Container", None,
                                                      building,
                                                      [building_storey])
    container_site = ifcfile.createIfcRelAggregates(create_guid(), owner_history, "Site Container", None, site,
                                                    [building])
    container_project = ifcfile.createIfcRelAggregates(create_guid(), owner_history, "Project Container", None, project,
                                                       [site])



    # ------------------------------------------------------------------------------------------------------------
    # WALL CREATION

    # Location
    wall_placement = create_ifclocalplacement(ifcfile, relative_to=storey_placement)

    def Wall(start_pt, end_pt, points_1, points_2, points_3, points_4, name, height):
        # Location
        wall_placement

        # Reference Line Wall
        polyline_1 = create_ifcpolyline(ifcfile, [(start_pt[0], start_pt[1]), (end_pt[0], end_pt[1])])

        # Representation Reference Line
        axis_representation = ifcfile.createIfcShapeRepresentation(context, "Axis", "Curve2D", [polyline_1])

        # Referenced Location and geometry processing
        extrusion_placement = create_ifcaxis2placement(ifcfile, (0.0, 0.0, 0.0), (0.0, 0.0, 1.0), (1.0, 0.0, 0.0))
        point_list_extrusion_area = [(points_1[0], points_1[1]), (points_2[0], points_2[1]), (points_3[0], points_3[1]),
                                     (points_4[0], points_4[1]), (points_1[0], points_1[1])]
        solid = create_ifcextrudedareasolid(ifcfile, point_list_extrusion_area, extrusion_placement, (0.0, 0.0, 1.0),
                                            height)

        # Representation 3D geometry
        body_representation = ifcfile.createIfcShapeRepresentation(context, "Body", "SweptSolid", [solid])
        product_shape = ifcfile.createIfcProductDefinitionShape(None, None, [axis_representation, body_representation])

        # IFCWALL in STEP
        return ifcfile.createIfcWallStandardCase(create_guid(), owner_history, "Wall", name, None, wall_placement,
                                                 product_shape, None, "STANDARD")

    # ------------------------------------------------------------------------------------------------------------
    # SLAB CREATION

    # Location
    slab_placement = create_ifclocalplacement(ifcfile, relative_to=storey_placement)

    def Slab(points_1, points_2, points_3, points_4, name, height):
        # Location
        slab_placement

        # Referenced Location and geometry processing
        extrusion_placement = create_ifcaxis2placement(ifcfile, (0.0, 0.0, 0.0), (0.0, 0.0, 1.0), (1.0, 0.0, 0.0))
        point_list_extrusion_area = [(points_1[0], points_1[1]), (points_2[0], points_2[1]), (points_3[0], points_3[1]),
                                     (points_4[0], points_4[1]), ]
        solid = create_ifcextrudedareasolid(ifcfile, point_list_extrusion_area, extrusion_placement, (0.0, 0.0, 1.0),
                                            height)

        # Representation 3D geometry
        body_representation = ifcfile.createIfcShapeRepresentation(context, "Body", "SweptSolid", [solid])
        product_shape = ifcfile.createIfcProductDefinitionShape(None, None, [body_representation])

        # IFCWALL in STEP
        return ifcfile.createIfcSlab(create_guid(), owner_history, "slab", name, None, slab_placement,
                                     product_shape, None , None)

    slab = Slab(point_7, point_8, point_10, point_6, "slab01", 0.005)
    # ------------------------------------------------------------------------------------------------------------
    # WC CREATION
    # rotate = 1.0
    rotateY = 0.0

    # 1.,0.,0.
    wc_placement = create_ifclocalplacement(ifcfile, (0., 0., 0.), (0., 0., 1.0), (rotate, rotateY, 0.),
                                            relative_to=wall_placement)

    def WC(start_pt, end_pt, mid_1_pt, mid_2_pt, points_1, points_2, points_3, points_4, points_5, points_6, points_7,
           points_8, points_9,
           name, height, x, y, z):
        global wc_point_center
        wc_placement

        polyline = create_ifcpolyline(ifcfile,
                                      [(start_pt[0], start_pt[1]), (mid_1_pt[0], mid_1_pt[1]),
                                       (mid_2_pt[0], mid_2_pt[1]),
                                       (end_pt[0], end_pt[1])])
        axis_representation = ifcfile.createIfcShapeRepresentation(context, "Axis", "Curve2D", [polyline])

        extrusion_placement = create_ifcaxis2placement(ifcfile, (x, y, z), (0.0, 0.0, 1.0), (1.0, 0.0, 0.0))

        point_list_extrusion_area = [(points_1[0], points_1[1]), (points_2[0], points_2[1]), (points_3[0],
                                                                                              points_3[1]),
                                     (points_4[0], points_4[1]), (points_5[0], points_5[1]),
                                     (points_6[0], points_6[1]), (points_7[0], points_7[1]), (points_8[0], points_8[1]),
                                     (points_9[0], points_9[1]), (points_1[0], points_1[1])]

        solid = create_ifcextrudedareasolid(ifcfile, point_list_extrusion_area, extrusion_placement, (0.0, 0.0, 1.0),
                                            height)
        body_representation = ifcfile.createIfcShapeRepresentation(context, "Body", "SweptSolid", [solid])

        product_shape = ifcfile.createIfcProductDefinitionShape(None, None, [axis_representation, body_representation])

        return ifcfile.createIfcSanitaryTerminal(create_guid(), owner_history, "Toilet", name, None, wc_placement,
                                                 product_shape, None, 'TOILETPAN')

    # -----------------

    furn_placement = create_ifclocalplacement(ifcfile, (0., 0., 0.), (0., 0.0, 1.0), (rotate, rotateY, 0.),
                                            relative_to=wall_placement)
    def FURNITURE(start_pt,  mid_1_pt, mid_2_pt, mid_3_pt,  mid_4_pt,  mid_5_pt,  mid_6_pt, end_pt, description ,name, height, x, y, z):
        furn_placement
        polyline = create_ifcpolyline(ifcfile,
                                      [(start_pt[0], start_pt[1]), (mid_1_pt[0], mid_1_pt[1]),
                                       (mid_2_pt[0], mid_2_pt[1]), (mid_3_pt[0], mid_3_pt[1]),(mid_4_pt[0], mid_4_pt[1]),(mid_5_pt[0], mid_5_pt[1]),(mid_6_pt[0], mid_6_pt[1]),
                                       (end_pt[0], end_pt[1])])
        axis_representation = ifcfile.createIfcShapeRepresentation(context, "Axis", "Curve2D", [polyline])

        extrusion_placement = create_ifcaxis2placement(ifcfile, (x, y, z), (0.0, 0.0, 1.0), (1.0, 0.0, 0.0))

        point_list_extrusion_area = [(start_pt[0], start_pt[1]), (mid_1_pt[0], mid_1_pt[1]),
                                       (mid_2_pt[0], mid_2_pt[1]), (mid_3_pt[0], mid_3_pt[1]),(mid_4_pt[0], mid_4_pt[1]),(mid_5_pt[0], mid_5_pt[1]),(mid_6_pt[0], mid_6_pt[1]),
                                       (end_pt[0], end_pt[1])]

        solid = create_ifcextrudedareasolid(ifcfile, point_list_extrusion_area, extrusion_placement, (0.0, 0.0, 1.0),
                                            height)
        body_representation = ifcfile.createIfcShapeRepresentation(context, "Body", "SweptSolid", [solid])

        product_shape = ifcfile.createIfcProductDefinitionShape(None, None, [axis_representation, body_representation])

        return ifcfile.createIfcFurniture(create_guid(), owner_history, description , name, None, furn_placement,
                                                 product_shape, None, None)


    #handles = FURNITURE((0.,0.017),(0.012, 0.012),(0.017, 0.),(0.012, -0.012), (0., -0.017), (-0.012, -0.012),(-0.017, 0.),(-0.012, 0.012) , "test" ,"handles", 0.75 , x, y, z)
   #handles = FURNITURE((0., 0.017), (0.012, 0.012), (0.017, 0.), (0.012, -0.012), (0., -0.017), (-0.012, -0.012),
                        #(-0.017, 0.), (-0.012, 0.012), "test", "handles", 0.75, x, y, z)


    mirror_placement = create_ifclocalplacement(ifcfile, (0., 0., 0.), (0., 0.0, 1.0), (rotate, rotateY, 0.),
                                              relative_to=wall_placement)

    def MIRROR(start_pt, mid_1_pt, mid_2_pt, end_pt, description, name,
                  height, xs, ys, zs):
        mirror_placement
        polyline = create_ifcpolyline(ifcfile,
                                      [(start_pt[0], start_pt[1]), (mid_1_pt[0], mid_1_pt[1]),
                                       (mid_2_pt[0], mid_2_pt[1]),
                                       (end_pt[0], end_pt[1])])
        axis_representation = ifcfile.createIfcShapeRepresentation(context, "Axis", "Curve2D", [polyline])

        extrusion_placement = create_ifcaxis2placement(ifcfile, (xs, ys, zs), (0.0, 0.0, 1.0), (1.0, 0.0, 0.0))

        point_list_extrusion_area = [(start_pt[0], start_pt[1]), (mid_1_pt[0], mid_1_pt[1]),
                                     (mid_2_pt[0], mid_2_pt[1]),
                                     (end_pt[0], end_pt[1])]

        solid = create_ifcextrudedareasolid(ifcfile, point_list_extrusion_area, extrusion_placement, (0.0, 0.0, 1.0),
                                            height)
        body_representation = ifcfile.createIfcShapeRepresentation(context, "Body", "SweptSolid", [solid])

        product_shape = ifcfile.createIfcProductDefinitionShape(None, None, [axis_representation, body_representation])

        return ifcfile.createIfcFurniture(create_guid(), owner_history, description, name, None, mirror_placement,
                                          product_shape, None, None)


    doorop_placement = create_ifclocalplacement(ifcfile, (0., 0., 0.), (0., 0.0, 1.0), (rotate, rotateY, 0.),
                                              relative_to=wall_placement)

    def DOOROP(start_pt, mid_1_pt, mid_2_pt, end_pt,start_pt2, mid_1_pt2, mid_2_pt2, end_pt2, description, name,
                  height, pluspos, pos_z):
        doorop_placement
        polyline = create_ifcpolyline(ifcfile,
                                      [(start_pt[0]+position_door + pluspos,start_pt[1]), (mid_1_pt[0]+position_door+ pluspos, mid_1_pt[1]),
                                       (mid_2_pt[0]+position_door+ pluspos, mid_2_pt[1]),
                                       (end_pt[0]+position_door+ pluspos, end_pt[1]), (start_pt2[0]+position_door+ pluspos, start_pt2[1]), (mid_1_pt2[0]+position_door+ pluspos, mid_1_pt2[1]),
                                       (mid_2_pt2[0]+position_door+ pluspos, mid_2_pt2[1]),
                                       (end_pt2[0]+position_door+ pluspos, end_pt2[1])])
        axis_representation = ifcfile.createIfcShapeRepresentation(context, "Axis", "Curve2D", [polyline])

        extrusion_placement = create_ifcaxis2placement(ifcfile, (pos_x, pos_y, pos_z), (0.0, 0.0, 1.0), (1.0, 0.0, 0.0))

        point_list_extrusion_area = [(start_pt[0]+position_door + pluspos,start_pt[1]), (mid_1_pt[0]+position_door+ pluspos, mid_1_pt[1]),
                                       (mid_2_pt[0]+position_door+ pluspos, mid_2_pt[1]),
                                       (end_pt[0]+position_door+ pluspos, end_pt[1]), (start_pt2[0]+position_door+ pluspos, start_pt2[1]), (mid_1_pt2[0]+position_door+ pluspos, mid_1_pt2[1]),
                                       (mid_2_pt2[0]+position_door+ pluspos, mid_2_pt2[1]),
                                       (end_pt2[0]+position_door+ pluspos, end_pt2[1])]

        solid = create_ifcextrudedareasolid(ifcfile, point_list_extrusion_area, extrusion_placement, (0.0, 0.0, 1.0),
                                            height)
        body_representation = ifcfile.createIfcShapeRepresentation(context, "Body", "SweptSolid", [solid])

        product_shape = ifcfile.createIfcProductDefinitionShape(None, None, [axis_representation, body_representation])

        return ifcfile.createIfcFurniture(create_guid(), owner_history, description, name, None, doorop_placement,
                                          product_shape, None, None)

    doorop = DOOROP((0.2, 0.16), (0.35, 0.16), (0.35, -0.16), (0.2, -0.16),(0.2, -0.13), (0.328, -0.13), (0.328, 0.13), (0.2,  0.13), "doorop", "doorop1",
                  0.03,0.45, 0.835)

    # -----------------------------ifcWalls--------------------------------------------------

    wall_test = Wall((point_0[0], point_0[1]), (point_1[0], point_1[1]), (point_4[0], point_4[1]),
                     (point_5[0], point_5[1]),
                     (point_6[0], point_6[1]), (point_7[0], point_7[1]), "wall 01", 3.0)

    wall_2 = Wall((point_0[0], point_0[1]), (point_3[0], point_3[1]), (point_7[0], point_7[1]),
                  (point_8[0], point_8[1]),
                  (point_9[0], point_9[1]), (point_4[0], point_4[1]), "wall 02", 3.0)

    wall_3 = Wall((point_2[0], point_2[1]), (point_3[0], point_3[1]), (point_9[0], point_9[1]),
                  (point_8[0], point_8[1]),
                  (point_10[0], point_10[1]), (point_11[0], point_11[1]), "wall 03", 3.0)

    wall_4 = Wall((point_1[0], point_1[1]), (point_2[0], point_2[1]), (point_5[0], point_5[1]),
                  (point_6[0], point_6[1]),
                  (point_10[0], point_10[1]), (point_11[0], point_11[1]), "wall 04", 3.0)

    walls = [wall_test, wall_2, wall_3, wall_4]

    # -----------------------------------------------------------------------------------------

    # ----------------------------
    # WALL MATERIAL

    material = ifcfile.createIfcMaterial("concrete")
    material_layer = ifcfile.createIfcMaterialLayer(material, t, None)
    material_layer_set = ifcfile.createIfcMaterialLayerSet([material_layer], None)
    material_layer_set_usage = ifcfile.createIfcMaterialLayerSetUsage(material_layer_set, "AXIS2", "POSITIVE", -0.1)
    ifcfile.createIfcRelAssociatesMaterial(create_guid(), owner_history, RelatedObjects=walls,
                                           RelatingMaterial=material_layer_set_usage)

    # ------------------------------------------------------------------------------------------------------------
    # WALL PROPS

    property_values = [
        ifcfile.createIfcPropertySingleValue("Reference", "Reference",
                                             ifcfile.create_entity("IfcText", "Describe the Reference"), None),
        ifcfile.createIfcPropertySingleValue("IsExternal", "IsExternal", ifcfile.create_entity("IfcBoolean", True),
                                             None),
        ifcfile.createIfcPropertySingleValue("ThermalTransmittance", "ThermalTransmittance",
                                             ifcfile.create_entity("IfcReal", 2.569), None),
        ifcfile.createIfcPropertySingleValue("IntValue", "IntValue", ifcfile.create_entity("IfcInteger", 2), None)
    ]
    property_set = ifcfile.createIfcPropertySet(create_guid(), owner_history, "Pset_WallCommon", None, property_values)
    ifcfile.createIfcRelDefinesByProperties(create_guid(), owner_history, None, None,
                                            [wall_test, wall_2, wall_3, wall_4], property_set)

    # ------------------------------------------------------------------------------------------------------------
    # WALL QUANTITIES
    quantity_values = [
        ifcfile.createIfcQuantityLength("Length", "Length of the wall", None, l),
        ifcfile.createIfcQuantityArea("Area", "Area of the front face", None, l * b),
        ifcfile.createIfcQuantityVolume("Volume", "Volume of the wall", None,
                                        l * 3.0 * material_layer.LayerThickness)
    ]

    element_quantity = ifcfile.createIfcElementQuantity(create_guid(), owner_history, "BaseQuantities", None, None,
                                                        quantity_values)
    ifcfile.createIfcRelDefinesByProperties(create_guid(), owner_history, None, None,
                                            [wall_test, wall_2, wall_3, wall_4], element_quantity)
    # -----------

    # Slab QUANTITIES
    quantity_values = [
        ifcfile.createIfcQuantityLength("Length", "Length of the slab", None, l),
        ifcfile.createIfcQuantityArea("Area", "Area of the front face", None, l * b),
        ifcfile.createIfcQuantityVolume("Volume", "Volume of the wall", None,
                                        l * 3.0 * material_layer.LayerThickness)
    ]

    element_quantity = ifcfile.createIfcElementQuantity(create_guid(), owner_history, "BaseQuantities", None, None,
                                                        quantity_values)
    ifcfile.createIfcRelDefinesByProperties(create_guid(), owner_history, None, None,
                                            [slab], element_quantity)
    # -----------
    # ------------------------------------------------------------------------------------------------------------
    # DOOR

    # wall selection for door placement
    """
    user_placement_door= eval(input("Geben sie die Nummer der Wand an, in der die Türe platziert werden soll (1-4): "))
    print(user_placement_door)

    wall_selection(user_placement_door)
    #---------------IFC DOOR---------------------
    """
    # wc_placement = create_ifclocalplacement(ifcfile, (0., 0., 0.), (0., 0., 1.0), (rotate, rotateY, 0.),relative_to=wall_placement)
    rotate_door_Y = 0.0
    opening_placement = create_ifclocalplacement(ifcfile, (0., 0., 0.), (0.0, 0.0, 1.0), (1.0, rotate_door_Y, 0.0),
                                                 relative_to=wall_placement)
    door_placement = create_ifclocalplacement(ifcfile, (0., 0. , 0.), (0.0, 0.0, 1.0), (1.0, 0.0, 0.0),
                                              relative_to=opening_placement)

    # start_pt, point_1, point_2, point_3, door_width, door_height, position_door, position_door_end, pos_x, pos_y
    def IfcOpening(point_1, point_2, point_3, point_4, wall_name):
        # Create and associate an opening for the door in the wall
        opening_placement
        opening_extrusion_placement = create_ifcaxis2placement(ifcfile, (pos_x, pos_y, 0.), (0.0, 0.0, 1.0),
                                                               (1.0, 0.0, 0.0))
        point_list_opening_extrusion_area_door = [(position_door, t), (position_door, -t), (position_door_end, -t),
                                                  (position_door_end, t)]
        opening_solid = create_ifcextrudedareasolid(ifcfile, point_list_opening_extrusion_area_door,
                                                    opening_extrusion_placement,
                                                    (0.0, 0.0, 1.0), door_heigth)
        opening_representation = ifcfile.createIfcShapeRepresentation(context, "Body", "SweptSolid", [opening_solid])
        opening_shape = ifcfile.createIfcProductDefinitionShape(None, None, [opening_representation])
        opening_element = ifcfile.createIfcOpeningElement(create_guid(), owner_history, "Opening", "An awesome opening",
                                                          None,
                                                          opening_placement, opening_shape, None)
        ifcfile.createIfcRelVoidsElement(create_guid(), owner_history, None, None, wall_name, opening_element)

        # Relate the door to the opening element
        return ifcfile.createIfcRelFillsElement(create_guid(), owner_history, None, None, opening_element)  # door

    def IfcDoor():
        # Create a simplified representation for the door
        door_placement
        # position door/window in wall:
        door_extrusion_placement = create_ifcaxis2placement(ifcfile, (pos_x, pos_y, 0.), (0.0, 0.0, 1.0),
                                                            (1.0, 0.0, 0.0))
        point_list_door_extrusion_area = [(position_door, t / 2), (position_door, -t / 2), (position_door_end, -t / 2),
                                          (position_door_end, t / 2), (position_door, t / 2)]

        door_solid = create_ifcextrudedareasolid(ifcfile, point_list_door_extrusion_area, door_extrusion_placement,
                                                 (0.0, 0.0, 1.0), door_heigth)
        door_representation = ifcfile.createIfcShapeRepresentation(context, "Body", "SweptSolid", [door_solid])
        door_shape = ifcfile.createIfcProductDefinitionShape(None, None, [door_representation])
        return ifcfile.createIfcDoor(create_guid(), owner_history, "Door", "An awesome door", None, door_placement,
                                     door_shape, "SINGLE_SWING_RIGHT", None)

    # -------------------------------
    # position door/window in wall:
    door_extrusion_placement = create_ifcaxis2placement(ifcfile, (pos_x, pos_y, 0.), (0.0, 0.0, 1.0), (1.0, 0.0, 0.0))
    point_list_door_extrusion_area = [(position_door, -t / 2), (position_door, -door_width),
                                      (position_door_end, -t / 2)]

    door_solid = create_ifcextrudedareasolid(ifcfile, point_list_door_extrusion_area, door_extrusion_placement,
                                             (0.0, 0.0, 1.0), 0.02)
    door_representation = ifcfile.createIfcShapeRepresentation(context, "Body", "Curve", [door_solid])
    door_shape = ifcfile.createIfcProductDefinitionShape(None, None, [door_representation])
    door_2D = ifcfile.createIfcDoor(create_guid(), owner_history, "Door", "An awesome door", None, door_placement,
                                    door_shape, None, None)

    """
    line_door = create_ifcline(ifcfile,(position_door, t / 2), (20.0, t)) #(position_door, door_width)
    door_representation_2D = ifcfile.createIfcShapeRepresentation(context, "Profile", "Curve", [line_door])
    door_shapeLine = ifcfile.createIfcProductDefinitionShape(None, None, [door_representation_2D])
    Line_door= ifcfile.createIfcDoor(create_guid(), owner_history, "Door", "An awesome Line", None, door_placement,
                                 door_shapeLine, None, None)



    line_2D_door = [(position_door, t / 2), (position_door, door_width),(position_door_end, t/2) ]
    polyline_door = create_ifcpolyline(ifcfile, line_2D_door)
    door_representation_2D = ifcfile.createIfcShapeRepresentation(context, "Profile", "Curve", [polyline_door])
    """
    # IfcDoor(start_pt, point_1, point_2, point_3, point_4, door_width, door_height, position_door, position_door_end, pos_x, pos_y
    # (position_door,t),(position_door,-t), (position_door_end, -t),(position_door_end, t),door_width, door_heigth,1.0, 1.0 + door_width, 1.0,0.2

    door_rot = IfcOpening((position_door, t), (position_door, -t), (position_door_end, -t),
                          (position_door_end, t), wall_test)

    door_solid = IfcDoor()
    # door_rot = IfcDoor(wall_2)

    # door_rot = IfcDoor((position_door,-t),(position_door,t), (position_door_end, t),(position_door_end, -t),door_width, door_heigth,1.0, 1.0 + door_width,-1.,2.)
    sink_point_0 = (-0.3, 0.275)
    sink_point_1 = (.3, 0.275)
    sink_point_2 = (0.3, -0.275)
    sink_point_3 = (-0.3, -0.275)

    # an wall 2
    sink_point_4 = (0.275, 0.3)
    sink_point_5 = (0.275, -0.3)
    sink_point_6 = (-0.275, -0.3)
    sink_point_7 = (-0.275, 0.3)

    sink_point_a = (-0.25, 0.15)
    sink_point_b = (0.25, 0.15)
    sink_point_c = (-0.25, -0.2)
    sink_point_d = (0.25, -0.2)

    center = (0., 0.)

    sink_point_list = [sink_point_0, sink_point_1, sink_point_2, sink_point_3,
                       sink_point_4, sink_point_5, sink_point_6, sink_point_7]

    # ---------------SINK--------------------


    sink_placement = create_ifclocalplacement(ifcfile, (0., 0., 0.), (0.0, 0.0, 1.0), (1.0, 0.0, 0.0), wall_placement)

    def sink(sink_point_0, sink_point_1, sink_point_2, sink_point_3, sink_point_4, sink_point_5, sink_point_6, sink_point_7, height ,name, xs, ys, zs):

        # Location
        sink_placement

        # Referenced Location and geometry processing
        extrusion_placement = create_ifcaxis2placement(ifcfile, (xs, ys, zs), (0.0, 0.0, 1.0), (1.0, 0.0, 0.0))
        point_list_extrusion_area = [(sink_point_0[0], sink_point_0[1]), (sink_point_1[0], sink_point_1[1]),
                                     (sink_point_2[0], sink_point_2[1]),
                                     (sink_point_3[0], sink_point_3[1]), (sink_point_4[0], sink_point_4[1]),
                                     (sink_point_5[0], sink_point_5[1]), (sink_point_6[0], sink_point_6[1]),
                                     (sink_point_7[0], sink_point_7[1]), (sink_point_0[0], sink_point_0[1])]
        solid = create_ifcextrudedareasolid(ifcfile, point_list_extrusion_area, extrusion_placement, (0.0, 0.0, 1.0),
                                            height)

        # Representation 3D geometry
        body_representation = ifcfile.createIfcShapeRepresentation(context, "Body", "SweptSolid", [solid])
        product_shape = ifcfile.createIfcProductDefinitionShape(None, None, [body_representation])

        # IFCSINK in STEP
        return ifcfile.createIfcSanitaryTerminal(create_guid(), owner_history, "Sink", name, None, sink_placement,
                                                 product_shape, None, 'SINK')

    def sink4(sink_point_0, sink_point_1, sink_point_2, sink_point_3,  height, name, xs, ys, zs):

        # Location
        sink_placement

        # Referenced Location and geometry processing
        extrusion_placement = create_ifcaxis2placement(ifcfile, (xs, ys, zs), (0.0, 0.0, 1.0), (1.0, 0.0, 0.0))
        point_list_extrusion_area = [(sink_point_0[0], sink_point_0[1]), (sink_point_1[0], sink_point_1[1]),
                                     (sink_point_2[0], sink_point_2[1]),
                                     (sink_point_3[0], sink_point_3[1]), (sink_point_0[0], sink_point_0[1])]
        solid = create_ifcextrudedareasolid(ifcfile, point_list_extrusion_area, extrusion_placement, (0.0, 0.0, 1.0),
                                            height)

        # Representation 3D geometry
        body_representation = ifcfile.createIfcShapeRepresentation(context, "Body", "SweptSolid", [solid])
        product_shape = ifcfile.createIfcProductDefinitionShape(None, None, [body_representation])

        # IFCSINK in STEP
        return ifcfile.createIfcSanitaryTerminal(create_guid(), owner_history, "Sink", name, None, sink_placement,
                                                 product_shape, None, 'SINK')

    def supportwc(point_0, point_1, point_2, point_3,  height, name, x, y, z):

        # Location
        wc_placement

        # Referenced Location and geometry processing
        extrusion_placement = create_ifcaxis2placement(ifcfile, (x, y, z), (0.0, 0.0, 1.0), (1.0, 0.0, 0.0))
        point_list_extrusion_area = [(point_0[0], point_0[1]), (point_1[0], point_1[1]),
                                     (point_2[0], point_2[1]),
                                     (point_3[0],point_3[1]), (point_0[0], point_0[1])]
        solid = create_ifcextrudedareasolid(ifcfile, point_list_extrusion_area, extrusion_placement, (0.0, 0.0, 1.0),
                                            height)

        # Representation 3D geometry
        body_representation = ifcfile.createIfcShapeRepresentation(context, "Body", "SweptSolid", [solid])
        product_shape = ifcfile.createIfcProductDefinitionShape(None, None, [body_representation])

        # IFCSINK in STEP
        return ifcfile.createIfcSanitaryTerminal(create_guid(), owner_history, "SupportWc", name, None, wc_placement,
                                                 product_shape, None, None)
    """

    sink_opening_placement = create_ifclocalplacement(ifcfile, (0.,0.,0.), (0.0, 0.0, 1.0), (1.0, 0.0, 0.0), wall_placement)
    sink_opening_extrusion_placement = create_ifcaxis2placement(ifcfile, ((-1.0),-0.2-t-0.075,1.0) , (0.0, 0.0, 1.0), (1.0, 0.0, 0.0))
    sink_point_list_opening_extrusion_area = [sink_point_4, sink_point_5, sink_point_6, sink_point_7]
    sink_opening_solid = create_ifcextrudedareasolid(ifcfile, sink_point_list_opening_extrusion_area, sink_opening_extrusion_placement,
                                                (0.0, 0.0, 1.0), 0.2)
    sink_opening_representation = ifcfile.createIfcShapeRepresentation(context, "Body", "SweptSolid", [sink_opening_solid])
    sink_opening_shape = ifcfile.createIfcProductDefinitionShape(None, None, [sink_opening_representation])
    sink_opening_element = ifcfile.createIfcOpeningElement(create_guid(), owner_history, "Opening", "An awesome opening", None,
                                                      sink_opening_placement, sink_opening_shape, None)
    ifcfile.createIfcRelVoidsElement(create_guid(), owner_history, None, None, wall_test, sink_opening_element)


    sink_placement = create_ifclocalplacement(ifcfile, (0.,0.,0.), (0.,0.,1.0), (-1.0,0.,0.), sink_opening_placement)
    polyline = create_ifcpolyline(ifcfile, [sink_point_list[0], sink_point_list[1], sink_point_list[2], sink_point_list[3]])
    axis_representation = ifcfile.createIfcShapeRepresentation(context, "Axis", "Curve2D", [polyline])

    extrusion_placement = create_ifcaxis2placement(ifcfile, ((-1.0),-0.2-t-0.075,0.9), (0.0, 0.0, 1.0), (1.0, 0.0, 0.0))
                                                            #(-2.0),-0.2-t,0.2)
                                                            #(2.0),4.2-t,0.2)


    sink_point_center = center

    point_list_extrusion_area = [sink_point_list[0], sink_point_list[1], sink_point_list[2], sink_point_list[3]]
    solid = create_ifcextrudedareasolid(ifcfile, point_list_extrusion_area, extrusion_placement, (0.0, 0.0, 1.0), 0.2)
    body_representation = ifcfile.createIfcShapeRepresentation(context, "Body", "SweptSolid", [solid])

    product_shape = ifcfile.createIfcProductDefinitionShape(None, None, [axis_representation, body_representation])

    sink = ifcfile.createIfcFlowTerminal(create_guid(), owner_history, "Sink", "A simple sink", None, sink_placement,
                                             product_shape, None)


    # Relate the door to the opening element
    ifcfile.createIfcRelFillsElement(create_guid(), owner_history, None, None, sink_opening_element, sink)


     """
    # ----------------------------ifcToilet------------------------------------------

    # rotation of the toilet

    if wallselwc == 3:
        #y == b - 2 * t:
        # Placement at wall 3
        wc_placement = create_ifclocalplacement(ifcfile, (0., 0., 0.), (0., 0., 1.0), (rotate, rotateY, 0.),
                                                relative_to=wall_placement)
        wc = WC((wc_point_0[0], wc_point_0[1]), (wc_point_1[0], wc_point_1[1]), (wc_point_2[0], wc_point_2[1]),
                (wc_point_3[0], wc_point_3[1]),
                (wc_point_0[0], wc_point_0[1]), (wc_point_1[0], wc_point_1[1]), (wc_point_2[0], wc_point_2[1]),
                (wc_point_6[0], wc_point_6[1]),
                (wc_point_7[0], wc_point_7[1]), (wc_point_4[0], wc_point_4[1]), (wc_point_9[0], wc_point_9[1]),
                (wc_point_8[0], wc_point_8[1]),
                (wc_point_3[0], wc_point_3[1]), "wc_new1", 0.4, x, y, z)

        support1 = supportwc(( 0.367, -0.55), ( 0.337,-0.55), ( 0.337, 0.2), (0.367, 0.2), 0.03, "supportL_wall3", x, y, z + 0.65)
        lehne = supportwc((0.337, 0.15), (-0.337, 0.15), (-0.337, 0.179 ), ( 0.337, 0.179), 0.4, "support_wall3_seat", x, y, z + 0.45)
        support2 = supportwc((-0.337, 0.15), (-0.367, 0.15), ( -0.367, 0.179), (-0.337, 0.179), 0.75, "supportR_wall3", x, y, z + 0.65)
        toilettenpapierv = supportwc(( 0.367, -0.4), (0.337, -0.4), ( 0.337, -0.37), (0.367, -0.37), 0.08, "toiletpapervertcal_wall3", x,y, z + 0.57)
        toilettenpapierh = supportwc(( 0.367, -0.45), (0.337, -0.45), ( 0.337, -0.37), (0.367, -0.37), 0.03, "toiletpaperhorizontal_wall3",x, y, z + 0.57)
        bin = supportwc(( 0.417, 0.1), (0.337, 0.1), ( 0.337, 0.2), ( 0.417, 0.2), 0.2, "bin_wall3",x, y, z + 0.15)



    elif wallselwc == 1:
        #y == 2 * t:

        # Placement at wall 1
        wc_placement = create_ifclocalplacement(ifcfile, (0., 0., 0.), (0., 0., 1.0), (rotate, rotateY, 0.),
                                                relative_to=wall_placement)
        wc = WC((wc_point_3[0], wc_point_3[1]), (wc_point_2[0], wc_point_2[1]), (wc_point_1[0], wc_point_1[1]),
                (wc_point_0[0], wc_point_0[1]),

                (wc_point_3[0], wc_point_3[1]), (wc_point_2[0], wc_point_2[1]), (wc_point_1[0], wc_point_1[1]),
                (wc_point_15[0], wc_point_15[1]), (wc_point_16[0], wc_point_16[1]), (wc_point_17[0], wc_point_17[1]),
                (-wc_point_16[0], wc_point_16[1]),
                (-wc_point_15[0], wc_point_15[1]), (wc_point_0[0], wc_point_0[1]), "wc_new2", 0.4, x, y, z)

        support1 = supportwc((-0.367, 0.55), (-0.337, 0.55), (-0.337, -0.2), (-0.367, -0.2), 0.03, "supportL_wall3", x, y,z + 0.65)
        lehne = supportwc((-0.337, -0.15), (0.337, -0.15), (0.337, -0.179), (-0.337, -0.179), 0.4, "support_wall3_seat", x,y, z + 0.45)
        support2 = supportwc((0.337, -0.15), (0.367, -0.15), (0.367, -0.179), (0.337, -0.179), 0.75, "supportR_wall3",x, y, z + 0.65)
        toilettenpapierv = supportwc((-0.367, 0.4), (-0.337,0.4), (-0.337, 0.37), (-0.367, 0.37), 0.08,"toiletpapervertcal_wall3", x, y, z + 0.57)
        toilettenpapierh = supportwc((-0.367, 0.45), (-0.337, 0.45), (-0.337, 0.37), (-0.367, 0.37), 0.03, "toiletpaperhorizontal_wall3", x, y, z + 0.57)
        bin = supportwc((-0.417, -0.1), (-0.337, -0.1), (-0.337, -0.2), (-0.417,-0.2), 0.2, "bin_wall3", x, y, z + 0.15)



    elif wallselwc == 2:
        #x == 2 * t:
        # Placement at wall 2
        wc_placement = create_ifclocalplacement(ifcfile, (0., 0., 0.), (0., 0., 1.0), (rotate, rotateY, 0.),
                                                relative_to=wall_placement)
        wc = WC((wc_point_0[0], wc_point_0[1]), (wc_point_1[0], wc_point_1[1]), (wc_point_2[0], wc_point_2[1]),
                (wc_point_3[0], wc_point_3[1]),
                (wc_point_3[0], wc_point_3[1]), (wc_point_0[0], wc_point_0[1]), (wc_point_1[0], wc_point_1[1]),
                (wc_point_10[0], wc_point_10[1]), (wc_point_11[0], wc_point_11[1]), (wc_point_12[0], wc_point_12[1]),
                (wc_point_13[0], wc_point_13[1]),
                (wc_point_14[0], wc_point_14[1]), (wc_point_2[0], wc_point_2[1]), "wc_rotated3", 0.4, x, y, z)

        support1 = supportwc((0.55, 0.367), (0.55, 0.337), (-0.2, 0.337), (-0.2, 0.367), 0.03, "supportL_wall2", x, y, z + 0.65)
        lehne = supportwc((-0.15, 0.337), (-0.15, -0.337), (-0.179, -0.337), (-0.179, 0.337), 0.4, "support_wall2_seat", x, y, z + 0.45)
        support2 = supportwc((-0.15, -0.337), (-0.15, -0.367), (-0.179, -0.367), (-0.179, -0.337), 0.75, "supportR_wall2", x, y, z + 0.65)
        toilettenpapierv = supportwc((0.4, 0.367), (0.4, 0.337), (0.37, 0.337), (0.37,0.367), 0.08, "toiletpapervertcal_wall2", x,y, z + 0.57)
        toilettenpapierh = supportwc((0.45, 0.367), (0.45, 0.337), (0.37, 0.337), (0.37, 0.367), 0.03, "toiletpaperhorizontal_wall2",x, y, z + 0.57)
        bin = supportwc((-0.1, 0.417), (-0.1, 0.337), (-0.2, 0.337), (-0.2, 0.417), 0.2, "bin_wall2",x, y, z + 0.15)


    elif wallselwc == 4:
        #x == l - 2 * t:
        # Placement at wall 4
        wc_placement = create_ifclocalplacement(ifcfile, (0., 0., 0.), (0., 0., 1.0), (rotate, rotateY, 0.),
                                                relative_to=wall_placement)
        wc = WC((wc_point_0[0], wc_point_0[1]), (wc_point_1[0], wc_point_1[1]), (wc_point_2[0], wc_point_2[1]),
                (wc_point_3[0], wc_point_3[1]),

                (wc_point_2[0], wc_point_2[1]), (wc_point_1[0], wc_point_1[1]), (wc_point_0[0], wc_point_0[1]),
                (-wc_point_10[0], wc_point_10[1]), (-wc_point_11[0], wc_point_11[1]), (-wc_point_12[0], wc_point_12[1]),
                (-wc_point_13[0], wc_point_13[1]),
                (-wc_point_14[0], wc_point_14[1]), (wc_point_3[0], wc_point_3[1]), "wc_rotated4", 0.4, x, y, z)

        support1 = supportwc((-0.55, -0.367), (-0.55, -0.337), (0.2, -0.337), (0.2, -0.367), 0.03, "supportL_wall2", x, y, z + 0.65)
        lehne = supportwc((0.15, -0.337), (0.15, 0.337), (0.179, 0.337), (0.179, -0.337), 0.4, "support_wall2_seat", x, y, z + 0.45)
        support2 = supportwc((0.15, 0.337), (0.15, 0.367), (0.179, 0.367), (0.179, 0.337), 0.75, "supportR_wall2", x, y, z + 0.65)
        toilettenpapierv = supportwc((-0.4, -0.367), (-0.4, -0.337), (-0.37, -0.337), (-0.37,-0.367), 0.08, "toiletpapervertcal_wall2", x,y, z + 0.57)
        toilettenpapierh = supportwc((-0.45, -0.367), (-0.45, -0.337), (-0.37, -0.337), (-0.37, -0.367), 0.03, "toiletpaperhorizontal_wall2",x, y, z + 0.57)
        bin = supportwc((0.1, -0.417), (0.1, -0.337), (0.2, -0.337), (0.2, -0.417), 0.2, "bin_wall2",x, y, z + 0.15)

    if wallselsink == 7:
        #ys == float(b - 2 * t - 0.075)

        # Placement at wall 3
        sink_placement = create_ifclocalplacement(ifcfile, (0., 0., 0.), (0.0, 0.0, 1.0), (1.0, 0.0, 0.0),
                                                  wall_placement)
        #sink = sink(sink_point_0, sink_point_1, sink_point_2, sink_point_3, "sink_wall3", xs, ys, zs)
        sink1 = sink((0.3, -0.275), (-0.3, -0.275), (-0.3, 0.275), (-0.267, 0.275), (-0.267, -0.242), (0.267, -0.242),(0.267, 0.275), (0.3, 0.275), 0.13, "sink_wall1", xs, ys, zs)
        sink2 = sink4((0.267, -0.242), (-0.267, -0.242), (-0.267, 0.158), (0.267, 0.158), 0.02, "sink_wall3_bottom", xs,ys, zs)
        sink3 = sink4((-0.267, 0.158), (-0.267, 0.275), (0.267, 0.275), (0.267, 0.158), 0.13, "sink_wall1_back", xs, ys, zs)

        sink4A = sink4((0.013, 0.192), (-0.013, 0.192), (-0.013, 0.217), (0.013, 0.217), 0.1,"sink_wall3_ArmaturVertikal", xs, ys, zs + 0.13)
        sink5A = sink4((0.013, 0.108), (-0.013, 0.108), (-0.013, 0.217), (0.013, 0.217), 0.025,"sink_wall3_ArmaturWasser", xs, ys, zs + 0.18)
        sink6A = sink4((0.013, 0.158), (-0.013, 0.158), (-0.013, 0.217), (0.013, 0.217), 0.01,"sink_wall3_ArmaturHebel", xs, ys, zs + 0.23)

        mirror = MIRROR((0.3, 0.26), (-0.3,0.26,), (-0.3, 0.275), ( 0.3, 0.275), "mirror", "mirror3",
                        1.0, xs, ys, 1.0)

    elif wallselsink == 5:
        #ys == 2 * t + 0.075:
        # Placement at wall 1
        sink_placement = create_ifclocalplacement(ifcfile, (0., 0., 0.), (0.0, 0.0, 1.0), (1.0, 0.0, 0.0),
                                                  wall_placement)

        sink1 = sink((-0.3, 0.275), (0.3, 0.275), (0.3, -0.275), (0.267, -0.275), (0.267, 0.242), (-0.267, 0.242), (-0.267, -0.275),(-0.3, -0.275), 0.13,  "sink_wall1", xs, ys, zs)
        sink2 = sink4((-0.267, 0.242), (0.267, 0.242), (0.267, -0.158), (-0.267, -0.158),0.02, "sink_wall1_bottom", xs, ys, zs)
        sink3 = sink4((0.267, -0.158), (0.267, -0.275), (-0.267, -0.275),(-0.267, -0.158), 0.13, "sink_wall1_back", xs, ys,zs)

        sink4A = sink4((-0.013, -0.192), (0.013, -0.192), (0.013, -0.217), (-0.013, -0.217), 0.1, "sink_wall1_ArmaturVertikal", xs, ys,zs+0.13)
        sink5A = sink4((-0.013, -0.108), (0.013, -0.108), (0.013, -0.217), (-0.013, -0.217), 0.025, "sink_wall1_ArmaturWasser",xs, ys, zs + 0.18)
        sink6A = sink4((-0.013, -0.158), (0.013, -0.158), (0.013, -0.217), (-0.013, -0.217), 0.01,"sink_wall1_ArmaturHebel", xs, ys, zs + 0.23)

        mirror = MIRROR((-0.3, -0.26), (0.3, -0.26), (0.3, -0.275), (-0.3, -0.275), "mirror", "mirror1",
                        1.0, xs, ys, 1.0)

    elif wallselsink == 6:
        #xs == float(2 * t  + 0.075):
        # xs == 2 * t  + 0.075:
        # Placement at wall 2
        sink_placement = create_ifclocalplacement(ifcfile, (0., 0., 0.), (0.0, 0.0, 1.0), (1.0, 0.0, 0.0),
                                                  wall_placement)
        #sink = sink(sink_point_4, sink_point_5, sink_point_6, sink_point_7, "sink_wall2", xs , ys, zs)

        sink1 = sink(( 0.275, 0.3), (0.275, -0.3), (-0.275, -0.3), (-0.275, -0.267), (0.242, -0.267), (0.242, 0.267), (-0.275, 0.267),(-0.275, 0.3), 0.13,  "sink_wall2", xs, ys, zs)
        sink2 = sink4((0.242, 0.267), ( 0.242, -0.267, ), (-0.158, -0.267), ( -0.158, 0.267),0.02, "sink_wall2_bottom", xs, ys, zs)
        sink3 = sink4(( -0.158, 0.267), (-0.158, -0.267), (-0.275, -0.267),(-0.275, 0.267), 0.13, "sink_wall2_back", xs, ys,zs)

        sink4A = sink4((-0.192, 0.013,), ( -0.192, -0.013), (-0.217, -0.013), (-0.217, 0.013), 0.1, "sink_wall2_ArmaturVertikal", xs, ys,zs+0.13)
        sink5A = sink4(( -0.108, 0.013), (-0.108, -0.013), (-0.217, -0.013), (-0.217, 0.013), 0.025, "sink_wall2_ArmaturWasser",xs, ys, zs + 0.18)
        sink6A = sink4((-0.158, 0.013), ( -0.158, -0.013), (-0.217, -0.013), (-0.217, 0.013), 0.01,"sink_wall2_ArmaturHebel", xs, ys, zs + 0.23)


        mirror = MIRROR((-0.26, 0.3), (-0.26, -0.3,), (-0.275, -0.3), (-0.275, 0.3), "mirror", "mirror2",
                        1.0, xs, ys, 1.0)

    elif wallselsink == 8:
        #xs == l - 2 * t - 0.075:
        # Placement at wall 4
        sink_placement = create_ifclocalplacement(ifcfile, (0., 0., 0.), (0.0, 0.0, 1.0), (1.0, 0.0, 0.0),
                                                  wall_placement)
        #sink = sink(sink_point_4, sink_point_5, sink_point_6, sink_point_7, "sink_wall4", xs, ys, zs)
        sink1 = sink(( -0.275, -0.3), (-0.275, 0.3), (0.275, 0.3), (0.275, 0.267), (-0.242, 0.267), (-0.242, -0.267), (0.275, -0.267),(0.275, -0.3), 0.13,  "sink_wall2", xs, ys, zs)
        sink2 = sink4((-0.242, -0.267), ( -0.242, 0.267, ), (0.158, 0.267), ( 0.158, -0.267),0.02, "sink_wall4_bottom", xs, ys, zs)
        sink3 = sink4(( 0.158, -0.267), (0.158, 0.267), (0.275, 0.267),(0.275, -0.267), 0.13, "sink_wall4_back", xs, ys,zs)

        sink4A = sink4((0.192, -0.013,), ( 0.192, 0.013), (0.217, 0.013), (0.217, -0.013), 0.1, "sink_wall4_ArmaturVertikal", xs, ys,zs+0.13)
        sink5A = sink4(( 0.108, -0.013), (0.108, 0.013), (0.217, 0.013), (0.217, -0.013), 0.025, "sink_wall4_ArmaturWasser",xs, ys, zs + 0.18)
        sink6A = sink4((0.158, -0.013), ( 0.158, 0.013), (0.217, 0.013), (0.217, -0.013), 0.01,"sink_wall4_ArmaturHebel", xs, ys, zs + 0.23)



        mirror = MIRROR((0.26, -0.3), (0.26, 0.3,), (0.275, 0.3), (0.275, -0.3), "mirror", "mirror4",
                        1.0, xs, ys, 1.0)


    # sink = sink(sink_point_4, sink_point_5, sink_point_6, sink_point_7, "sink_wall2", xs, ys, zs)
    # Variables for the position of the toilet in terms of the vertices of the room
    vertex_0_x = float("%8.1f" % (point_7[0]))
    vertex_0_y = float("%8.1f" % (point_7[1]))

    vertex_1_x = float("%8.1f" % (point_8[0]))
    vertex_1_y = float("%8.1f" % (point_8[1]))

    vertex_2_x = float("%8.1f" % (point_10[0]))
    vertex_2_y = float("%8.1f" % (point_10[1]))

    vertex_3_x = float("%8.1f" % (point_6[0]))
    vertex_3_y = float("%8.1f" % (point_6[1]))

    # 90cm Bewegungsfläche neben Klo
    movearea_point_0 = float("%8.1f" % (x - 1.1))
    movearea_point_1 = float("%8.1f" % (x + 1.1))
    movearea_point_2 = float("%8.1f" % (y - 1.1))
    movearea_point_3 = float("%8.1f" % (y + 1.1))

    # ist Bewegungsfläche seitlich Klo innerhalb des Raums?
    def rulecheck(axis, value, value_rotate, vertex_left, vertex_right, area1, area2):
        if axis == value and rotate == value_rotate:
            if area1 > vertex_left:
                print("Die Bewegungsfläche ist außerhalb des Raums!")
                return 1

            elif area1 == vertex_left:
                print("Achtung, die Bewegungsfläche ist gerade noch innerhalb des Raums!")


            elif area2 < vertex_right:
                print("Die Bewegungsfläche ist außerhalb des Raums!!")
                return 2

            elif area2 == vertex_right:
                print("Achtung, die Bewegungsfläche ist gerade noch innerhalb des Raums!!")

    test_1_w2 = rulecheck(x, (2 * t), 1.0, vertex_1_y, vertex_0_y, movearea_point_3, movearea_point_2)
    test_1_w4 = rulecheck(x, (2 * t - l), -1.0, -vertex_3_y, -vertex_2_y, movearea_point_3, movearea_point_2)

    test_1_w3 = rulecheck(y, (b - 2 * t), 1.0, vertex_2_x, vertex_1_x, movearea_point_1, movearea_point_0)
    # print(y,(b-2*t),1.0, "vertexleft", vertex_2_x, vertex_1_x, "area1", movearea_point_1,movearea_point_0)

    test_1_w1 = rulecheck(y, (-2 * t), -1.0, -vertex_0_x, -vertex_3_x, movearea_point_1, movearea_point_0)

    # --------------------------------------------------------------------------------#--------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------#--------------------------------------------------------------------------------

    # -----------------------------------------------------
    # Relate the window and wall to the building storey
    ifcfile.createIfcRelContainedInSpatialStructure(create_guid(), owner_history, "Building Storey Container", None,
                                                    [wall_test, wall_2, wall_3, wall_4, wc,support1,lehne, support2,toilettenpapierv, toilettenpapierh, door_rot, sink1, sink2,sink3,sink4A,sink5A, sink6A ,slab,
                                                     door_solid, door_2D, mirror, doorop, bin
                                                     ], building_storey)  #

    ifcfile.write(filename)

    # ------------------------------------------------------------------------------------------------------------

    # -----------------------------

    ifcfile = ifcopenshell.open(temp2_filename)
    owner_history = ifcfile.by_type("IfcOwnerHistory")[0]
    project = ifcfile.by_type("IfcProject")[0]
    context = ifcfile.by_type("IfcGeometricRepresentationContext")[0]

    # ------------------------------------------------------------------------------------------------------------
    # IFC HIERARCHY

    site_placement = create_ifclocalplacement(ifcfile)
    site = ifcfile.createIfcSite(create_guid(), owner_history, "Site", None, None, site_placement, None, None,
                                 "ELEMENT",
                                 None, None, None, None, None)

    building_placement = create_ifclocalplacement(ifcfile, relative_to=site_placement)
    building2 = ifcfile.createIfcBuilding(create_guid(), owner_history, 'Building', None, None, building_placement,
                                          None,
                                          None, "ELEMENT", None, None, None)

    storey_placement = create_ifclocalplacement(ifcfile, relative_to=building_placement)
    elevation = 0.0
    building_storey2 = ifcfile.createIfcBuildingStorey(create_guid(), owner_history, 'Storey2', None, None,
                                                       storey_placement,
                                                       None, None, "ELEMENT", elevation)

    container_storey = ifcfile.createIfcRelAggregates(create_guid(), owner_history, "Building Container", None,
                                                      building2,
                                                      [building_storey2])
    container_site = ifcfile.createIfcRelAggregates(create_guid(), owner_history, "Site Container", None, site,
                                                    [building2])
    container_project = ifcfile.createIfcRelAggregates(create_guid(), owner_history, "Project Container", None, project,
                                                       [site])

    wc_placement
    sink_placement
    wall_placement
    door_placement
    position_door

    def AREA(point_a, point_b, point_c, point_d, name, placement, x, y):
        polyline = create_ifcpolyline(ifcfile,
                                      [(point_a[0], point_a[1]), (point_b[0], point_b[1]), (point_c[0], point_c[1]),
                                       (point_d[0], point_d[1]), (point_a[0], point_a[1])])
        axis_representation = ifcfile.createIfcShapeRepresentation(context, "Axis", "Curve2D", [polyline])

        extrusion_placement = create_ifcaxis2placement(ifcfile, (x, y, 0.009), (0.0, 0.0, 1.0), (1.0, 0.0, 0.0))

        point_list_extrusion_area = [(point_a[0], point_a[1]), (point_b[0], point_b[1]), (point_c[0], point_c[1]),
                                     (point_d[0], point_d[1]), (point_a[0], point_a[1]), (point_b[0], point_b[1])]

        solid = create_ifcextrudedareasolid(ifcfile, point_list_extrusion_area, extrusion_placement, (0.0, 0.0, 1.0),
                                            0.001)
        body_representation = ifcfile.createIfcShapeRepresentation(context, "Body", "SweptSolid", [solid])

        product_shape = ifcfile.createIfcProductDefinitionShape(None, None, [axis_representation, body_representation])

        return ifcfile.createIfcSanitaryTerminal(create_guid(), owner_history, "space", name, None,
                                                 placement,
                                                 product_shape, None, "USERDEFINED")

    # ----------150 x 150 Movement area----------------------------
    # Mittelpunkt Raum 2D
    if wallselwc == 1 or wallselwc == 3 :
        area_room = AREA((-0.75, 0.75), (0.75, 0.75), (0.75, -0.75), (-0.75, -0.75), "roomarea", wc_placement, xm, ym)

    if  wallselwc == 2 or wallselwc == 4:
        area_room = AREA((-0.75, 0.75), (0.75, 0.75), (0.75, -0.75), (-0.75, -0.75), "roomarea", wc_placement, xm,
                         ym)

    if wallselsink == 5  or wallselsink == 7 :
        area_room_sink = AREA((-0.75, 0.75), (0.75, 0.75), (0.75, -0.75), (-0.75, -0.75), "roomareaSink", wc_placement, xms, yms)

    if wallselsink == 6 or wallselsink == 8:
        area_room_sink = AREA((-0.75, 0.75), (0.75, 0.75), (0.75, -0.75), (-0.75, -0.75), "roomareaSink", wc_placement, xms, yms)

    door_area = AREA((0.7, 0.2), (0.7, 1.4), (2.2, 1.4), (2.2, 0.2), "roomarea", door_placement,  position_door - door_width , pos_y)

    # -------door area-------------
    coords_area_door_int = [point_list_opening_extrusion_area[0],
                            (
                            (point_list_opening_extrusion_area[0][0] - 0.5), (point_list_opening_extrusion_area[0][1])),
                            ((point_list_opening_extrusion_area[0][0] - 0.5),
                             (point_list_opening_extrusion_area[0][1] + 1.2)),
                            ((point_list_opening_extrusion_area[0][0] + 1.),
                             (point_list_opening_extrusion_area[0][1] + 1.2)),
                            ((point_list_opening_extrusion_area[0][0] + 1.), (point_list_opening_extrusion_area[0][1])),
                            (
                            (point_list_opening_extrusion_area[0][0] + 1.0), (point_list_opening_extrusion_area[0][1]))]

    print(coords_area_door_int)
    # door_area2 = AREA(((point_list_opening_extrusion_area[0][0] - 0.5), (point_list_opening_extrusion_area[0][1])),((point_list_opening_extrusion_area[0][0] - 0.5),(point_list_opening_extrusion_area[0][1] + 1.2)), ((point_list_opening_extrusion_area[0][0] + 1.), (point_list_opening_extrusion_area[0][1] + 1.2)),((point_list_opening_extrusion_area[0][0] + 1.), (point_list_opening_extrusion_area[0][1])), "doorarea", door_placement, pos_x, pos_y)
    door_placement = create_ifclocalplacement(ifcfile, (0., 0., 0.), (0.0, 0.0, 1.0), (1.0, rotate_door_Y, 0.0),
                                              relative_to=opening_placement)

    def AREADOORINT(point_a, point_b, point_c, point_d, point_e, point_f, name, placement, pos_x, pos_y):
        door_placement
        polyline = create_ifcpolyline(ifcfile,
                                      [(point_a[0], point_a[1]), (point_b[0], point_b[1]), (point_c[0], point_c[1]),
                                       (point_d[0], point_d[1]), (point_e[0], point_e[1]), (point_f[0], point_f[1]),
                                       (point_a[0], point_a[1])])
        axis_representation = ifcfile.createIfcShapeRepresentation(context, "Axis", "Curve2D", [polyline])

        extrusion_placement = create_ifcaxis2placement(ifcfile, (pos_x, pos_y, 0.009), (0.0, 0.0, 1.0), (1.0, 0.0, 0.0))

        point_list_extrusion_area = [(point_a[0], point_a[1]), (point_b[0], point_b[1]), (point_c[0], point_c[1]),
                                     (point_d[0], point_d[1]), (point_e[0], point_e[1]), (point_f[0], point_f[1]),
                                     (point_a[0], point_a[1])]

        solid = create_ifcextrudedareasolid(ifcfile, point_list_extrusion_area, extrusion_placement, (0.0, 0.0, 1.0),
                                            0.2)
        body_representation = ifcfile.createIfcShapeRepresentation(context, "Body", "SweptSolid", [solid])

        product_shape = ifcfile.createIfcProductDefinitionShape(None, None, [axis_representation, body_representation])

        return ifcfile.createIfcSanitaryTerminal(create_guid(), owner_history, "spaceDoor", name, None,
                                                 placement,
                                                 product_shape, None, "USERDEFINED")

    # --------------WC ROTATION------------------------
    # rotation of the areas wc
    if wallselwc == 3:
        #y == b - 2 * t:
        # Placement at wall 3
        wc_area = AREA((1.1, - 0.5), (- 1.1, - 0.5), (- 1.1, 0.2), (1.1, 0.2), "wcarea1", wc_placement, x, y)


    elif wallselwc == 1:
        #y == 2 * t:
        # Placement at wall 1
        wc_area = AREA((- 1.1, 0.5), (1.1, 0.5), (1.1, - 0.2), (- 1.1, - 0.2), "wcarea2", wc_placement, x, y )


    elif wallselwc == 2:
        #x == 2 * t:
        # Placement at wall 2
        wc_area = AREA((0.5, 1.1), (0.5, -1.1), (-0.2, -1.1), (- 0.2, 1.1), "wcarea3", wc_placement, x, y)


    elif wallselwc == 4:
        #x == l - 2 * t:
        # Placement at wall 4
        wc_area = AREA((-0.5, -1.1), (-0.5, 1.1), (0.2, 1.1), (0.2, -1.1), "wcarea4", wc_placement, x, y)

    # --------------SINK ROTATION------------------------
    # rotation of the areas wc
    if wallselsink == 7:
        #ys == b - 2 * t - 0.075
        # Placement at wall 3
        sink_area = AREA((0.45, -0.275), (-0.45, -0.275), (-0.45, 0.275), (0.45, 0.275), "sinkarea3", sink_placement,
                         xs, ys)


    elif wallselsink == 5:
        #ys == 2 * t + 0.075:
        # Placement at wall 1
        sink_area = AREA((-0.45, 0.275), (0.45, 0.275), (0.45, -0.275), (-0.45, -0.275), "sinkarea1", sink_placement,
                         xs, ys)

    elif wallselsink == 6:
        #xs == float(2 * t + 0.075):
        # Placement at wall 2
        sink_area = AREA((0.275, 0.45), (0.275, -0.45), (-0.275, -0.45), (-0.275, 0.45), "sinkarea2", sink_placement,
                         xs , ys)

    elif wallselsink == 8:
        #xs == l - 2 * t - 0.075:
        # Placement at wall 4
        sink_area = AREA((-0.275, -0.45), (-0.275, 0.45), (0.275, 0.45), (0.275, -0.45), "sinkarea4", sink_placement,
                         xs, ys)

    # sink_area = AREA((0.275, 0.45), (0.275, -0.45), (-0.275, -0.45), (-0.275, 0.45), "sinkarea2", sink_placement, xs,ys)
    """
    door_area = AREADOORINT(coords_area_door_int[0], coords_area_door_int[1], coords_area_door_int[2],
                            coords_area_door_int[3],
                            coords_area_door_int[4], coords_area_door_int[5], "doorarea", door_placement, pos_x,
                            pos_y)    """

    # ------------------------------------------------------------------------------------------------------------
    # Relate the window and wall to the building storey
    ifcfile.createIfcRelContainedInSpatialStructure(create_guid(), owner_history, "Building Storey Container", None,
                                                    [door_area, sink_area, wc_area, area_room, area_room_sink], building_storey2)

    # OUTPUT

    ifcfile.write(filename_area)

    # ------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------
    # liegen die Eckpunkte der Movearea im Raum?
    wc_pos = (abs(float(x)), abs(float(y)))
    wc_dist = 1.118

    sink_pos = (abs(float(xs)), abs(float(ys)))
    # print(sink_pos)
    sink_dist = 0.527

    # Check point_8 und WC
    def CheckWC(point_a, point_b, distance):
        d = math.sqrt((point_a[0] - point_b[0]) ** 2 + (point_a[1] - point_b[1]) ** 2)
        # print(d)
        if d < distance:
            # print("WC position is NOT code compliant")
            return False

        else:
            # print("WC position is code compliant")
            return True

    WC_CHECK = [
        CheckWC(point_8, wc_pos, wc_dist),
        CheckWC(point_10, wc_pos, wc_dist),
        CheckWC(point_7, wc_pos, wc_dist),
        CheckWC(point_6, wc_pos, wc_dist)]

    # print(WC_CHECK)
    for w in WC_CHECK:
        if w == False:
            print("WC position is not code compliant")

    SINK_CHECK = [
        CheckWC(sink_pos, point_8, sink_dist),
        CheckWC(sink_pos, point_10, sink_dist),
        CheckWC(sink_pos, point_7, sink_dist),
        CheckWC(sink_pos, point_6, sink_dist)]

    print(SINK_CHECK)
    for s in SINK_CHECK:
        if s == False:
            print("Sink position is not code compliant")

    # Flöchenoptimierung
    roomWidth = float(roomWidth)
    roomLength = float(roomLength)

    roomarea_total = roomLength * roomWidth

    ##!!!!!! Move Areas dürfen nicht rotiete werden mit -1, sie müssen neu erzeugt werden, wie das Klo siehe oben!!!!!!
    import threading

    #time.sleep(20)
    #main()


    while True:
        time.sleep(random.random() * 5)  # wait 0 to 5 seconds
        area = l * b  # -5 to 15
        print(area, flush=True, end='')
        break


#-----------------------POS X -------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------



if __name__ == '__main__':
    main()

