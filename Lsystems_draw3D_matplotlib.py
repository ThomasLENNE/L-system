# PARAMETRIC L-SYSTEM
# Based on Algorithmic Beauty Of Plants Book
# @author : Thomas LENNE
# branching  drawing3D script



from Lsystems_creation import *
from math import *
from random import *
from numpy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d  # for 3D

#rotations functions
def RU(a,hlu):
    '''rotate the turtle around U, by angle a
    parameters : a (angle in radians)
                 hlu (turtle orientation in a tuple of list)
    return : H,L,U, turtle orienation after rotation
    '''
    hlu=array([hlu[0],hlu[1],hlu[2]]).transpose()
    ru=array([(cos(a),sin(a),0),
              (-sin(a),cos(a),0),
              (0,0,1)]) #rotaton matrix around U
    hlu=dot(hlu,ru)
    H,L,U=hlu.transpose()[0],hlu.transpose()[1],hlu.transpose()[2]
    return list(H),list(L),list(U)

def RH(a,hlu):
    '''rotate the turtle around H, by angle a
    parameters : a (angle in radians)
                 hlu (turtle orientation in a tuple of list)
    return : H,L,U, turtle orienation after rotation
    '''
    hlu=array([hlu[0],hlu[1],hlu[2]]).transpose()
    rh=array([(1,0,0),
              (0,cos(a),-sin(a)),
              (0,sin(a),cos(a))]) #rotaton matrix around H
    hlu=dot(hlu,rh)
    H,L,U=hlu.transpose()[0],hlu.transpose()[1],hlu.transpose()[2]
    return list(H),list(L),list(U)

def RL(a,hlu):
    '''rotate the turtle around L, by angle a
    parameters : a (angle in radians)
                 hlu (turtle orientation in a tuple of list)
    return : H,L,U, turtle orientation after rotation
    '''
    hlu=array([hlu[0],hlu[1],hlu[2]]).transpose()
    rl=array([(cos(a),0,-sin(a)),
              (0,1,0),
              (sin(a),0,cos(a))]) #rotaton matrix around L
    hlu=dot(hlu,rl)
    H,L,U=hlu.transpose()[0],hlu.transpose()[1],hlu.transpose()[2]
    return list(H),list(L),list(U)


#translation (x,y,z) to (x',y',z')
def translate(xyz,l,h):
    '''translate a point m from l length with h vector
    parameters : xyz (tuple) coordinates before translation
                 l (float) lenght
                 h (list) translation heading vector
    return : x,y,z (tuple) coordinates after translation'''
    x=xyz[0] + l*h[0]
    y=xyz[1] + l*h[1]
    z=xyz[2] + l*h[2]

    return x,y,z

#keep turtle orientation
def L_horizontal(hlu):
    ''' keep L horizontal
    parameters : hlu (tuple of list) turtle orientation
    return H,L,U (tuple of list) : new turtle orientation'''
    H=hlu[0]
    [xh,yh,zh]=H
    V=[0,0,1]
    L=[-yh,-xh,0]
    U=[xh*zh,-zh*yh,-xh**2-yh**2]

    return H,L,U

#tropism
def normalize(vect):
    '''normalize a vector'''
    norm = linalg.norm(vect)
    if norm == 0: 
       return vect
    return vect / norm

def torque(hlu,t):
    ''' define torque h*t
    parameters : hlu (tuple of list) orientation
                 t (list) tropism vector
    return : torq (list) H*t
    '''
    H=hlu[0]
    [xh,yh,zh]=H
    [xt,yt,zt]=t
    torq=[yh*zt-zh*yt,zh*xt-xh*zt,xh*yt-yh*xt]

    return torq


def rotation(hlu,u,a):
    '''rotate the turtle vector around an axis by angle
    parameters : hlu (tuple of list) turtle orientation before rotation
                 u (list) axis vector
                 a(float) rotation angle in radians
    return  H,L,U (tuple of list) turtle orientation after rotation
    '''
    u=normalize(u)
    [ux,uy,uz]=u
    c=cos(a)
    s=sin(a)
    R=array([(ux**2*(1-c)+c,ux*uy*(1-c)-uz*s,ux*uz*(1-c)+uy*s),
            (ux*uy*(1-c)+uz*s,uy**2*(1-c)+c,uy*uz*(1-c)-ux*s),
            (ux*uz*(1-c)-uy*s,uy*uz*(1-c)+ux*s,uz**2*(1-c)+c)])
    
    [H,L,U]=hlu
    H=array(H)
    L=array(L)
    U=array(U)
    H=R.dot(H)
    L=R.dot(L)
    U=R.dot(U)
    return list(H),list(L),list(U)
    

