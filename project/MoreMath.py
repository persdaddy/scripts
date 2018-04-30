import numpy as np
class uid:
    def __init__(self):
        nextVal = 0
        self.uid = nextVal
        nextVal += 1

class vertex(uid):
    def __init__(self,loc):
        #print type(loc),type(np.ndarray)
        if isinstance(loc, np.ndarray):
            self.pos = loc
        elif len(loc) == 3: #isinstance(loc,'list')
            self.pos = np.array(loc,dtype=float)
            
    def __str__(self):
        return str((self.pos[0],self.pos[1],self.pos[2]))

    def __sub__(self,other):
        return np.subtract(self.pos,other.pos)
                    
    def __eq__(self, other): 
        return np.array_equal(self.pos,other.pos)

    def coincident(self, other, tol=1e-2):
        test = np.isClose(self.pos,other.pos,rtol=tol)
        return (test[0] and test[0])

    def distanceToVertex(self, other):
        return np.linalg.norm(self.pos-other.pos)

class edge:
    def __init__(self,vertexA, vertexB):
        self.vertexA = vertexA
        self.vertexB = vertexB

    def __str__(self):
        return str(self.vertexA) + "," + str(self.vertexB)
        
    def __eq__(self, other):
        A = (self.vertexA == other.vertexA) or (self.vertexA == other.vertexB)
        B = (self.vertexB == other.vertexA) or (self.vertexB == other.vertexB)
        return (A and B)

    def getLength(self):
        return self.vertexA.distanceToVertex(self.vertexB)
                
    def vertexInEdge(self,vertex,tol=0.00):
        AB = self.vertexA.distanceToVertex(self.vertexB)
        AV = self.vertexA.distanceToVertex(vertex)
        VB = vertex.distanceToVertex(self.vertexB)
        #print AB,AV,VB,AV+VB
        return AB == AV + VB

    def intersectEdge(self,other):
        '''
        L1 = P1 + a V1
        L2 = P2 + b V2
        a (V1 X V2) = (P2 - P1) X V2
        If the lines intersect at a single point, then the resultant vectors 
        on each side of this equation must be parallel, and the left side must 
        not be the zero vector. We should check to make sure that this is 
        true. Once we have checked this, we can solve for 'a' by taking the 
        magnitude of each side and dividing. If the resultant vectors are 
        parallel, but in opposite directions, then 'a' is the negative of the 
        ratio of magnitudes. Once we have 'a' we can go back to the equation 
        for L1 to find the intersection point.
        '''
        da = self.vertexB-self.vertexA
        db = other.vertexB-other.vertexA
        dp =  other.vertexA -self.vertexA
                
        #Left and right side must be parallel, test this cos theta = (dVa * dVb)/(mag_da*mag_db)
        left = np.cross(da,db)
        mag_left = np.linalg.norm(left)
        right = np.cross(dp,db)
        mag_right = np.linalg.norm(right)
        angleBtwn = np.arccos(np.dot(left,right)/(mag_left*mag_right))
        
        if angleBtwn == 0.0 or angleBtwn == np.pi:
            print "Lines will intersect"
            a = mag_right/mag_left
            intPt = self.vertexA.pos + (a * da)
        else:
            print "Never intersect"
        return None
class orderEdgeLoop:
    def __init__(self,edgeLoop=[]):
        self.edgeLoop = edgeLoop
        self.valid = self.isLoop()
        
    def insertEdgeAfterIndex(self,edge,after=None):
        '''Given an edge, index to insert after'''        
        v1N = edge.vertexA
        v2N = edge.vertexB
        if not after == None:
            nextIndex = self.wrapAroundIndex(after,1)
            if (
                    v1N == self.edgeLoop[after].vertexB and 
                    v2N == self.edgeLoop[nextIndex].vertexA
                ):
                #Insert edge into loop
                self.edgeLoop.insert(edge,after)
   
    def isLoop(self):
        '''Verify that the loop is valid'''
        if len(self.edgeLoop) == 0:
            return False
        else:
            for i,edge in enumerate(self.edgeLooap):
                vEnd = edge.vertexA
                vNext = edge[self.wrapAroundIndex(i,1)].vertexA
                if not vEnd == vNext:
                    return False       
            return True

    def findEdge(self,edge):
        for i,_edge in enumerate(self.edgeLoop):
            if _edge == edge:
                return i
        return None
            
    def next(self,edge):
        for i,_edge in enumerate(self.edgeLoop):
            if _edge == edge:
                return wrapAroundIndex(i,1)
        return None
                        
    def wrapAroundIndex(self,i,loc):
        return (i+loc) % len(self.edgeLoop)

class face:
    '''A face'''
    def __init__(self,edgeLoop=None,name=None):
        self.uid = 1
        self.name = name
        self.edgeLoop = edgeLoop

    def teselateFace(self):
        pass

    def normal(self):
        return np.array([1,0,0])

class mesh:
    def __init__(self,name):
        self.name = name

    def addFace(self):
        pass

    def ifClosed(self):
        return True

    def findVolume(self):
        if isClosed():
            return 9000.0

if __name__ == '__main__':
    #Test all functions
    #Vertex Tests
    #v0 = vertex([0,0,0])
    #v1 = vertex([0,0,0])
    #v2 = vertex([0.0,0.0,0.0])
    #v3 = vertex([0,0,10])
    #v4 = vertex([1e-12,0,0])           
    #print "Testing equivilency test for %s" %(v0)
    #print "  %s: Expect True, Recieved %s" %(v1,v0==v1)
    #print "  %s: Expect True, Recieved %s" %(v2,v0==v2)
    #print "  %s: Expect False, Recieved %s" %(v3,v0==v4)
    #print "  %s: Expect False, Recieved %s" %(v4,v0==v4)
    

    v0 = vertex([0,0,0])
    v1 = vertex([0,0,10])
    #v2 = vertex([1,0,0])
    #v3 = vertex([1,0,5])    
    v2 = vertex([-10,0,0])
    v3 = vertex([10,0,8])    
    edge1 = edge(v0,v1)
    edge2 = edge(v2,v3)
    print "Testing edge intersection %s and %s" %(edge1,edge2)    
    print "-->%s" %(edge1.intersectEdge(edge2))
    #print "-->%s" %(edge2.intersectEdge(edge1))