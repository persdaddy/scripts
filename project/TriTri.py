import math
import itertools

A = [0,0,0]
B = [0,0,2]
C = [0,0,5]
D = [0,0,10]
E = [0,10,0.0]
F = [0,5,0]

d = {'A':A,'B':B,'C':C,'D':D,'E':E,'F':F}
loop = ['A','B','C','D','E','F']

def ptInSeg(P1,P2,PTest,tolerance=1e-5):
    x0,y0,z0 = P1
    x1,y1,z1 = P2
    xt,yt,zt = PTest

    P1P2 = math.sqrt((x1-x0)*(x1-x0) + (y1-y0)*(y1-y0) + (z1-z0)*(z1-z0))
    P1PTest = math.sqrt((xt-x0)*(xt-x0) + (yt-y0)*(yt-y0) + (zt-z0)*(zt-z0))
    PTestP2 = math.sqrt((x1-xt)*(x1-xt) + (y1-yt)*(y1-yt) + (z1-zt)*(z1-zt))
    diff = abs(P1P2 - (P1PTest + PTestP2))
    return ( diff <= tolerance )

def itemsBtwn(l,start,end):
    #print("Id:",start,end)
    lreturn = []
    i = (start + 1) % len(l)
    while i != end:
        #print('#',i)
        lreturn.append(l[i])
        i = (i + 1) % len(l)
    return lreturn
    
triangles = len(loop) - 2
numbPts = len(loop)
i = 0
A = loop[i]
t = []
while triangles > 0:
    Bindex = ( i+ 1 ) % numbPts
    Cindex = (i + 2 ) % numbPts
    B = loop[Bindex]
    C = loop[Cindex]
    #print('{} {} {}'.format(A, B, C))
    ptA = d[A]
    ptB = d[B]
    ptC = d[C]
    if ptInSeg(ptA,ptC,ptB):
        #print("Straight line")
        A = B
        i += 1
    else:
        ptsBtwn = itemsBtwn(loop,Cindex,i) 
        #print("Btwn:",ptsBtwn)
        for p in ptsBtwn:
            ptp = d[p]
            if ptInSeg(ptA,ptC,ptp):
                #print("Straight line $")
                A = B
                i += 1
                break
            else:
                #print("Approve")
                triangles -= 1
                t.append((A,B,C))
                i = Bindex
                break
                
for s in t:
    print(s)