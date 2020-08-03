import do_work_pb2_grpc
import do_work_pb2
from theatre_ag import Cast, Episode, SynchronizingClock, TaskQueueActor, default_cost
import workflow as w 
import threading
from wait_for_tick_workflow import WaitForTickWorkflow


class Service(do_work_pb2_grpc.SimulateServiceServicer):

    def __init__(self,episode):
        self.episode = episode
        

    def do_work(self, request, context):
        ##this is the blocking mechanism. Each time a message is sent, the simulation is freed for one tick.
        if request.body == "Tick":
            self.episode.blocked = False
        elif request.body == "addActor":

            workflow_string = """
class jackWorkflow:
    is_workflow=True
    pass
"""
            eve = TaskQueueActor('eve',self.episode.clock)
            self.episode.cast.add_member(eve)
            wash_workflow = w.WashWorkflow(w.Hands())
            eve.allocate_task(wash_workflow.wash)
            eve.start()


        return do_work_pb2.Message(body="hello from the server")

    #def StartSimulation(self,request,context):
        #self.episode.perform()
