from theatre_ag import Episode, TaskQueueActor, default_cost
import go_client_listener as g


class Hands(object):
    def __init__(self):
        self.clean = False
        self.soaped = False


class RinseWorkflow(object):

    is_workflow = True

    def __init__(self, washable):
        self.washable = washable

    @default_cost(1)
    def rinse(self):
        print("started rinsing hands")
        self.washable.soaped = False


class WashWorkflow(object):

    is_workflow = True

    def __init__(self, washable):
        self.washable = washable
        self.rinse = RinseWorkflow(washable)

    @default_cost(1)
    def add_soap(self):
        print("started soaping hands")
        self.washable.soaped = True

    @default_cost(1)
    def scrub(self):
        print("started scrubbing hands")
        if self.washable.soaped:
            self.washable.clean = True

    @default_cost(1)
    def wash(self):
        print("started washing hands")
        self.add_soap()
        self.scrub()
        self.rinse.rinse()


class Direction(object):

    def __init__(self):
        self.hands = Hands()

    def apply(self, cast):
        self.listener = g.GoClientListener()
        wash_workflow = WashWorkflow(self.hands)
        list(cast)[0].allocate_task(self.listener.the_main_entry_point)
        list(cast)[1].allocate_task(wash_workflow.wash)

        