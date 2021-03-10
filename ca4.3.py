import math
import sys
sys.setrecursionlimit (10**5)
class number:
    def __init__(self,num,x,y):
        self.number = num
        self._x = x
        self._y = y
        
class Matrix:
    def __init__(self,n):
        self.numbers = []
        self.n = n
        self.answer = math.inf
        self.main_matrix = [[0 for i in range(n)] for j in range(n)]
        self.temp_forfalkerson_graph = [[0 for i in range(2*n + 2)] for j in range(2*n + 2)]
        self.num_of_nodes = 2*self.n + 2
        self.parent = [-1] * self.num_of_nodes
        self.max_flow = 0 

    def add_number(self,num,x,y): 
        self.main_matrix[x][y] = num 
        new_num = number(num,x,y)
        self.numbers.append(new_num) 


    def there_is_path(self): 
        self.parent = [-1] * self.num_of_nodes
        passed =[0] * self.num_of_nodes
        queue=[] 
        queue.append(0) 
        passed[0] = 1
        while True: 
            if len(queue) == 0:
                return
            u = queue.pop(0) 
            for i in range(len(self.temp_forfalkerson_graph[u])): 
                weight = self.temp_forfalkerson_graph[u][i]
                if passed[i] == 0 and weight > 0 : 
                    queue.append(i) 
                    passed[i] = 1
                    self.parent[i] = u 
            if passed[-1] == 1:
                return True
        return False
    
    def update_capacities(self,min_capacity):
        node_id = self.num_of_nodes - 1 
        while True:
            if node_id == 0:
                return 
            parent_node_id = self.parent[node_id] 
            self.temp_forfalkerson_graph[parent_node_id][node_id] -= min_capacity 
            self.temp_forfalkerson_graph[node_id][parent_node_id] += min_capacity 
            node_id = self.parent[node_id] 
    
    def find_min_flow(self):
        min_capacity = math.inf
        node_id = self.num_of_nodes - 1 
        while True: 
            if node_id == 0:
                break
            new_yaal_capacity = self.temp_forfalkerson_graph[self.parent[node_id]][node_id]
            
            if min_capacity > new_yaal_capacity:
                min_capacity = new_yaal_capacity
                
            node_id = self.parent[node_id]    
        return min_capacity   
                    
    def calculate_max_flow(self):
        self.max_flow = 0
        while self.there_is_path() : 
            min_capacity = self.find_min_flow()
            self.max_flow +=  min_capacity 
            self.update_capacities(min_capacity)
        
        return self.max_flow
          
    def sort_nums(self):
        self.numbers.sort(key = lambda x:x.number)
        
    def restart_graph(self):
        self.temp_forfalkerson_graph = [[0 for i in range(2*n + 2)] for j in range(2*n + 2)]
        for i in range(1,self.n+1):
            self.temp_forfalkerson_graph[0][i] = 1
            
        for i in range(self.n+1,2 * self.n + 1):
            self.temp_forfalkerson_graph[i][-1] = 1

    def calc_min_payment(self,num_list):
        if len(num_list) == 0 : 
            return 
        temp_num = num_list[len(num_list)//2].number 
        self.restart_graph() 
        for i in range(len(self.numbers)) :  
            if self.numbers[i].number <= temp_num:
                self.temp_forfalkerson_graph[1 + self.numbers[i]._x][1 + self.n + self.numbers[i]._y] = 1 
        num = self.calculate_max_flow() 
        if num == self.n:
            self.answer = temp_num
            self.calc_min_payment(num_list[:len(num_list)//2])
        else:
            self.calc_min_payment(num_list[len(num_list)//2+1:])

n = int(input())
matrix = Matrix(n)
main_matrix = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    line = [int(x) for x in input().strip().split()]
    for j in range(len(line)):
        matrix.add_number(line[j],i,j)

matrix.sort_nums()
matrix.calc_min_payment(matrix.numbers)
print(matrix.answer)
