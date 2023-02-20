def PositionMax(xs, x, ys, y, point_6, pt_1, pt_2, pt_3, pt_4, wc_1, wc_2, wc_3, wc_4):
    # ------------Check 1----------------
    # sink and door Wall 1
    XSPosPositions = []
    XSNotPositions = []
    XSContainsPositions = []

    room = InputPoints(point_8, point_10, point_6, point_7)
    # print("room;", room)

    # wall1
    door = InputPoints(
        ((point_list_opening_extrusion_area[0][0] - 0.2), (point_list_opening_extrusion_area[0][1] + 1.2)),
        ((point_list_opening_extrusion_area[0][0] + 1.3), (point_list_opening_extrusion_area[0][1] + 1.2)),
        ((point_list_opening_extrusion_area[0][0] + 1.3), (point_list_opening_extrusion_area[0][1])),
        ((point_list_opening_extrusion_area[0][0] - 0.2), point_list_opening_extrusion_area[0][1]))
    # print("door", door)
    while xs < point_6[0]:
        if xs != point_6[0]:
            xs = xs + 0.2
            ValuesXS.append(xs)
        elif xs == point_6[0]:
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

        if SinkCheck[-1] == True:
            # XSNotPositions.append()
            # print(xs, "position")
            XSPosPositions.append(xs)

        if SinkCheck[-1] == False:
            # print(xs, "position not")
            XSNotPositions.append(xs)

        if SinkCheck[-1] == None:
            # print(xs, "position contains")
            XSContainsPositions.append(xs)

    print("Pos sink", XSPosPositions)
    # print("NotPos sink", XSNotPositions)
    # print("ContPos sink", XSContainsPositions)
    # ------------------------------------------

    # ------------------------------------------

    # wc and door Wall 1
    XPosPositionsWc = []
    XNotPositionsWc = []
    WcOutDoor = []

    XContainsPositionsWc = []

    while x < point_6[0]:
        if x != point_6[0]:
            x = x + 0.2
            ValuesX.append(x)
        elif x == point_6[0]:
            break

    for valuesX in ValuesX:
        # print(values)
        x = valuesX

        wc1 = (wc_1[0] + x, wc_1[1] + y)  # (1.1 + x, 0.2 + y)
        wc2 = (wc_2[0] + x, wc_2[1] + y)  # (1.1 + x, -0.5 + y)
        wc3 = (wc_3[0] + x, wc_3[1] + y)  # (-1.1 + x, -0.5 + y)
        wc4 = (wc_4[0] + x, wc_4[1] + y)  # (-1.1 + x, 0.2 + y)
        wc = InputPoints(wc1, wc2, wc3, wc4)

        WcCheck = PositionChecking(door[11], wc[11],
                                   wc[1], wc[3], wc[5], wc[7],
                                   wc[9], door[1], door[3], door[5], door[7])

        if WcCheck[-1] == True:
            # print(x, "position")

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

        if WcCheck[-1] == False:
            # print(x, "position not")
            XNotPositionsWc.append(x)

        if WcCheck[-1] == None:
            # print(x, "position contains")
            XContainsPositionsWc.append(x)

    print("Pos Wc", XPosPositionsWc)
    # print("NotPos Wc", XNotPositions)
    # print("ContPos Wc", XContainsPositions)

    # ------------------------------------------
    # ------------Check 2----------------

    #  and door Wall 1
    XPosPositionsWcandSink = []
    XNotPositionsWcandSink = []
    XContainsPositionsWcandSink = []

    XPosPositionsRoomandWc = []
    XSPosPositionsRoomandSink = []

    XSPosPositionsWcandSink = []
    XSNotPositionsWcandSink = []
    XSContainsPositionsWcandSink = []

    both = []
    roomParams = []
    PositionFinalsSink = []
    PositionFinalsWc = []

    PositionFinalsRoomSink = []
    PositionFinalsRoomWc = []

    FinalXS = []
    XS = []
    FinalX = []
    X = []
    PositionsRoom = []
    Positions = []
    XValues = []
    XSValues = []
    wcpoint = []

    for posSink in XSPosPositions:
        for posWc in XPosPositionsWc:

            xs = posSink
            x = posWc
            # print(xs , "---NO" , x)

            pt1 = (pt_1[0] + xs, pt_1[1] + ys)  # (-0.45 + xs, 0.275 + ys)
            pt2 = (pt_2[0] + xs, pt_2[1] + ys)  # (0.45 + xs, 0.275 + ys)
            pt3 = (pt_3[0] + xs, pt_3[1] + ys)  # (0.45 + xs, -0.275 + ys)
            pt4 = (pt_4[0] + xs, pt_4[1] + ys)  # (-0.45 + xs, -0.275 + ys)
            sink = InputPoints(pt1, pt2, pt3, pt4)

            # ----------------------------

            wc1 = (wc_1[0] + x, wc_1[1] + y + 0.1)  # (1.1 + x, 0.2 + y)
            wc2 = (wc_2[0] + x, wc_2[1] + y + 0.1)  # (1.1 + x, -0.5 + y)
            wc3 = (wc_3[0] + x, wc_3[1] + y + 0.1)  # (-1.1 + x, -0.5 + y)
            wc4 = (wc_4[0] + x, wc_4[1] + y + 0.1)  # (-1.1 + x, 0.2 + y)
            wc = InputPoints(wc1, wc2, wc3, wc4)

            # ---------------------------------
            # liegen die Moveareas bei den möglichen Kombis im Raum?
            RoomSinkCheck = PositionChecking(room[11], sink[11],
                                             sink[1], sink[3], sink[5], sink[7],
                                             sink[9], room[1], room[3], room[5], room[7])
            # print(RoomSinkCheck)
            if RoomSinkCheck[-1] == None:
                # print(xs, "position contains")
                XSPosPositionsRoomandSink.append(xs)
                roomParams.append(XSPosPositionsRoomandSink)

            RoomWcCheck = PositionChecking(room[11], wc[11],
                                           wc[1], wc[3], wc[5], wc[7],
                                           wc[9], room[1], room[3], room[5], room[7])
            # print(RoomWcCheck)
            if RoomWcCheck[-1] == None:
                XPosPositionsRoomandWc.append(x)
                roomParams.append(XPosPositionsRoomandWc)
                # print("          ", XPosPositionsRoomandWc)

            SinkWCCheck = PositionChecking(wc[11], sink[11],
                                           sink[1], sink[3], sink[5], sink[7],
                                           sink[9], wc[1], wc[3], wc[5], wc[7])
            # print(SinkWCCheck)
            if SinkWCCheck[-1] == True:
                # print(xs, "position", x)
                XPosPositionsWcandSink.append(x)
                XSPosPositionsWcandSink.append(xs)
                both.append(XSPosPositionsWcandSink)
                both.append(XPosPositionsWcandSink)

            if SinkWCCheck[-1] == False:
                # print(x, "position not")
                XNotPositionsWcandSink.append(x)
                XSNotPositionsWcandSink.append(xs)

            if SinkWCCheck[-1] == None:
                # print(x, "position contains")
                XContainsPositionsWcandSink.append(x)
                XSContainsPositionsWcandSink.append(xs)

    # print("Pos sw", both)
    try:
        # mögliche Position für das Waschbecken, ohne Überlappung mit dem Klo, oder der Türe
        # --------remove identische Werte----------

        for xsValues in both[0]:
            for xsPositions in XSPosPositions:
                if xsValues == xsPositions:
                    PositionFinalsSink.append(xsPositions)
        for pos in PositionFinalsSink:
            if pos == pos:
                PositionFinalsSink.remove(pos)
        # print((PositionFinalsSink))

        for xValues in both[1]:
            for xPositions in XPosPositionsWc:
                if xValues == xPositions:
                    PositionFinalsWc.append(xPositions)
        for pos in PositionFinalsWc:
            if pos == pos:
                PositionFinalsWc.remove(pos)
        # print((PositionFinalsWc))

        # liegen die Positions mit Moveareas im  Raum?
        for xsValues in roomParams[0]:
            for xsPositions in XSPosPositionsRoomandSink:
                if xsValues == xsPositions:
                    PositionFinalsRoomSink.append(xsPositions)
        for pos in PositionFinalsRoomSink:
            if pos == pos:
                PositionFinalsRoomSink.remove(pos)
        # print(("PositionFinalsRoomSink", PositionFinalsRoomSink))

        for xValues in roomParams[1]:
            for xPositions in XPosPositionsRoomandWc:
                if xValues == xPositions:
                    PositionFinalsRoomWc.append(xPositions)
        for pos in PositionFinalsRoomWc:
            if pos == pos:
                PositionFinalsRoomWc.remove(pos)
        # print(("PositionFinalsRoomWc", PositionFinalsRoomWc))

        for pos1 in PositionFinalsSink and PositionFinalsRoomSink:
            FinalXS.append(pos1)

        for equals in FinalXS:
            if equals not in XS:
                XS.append(equals)
        # print("FInal XS: ", XS)

        for pos1 in PositionFinalsWc and PositionFinalsRoomWc:
            FinalX.append(pos1)

        for equals in FinalX:
            if equals not in X:
                X.append(equals)
        # print("FInal X: ", X)

        # alle möglichen Positionen  im Raum:
        PositionsRoom.append(XS)
        PositionsRoom.append(X)
        # print(PositionsRoom)

        # ------------Check 3----------------
        # bei den Positionen, gibt es intersections zwischen den Möbeln?
        for xx in X:
            for xxs in XS:
                x = xx
                xs = xxs

                pt1 = (pt_1[0] + xs, pt_1[1] + ys)  # (-0.45 + xs, 0.275 + ys)
                pt2 = (pt_2[0] + xs, pt_2[1] + ys)  # (0.45 + xs, 0.275 + ys)
                pt3 = (pt_3[0] + xs, pt_3[1] + ys)  # (0.45 + xs, -0.275 + ys)
                pt4 = (pt_4[0] + xs, pt_4[1] + ys)  # (-0.45 + xs, -0.275 + ys)
                sink = InputPoints(pt1, pt2, pt3, pt4)

                # ----------------------------

                wc1 = (wc_1[0] + x, wc_1[1] + y)  # (1.1 + x, 0.2 + y)
                wc2 = (wc_2[0] + x, wc_2[1] + y)  # (1.1 + x, -0.5 + y)
                wc3 = (wc_3[0] + x, wc_3[1] + y)  # (-1.1 + x, -0.5 + y)
                wc4 = (wc_4[0] + x, wc_4[1] + y)  # (-1.1 + x, 0.2 + y)
                wc = InputPoints(wc1, wc2, wc3, wc4)
                # ---------------------------------

                SinkWCCheckUpdate = PositionChecking(wc[11], sink[11],
                                                     sink[1], sink[3], sink[5], sink[7],
                                                     sink[9], wc[1], wc[3], wc[5], wc[7])

                print(SinkWCCheck)
                if SinkWCCheckUpdate[-1] == True:
                    # print(xs, "position", x)
                    XValues.append(x)
                    XSValues.append(xs)
                    Positions.append(XSValues)
                    Positions.append(XValues)
                    print(Positions)
        # ----------------POSSIBLE POSITIONS---------------------------
        coords = random.randint(0, len(Positions[0]))
        if len(Positions[0]) == 2:
            coords = 0
            coordsx = 1
            print("just 2")
        else:
            coordsx = coords + 1
            # coords = coordsx - 1
        # else:
        # coordsx = coords + 1
        print(coords)
        print(coordsx)

        xs = Positions[0][coords]
        x = Positions[1][coordsx]
        if xs == None or x == None:
            print("Error positioning not possible")
        else:
            print("sink position: ", xs)
            print("wc position: ", x)
            print("number of possible solutions: ", len(Positions[0]))
        return xs, x
    except:
        print("Die gewünschte Positionierung ist nicht möglich!")
        xs = 1.0
        x = 2.0


