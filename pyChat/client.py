import grpc
import doWork_pb2
import doWork_pb2_grpc


with grpc.insecure_channel('localhost:9000') as channel:
    stub = doWork_pb2_grpc.SimulateServiceStub(channel)
    message = doWork_pb2.Message(body="Wash your hands!")
    response = stub.DoWork(message)
print("received response from the server: " + str(response.body))