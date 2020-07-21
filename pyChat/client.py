import grpc
import chat_pb2
import chat_pb2_grpc


with grpc.insecure_channel('localhost:9000') as channel:
    stub = chat_pb2_grpc.ChatServiceStub(channel)
    message = chat_pb2.Message(body="Wash your hands!")
    response = stub.SayHello(message)
print("received response from the server: " + str(response.body))