from theatre_ag import default_cost
import grpc
import time

class goClientListener(object):

    def the_main_entry_point(self):
        while True:
            self.wait_for_message()

    @default_cost(0)
    def wait_for_message(self):
        try:
            new CallOptions().WithWaitForReady(true))
            print("idling")
            time.sleep(1)
        except:
            return False