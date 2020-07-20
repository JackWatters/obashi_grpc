import chat_pb2_grpc
import chat_pb2

class Server(chat_pb2_grpc.ChatServiceServicer):

    def SayHello(self, request, context):
        print("Received message from the client: "+str(request.body))
        return chat_pb2.Message(body="Hello from the server!")