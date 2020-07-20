import grpc
import chat_pb2
import chat_pb2_grpc


with grpc.insecure_channel('localhost:9000') as channel:
    stub = chat_pb2_grpc.ChatServiceStub(channel)
    message = chat_pb2.Message(body="Hello from the client!")
    response = stub.SayHello(message)
print("Greeter client received: " + str(response.body))