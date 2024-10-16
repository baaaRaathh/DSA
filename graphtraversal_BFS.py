# class graph:
#     def __init__(self,size):
#         self.size = size
#         self.adj_data = [[0] * size for i in range(size)]
#         self.vertix_data = [''] * size
        
#     def addvertix(self,v,data):
#         if 0 <= v < self.size:
#             self.vertix_data[v] = data
                     
#     def addadj(self,u,v):
#         if 0 <= u < self.size and 0 <= v < self.size:
#             self.adj_data[u][v] = 1
#             self.adj_data[v][u]=  1
                                
#     def print_graph(self):
#         print('\nvertix')
#         for i in self.adj_data:
#             print(' '.join(map(str,i)))
#         for v,j in enumerate(self.vertix_data):
#             print(v,j)
            
#     def bfs(self,start):
#         q = [self.vertix_data.index(start)]
#         visite = [False] * self.size
#         visite[q[0]] = True
#         while q:
#             current = q.pop(0)
#             print(self.vertix_data[current],end=' ')
#             for i in range(self.size):
                
#                 if self.adj_data[current][i] == 1 and not visite[i]:
#                     q.append(i)
#                     visite[i] = True                                      
                     
# g =graph(4)
# g.addvertix(0,'A')
# g.addvertix(1,'B')
# g.addvertix(2,'C')
# g.addvertix(3,'D')
# g.addadj(0, 1)  # A - B
# g.addadj(0, 2)  # A - C
# g.addadj(0, 3)  # A - D
# g.addadj(1, 2)  # B - C

# g.print_graph()   

# g.bfs('D')
                                   
                                        
# # a = [[1,2.3],[34,5,6],[23,4,2],[2,4,5],[4,5,6],[2,4.2,2]]
# # for i in a:
# #     print('- '.join(map(str,i)))



# a = 78
# b = 30
# print = (a+b)
# print =(a-b)
# print = (a/b)
# print = (a*b)
# # a =((1,2<))


def mail(models): return models

models = 10

print(mail(2))