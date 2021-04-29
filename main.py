import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import copy
import time
from multiprocessing import Process
import threading

StartingColor = 60
EndingColor = 65
wall = 1
visitState = 90
ShowColor = 35
GoingToVisitColor = 80
nullStateColor = 100
speed = .01
LevelLimit = 20

cost1 = 0
cost2 = 0
cost3 = 0
foundCount = 0
data = []


def animateGBFS(i):
    drawplt()


def drawplt():
    try:
        cols, rows, EndingRow, EndingCol, StartingRow, StartingCol, Data = 0, 0, 0, 0, 0, 0, 0
        cols, rows, EndingRow, EndingCol, StartingRow, StartingCol, Data = ReadFromFile("AHuristic.txt", cols, rows,
                                                                                        StartingRow, StartingCol,
                                                                                        EndingRow, EndingCol, Data)
        m = copy.copy(Data)
        ax4.clear()
        ax4.set_xticks(np.arange(0, rows - 1, 1))
        ax4.set_yticks(np.arange(0, cols - 1, 1))
        ax4.set_xticklabels(np.arange(1, rows, 1))
        ax4.set_yticklabels(np.arange(1, cols, 1))
        ax4.set_xticks(np.arange(-.5, rows - 1, 1), minor=True)
        ax4.set_yticks(np.arange(-.5, cols - 1, 1), minor=True)
        ax4.set_title('Huristic Matrix For A*')
        ax4.matshow(m, cmap='jet', interpolation='nearest', aspect='equal')
        ax4.grid(which='minor', color='w', linestyle='-', linewidth=2)

    except:
        pass
    try:
        cols, rows, EndingRow, EndingCol, StartingRow, StartingCol, Data = 0, 0, 0, 0, 0, 0, 0
        cols, rows, EndingRow, EndingCol, StartingRow, StartingCol, Data = ReadFromFile("AG.txt", cols, rows,
                                                                                        StartingRow, StartingCol,
                                                                                        EndingRow, EndingCol, Data)
        m = copy.copy(Data)
        ax5.clear()
        ax5.set_xticks(np.arange(0, rows - 1, 1))
        ax5.set_yticks(np.arange(0, cols - 1, 1))
        ax5.set_xticklabels(np.arange(1, rows, 1))
        ax5.set_yticklabels(np.arange(1, cols, 1))
        ax5.set_xticks(np.arange(-.5, rows - 1, 1), minor=True)
        ax5.set_yticks(np.arange(-.5, cols - 1, 1), minor=True)
        ax5.set_title('G\'s Matrix For A*')
        ax5.matshow(m, cmap='jet', interpolation='nearest', aspect='equal')
        ax5.grid(which='minor', color='w', linestyle='-', linewidth=2)

    except:
        pass
    try:
        cols, rows, EndingRow, EndingCol, StartingRow, StartingCol, Data = 0, 0, 0, 0, 0, 0, 0
        cols, rows, EndingRow, EndingCol, StartingRow, StartingCol, Data = ReadFromFile("IDAHuristic.txt", cols, rows,
                                                                                        StartingRow, StartingCol,
                                                                                        EndingRow, EndingCol, Data)
        m = copy.copy(Data)
        ax6.clear()
        ax6.set_xticks(np.arange(0, rows - 1, 1))
        ax6.set_yticks(np.arange(0, cols - 1, 1))
        ax6.set_xticklabels(np.arange(1, rows, 1))
        ax6.set_yticklabels(np.arange(1, cols, 1))
        ax6.set_xticks(np.arange(-.5, rows - 1, 1), minor=True)
        ax6.set_yticks(np.arange(-.5, cols - 1, 1), minor=True)
        ax6.set_title('Huristic Matrix For IDA')
        ax6.matshow(m, cmap='jet', interpolation='nearest', aspect='equal')
        ax6.grid(which='minor', color='w', linestyle='-', linewidth=2)

    except:
        pass
    try:
        cols, rows, EndingRow, EndingCol, StartingRow, StartingCol, Data = 0, 0, 0, 0, 0, 0, 0
        cols, rows, EndingRow, EndingCol, StartingRow, StartingCol, Data = ReadFromFile("IDAG.txt", cols, rows,
                                                                                        StartingRow, StartingCol,
                                                                                        EndingRow, EndingCol, Data)
        m = copy.copy(Data)
        ax7.clear()
        ax7.set_xticks(np.arange(0, rows - 1, 1))
        ax7.set_yticks(np.arange(0, cols - 1, 1))
        ax7.set_xticklabels(np.arange(1, rows, 1))
        ax7.set_yticklabels(np.arange(1, cols, 1))
        ax7.set_xticks(np.arange(-.5, rows - 1, 1), minor=True)
        ax7.set_yticks(np.arange(-.5, cols - 1, 1), minor=True)
        ax7.set_title('G\'s Matrix For IDA')
        ax7.matshow(m, cmap='jet', interpolation='nearest', aspect='equal')
        ax7.grid(which='minor', color='w', linestyle='-', linewidth=2)

    except:
        pass

    try:
        cols, rows, EndingRow, EndingCol, StartingRow, StartingCol, Data = 0, 0, 0, 0, 0, 0, 0
        cols, rows, EndingRow, EndingCol, StartingRow, StartingCol, Data = ReadFromFile("GBFS.txt", cols, rows,
                                                                                        StartingRow, StartingCol,
                                                                                        EndingRow, EndingCol, Data)
        m = copy.copy(Data)
        ax1.clear()
        ax1.set_xticks(np.arange(0, rows - 1, 1))
        ax1.set_yticks(np.arange(0, cols - 1, 1))
        ax1.set_xticklabels(np.arange(1, rows, 1))
        ax1.set_yticklabels(np.arange(1, cols, 1))
        ax1.set_xticks(np.arange(-.5, rows - 1, 1), minor=True)
        ax1.set_yticks(np.arange(-.5, cols - 1, 1), minor=True)
        ax1.set_title('Greedy Best First Search')
        ax1.matshow(m, cmap='cubehelix', interpolation='nearest', aspect='equal')
        ax1.grid(which='minor', color='w', linestyle='-', linewidth=2)
    except:
        pass
    try:
        cols, rows, EndingRow, EndingCol, StartingRow, StartingCol, Data = 0, 0, 0, 0, 0, 0, 0
        cols, rows, EndingRow, EndingCol, StartingRow, StartingCol, Data = ReadFromFile("ASearch.txt", cols, rows,
                                                                                        StartingRow, StartingCol,
                                                                                        EndingRow, EndingCol, Data)
        m = copy.copy(Data)
        ax2.clear()
        ax2.set_xticks(np.arange(0, rows - 1, 1))
        ax2.set_yticks(np.arange(0, cols - 1, 1))
        ax2.set_xticklabels(np.arange(1, rows, 1))
        ax2.set_yticklabels(np.arange(1, cols, 1))
        ax2.set_xticks(np.arange(-.5, rows - 1, 1), minor=True)
        ax2.set_yticks(np.arange(-.5, cols - 1, 1), minor=True)
        ax2.set_title('A* Search')
        ax2.matshow(m, cmap='cubehelix', interpolation='nearest', aspect='equal')
        ax2.grid(which='minor', color='w', linestyle='-', linewidth=2)
    except:
        pass
    try:
        cols, rows, EndingRow, EndingCol, StartingRow, StartingCol, Data = 0, 0, 0, 0, 0, 0, 0
        cols, rows, EndingRow, EndingCol, StartingRow, StartingCol, Data = ReadFromFile("IDASearch.txt", cols, rows,
                                                                                        StartingRow, StartingCol,
                                                                                        EndingRow, EndingCol, Data)
        m = copy.copy(Data)
        ax3.clear()
        ax3.set_xticks(np.arange(0, rows - 1, 1))
        ax3.set_yticks(np.arange(0, cols - 1, 1))
        ax3.set_xticklabels(np.arange(1, rows, 1))
        ax3.set_yticklabels(np.arange(1, cols, 1))
        ax3.set_xticks(np.arange(-.5, rows - 1, 1), minor=True)
        ax3.set_yticks(np.arange(-.5, cols - 1, 1), minor=True)
        ax3.set_title('IDA* Search')
        ax3.matshow(m, cmap='cubehelix', interpolation='nearest', aspect='equal')
        ax3.grid(which='minor', color='w', linestyle='-', linewidth=2)
    except:
        pass