def PositionMaxYAxis(xs, x, ys, y, point_10, pt_1, pt_2, pt_3, pt_4, wc_1, wc_2, wc_3, wc_4):
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
        # print(values)
        ys = values

        pt1 = (pt_1[0] + xs, pt_1[1] + ys)  # (-0.45 + xs, 0.275 + ys)
        pt2 = (pt_2[0] + xs, pt_2[1] + ys)  # (0.45 + xs, 0.275 + ys)
        pt3 = (pt_3[0] + xs, pt_3[1] + ys)  # (0.45 + xs, -0.275 + ys)
        pt4 = (pt_4[0] + xs, pt_4[1] + ys)  # (-0.45 + xs, -0.275 + ys)
        sink = InputPoints(pt1, pt2, pt3, pt4)

        SinkCheck = PositionChecking(door[11], sink[11],
                                     sink[1], sink[3], sink[5], sink[7],
                                     sink[9], door[1], door[3], door[5], door[7])

        if SinkCheck[-1] == True:
            # XSNotPositions.append()
            # print(xs, "position")
            YSPosPositions.append(ys)

        if SinkCheck[-1] == False:
            # print(xs, "position not")
            YSNotPositions.append(ys)

        if SinkCheck[-1] == None:
            # print(xs, "position contains")
            YSContainsPositions.append(ys)

    print("Pos sink", YSPosPositions)
    # print("NotPos sink", XSNotPositions)
    # print("ContPos sink", XSContainsPositions)
    # ------------------------------------------

    # ------------------------------------------

    # wc and door Wall 1
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

        if WcCheck[-1] == True:
            # print(x, "position")
            YPosPositionsWc.append(y)

        if WcCheck[-1] == False:
            # print(x, "position not")
            YNotPositionsWc.append(y)

        if WcCheck[-1] == None:
            # print(x, "position contains")
            YContainsPositionsWc.append(y)

    print("Pos Wc", YPosPositionsWc)
    # print("NotPos Wc", XNotPositions)
    # print("ContPos Wc", XContainsPositions)

    # ------------------------------------------

    print("---------------------")

    #  and door Wall 1
    YPosPositionsWcandSink = []
    YNotPositionsWcandSink = []
    YContainsPositionsWcandSink = []

    YPosPositionsRoomandWc = []
    YSPosPositionsRoomandSink = []

    YSPosPositionsWcandSink = []
    YSNotPositionsWcandSink = []
    YSContainsPositionsWcandSink = []

    both = []
    roomParams = []
    PositionFinalsSink = []
    PositionFinalsWc = []

    PositionFinalsRoomSink = []
    PositionFinalsRoomWc = []

    FinalYS = []
    YS = []
    FinalY = []
    Y = []
    PositionsRoom = []
    Positions = []
    YValues = []
    YSValues = []

    for posSink in YSPosPositions:
        for posWc in YPosPositionsWc:

            ys = posSink
            y = posWc
            # print(xs , "---NO" , x)

            pt1 = (pt_1[0] + xs, pt_1[1] + ys)  # (-0.45 + xs, 0.275 + ys)
            pt2 = (pt_2[0] + xs, pt_2[1] + ys)  # (0.45 + xs, 0.275 + ys)
            pt3 = (pt_3[0] + xs, pt_3[1] + ys)  # (0.45 + xs, -0.275 + ys)
            pt4 = (pt_4[0] + xs, pt_4[1] + ys)  # (-0.45 + xs, -0.275 + ys)
            sink = InputPoints(pt1, pt2, pt3, pt4)

            # ----------------------------

            # wall2
            wc1 = (wc_1[0] + x, wc_1[1] + y)
            wc2 = (wc_2[0] + x, wc_2[1] + y)
            wc3 = (wc_3[0] + x, wc_3[1] + y)
            wc4 = (wc_4[0] + x, wc_4[1] + y)
            wc = InputPoints(wc1, wc2, wc3, wc4)
            # ---------------------------------

            SinkWCCheck = PositionChecking(wc[11], sink[11],
                                           sink[1], sink[3], sink[5], sink[7],
                                           sink[9], wc[1], wc[3], wc[5], wc[7])
            # print(SinkWCCheck)
            if SinkWCCheck[-1] == True:
                # print(xs, "position", x)
                YPosPositionsWcandSink.append(y)
                YSPosPositionsWcandSink.append(ys)
                both.append(YSPosPositionsWcandSink)
                both.append(YPosPositionsWcandSink)

            if SinkWCCheck[-1] == False:
                # print(x, "position not")
                YNotPositionsWcandSink.append(y)
                YSNotPositionsWcandSink.append(ys)

            if SinkWCCheck[-1] == None:
                # print(x, "position contains")
                YContainsPositionsWcandSink.append(y)
                YSContainsPositionsWcandSink.append(ys)

            # liegen die Moveareas bei den möglichen Kombis im Raum?
            RoomSinkCheck = PositionChecking(room[11], sink[11],
                                             sink[1], sink[3], sink[5], sink[7],
                                             sink[9], room[1], room[3], room[5], room[7])
            # print(RoomSinkCheck)
            if RoomSinkCheck[-1] == None:
                # print(xs, "position contains")
                YSPosPositionsRoomandSink.append(ys)
                roomParams.append(YSPosPositionsRoomandSink)

            RoomWcCheck = PositionChecking(wc[11], room[11],
                                           room[1], room[3], room[5], room[7],
                                           room[9], wc[1], wc[3], wc[5], wc[7])

            # print(RoomWcCheck)
            if RoomWcCheck[-1] == True:
                # print("    position contains", x)
                YPosPositionsRoomandWc.append(y)
                roomParams.append(YPosPositionsRoomandWc)

    # print("Pos sw", roomParams[1])
    try:
        # mögliche Position für das Waschbecken, ohne Überlappung mit dem Klo, oder der Türe
        # --------remove identische Werte----------
        for ysValues in both[0]:
            for ysPositions in YSPosPositions:
                if ysValues == ysPositions:
                    PositionFinalsSink.append(ysPositions)
        for pos in PositionFinalsSink:
            if pos == pos:
                PositionFinalsSink.remove(pos)
        # print((PositionFinalsSink))

        for yValues in both[1]:
            for yPositions in YPosPositionsWc:
                if yValues == yPositions:
                    PositionFinalsWc.append(yPositions)
        for pos in PositionFinalsWc:
            if pos == pos:
                PositionFinalsWc.remove(pos)
        # print((PositionFinalsWc))

        # liegen die Positions mit Moveareas im  Raum?
        for ysValues in roomParams[0]:
            for ysPositions in YSPosPositionsRoomandSink:
                if ysValues == ysPositions:
                    PositionFinalsRoomSink.append(ysPositions)
        for pos in PositionFinalsRoomSink:
            if pos == pos:
                PositionFinalsRoomSink.remove(pos)
        ##print(("PositionFinalsRoomSink", PositionFinalsRoomSink))

        for yValues in roomParams[1]:
            for yPositions in YPosPositionsRoomandWc:
                if yValues == yPositions:
                    PositionFinalsRoomWc.append(yPositions)
        for pos in PositionFinalsRoomWc:
            if pos == pos:
                PositionFinalsRoomWc.remove(pos)
        # print(("PositionFinalsRoomWc", PositionFinalsRoomWc))

        for pos1 in PositionFinalsSink and PositionFinalsRoomSink:
            FinalYS.append(pos1)

        for equals in FinalYS:
            if equals not in YS:
                YS.append(equals)
        # print("FInal XS: ", XS)

        for pos1 in PositionFinalsWc and PositionFinalsRoomWc:
            FinalY.append(pos1)

        for equals in FinalY:
            if equals not in Y:
                Y.append(equals)
        # print("FInal X: ", X)

        # alle möglichen Positionen  im Raum:
        PositionsRoom.append(YS)
        PositionsRoom.append(Y)
        # print(PositionsRoom)

        # bei den Positionen, gibt es intersections zwischen den Möbeln?
        for yy in Y:
            for yys in YS:
                y = yy
                ys = yys

                pt1 = (pt_1[0] + xs, pt_1[1] + ys)  # (-0.45 + xs, 0.275 + ys)
                pt2 = (pt_2[0] + xs, pt_2[1] + ys)  # (0.45 + xs, 0.275 + ys)
                pt3 = (pt_3[0] + xs, pt_3[1] + ys)  # (0.45 + xs, -0.275 + ys)
                pt4 = (pt_4[0] + xs, pt_4[1] + ys)  # (-0.45 + xs, -0.275 + ys)
                sink = InputPoints(pt1, pt2, pt3, pt4)

                # ----------------------------
                # wall2
                wc1 = (wc_1[0] + x, wc_1[1] + y)
                wc2 = (wc_2[0] + x, wc_2[1] + y)
                wc3 = (wc_3[0] + x, wc_3[1] + y)
                wc4 = (wc_4[0] + x, wc_4[1] + y)
                wc = InputPoints(wc1, wc2, wc3, wc4)
                # ---------------------------------

                SinkWCCheckUpdate = PositionChecking(wc[11], sink[11],
                                                     sink[1], sink[3], sink[5], sink[7],
                                                     sink[9], wc[1], wc[3], wc[5], wc[7])

                print(SinkWCCheck)
                if SinkWCCheckUpdate[-1] == True:
                    # print(xs, "position", x)
                    YValues.append(y)
                    YSValues.append(ys)
                    Positions.append(YSValues)
                    Positions.append(YValues)

        # ----------------POSSIBLE POSITIONS---------------------------
        print(Positions)
        coords = random.randint(0, len(Positions[0]))
        print(coords)
        coordsy = coords + 1
        print(coordsy)

        ys = Positions[0][coords]
        y = Positions[1][coordsy]
        if ys == None or y == None:
            print("Error positioning not possible")
        else:
            print("sink position: ", ys)
            print("wc position: ", y)
            print("number of possible solutions: ", len(Positions[0]))
        return ys, y
    except:
        print("Die gewünschte Positionierung ist nicht möglich!")
        ys = 1.0
        y = 2.0

