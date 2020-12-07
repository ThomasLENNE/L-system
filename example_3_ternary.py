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
d1=94.74*pi/180 # divergence angle 1
d2=132.63*pi/180 # divergence angle 2
a=18.95*pi/180 # branching angle
lr=1.15 # elongation rate
vr=1.45 #width increase rate

#Production
AXIOME='!(1.9)F(40)|(pi/4)A()'
PRODUCTION=['A():True→!(1.5*vr)F(30)[&(a)!(vr)F(20)A()$()]|(d1)[&(a)!(vr)F(20)A()$()]|(d2)[&(a)!(vr)F(20)A()$()]',
             'F(l):True→F(l*lr)',
             '!(w):True→!(w*vr)'
            ]

AXIOMES=[AXIOME,AXIOME]
PRODUCTIONS=[PRODUCTION,PRODUCTION]