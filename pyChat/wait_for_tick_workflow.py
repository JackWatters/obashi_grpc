from theatre_ag import default_cost
import grpc
import time

class WaitForTickWorkflow(object):

    def __init__(self,improv):
        self.improv = improv

    def the_main_entry_point(self):
        while True:
            self.wait_for_message()

    @default_cost(1)
    def wait_for_message(self):
        try:
            while self.improv.blocked:
                pass
            self.improv.blocked = True
        except:
            return False