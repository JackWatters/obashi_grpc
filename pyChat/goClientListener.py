from theatre_ag import default_cost
import grpc
import time

class goClientListener(object):

    def __init__(self):
        self.blocked = True

    def the_main_entry_point(self):
        while True:
            self.wait_for_message()

    @default_cost(1)
    def wait_for_message(self):
        try:
            while self.blocked:
                pass
            self.blocked = True
            print("idling")
        except:
            return False