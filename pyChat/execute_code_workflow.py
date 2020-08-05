class ExecuteCode(object):

    is_workflow = True
    
    def __init__(self):
        pass

    def read_file(self,filename):
        with open(filename) as workflow_code:
            exec(workflow_code.read())
        test = Test()
        print(test.is_workflow)

if __name__ == '__main__':
    execute_code = ExecuteCode()
    execute_code.read_file("example-workflow.txt")