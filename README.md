##gRPC example 

A client/server gRPC communication application which allows the simulation of workflows on the server using the theatre_ag package. The client activates the workflow.

## Contributions

Jack Watters <br/>
Student, School of Computing Science, University of Glasgow <br/>
GitHub ID: JackWatters <br/>
Email: [2314993w@student.gla.ac.uk](mailto:2314993w@student.gla.ac.uk)

## Details
In the root directory: <br/>

* client.go and client.py both have the same functionality. They attempt to connect to a gRPC server on port 9000 and send a simple request message, then wait for a response. 

* server.go and server.py both create a gRPC server on port 9000 and add the doWorkService functionality to respond to any messages received after work has been completed.

* doWork.proto is a file used to generate code found in the pyChat and goChat directories. It acts as a contract by declaring the Message class and the DoWork method. The code generated then implements this in either python or go.

In the pyChat directory: <br/>

* This contains generated code from chat.proto which provides the python files with functionality to communicate across a gRPC server

In the goChat directory: <br/>

* This contains go files generated from chat.proto and acts in the same way as pyChat but for go.

## Instructions

To run this properly, start up one server file (either server.go or server.py) by typing in "go run server.go" or "python server.py" into a terminal at the root directory of the package. <br/>
Then, run a client file (either client.go or client.py) in a separate terminal by typing in "go run client.go" or "python client.py" in the root directory of the package. <br/>
This will display a message saying "Wash your hands!", and in the original terminal, a message will be displayed to tell the client if the hands have been washed at the end of the workflow. <br/> <br/>
Note: The server file must be shut down, or else it will continue to run. Do this by performing cmd-c in the terminal which it is open in.



