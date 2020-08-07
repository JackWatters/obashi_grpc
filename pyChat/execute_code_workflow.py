#from theatre_ag import default_cost

class ExecuteCode:

    is_workflow = True
    
    def __init__(self):
        pass

    #@default_cost(1)
    def read_file(self):
        with open('example-workflow.txt') as workflow_code:
            exec(workflow_code.read())
        test = Test()
        print(test.is_workflow)

if __name__ == '__main__':
    e = ExecuteCode()
    e.read_file()