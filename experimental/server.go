package main

import (
	"goChat/doWork"
	"log"
	"net"
	"google.golang.org/grpc"
)

func main() {
	lis, err := net.Listen("tcp", ":9000")

	if err != nil {
		log.Fatalf("failed to listen on port 9000: %v", err)
	}

	s := doWork.Server{}

	grpcServer := grpc.NewServer()

	doWork.RegisterSimulateServiceServer(grpcServer,&s)

	if err := grpcServer.Serve(lis); err != nil {
		log.Fatalf("failed to serve gRPC server over port 9000: %v", err)
	}

}
