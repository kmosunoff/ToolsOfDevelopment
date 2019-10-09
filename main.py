from matrix import Matrix
from sorting import Sorter

class Main():
    input_file_name = "input.txt"
    matrix = Matrix()
    
    def read_matrix(self):
        fin = open(self.input_file_name, 'r')
        for line in fin.readlines():
            self.matrix.append(list(map(int, line.split(' '))))
    
    def sort_matrix(self):
        sorter = Sorter()
        for line in self.matrix.data:
            sorter.selection_sort(line)
        
    def write_matrix(self):
        for line in self.matrix.data:
            print(line)

main = Main()
main.read_matrix()
main.sort_matrix()
main.write_matrix()
