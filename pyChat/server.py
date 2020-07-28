import grpc 
import do_work_pb2
import do_work_pb2_grpc
import do_work 
from concurrent import futures

service = do_work.Service()
grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
do_work_pb2_grpc.add_SimulateServiceServicer_to_server(service, grpc_server)
grpc_server.add_insecure_port('[::]:9000')
grpc_server.start()
grpc_server.wait_for_termination()
