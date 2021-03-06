# Ex4_OOP - Pokemon Game
This project has written by [Adi Oman](https://github.com/adiOmann) and [Adi Miller](https://github.com/AdiMM1).

This task is the fourth task in our object-oriented course. <br />
In this task we were asked to create a Pokemon game according to the directed graph from our previous task. <br /> 
The game has 15 stages, each stage has one or several agents. The agent's goal is to eat the Pokemon that appear on the graph, and earn as many points as possible (Each Pokemon contains a different value of points). <br />
When agent eating a Pokemon, another Pokemon is created, and the game ends when the user clicks on the stop button or the time set for this stage ends.

![image](https://github.com/adiOmann/Ex4_OOP/blob/master/1200px-International_Pok%C3%A9mon_logo.svg.png)

Our code is based on the writing classes in the previous assignment (ex3): DiGraph and GraphAlgo

## client_python
### Classes fron OOP_Ex3
#### DiGraph
In this class we add the next functions:
* dist - Calculates the distance between 2 nodes.
* closest - Returns the edge that the pokemon stand on.
#### GraphAlgo
We used in the function:
* shortestPath - this method find the short route between 2 nodes.
#### GraphInterface and GraphAlgoInterface 
the intterfaces
## New Classes
#### client
This class represents the server.
#### student_code
This class contains the GUI and the main function that run the game. <br />
The GUI contains the directed graph route - edges, nodes, agents and pokemons. <br />
In addition, there is a stop button to stop the game, 
and buttons that show the level of the game and the time from start of the game. <br />
From this class, we call the surver to find the most effective route from the agent to the pokemon by the function shortsetPath.
### Classes written by us
#### agent:
* ID
* Value
* Src
* Dest
* Pos
#### pokemon:
* Edge
* Value
* Pos
* Type

## Our GUI



https://user-images.githubusercontent.com/94624875/148791230-cc36e88f-0b0b-4896-9ecd-cd8d4853f69c.mp4




## How to run the game
* At the terminal: <java -jar Ex4_Server_v0.0.jar 0> (instead of 0 put any level you want to run). <br />
* run the "student_code" at the project.
