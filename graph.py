from heapq import *
class node:
    def __init__(self,id):
        self.id = id
        self.neighs = []
        self.dist = -1

def shortestPath(source, dest, ):
    h = []
    s = source
    s.dist = 0
    heappush(h, [0, s])
    while h:
        s = heappop(h)[1]
        for v in s.neighs:
            if v.dist == -1 or s.dist + 1 < v.dist :
                v.dist = s.dist+1
                heappush(h, [v.dist, v])
        if (s == dest):
            break
    
    return  dest.dist

def stuck(src, dest , visited):
    if src == dest:
        return False
    for y in src.neighs:       
        if y not in visited:
            visited.add(y)
            if  not stuck(y, dest, visited):
                return False
    return True

def allPaths(src, dest, path):
    if src == dest:
        print path
    visited = set(path)
    if stuck(src, dest, visited):
        return
    for v in src.neighs:
        path.append(v)
        allPaths(v, dest, path )
        path.pop()
    
def createG():
    a = node('A')
    b = node('B')
    c = node('C')
    d = node('D')
    e = node('E')
    f = node('F')
    g = node('G')
    h = node('H')
    a.neighs.extend([b,d,h])
    b.neighs.extend([c,d,a])
    c.neighs.extend([b,d,f])
    d.neighs.extend([a,b,c,e])
    e.neighs.extend([f,d,h])
    f.neighs.extend([c,e,g])
    g.neighs.extend([f,h])
    h.neighs.extend([a,e,g])
    return (a,h)

if __name__ == "__main__":
    src, dest = createG()
    print (shortestPath(src, dest))
    #allPaths(src, dest, [src, ])
