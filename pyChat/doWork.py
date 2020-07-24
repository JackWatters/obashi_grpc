import doWork_pb2_grpc
import doWork_pb2
from theatre_ag import Cast, Episode, SynchronizingClock, TaskQueueActor, default_cost
import handwash_workflow as h 


class Server(doWork_pb2_grpc.SimulateServiceServicer):

    def DoWork(self, request, context):
        clock = SynchronizingClock(max_ticks=10)

        cast = Cast()
        bob = TaskQueueActor('bob',clock)
        cast.add_member(bob)
        alice = TaskQueueActor('alice', clock)
        cast.add_member(alice)


        direction = h.WashHandsDirection()
        episode = Episode(clock, cast, direction)
        episode.perform()

        return doWork_pb2.Message(body="Hands clean = " + str(direction.hands.clean))