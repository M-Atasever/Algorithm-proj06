#cse 331
#Kunyu Chen
#project 06

import math


class Digraph:
    def __init__(self, n):
        """
        Constructor
        :param n: Number of vertices
        """
        self.order = n
        self.size = 0
        # You may put any required initialization code here

        self.map = {};
        for i in range(n):
            self.map[i]= {}

    def insert_arc(self, s, d, w):
        """
        Insert a connection arc between two vertices
        """
        if s not in self.map or d not in self.map:
            raise IndexError
        # if s has no child d before, insert it 
        if d not in self.map[s]:
            self.map[s][d] = w
            self.size +=1
            return True 

            
    def out_degree(self, v):
        """
        Count how many arc pointing out from the vertex
        return number of out_degree
        """
        if v not in self.map:
            raise IndexError
        else:
            #
            return len(self.map[v])
        

    def are_connected(self, s, d):
        """
        Determine if there's connection between source and destination vertex
        Return true if there's a arc point from s to d
        """
        if s not in self.map or d not in self.map:
            raise IndexError
        if(d not in self.map[s]):
            return False
        else:
            return True 

    def is_path_valid(self, path):
        """
        whether there is a valid path through the path list
        return true if valid.
        """
        if len(path)==0:
            return False
        if len(path)==1:
            if path[0] in self.map:
                return True
            else:
                raise IndexError
        # compare each two nearby vertexs and find if they're connected          
        for i in range(len(path)-1):
            #not connected return false
            if self.are_connected(path[i],path[i+1]) == 0:
                return False
        return True 
                

    def arc_weight(self, s, d):
        """
        find the arc weight from s to d
        return weight if valid, infinity if invalid arc
        """
        if s not in self.map or d not in self.map:
            raise IndexError
        #s has no child d,return infinity
        if d not in self.map[s]:
            return math.inf
        else:
            
            return self.map[s][d]

    def path_weight(self, path):
        """
        calculate the weight of path
        return weight of path
        """
        #if path only contain 1 vertex 
        if len(path)==1:
            #self's weight is 0
            if path[0] not in self.map:
                raise IndexError
            else:
                return 0
        weights = 0
        #sum the weight from the first vertex to the last one 
        for i in range(len(path)-1):
            weights += self.arc_weight(path[i],path[i+1])
        return weights


    def does_path_exist(self, s, d):
        """
        determine if there's a path from vertex s to d
        return True if exists, False otherwise
        """
        if s not in self.map or d not in self.map:
            raise IndexError
        if s==d:
            return True
        
        item = s
        wait_set = set()
        list1 = [item]
        #while loop the list1
        while list1:
            item=list1.pop()
            #add item in wait_set 
            if item not in wait_set:
                wait_set.add(item)
                #check whether the self.map has item
                if item not in self.map:
                    return False
                for i in self.map[item]:
                    if i not in wait_set:
                        if i == d:
                            return True
                        else:
                            list1.append(i)
        

    def find_min_weight_path(self, s, d):
        """
        find the minimum weight from vertex s to d
        return min weight of path, raise IndexError if necessary
        """
        if s not in self.map or d not in self.map:
            raise IndexError
        if self.does_path_exist(s,d)==False:
            raise IndexError
        #all distance to be inf.
        dist = [math.inf] * self.order
        prev = [None] * self.order
        dist[s] = 0
        visit = set(range(self.order))
        nextnodes = set((0,))
        #check the nodes has been visited or not
        while visit:
            if nextnodes:
                cur = next(iter(sorted(nextnodes, key=lambda x: dist[x])))
                #if nextnode is not empty, remove the cur(node) from visit and nextnode
                visit.remove(cur)
                nextnodes.remove(cur)
            else:
                #if nextnodes is empty, the first element in the visit is cur(node)
                cur = visit.pop()
                
            #use the cur(node) we get to find the curdist from dist(it is is a distance)
            curdist = dist[cur]
            
            try:
            #use the cur(node) to get the vertex with its weight(dictionary) from self.map
                links = self.map[cur]
                #get the keys from the vertex's dictionary
                for nxt in links.keys() & visit:
                    tmpdist = links[nxt] + curdist
                    #check if the distance is larger than the previous one
                    if tmpdist < dist[nxt]:
                        dist[nxt] = tmpdist
                        prev[nxt] = cur
                        nextnodes.add(nxt)
            #if any keyerror appear, raise keyerror
            except KeyError:
                pass
        #get the distance from the dictionary map
        #if the distance is not inf, which means there exists a path between s and d
        #then find the path and return the path
        if dist[d] < math.inf:
            path = []
            tmp = d
            while tmp != s:
                path.insert(0, tmp)
                tmp = prev[tmp]
            path.insert(0, s)
            return path
        #if s and d are not connected, return a empty list
        else:
            return []
            
