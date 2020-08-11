import grpc
from pyChat import do_work_pb2
from pyChat import do_work_pb2_grpc


with grpc.insecure_channel('localhost:9000') as channel:
    stub = do_work_pb2_grpc.SimulateServiceStub(channel)
    message = do_work_pb2.Message(body="addActor")
    response = stub.do_work(message)
print("received response from the server: " + str(response.body))