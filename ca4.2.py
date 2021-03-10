import math
import sys
sys.setrecursionlimit (10**5)
class Node:
    def __init__(self,_id):
        self.node_id = _id    
        self.connections = []
        
    def add_connection(self,bi,weight):
        self.connections.append([bi,weight])
    
class Graph:
    def __init__(self,ais,bis):
        self.ais = ais
        self.bis = bis    
        self.num_of_nodes = len(ais) + len(bis) + 2
        self.matrix = [[0 for i in range(self.num_of_nodes)] for j in range(self.num_of_nodes)]
        self.set_matrix()
        self.parent = [-1] * self.num_of_nodes
        self.max_flow = 0 
        self.max_profit = sum(bis)
         
    def set_matrix(self):
        for i in range(len(self.bis)):
            self.matrix[0][i+1] = self.bis[i]
        for i in range(len(self.ais)):
            self.matrix[i+len(bis) + 1][self.num_of_nodes-1] = ais[i]
            
    def set_connection(self,bi,line):            
        for i in range(len(line)):
            if line[i] == 1:
                self.matrix[bi+1][i+len(bis)+1] = math.inf
    
    
    def there_is_path(self): 
        # queue=[] 
        # queue.append(0) 
        # passed[0] = 1
        while 1:
            flow =[None] * self.num_of_nodes 
            flow = self.dfs(0,math.inf,flow)
            if flow[-1] == None:
                return False
            self.min_capacity = flow[-1]
            self.max_flow += flow[-1]
        # while True: 
        #     if len(queue) == 0:
        #         return
        #     u = queue.pop(0) 
        #     for i in range(len(self.matrix[u])): 
        #         weight = self.matrix[u][i]
        #         if passed[i] == 0 and weight > 0 : 
        #             queue.append(i) 
        #             passed[i] = 1
        #             self.parent[i] = u 
        #     if passed[-1] == 1:
        #         return True
        # return False
    
    def update_capacities(self,min_capacity):
        node_id = self.num_of_nodes - 1 
        while True:
            if node_id == 0:
                return 
            parent_node_id = self.parent[node_id] 
            self.matrix[parent_node_id][node_id] -= self.min_capacity 
            self.matrix[node_id][parent_node_id] += self.min_capacity 
            node_id = self.parent[node_id] 
    
    def find_min_flow(self):
        min_capacity = math.inf
        node_id = self.num_of_nodes - 1 
        while True: 
            if node_id == 0:
                break
            new_yaal_capacity = self.matrix[self.parent[node_id]][node_id]
            
            if min_capacity > new_yaal_capacity:
                min_capacity = new_yaal_capacity
                
            node_id = self.parent[node_id]    
        return min_capacity   

    def dfs(self,u,x):
        self.flow[u] = x
        for i in range(len(self.matrix[u])): 
            # if flow[-1] != None:
            #     return flow
            weight = self.matrix[u][i] - self.f[u][i]
            if self.flow[i] == None and weight > 0 : 
                self.parent[i] = u
                self.dfs(i,min(x,weight))

    def calculate_max_profit(self):
        self.f = [[0 for i in range(self.num_of_nodes)] for j in range(self.num_of_nodes)]

        while True:
            self.flow =[None] * self.num_of_nodes 
            self.dfs(0,math.inf)
            if self.flow[-1] == None:
                break
            
            node_id = self.num_of_nodes - 1 
            while True: 
                if node_id == 0:
                    break
                u = self.parent[node_id]
                self.f[u][node_id] -= self.flow[-1]     
                self.f[node_id][u] += self.flow[-1]     
                node_id = u  
            print(self.max_flow)
            print("p e",self.parent[-1],self.f[self.parent[-1]][-1])
            self.max_flow += self.f[self.parent[-1]][-1]

            
        self.max_profit -= self.max_flow
          
n_m = [int(x) for x in input().strip().split()]
n = n_m[0]
m = n_m[1]
ais = [int(x) for x in input().strip().split()]
bis = [int(x) for x in input().strip().split()]
graph = Graph(ais,bis)
for i in range(m):
    line = [int(x) for x in input().strip().split()]
    graph.set_connection(i,line)

graph.calculate_max_profit()
print(graph.max_profit)