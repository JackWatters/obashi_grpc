#from theatre_ag import default_cost

class ExecuteCode:

    is_workflow = True
    
    def __init__(self):
        pass

    def execute(self,code):
        to_return = list()
        name = None
        old_locals = list(locals().keys())
        exec(code)
        for name in locals().keys():
            if name not in old_locals and name != 'old_locals':
                to_return.append(eval(name))
        return to_return


