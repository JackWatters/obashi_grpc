package doWork 

import (
	"log"
	"golang.org/x/net/context"
)

type Server struct {
}


func (s *Server) do_work(ctx context.Context,message *Message) (*Message,error) {
	log.Printf("Received message body from client: %s",message.Body)
	return &Message{Body:"Hello from the server"},nil
}