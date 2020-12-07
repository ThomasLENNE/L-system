#L-SYSTEM DEFINITION
# Turtle orientation : H,U,L vectors (Heading, Up, Left)
# ^ : Left or Right around U
# & : pitch down or up around L
# | : roll left or right around H
# $ : force L to be horizontal (x,y,0)
# { : begin fill
# } : end fill
# ° : mark the turtle position


from math import *


ALPHABET=['A','B','C','F','G','L','!','^','&','$','|','[',']','{','}','°']
PARAMETERS=['l','w','t','s','r']

#leaf Constants
la=5 # initial length - main segment
ra=1.1 # growth rate - main segment
lb=1 # initial length - lateral segment
rb=1.3 # growth rate - lateral segment 
pd=1 # growth potential decrement 
b=40*pi/180


#tree constants
d1=94.74*pi/180 # divergence angle 1
d2=132.63*pi/180 # divergence angle 2
a=18.95*pi/180 # branching angle
lr=1.15 # elongation rate
vr=1.45 #width increase rate
c=45*pi/180 #leaf angle
#Tree Production
AXIOME_T='!(1.9)F(30)|(pi/4)A()L()'
PRODUCTION_T=['A():True→!(1.5*vr)F(30)[&(a)!(vr)F(20)A()$()[^(c)L()][^(-c)L()]L()]|(d1)[&(a)!(vr)F(20)A()$()[^(c)L()][^(-c)L()]L()]|(d2)[&(a)!(vr)F(20)A()$()[^(c)L()][^(-c)L()]L()]',
             'F(l):True→F(l*lr)',
             '!(w):True→!(w*vr)'
            ]

#Leaf Production
AXIOME_L='{°C(0)}'
PRODUCTION_L=['C(t):True→G(la,ra)[^(-a)B(t)°][C(t+1)][^(a)B(t)°]',
             'B(t):t>0→G(lb,rb)B(t-pd)',
             'G(s,r):True→G(s*r,r)'
            ]

#Productions
AXIOMES=[AXIOME_T,AXIOME_L]
PRODUCTIONS=[PRODUCTION_T,PRODUCTION_L]