package main

import (
	"log"

	"golang.org/x/net/context"
	"google.golang.org/grpc"
	"goChat/doWork"
)

func main() {
	var conn *grpc.ClientConn
	conn, err := grpc.Dial(":9000",grpc.WithInsecure())

	if err != nil {
		log.Fatalf("could not connect: %s",err)
	}
	defer conn.Close()

	c := doWork.NewSimulateServiceClient(conn)

	message := doWork.Message{
		Body: "Hello from the client",
	}

	response, err := c.DoWork(context.Background(),&message)

	if err != nil {
		log.Fatalf("Error when calling DoWork: %s",err)
	}
	
	log.Printf("Response from the server: %s",response.Body)

}