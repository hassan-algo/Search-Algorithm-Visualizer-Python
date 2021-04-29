# algorithm-visualizer-python

ALGORITHMS IMPLEMENTED:
1. Greedy Best First Search 
2. A* Search
3. IDA*

The obstacles are filled rectangles of unknown dimensions and can be found anywhere in the maize.  The robot cannot be in those cells. There are 3 actions allowed. Up one cell (cost is 1), right one cell  (cost is 3), diagonally up towards the right (cost is 2). The system should output: 1. The complete path if goal is found otherwise show path’s followed by algorithm to search for  goal 2. The sequence of actions performed to reach the goal from start 3. The total cost of the path 4. A grid which shows the path followed.

FEATURES:

•	2D- Array (matrix) used to represent nodes of maize.

•	Code is in python language. 

•	Graphical Interface (matplotlib) to visualize working of all three algorithms which further leads to final path and cost. 

•	Multiprocessing and threading is used to visualize working of algorithms parallel.

Instructions:
1. Open main.py with pycharm. 
2. If there is " <No interpreter> " on bottom right of pycharm 
   window(status bar) , click on it and select python 3.9
3. Run the program (main.py).
4. Enter speed (suggested 8.5) for graphics. 
5. Enter limit for IDA*(Press Enter for default). 
6. Graphical visualization of algorithms will pop-up in
 few moments. (Cost will be shown after completion of 
 every algorithm).

In case of any error regarding matplotlib(library) follow the following instruction:

3.1 Go to terminal of pycharm (on statusbar).

3.2 Type "pip install numpy"

3.3 Type "pip install matplotlib"

3.4 Type "pip install multiprocessing" 

3.5 Now run the program and follow up above schedule. 


 ![image](https://user-images.githubusercontent.com/63236001/116530789-db072880-a8f7-11eb-87ff-a5e7c1ad786c.png)
![image](https://user-images.githubusercontent.com/63236001/116530808-df334600-a8f7-11eb-99d9-1d4c41485435.png)

•	Green color -> Final path nodes.

•	Pink color ->Start and goal.

•	Black color -> Obstacles.

•	Blue color -> visited.

•	Purple color -> Expected to visit.

