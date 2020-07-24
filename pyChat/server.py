import grpc 
import doWork_pb2
import doWork_pb2_grpc
import doWork 
from concurrent import futures
import contextlib

server = doWork.Server()
grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
doWork_pb2_grpc.add_SimulateServiceServicer_to_server(server, grpc_server)
grpc_server.add_insecure_port('[::]:9000')
message = doWork_pb2.Message(body="Wash your hands!")
grpc_server.start()
server.DoWork(message,contextlib.nullcontext)
grpc_server.wait_for_termination()
