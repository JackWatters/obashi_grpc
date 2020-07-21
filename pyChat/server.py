import grpc 
import doWork_pb2
import doWork_pb2_grpc
import doWork 
from concurrent import futures

server = doWork.Server()
grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
doWork_pb2_grpc.add_SimulateServiceServicer_to_server(server, grpc_server)
grpc_server.add_insecure_port('[::]:9000')
grpc_server.start()
grpc_server.wait_for_termination()