def backTrackGBFS(Data, queue, StartingRow, StartingCol, EndingRow, EndingCol, rows, cols, visited):
    i = EndingRow
    j = EndingCol
    global cost1
    while True:
        try:
            if i == StartingRow and j == StartingCol:

                global foundCount
                foundCount = foundCount + 1
                break
            elif i != EndingRow or j != EndingCol:
                Data[i][j] = ShowColor
                WriteIntoFile("GBFS.txt", cols, rows, StartingRow, StartingCol, EndingRow, EndingCol, Data)

        except:
            print("ERR1")
        try:
            Got = False
            if i + 1 < rows and [i + 1, j] in visited:
                if Data[i + 1][j] != wall:
                    i = i + 1
                    cost1 += 1
                    Got = True
            if i + 1 < cols and j - 1 >= 0 and not Got and [i + 1, j - 1] in visited:
                if Data[i + 1][j - 1] != wall:
                    i = i + 1
                    j = j - 1
                    cost1 += 2
                    Got = True
            if j - 1 >= 0 and not Got and [i, j - 1] in visited:
                if Data[i][j - 1] != wall:
                    j = j - 1
                    cost1 += 3
                    Got = True
            if not Got:
                popped_Element = queue.pop()
                if popped_Element[0] > i and popped_Element[1] < j:
                    cost1 += 2
                elif popped_Element[0] > i:
                    cost1 += 3
                elif popped_Element[1] < j:
                    cost1 += 1

                i = popped_Element[0]
                j = popped_Element[1]

        except:
            print("Err2")
        time.sleep(speed)


