package main

import (
	"log"
	"io/ioutil"
	"strings"
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

	file, err := ioutil.ReadFile("command.txt")
    if err != nil {
		log.Fatalf("Error when reading comand file: %s",err)
	}
	
	data := strings.Split(string(file),"\n")

	for line := range data {
		
		message := doWork.Message{
			Body: string(data[line]),
		}

		response, err := c.DoWork(context.Background(),&message)

		if err != nil {
			log.Fatalf("Error when calling DoWork: %s",err)
		}
		
		log.Printf("Response from the server: %s",response.Body)

	}

}