def tropism(hlu,t):
    ''' define turtle orientation after tropism
    parameters : hlu (tuple of list) orientation without tropism
                 t (tuple) tropism vector
    return : H,L,U (tuple of list) orientation with tropism
    '''
    
    M=torque(hlu,t) # rotation axe
    alpha=linalg.norm(M) # rotation angle
    
    H,L,U = rotation(hlu,M,alpha)
    

    return H,L,U

#draw
def draw(words,alphabet):
    '''draw the 3d pattern according to alphabet
    parameters : patterns (string list), alphabet (list of strings)
    '''
    #environment
    sigma=pi/16#standard variation of rotation angle
    T=[0,0,-0.5] #tropism vector
    e=0.5 # susceptibility to bending
    T=list(e*array(T))
    
    #init coordinates
    xyz=(0,0,0) 
    x,y,z=xyz
    
    #init orientation
    teta=pi/6
    HLU=([0,0,1],[-sin(teta),-cos(teta),0],[-cos(teta),sin(teta),0])
    stack=[] # to memorize the turtle state
    # polygon=[] #coordinates for surface
    
    modules_t=word_to_modules(words[0], alphabet) #tree modules

    #init matplotlib
    X,Y,Z=[x],[y],[z] #matplotlib current tabs
    LINEWIDTH=1
    LINES=[] #Lines to draw
    
    
    for module in modules_t :
        if module[0]=='F':
            H=HLU[0]
            xyz=translate(xyz,eval(parameters(module)[0]),H)
            x,y,z=xyz
            X.append(x)
            Y.append(y)
            Z.append(z)
            HLU=tropism(HLU,T)
            
        elif module[0]=='^':
            angle=eval(parameters(module)[0])
            HLU=RU(gauss(angle,sigma),HLU)
        
        elif module[0]=='&':
            angle=eval(parameters(module)[0])
            HLU=RL(gauss(angle,sigma),HLU)
        
        elif module[0]=='|':
            angle=eval(parameters(module)[0])
            HLU=RH(gauss(angle,sigma),HLU)

        elif module[0]=='[':
            stack.append((xyz,HLU))
            LINES.append([(X,Y,Z),LINEWIDTH])
            x,y,z=xyz
            X,Y,Z=[x],[y],[z]
        
        elif module[0]==']':
            xyz=stack[-1][0]
            HLU=stack[-1][1]
            stack=stack[:-1]
            LINES.append([(X,Y,Z),LINEWIDTH])
            x,y,z=xyz
            X,Y,Z=[x],[y],[z]
        
        elif module[0]=='!':
            LINEWIDTH=eval(parameters(module)[0])

        elif module[0]=='$':
            HLU=L_horizontal(HLU)
        
        if module[0]=='G':
            H=HLU[0]
            xyz=translate(xyz,eval(parameters(module)[0]),H)
            x,y,z=xyz
            X.append(x)
            Y.append(y)
            Z.append(z)
    
        
    #plotting
    fig = plt.figure()
    ax = fig.gca(projection='3d')  # 3D display
    for line in LINES:
        X,Y,Z=line[0]
        LINEWIDTH=line[1]
        ax.plot(X, Y, Z, 'k',linewidth=LINEWIDTH)  # Drawing 
    #plt.axis('off')
    plt.show()


N=10 #steps
AXIOME_T,AXIOME_L=AXIOMES
PRODUCTION_T,PRODUCTION_L=PRODUCTIONS
PATTERNS=[parametric_word(AXIOME_T,PRODUCTION_T,ALPHABET,N),parametric_word(AXIOME_L,PRODUCTION_L,ALPHABET,N+4)] 
#print(PATTERNS)

draw(PATTERNS, ALPHABET)  