def GreedyBestFirstSearch(cols, rows, StartingRow, StartingCol, EndingRow, EndingCol, Data, speed):
    visited = []
    queue = []
    global foundCount, cost1
    i = StartingRow  # 12
    j = StartingCol  # 0
    queue.append([i, j])
    visited.append([i, j])
    while True:
        try:
            if i == EndingRow and j == EndingCol:
                print("Found1!!")

                backTrackGBFS(Data, queue, StartingRow, StartingCol, EndingRow, EndingCol, rows, cols, visited)
                break
            if isinstance(Data[i][j], int) and not [i, j] == [StartingRow, StartingCol]:

                if Data[i][j] == wall:
                    if i != 0:
                        i -= 1
                        j = StartingCol
                    else:
                        break
                if [i, j] not in visited:
                    queue.append([i, j])
                    visited.append([i, j])

                    Data[i][j] = visitState
                    if i - 1 >= 0 and [i - 1, j] not in visited and [i - 1, j] != [EndingRow, EndingCol]:
                        if Data[i - 1][j] != wall:
                            Data[i - 1][j] = GoingToVisitColor
                    if i - 1 >= 0 and j + 1 < cols and [i - 1, j + 1] not in visited and [i - 1, j + 1] != [EndingRow,
                                                                                                            EndingCol]:
                        if Data[i - 1][j + 1] != wall:
                            Data[i - 1][j + 1] = GoingToVisitColor
                    if j + 1 < cols and [i, j + 1] not in visited and [i, j + 1] != [EndingRow, EndingCol]:
                        if Data[i][j + 1] != wall:
                            Data[i][j + 1] = GoingToVisitColor
                    WriteIntoFile("GBFS.txt", cols, rows, StartingRow, StartingCol, EndingRow, EndingCol, Data)
        except:
            print("ERR1")
        try:
            Got = False
            if i - 1 >= 0 and [i - 1, j] not in visited:
                if Data[i - 1][j] != wall:
                    i = i - 1
                    Got = True
            if i - 1 >= 0 and j + 1 < cols and not Got and [i - 1, j + 1] not in visited:
                if Data[i - 1][j + 1] != wall:
                    i = i - 1
                    j = j + 1
                    Got = True
            if j + 1 < cols and not Got and [i, j + 1] not in visited:
                if Data[i][j + 1] != wall:
                    j = j + 1
                    Got = True
            if not Got:
                if not queue:
                    print("GBFS Path Not Found!")
                    cost1 = "Path Not Found!"
                    foundCount += 1
                    return
                popped_Element = queue.pop()
                i = popped_Element[0]
                j = popped_Element[1]
        except:
            print("Err2")
        time.sleep(speed)


def calculateHuristic(FileName, Data, StartingRow, StartingCol, EndingRow, EndingCol, rows, cols):
    for i in range(len(Data)):
        for j in range(len(Data[i])):
            if Data[i][j] == wall:
                Data[i][j] = 40
            else:
                Data[i][j] = abs((EndingRow - i)) + abs((EndingCol - j))

    WriteIntoFile(FileName, cols, rows, StartingRow, StartingCol, EndingRow, EndingCol, Data)
    return Data


def calculateG(FileName, Data, StartingRow, StartingCol, EndingRow, EndingCol, rows, cols):
    for i in range(len(Data)):
        for j in range(len(Data[i])):
            if Data[i][j] == wall:
                Data[i][j] = 40
            else:
                Data[i][j] = abs((StartingRow - i)) + abs((StartingCol - j))

    WriteIntoFile(FileName, cols, rows, StartingRow, StartingCol, EndingRow, EndingCol, Data)
    return Data


def CalculateMyHuristic(Huristic, Gs, CurrentX, CurrentY):
    return Huristic[CurrentX][CurrentY] + Gs[CurrentX][CurrentY]


