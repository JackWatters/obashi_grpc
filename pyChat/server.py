import grpc 
import do_work_pb2_grpc
import do_work 
from concurrent import futures
from theatre_ag import Cast, Episode, SynchronizingClock, TaskQueueActor, default_cost
from wait_for_tick_workflow import WaitForTickWorkflow
from improv import Improv


clock = SynchronizingClock(max_ticks=10)

cast = Cast()
tick_listening_actor = TaskQueueActor('tick_listener',clock)
cast.add_member(tick_listening_actor)

improv = Improv(clock, cast)
wait_for_tick_workflow = WaitForTickWorkflow(improv)
tick_listening_actor.allocate_task(wait_for_tick_workflow.the_main_entry_point)
improv.perform()


service = do_work.Service(improv)
grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
do_work_pb2_grpc.add_SimulateServiceServicer_to_server(service, grpc_server)
grpc_server.add_insecure_port('[::]:9000')
grpc_server.start()
grpc_server.wait_for_termination()
