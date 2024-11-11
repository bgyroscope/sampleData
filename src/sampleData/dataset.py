'''main data class '''
import json

class DataSet:
    '''manages sample data '''

    def __init__(self, input_file, nrows=10): 
        pass


    def load_input(self,input_file):
        with open(input_file, 'r') as f:
            vardata = json.load(f) 

        return vardata 

    # Input and Output --------------------
    def save(self, loc):
        '''save the data as a flattened csv '''
        pass

    # Simulate data -----------------------
    def generate(self):
        '''generate the data '''
        pass