def IsMyHuristicOkay(Huristic, Gs, CurrentX, CurrentY, queue):
    while queue:
        poppedElement = queue.pop()
        if CalculateMyHuristic(Huristic, Gs, poppedElement[0], poppedElement[1]) < CalculateMyHuristic(Huristic, Gs,
                                                                                                       CurrentX,
                                                                                                       CurrentY):
            return False
    return True


def ASearchBackTrack(visited, queue, cols, rows, StartingRow, StartingCol, EndingRow, EndingCol, Data, speed, huristic,
                     Gs):
    i = EndingRow  # 12
    j = EndingCol  # 0
    global cost2
    while True:
        try:
            if i == StartingRow and j == StartingCol:
                global foundCount
                foundCount = foundCount + 1
                break
            elif i != EndingRow or j != EndingCol:
                Data[i][j] = ShowColor
                WriteIntoFile("ASearch.txt", cols, rows, StartingRow, StartingCol, EndingRow, EndingCol, Data)
        except:
            print("ERR1")
        try:
            Got = False

            if i + 1 < rows and [i + 1, j] in visited:
                if Data[i + 1][j] != wall:
                    if (CalculateMyHuristic(huristic, Gs, (i + 1), j) <= CalculateMyHuristic(
                            huristic, Gs, (i + 1), (j - 1)) or Data[i + 1][j - 1] == wall) and (CalculateMyHuristic(
                        huristic, Gs, (i + 1), j) <= CalculateMyHuristic(
                        huristic, Gs, i, (j - 1)) or Data[i][j - 1] == wall):
                        i = i + 1
                        cost2 += 1
                        Got = True
            if i + 1 < rows and j - 1 >= 0 and not Got and [i + 1, j - 1] in visited:
                if Data[i + 1][j - 1] != wall:
                    if (CalculateMyHuristic(
                            huristic, Gs, (i + 1), j - 1) <= CalculateMyHuristic(
                        huristic, Gs, i, (j - 1)) or Data[i][j - 1] == wall):
                        i = i + 1
                        j = j - 1
                        cost2 += 2
                        Got = True
            if j - 1 >= 0 and not Got and [i, j - 1] in visited:
                if Data[i][j - 1] != wall:
                    cost2 += 3
                    j = j - 1
                    Got = True
            if not Got:
                popped_Element = queue.pop()
                i = popped_Element[0]
                j = popped_Element[1]
        except:
            print("Send Help")
        time.sleep(speed)


