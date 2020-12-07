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


ALPHABET=['A','B','C','F','G','!','^','&','$','|','[',']','{','}','°']
PARAMETERS=['t','s','r']

#Constants
la=5 # initial length - main segment
ra=1.1 # growth rate - main segment
lb=1 # initial length - lateral segment
rb=1.3 # growth rate - lateral segment 
pd=1 # growth potential decrement 
a=40*pi/180

#Productions
AXIOME='{°C(0)}'
PRODUCTION=['C(t):True→G(la,ra)[^(-a)B(t)°][C(t+1)][^(a)B(t)°]',
             'B(t):t>0→G(lb,rb)B(t-pd)',
             'G(s,r):True→G(s*r,r)'
            ]

AXIOMES=[AXIOME,AXIOME]
PRODUCTIONS=[PRODUCTION,PRODUCTION]