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


ALPHABET=['A','B','C','F','G','X','!','^','&','$','|','[',']','{','}','°']
PARAMETERS=['l']

#Constants
gl=20
a=10*pi/180



#Productions
AXIOME='[X(36)A()]|(2*pi/5)[X(36)B()]'
PRODUCTION=['A():True→[&(a)G(gl)A(){°]°',
            'B():True→B()&(a)°G(gl)°}',
            'X(a):True→X(a+4.5)'
            ]

AXIOMES=[AXIOME,AXIOME]
PRODUCTIONS=[PRODUCTION,PRODUCTION]