def ASearch(cols, rows, StartingRow, StartingCol, EndingRow, EndingCol, Data, speed):
    visited = []
    queue = []
    global cost2, foundCount
    innerData = copy.deepcopy(Data)


    i = StartingRow  # 12
    j = StartingCol  # 0
    queue.append([i, j])
    visited.append([i, j])

    while True:
        huristic = copy.deepcopy(Data)
        Gs = copy.deepcopy(Data)
        huristic = calculateHuristic("AHuristic.txt", huristic, i, j, EndingRow, EndingCol, rows, cols)
        Gs = calculateG("AG.txt", Gs, StartingRow, i, j, EndingCol, rows, cols)
        try:

            if i == EndingRow and j == EndingCol:
                print("Found2!!")
                ASearchBackTrack(visited, queue, cols, rows, StartingRow, StartingCol, EndingRow, EndingCol, innerData,
                                 speed, huristic, Gs)
                break
            if isinstance(innerData[i][j], int) and not [i, j] == [StartingRow, StartingCol]:

                if [i, j] not in visited:
                    queue.append([i, j])
                    visited.append([i, j])

                    innerData[i][j] = visitState

                    if i - 1 >= 0 and [i - 1, j] not in visited and [i - 1, j] != [EndingRow, EndingCol]:
                        if innerData[i - 1][j] != wall:
                            queue1 = copy.deepcopy(queue)
                            if (CalculateMyHuristic(huristic, Gs, (i - 1), j) <= CalculateMyHuristic(
                                    huristic, Gs, (i - 1), (j + 1)) or innerData[i - 1][j + 1] == wall) and (
                                    CalculateMyHuristic(
                                        huristic, Gs, (i - 1), j) <= CalculateMyHuristic(
                                huristic, Gs, i, (j + 1)) or innerData[i][j + 1] == wall) and IsMyHuristicOkay(huristic, Gs,
                                                                                                               (i - 1), j,
                                                                                                               queue1):


                                innerData[i - 1][j] = GoingToVisitColor
                    if i - 1 >= 0 and j + 1 < cols and [i - 1, j + 1] not in visited and [i - 1, j + 1] != [EndingRow,
                                                                                                            EndingCol]:
                        if innerData[i - 1][j + 1] != wall:
                            queue1 = copy.deepcopy(queue)

                            if CalculateMyHuristic(huristic, Gs, (i - 1), j + 1) <= CalculateMyHuristic(
                                    huristic, Gs, i, (j + 1)) or innerData[i][j + 1] == wall and IsMyHuristicOkay(huristic,
                                                                                                                  Gs,
                                                                                                                  (i - 1),
                                                                                                                  (j + 1),
                                                                                                                  queue1):
                                innerData[i - 1][j + 1] = GoingToVisitColor
                    if j + 1 < cols and [i, j + 1] not in visited and [i, j + 1] != [EndingRow, EndingCol]:
                        if innerData[i][j + 1] != wall:
                            queue1 = copy.deepcopy(queue)

                            if IsMyHuristicOkay(huristic, Gs, i, (j + 1), queue1):
                                innerData[i][j + 1] = GoingToVisitColor

                    WriteIntoFile("ASearch.txt", cols, rows, StartingRow, StartingCol, EndingRow, EndingCol, innerData)
        except:
            pass
        try:
            Got = False
            if i - 1 >= 0 and [i - 1, j] not in visited:
                if innerData[i - 1][j] != wall:
                    queue1 = copy.deepcopy(queue)
                    if (CalculateMyHuristic(huristic, Gs, (i - 1), j) <= CalculateMyHuristic(
                            huristic, Gs, (i - 1), (j + 1)) or innerData[i - 1][j + 1] == wall) and (CalculateMyHuristic(
                        huristic, Gs, (i - 1), j) <= CalculateMyHuristic(
                        huristic, Gs, i, (j + 1)) or innerData[i][j + 1] == wall) and IsMyHuristicOkay(huristic, Gs, (i - 1),
                                                                                                       j, queue1):
                        i = i - 1
                        Got = True
            if i - 1 >= 0 and j + 1 < cols and not Got and [i - 1, j + 1] not in visited:
                if innerData[i - 1][j + 1] != wall:
                    queue1 = copy.deepcopy(queue)
                    if (CalculateMyHuristic(
                            huristic, Gs, (i - 1), j + 1) <= CalculateMyHuristic(
                        huristic, Gs, i, (j + 1)) or innerData[i][j + 1] == wall) and IsMyHuristicOkay(huristic, Gs, (i - 1),
                                                                                                       (j + 1), queue1):
                        i = i - 1
                        j = j + 1
                        Got = True
            if j + 1 < cols and not Got and [i, j + 1] not in visited:
                queue1 = copy.deepcopy(queue)
                if innerData[i][j + 1] != wall:
                    if IsMyHuristicOkay(huristic, Gs, i, (j + 1), queue1):
                        j = j + 1
                        Got = True
            if not Got:
                if not queue:
                    print("A* Path Not Found!")
                    cost2 = "Path Not Found!"
                    foundCount += 1
                    return
                popped_Element = queue.pop()
                i = popped_Element[0]
                j = popped_Element[1]
        except:
            pass
        Gs = calculateG("AG.txt", Gs, i, j, EndingRow, EndingCol, rows, cols)
        time.sleep(speed)


def IDATrackBack(visited, queue, cols, rows, StartingRow, StartingCol, EndingRow, EndingCol, Data,
                 speed, huristic, Gs):
    i = EndingRow  # 12
    j = EndingCol  # 0
    global cost3
    while True:
        try:
            if i == StartingRow and j == StartingCol:
                global foundCount
                foundCount = foundCount + 1
                break
            elif i != EndingRow or j != EndingCol:
                Data[i][j] = ShowColor
                WriteIntoFile("IDASearch.txt", cols, rows, StartingRow, StartingCol, EndingRow, EndingCol, Data)
        except:
            pass
        try:
            Got = False

            if i + 1 < rows and [i + 1, j] in visited:
                if Data[i + 1][j] != wall:
                    if (CalculateMyHuristic(huristic, Gs, (i + 1), j) <= CalculateMyHuristic(
                            huristic, Gs, (i + 1), (j - 1)) or Data[i + 1][j - 1] == wall) and (CalculateMyHuristic(
                        huristic, Gs, (i + 1), j) <= CalculateMyHuristic(
                        huristic, Gs, i, (j - 1)) or Data[i][j - 1] == wall):
                        i = i + 1
                        cost3 += 1
                        Got = True
            if i + 1 < rows and j - 1 >= 0 and not Got and [i + 1, j - 1] in visited:
                if Data[i + 1][j - 1] != wall:
                    if (CalculateMyHuristic(
                            huristic, Gs, (i + 1), j - 1) <= CalculateMyHuristic(
                        huristic, Gs, i, (j - 1)) or Data[i][j - 1] == wall):
                        i = i + 1
                        j = j - 1
                        cost3 += 2
                        Got = True
            if j - 1 >= 0 and not Got and [i, j - 1] in visited:
                if Data[i][j - 1] != wall:
                    j = j - 1
                    cost3 += 3
                    Got = True
            if not Got:
                popped_Element = queue.pop()
                i = popped_Element[0]
                j = popped_Element[1]
        except:
            pass
        time.sleep(speed)


