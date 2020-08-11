## obashi gRPC theatre simulation 

A client/server gRPC communication application which allows the simulation of workflows on the server using theatre_ag. The server sets up and begins the simulation. The client controls the simulation.

## Contributions

Jack Watters <br/>
Student, School of Computing Science, University of Glasgow <br/>
GitHub ID: JackWatters <br/>
Email: [2314993w@student.gla.ac.uk](mailto:2314993w@student.gla.ac.uk)

## Details
In the root directory: <br/>

* do_work.proto is a file used to generate code found in the pyChat and goChat/doWork directories. It acts as a contract by declaring the Message class and the do_work method. The code generated then implements this in either python or go.

In the pyChat directory: <br/>

* This contains all python code, including generated code from do_work.proto which provides functionality to communicate across a gRPC server.

* server.py creates a gRPC server on port 9000 and begins a simulated environment using theatre_ag.

* do_work.py receieves a request (message) from the client, and decides what conditions should be changed based on its contents. It then sends back a response from the server to the client.

In the goChat directory: <br/>

* This contains the go client code, and code generated from the protobuf is stored in the doWork folder.

* client.go attempts to connect to a gRPC server on port 9000. It then reads in text from command.txt, one line at a time, and sends it to the server. 

In the experimental directory: <br/>

* Partial implementation of a reversed role: with a go server and a python client. It does not affect the rest of the project at the moment.

## Instructions

To run this properly, first start up the server by typing in "python server.py" into a terminal in the appropriate directory. This will set up the initial simulation with a simple tick_listener workflow actor that moderates the simulation based on client messages. <br/> <br/>
Improv.perform begins the simulation clock, and tick_listener then acts as a blocking/control mechanism which will release the clock for one tick once a blocked variable is set to False. <br/><br/>
To run the client, open a second terminal and type "go run client.go" in the appropriate directory. This will call the do_work method using a gRPC connection which allows messages to be sent from client to server. If "Tick" is sent, the blocking variable is set to False. If add_actor is read, a new actor will be assigned the workflow found in example-workflow.txt after compilation. <br/> <br/>
Once this is run, the client terminal should receive a status message from the server. In the server terminal, a status will be printed after each message has been sent from the client detailing how far along the workflow an actor is. <br/> <br/>
Note: The server file must be shut down, or else it will continue to run. Do this by performing cmd-c in the terminal which it is open in.