import do_work_pb2_grpc
import do_work_pb2
from theatre_ag import Cast, Episode, SynchronizingClock, TaskQueueActor, default_cost
import workflow as w 
import threading
from wait_for_tick_workflow import WaitForTickWorkflow
import execute_code_workflow as e


class Service(do_work_pb2_grpc.SimulateServiceServicer):


    def __init__(self,episode):
        self.episode = episode


    def assign_workflow(self, entry_method):
            eve = TaskQueueActor('eve',self.episode.clock)
            self.episode.cast.add_member(eve)
            eve.allocate_task(entry_method)
            eve.start()
        

    def do_work(self, request, context):
        ##this is the blocking mechanism. Each time a message is sent, the simulation is freed for one tick.
        if request.body == "Tick":
            self.episode.blocked = False
        elif request.body == "addActor":
            wash_workflow = w.WashWorkflow(w.Hands())
            self.assign_workflow(wash_workflow.wash)

        return do_work_pb2.Message(body="hello from the server")


    #def StartSimulation(self,request,context):
        #self.episode.perform()
