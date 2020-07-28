import do_work_pb2_grpc
import do_work_pb2
from theatre_ag import Cast, Episode, SynchronizingClock, TaskQueueActor, default_cost
import handwash_workflow as h 
import threading


class Service(do_work_pb2_grpc.SimulateServiceServicer):

    def __init__(self):
        clock = SynchronizingClock(max_ticks=10)

        cast = Cast()
        bob = TaskQueueActor('bob',clock)
        cast.add_member(bob)
        alice = TaskQueueActor('alice', clock)
        cast.add_member(alice)

        self.direction = h.Direction()
        episode = Episode(clock, cast, self.direction)
        self.perform_thread = threading.Thread(target=episode.perform)
        self.perform_thread.start()


    def do_work(self, request, context):
        ##this is the blocking mechanism. Each time a message is sent, the simulation is freed for one tick.
        self.direction.listener.blocked = False 
        return do_work_pb2.Message(body="Hands clean = " + str(self.direction.hands.clean))

    #def StartSimulation(self,request,context):
        #self.episode.perform()
