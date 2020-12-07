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
PARAMETERS=['l']

#Constants

a=20*pi/180 #angle
lg=15 #ax length



#Productions
AXIOME='[A(lg)][B(lg)]'
PRODUCTION=['A(l):True→[^(a)A(lg){°]°C(lg)°}',
            'B(l):True→[^(-a)B(lg){°]°C(lg)°}',
             'C(l):True→G(lg)C(lg)'
            ]

AXIOMES=[AXIOME,AXIOME]
PRODUCTIONS=[PRODUCTION,PRODUCTION]

