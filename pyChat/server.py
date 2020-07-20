import grpc 
import chat_pb2
import chat_pb2_grpc
import chat 
from concurrent import futures

server = chat.Server()
grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
chat_pb2_grpc.add_ChatServiceServicer_to_server(server, grpc_server)
grpc_server.add_insecure_port('[::]:9000')
grpc_server.start()
grpc_server.wait_for_termination()
