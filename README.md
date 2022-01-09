# Ex4_OOP - Pokemon Game
This project has written by [Adi Oman](https://github.com/adiOmann) and [Adi Miller](https://github.com/AdiMM1).

This task is the fourth task in our object-oriented course. In this task we were asked to create a Pokemon game according to the directed graph from our previous task. 
The game has 15 stages, each stage has one or several agents. The agent's goal is to eat the Pokemon that appear on the graph, and earn as many points as possible (Each Pokemon contains a different value of points).
When eating a Pokemon, another Pokemon is created, and the game ends when the user clicks on the stop button or the time set for this stage ends.

![image](https://github.com/adiOmann/Ex4_OOP/blob/master/1200px-International_Pok%C3%A9mon_logo.svg.png)

## client_python
### DiGraph
In this class we add the next functions:
* dist - Calculates the distance between 2 nodes.
* closest - Returns the edge that the pokemon stand on.
### GraphAlgo
### GraphInterface
### GraphAlgoInterface
### client
This class represents the server.
### student_code
This class contains the GUI and the main function that run the game.
### agent:
* ID
* Value
* Src
* Dest
* Pos
### pokemon:
* Edge
* Value
* Pos
* Type

## Our GUI




## How to run the game
* At the terminal: <java -jar Ex4_Server_v0.0.jar 0> (instead of 0 put any level you want to run). <br />
* run the "student_code" at the project.