def IDASeach(cols, rows, StartingRow, StartingCol, EndingRow, EndingCol, Data, speed):
    global foundCount, cost3
    visited = []
    queue = []

    i = StartingRow  # 12
    j = StartingCol  # 0
    queue.append([i, j])
    visited.append([i, j])
    Level = 0
    while True:
        visited = []
        queue = []

        innerData = copy.deepcopy(Data)
        for i in range(len(Data)):
            for j in range(len(Data[i])):
                if Data[i][j] == 1:
                    Data[i][j] = wall
                elif Data[i][j] == 0:
                    Data[i][j] = nullStateColor
        Data[StartingRow][StartingCol] = StartingColor
        Data[EndingRow][EndingCol] = EndingColor

        i = StartingRow  # 12
        j = StartingCol  # 0
        queue.append([i, j])
        visited.append([i, j])
        print(f"IDA* Level: {Level}")
        while True:
            huristic1 = copy.deepcopy(Data)
            Gs1 = copy.deepcopy(Data)
            huristic1 = calculateHuristic("IDAHuristic.txt", huristic1, i, j, EndingRow, EndingCol, rows, cols)
            Gs1 = calculateG("IDAG.txt", Gs1, StartingRow, i, j, EndingCol, rows, cols)
            try:

                if i == EndingRow and j == EndingCol:
                    print("Found3!!")

                    IDATrackBack(visited, queue, cols, rows, StartingRow, StartingCol, EndingRow, EndingCol, innerData,
                                 speed, huristic1, Gs1)
                    return

                if isinstance(innerData[i][j], int) and not [i, j] == [StartingRow, StartingCol]:

                    if [i, j] not in visited:
                        queue.append([i, j])
                        visited.append([i, j])
                        innerData[i][j] = visitState

                        if i - 1 >= 0 and [i - 1, j] not in visited and [i - 1, j] != [EndingRow, EndingCol]:
                            if innerData[i - 1][j] != wall:
                                if Gs1[i - 1][j] <= Level:
                                    queue1 = copy.deepcopy(queue)
                                    if (CalculateMyHuristic(huristic1, Gs1, (i - 1), j) <= CalculateMyHuristic(
                                            huristic1, Gs1, (i - 1), (j + 1)) or innerData[i - 1][j + 1] == wall) and (
                                            CalculateMyHuristic(
                                                huristic1, Gs1, (i - 1), j) <= CalculateMyHuristic(
                                        huristic1, Gs1, i, (j + 1)) or innerData[i][j + 1] == wall) and IsMyHuristicOkay(
                                        huristic1, Gs1, (i - 1), j, queue1):
                                        innerData[i - 1][j] = GoingToVisitColor
                        if i - 1 >= 0 and j + 1 < cols and [i - 1, j + 1] not in visited and [i - 1, j + 1] != [
                            EndingRow,
                            EndingCol]:
                            if innerData[i - 1][j + 1] != wall:
                                if Gs1[i - 1][j + 1] <= Level + 1:
                                    queue1 = copy.deepcopy(queue)
                                    if CalculateMyHuristic(huristic1, Gs1, (i - 1), j + 1) <= CalculateMyHuristic(
                                            huristic1, Gs1, i, (j + 1)) or innerData[i][
                                        j + 1] == wall and IsMyHuristicOkay(
                                        huristic1,
                                        Gs1,
                                        (i - 1),
                                        (j + 1),
                                        queue1):
                                        innerData[i - 1][j + 1] = GoingToVisitColor
                        if j + 1 < cols and [i, j + 1] not in visited and [i, j + 1] != [EndingRow, EndingCol]:
                            if innerData[i][j + 1] != wall:
                                if Gs1[i][j + 1] <= Level:
                                    queue1 = copy.deepcopy(queue)
                                    if IsMyHuristicOkay(huristic1, Gs1, i, (j + 1), queue1):
                                        innerData[i][j + 1] = GoingToVisitColor

                        WriteIntoFile("IDASearch.txt", cols, rows, StartingRow, StartingCol, EndingRow, EndingCol,
                                      innerData)


            except:
                pass
            try:
                Got = False

                if i - 1 >= 0 and [i - 1, j] not in visited:
                    if Data[i - 1][j] != wall:
                        if Gs1[i - 1][j] <= Level:
                            queue1 = copy.deepcopy(queue)
                            if (CalculateMyHuristic(huristic1, Gs1, (i - 1), j) <= CalculateMyHuristic(
                                    huristic1, Gs1, (i - 1), (j + 1)) or Data[i - 1][j + 1] == wall) and (
                                    CalculateMyHuristic(
                                        huristic1, Gs1, (i - 1), j) <= CalculateMyHuristic(
                                huristic1, Gs1, i, (j + 1)) or Data[i][j + 1] == wall) and IsMyHuristicOkay(huristic1, Gs1,
                                                                                                            (i - 1),
                                                                                                            j, queue1):
                                i = i - 1
                                Got = True
                if i - 1 >= 0 and j + 1 < cols and not Got and [i - 1, j + 1] not in visited:
                    if Data[i - 1][j + 1] != wall:
                        if Gs1[i - 1][j + 1] <= Level + 1:
                            queue1 = copy.deepcopy(queue)
                            if (CalculateMyHuristic(
                                    huristic1, Gs1, (i - 1), j + 1) <= CalculateMyHuristic(
                                huristic1, Gs1, i, (j + 1)) or Data[i][j + 1] == wall) and IsMyHuristicOkay(huristic1, Gs1,
                                                                                                            (i - 1),
                                                                                                            (j + 1),
                                                                                                            queue1):
                                i = i - 1
                                j = j + 1
                                Got = True
                if j + 1 < cols and not Got and [i, j + 1] not in visited:
                    if Gs1[i][j + 1] <= Level:
                        queue1 = copy.deepcopy(queue)
                        if Data[i][j + 1] != wall:
                            if IsMyHuristicOkay(huristic1, Gs1, i, (j + 1), queue1):
                                j = j + 1
                                Got = True
                if not Got:
                    if not queue:
                        if Level <= LevelLimit:
                            Level += 1
                            break
                        else:
                            print("IDA Path Not Found!")
                            cost3 = 'Path Not Found!'
                            foundCount += 1
                            return
                    popped_Element = queue.pop()
                    i = popped_Element[0]
                    j = popped_Element[1]
            except:
                pass

            time.sleep(speed)


