import do_work_pb2_grpc
import do_work_pb2
from theatre_ag import Cast, Episode, SynchronizingClock, TaskQueueActor, default_cost


def load_workflow_class(file_path, class_name):

    with open(file_path, 'r') as workflow_code_file:
        code = workflow_code_file.read()
        old_locals = list(locals().keys())
        exec(code)
        return locals()[class_name]


class Service(do_work_pb2_grpc.SimulateServiceServicer):

    def __init__(self, episode):
        self.episode = episode

    def assign_task_to_new_actor(self, entry_method):
            eve = TaskQueueActor('eve',self.episode.clock)
            self.episode.cast.add_member(eve)
            eve.allocate_task(entry_method)
            eve.start()

    def do_work(self, request, context):
        # This is the blocking mechanism. Each time a message is sent, the simulation is freed for one tick.
        if request.body == "Tick":
            self.episode.blocked = False
        elif request.body == "addActor":

            workflow_class = load_workflow_class('example-workflow.txt', 'Test')
            dynamic_class_instance = workflow_class()
            self.assign_task_to_new_actor(dynamic_class_instance.the_main_entry_point)

        return do_work_pb2.Message(body="hello from the server")


