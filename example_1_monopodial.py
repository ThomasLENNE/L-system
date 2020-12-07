#L-SYSTEM DEFINITION
# Turtle orientation : H,U,L vectors (Heading, Up, Left)
# ^ : Left or Right around U
# & : pitch down or up around L
# | : roll left or right around H
# $ : force L to be horizontal (x,y,0)


from math import *


ALPHABET=['A','B','C','F','!','^','&','$','|','[',']']
PARAMETERS=['l','w']

#Constants
r1=0.9
r2=0.6
a0=pi/4
a2=pi/4
d=137.5*pi/180
wr=0.707

#Productions
AXIOME='A(75,15)'
PRODUCTION=['A(l,w):True→!(w)F(l)[&(a0)B(l*r2,w*wr)]|(d)A(l*r1,w*wr)',
             'B(l,w):True→!(w)F(l)[^(-a2)$()C(l*r2,w*wr)]C(l*r1,w*wr)',
             'C(l,w):True→!(w)F(l)[^(a2)$()B(l*r2,w*wr)]B(l*r1,w*wr)'
]

AXIOMES=[AXIOME,AXIOME]
PRODUCTIONS=[PRODUCTION,PRODUCTION]