def ReadFromFile(FileName, cols, rows, StartingRow, StartingCol, EndingRow, EndingCol, Data):
    file_handle = open(FileName, 'r')
    lines_list = file_handle.readlines()
    try:
        rows, cols = (int(val) for val in lines_list[0].split())
        StartingRow, StartingCol = (int(val) for val in lines_list[1].split())
        EndingRow, EndingCol = (int(val) for val in lines_list[2].split())
        Data = [[int(val) for val in line.split()] for line in lines_list[3:]]

        return cols, rows, EndingRow, EndingCol, StartingRow, StartingCol, Data
    except:
        pass


def WriteIntoFile(FileName, cols, rows, StartingRow, StartingCol, EndingRow, EndingCol, Data):
    f = open(FileName, "w")
    f.write(str(cols))
    f.write(' ')
    f.write(str(rows))
    f.write('\n')
    f.write(str(StartingRow))
    f.write(' ')
    f.write(str(StartingCol))
    f.write('\n')
    f.write(str(EndingRow))
    f.write(' ')
    f.write(str(EndingCol))
    f.write('\n')
    for i in range(len(Data)):
        for j in range(len(Data[i])):
            f.write(str(Data[i][j]))
            f.write(' ')
        f.write('\n')


fig = plt.figure(figsize=(17, 12))
ax1 = fig.add_subplot(2, 4, 1)
ax2 = fig.add_subplot(2, 4, 2)
ax3 = fig.add_subplot(2, 4, 3)
ax4 = fig.add_subplot(2, 4, 4)
ax5 = fig.add_subplot(2, 4, 5)
ax6 = fig.add_subplot(2, 4, 6)
ax7 = fig.add_subplot(2, 4, 7)
ax2.set_title('A* Search')
ax3.set_title('IDA* Search')
ax4.set_title('Huristic Table For A*')
ax5.set_title('G\'s Table For A*')
ax4.set_title('Huristic Table For IDA')
ax5.set_title('G\'s Table For IDA')

ax1.clear()
ax2.clear()
ax3.clear()
ax4.clear()
ax5.clear()
ax6.clear()
ax7.clear()
ani = animation.FuncAnimation(fig, animateGBFS, interval=speed * 1000)


