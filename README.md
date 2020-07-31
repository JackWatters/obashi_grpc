## gRPC example 

A client/server gRPC communication application which allows the simulation of workflows on the server using the theatre_ag package. The server sets up and begins the workflow. The client regulates how much work is to be completed.

## Contributions

Jack Watters <br/>
Student, School of Computing Science, University of Glasgow <br/>
GitHub ID: JackWatters <br/>
Email: [2314993w@student.gla.ac.uk](mailto:2314993w@student.gla.ac.uk)

## Details
In the root directory: <br/>

* client.go and client.py both have the same functionality. They attempt to connect to a gRPC server on port 9000 and send a simple request message, then wait for a response. 

* server.py creates a gRPC server on port 9000 and begins a simulated environment using theatre_ag. It will then respond to the message after appropriate work has been completed.

* do_work.proto is a file used to generate code found in the pyChat and goChat directories. It acts as a contract by declaring the Message class and the DoWork method. The code generated then implements this in either python or go.

In the pyChat directory: <br/>

* This contains all python code, including generated code from do_work.proto which provides functionality to communicate across a gRPC server

In the goChat directory: <br/>

* This contains all the go code, generated code is found in the doWork folder

## Instructions

To run this properly, first start up the server by typing in "python server.py" into a terminal in the appropriate directory. This will set up the entire simulation including all actors and their directions using do_work.py Service class. Episode.perform then starts the simulation clock and allows the actors to begin their assigned tasks. One actor is given the goClientListener workflow. This acts as a blocking/control mechanism which will halt the simulation until a given condition is met. In this case, the simulation will be halted until the blocked variable is set to false. This occurs when the do_work method is called (in do_work.py) when the client is run. Therefore, the simulation moves forward a given number of steps only when the client sends a message to the server. Near the end of each tick, the blocked variable is set back to true. <br/>
To run the client (either client.go or client.py), open a second terminal and type "go run client.go" or "python client.py" in the appropriate directory. This will call the do_work method using a gRPC connection which allows work do be done in the simulation. <br/>
Once this is run, the client terminal should receive a status message telling them if the hands are washed yet. It will take a few times until this message returns True. In the server terminal, a status will be printed after each message has been sent from the client detailing how far along the workflow an actor is. <br/> <br/>
Note: The server file must be shut down, or else it will continue to run. Do this by performing cmd-c in the terminal which it is open in.