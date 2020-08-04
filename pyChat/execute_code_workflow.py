class ExecuteCode(object):
    
    def __init__(self):
        pass

    def read_file(self,filename):
        with open(filename) as workflow_code:
            exec(workflow_code.read())

if __name__ == '__main__':
    execute_code = ExecuteCode()
    execute_code.read_file("example-workflow.txt")