def Draw(Data):

    plt.figtext(.18, .97, "Cost: Calculating....", fontsize=14, horizontalalignment='center')
    plt.figtext(.38, .97, "Cost:  Calculating....", fontsize=14, horizontalalignment='center')
    plt.figtext(.58, .97, "Cost:  Calculating....", fontsize=14, horizontalalignment='center')
    plt.xticks(range(1, len(Data)))
    plt.yticks(range(1, len(Data[0])))
    z4 = ax7.matshow(Data, cmap='jet', interpolation='nearest', aspect='equal')
    plt.colorbar(z4)

    plt.tick_params(axis='x', bottom=False)
    plt.grid(c='indigo', ls=':', lw='0.4')
    plt.ioff()
    plt.show()


def main():
    cols, rows, EndingRow, EndingCol, StartingRow, StartingCol, Data = 0, 0, 0, 0, 0, 0, 0
    cols, rows, EndingRow, EndingCol, StartingRow, StartingCol, Data = ReadFromFile("grid.txt", cols, rows, StartingRow,
                                                                                    StartingCol, EndingRow, EndingCol,
                                                                                    Data)
    for i in range(len(Data)):
        for j in range(len(Data[i])):
            if Data[i][j] == 1:
                Data[i][j] = wall
            elif Data[i][j] == 0:
                Data[i][j] = nullStateColor
    Data[StartingRow][StartingCol] = StartingColor
    Data[EndingRow][EndingCol] = EndingColor
    GBFSData = copy.deepcopy(Data)
    AData = copy.deepcopy(Data)
    IDAData = copy.deepcopy(Data)
    p = Process(target=Draw, args=[Data])
    t1 = threading.Thread(target=GreedyBestFirstSearch,
                          args=(cols, rows, StartingRow, StartingCol, EndingRow, EndingCol, GBFSData, speed))
    t2 = threading.Thread(target=ASearch,
                          args=(cols, rows, StartingRow, StartingCol, EndingRow, EndingCol, AData, speed))
    t3 = threading.Thread(target=IDASeach,
                          args=(cols, rows, StartingRow, StartingCol, EndingRow, EndingCol, IDAData, speed))
    WriteIntoFile("GBFS.txt", cols, rows, StartingRow, StartingCol, EndingRow, EndingCol, Data)
    WriteIntoFile("ASearch.txt", cols, rows, StartingRow, StartingCol, EndingRow, EndingCol, Data)
    WriteIntoFile("IDASearch.txt", cols, rows, StartingRow, StartingCol, EndingRow, EndingCol, Data)

    p.start()
    time.sleep(2)
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    global fig, ax1, ax2, ax3, ax4, ax5, ax6, ax7

    if foundCount >= 3:
        time.sleep(1)
        p.terminate()
    p.join()
    fig = plt.figure(figsize=(17, 12))

    ax1 = fig.add_subplot(2, 4, 1)
    ax2 = fig.add_subplot(2, 4, 2)
    ax3 = fig.add_subplot(2, 4, 3)
    ax4 = fig.add_subplot(2, 4, 4)
    ax5 = fig.add_subplot(2, 4, 5)
    ax6 = fig.add_subplot(2, 4, 6)
    ax7 = fig.add_subplot(2, 4, 7)
    plt.xticks(range(1, len(Data)))
    plt.yticks(range(1, len(Data[0])))
    z4 = ax7.matshow(Data, cmap='jet', interpolation='nearest', aspect='equal')
    plt.colorbar(z4)

    plt.tick_params(axis='x', bottom=False)
    plt.grid(c='indigo', ls=':', lw='0.4')
    ax2.set_title('A* Search')
    ax3.set_title('IDA* Search')
    ax4.set_title('Huristic Table For A*')
    ax5.set_title('G\'s Table For A*')
    ax4.set_title('Huristic Table For IDA')
    ax5.set_title('G\'s Table For IDA')


    plt.figtext(.18, .97, "Cost: " + str(cost1), fontsize=14, horizontalalignment='center')
    plt.figtext(.38, .97, "Cost: " + str(cost2), fontsize=14, horizontalalignment='center')
    plt.figtext(.58, .97, "Cost: " + str(cost3), fontsize=14, horizontalalignment='center')
    plt.close(1)
    drawplt()
    plt.show()


if __name__ == '__main__':
    while True:
        try:
            speed = float(input("\n10 Being Fastest\nEnter the Speed From 1 to 10: "))
            speed = (10 - speed) / 10
            break
        except:
            continue
    p = (input(f'\nEnter Level Limit for IDA Search 0-99: By Default Set to {LevelLimit}: '))
    if '0' <= p <= '99':
        LevelLimit = int(p)
    main()