# --------------------------------------------------------------------------------
# --------------------------Helper Functions Positioning--------------------------
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
            if moveandsink[-1] == False or moveandsink[-1] == None:
                #if ym in PosMoveArea:
                PosMoveAreaDel.append(ym)


        print("PosMoveAreaDel", PosMoveAreaDel)
        #print("PosMoveArea", PosMoveArea)
        for val in PosMoveAreaDel:
            for values in PosMoveArea:
                if values == val:
                    PosMoveArea.remove(values)
        print("PosMoveArea2", PosMoveArea)
        print("ym", ym)
        for value in PosMoveAreaDel:
            if ym == value:
                print("FAlse")
                return False


        if len(PosMoveArea) == 0:
            return False
        else:
            return PosMoveArea    def MoveareaWCY(x , y, xm, ym, xs, ys, sink_point_out_1, sink_point_out_2, sink_point_out_3, sink_point_out_4):
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
            if moveandsink[-1] == False or moveandsink[-1] == None:
                #if ym in PosMoveArea:
                PosMoveAreaDel.append(ym)


        print("PosMoveAreaDel", PosMoveAreaDel)
        #print("PosMoveArea", PosMoveArea)
        for val in PosMoveAreaDel:
            for values in PosMoveArea:
                if values == val:
                    PosMoveArea.remove(values)
        print("PosMoveArea2", PosMoveArea)
        print("ym", ym)
        for value in PosMoveAreaDel:
            if ym == value:
                print("FAlse")
                return False


        if len(PosMoveArea) == 0:
            return False
        else:
            return PosMoveArea
