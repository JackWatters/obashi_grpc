import doWork_pb2_grpc
import doWork_pb2
from theatre_ag import Cast, Episode, SynchronizingClock, TaskQueueActor, default_cost
import handwash_workflow as h 
import threading


class Server(doWork_pb2_grpc.SimulateServiceServicer):

    def __init__(self):
        print("entered server constructor")
        clock = SynchronizingClock(max_ticks=10)

        cast = Cast()
        bob = TaskQueueActor('bob',clock)
        cast.add_member(bob)
        alice = TaskQueueActor('alice', clock)
        cast.add_member(alice)
        print("added member")


        self.direction = h.WashHandsDirection()
        episode = Episode(clock, cast, self.direction)
        print("about to perform")
        self.perform_thread = threading.Thread(target=episode.perform)
        self.perform_thread.start()

        print("started simulation")


    def DoWork(self, request, context):
        self.direction.listener.blocked = False
        
        return doWork_pb2.Message(body="Hands clean = " + str(self.direction.hands.clean))

    #def StartSimulation(self,request,context):
        #self.episode.perform()
