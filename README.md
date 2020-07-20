##gRPC example 

A simple client/server GRPC communication between Python and Golang. Works for both a python client with a Go server and vice versa.

## Contributions

Jack Watters <br/>
Student, School of Computing Science, University of Glasgow <br/>
GitHub ID: JackWatters <br/>
Email: [2314993w@student.gla.ac.uk](mailto:2314993w@student.gla.ac.uk)

## Details
In the root directory: <br/>

* client.go and client.py both have the same functionality. They attempt to connect to a gRPC server on port 9000 and send a simple hello message, then wait for a response. 

*server.go and server.py both create a gRPC server on port 9000 and add the ChatService functionality to respond to any messages received.

*chat.proto is a file used to generate code found in the pyChat and chat directories. It acts as a contract by declaring the Message class and the SayHello method. The code generated then implements this in either python or go.

In the pyChat directory: <br/>

*This contains generated code from chat.proto which provides the python files with functionality to communicate across a gRPC server

In the chat directory: <br/>

*This contains go files generated from chat.proto and acts in the same way as pyChat but for go.

## Instructions

To run this properly, start up one server file (either server.go or server.py) by typing in "go run server.go" or "python server.py" into a terminal at the root directory of the package. <br/>
Then, run a client file (either client.go or client.py) in a separate terminal by typing in "go run client.go" or "python client.py" in the root directory of the package. <br/>
This will display a message saying "hello from the server", and in the original terminal, a message will be displayed saying "hello from the client". <br/> <br/>
Note: The server file must be shut down, or else it will continue to run. Do this by performing cmd-c in the terminal which it is open in.



