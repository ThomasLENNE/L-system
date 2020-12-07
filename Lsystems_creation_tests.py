from Lsystems_creation import *
from example_0 import *


#test split
print(split_production(PRODUCTIONS[0]))

#test word_to_modules
print(word_to_modules(AXIOME,ALPHABET)) #word with actual modules
print(word_to_modules(split_production(PRODUCTIONS[1])[2],ALPHABET)) #word with formal modules

#test n_parameters
#actual modules
print(n_parameters('B(2)'))
print(n_parameters('A(4,4)'))
#formal modules
print(n_parameters('B(x)'))
print(n_parameters('A(x,y)'))
print(n_parameters('C()'))

#test parameters
#actual modules
print(parameters('B(2)'))
print(parameters('A(4,4'))
#formal modules
print(parameters('B(x)'))
print(parameters('A(x,y'))
print(parameters('A(x/y,0)'))

#test match
print(match('A(4,4)', PRODUCTIONS[0])) #False
print(match('B(2)', PRODUCTIONS[0])) # False
print(match('A(4,4)', PRODUCTIONS[1])) # True
print(match('B(2)', PRODUCTIONS[2])) # False
print(match('B(2)', PRODUCTIONS[3])) # True

#test apply
print(apply('A(4,4)', PRODUCTIONS[1],ALPHABET))
print(apply('B(2)',PRODUCTIONS[3],ALPHABET))

#test next word
print(next(AXIOME,PRODUCTIONS,ALPHABET))

# test parametric_word
print(parametric_word(AXIOME,PRODUCTIONS,ALPHABET,4))