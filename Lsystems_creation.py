# PARAMETRIC L-SYSTEM
# ABOP chapter 1
# @author : Thomas LENNE
# branching string creation script

from math import *

#examples
from example_1_monopodial import *
#from example_2_sympodial import *
#from example_3_ternary import *
#from example_4_leaf import *
#from example_5_tree_leaf import *
#from example_6_cordate_leaf import *
#from example_7_lily import *


#Split
def split_production(production):
    '''split production
    parameter : a production (string)
    return : list with three strings
    - predecessor
    - condition
    - successor '''
    predecessor=production.split(':')[0]
    condition=production.split(':')[1].split('→')[0]
    successor=production.split(':')[1].split('→')[1]
    
    return [predecessor, condition,successor]


#convert word to modules
def word_to_modules(word,alphabet):
    '''split a parametric word to 
    a list of string modules according 
    the content of alphabet'''
    modules=[]
    module=''
    for character in word:
        if character in alphabet :
            modules.append(module)
            module=character
        else :
            if character not in ['[',']','{','}','°']:
                module=module + character
    modules.append(module) #append last module
    modules=modules[1:]
    
    return modules
        

#number of parameters in a module
def n_parameters(module):
    '''return the number of parameters
    in a module(actual or formal)
    parameter: module (string)
    return : integer'''
    n=0
    for car in module:
        if car==',':
            n=n+1
    if '()' in module:
        return 0
    else:
        return n+1
    

#parameters in a module
def parameters(module):
    '''list of modules's parameters'''
    param=''
    if module not in ['[',']','{','}','°']:
        param=module.split('(')[1].split(')')[0].split(',')
    return param


#matching modules
def match(actual,production):
    '''Return True if modules match, else False
    Parameters : actual module, production (strings)
    return : boolean'''
    [predecessor,condition,successor]=split_production(production)
    if predecessor[0]==actual[0]  and n_parameters(predecessor)==n_parameters(actual) :
        for i in range(n_parameters(actual)):
            exec(parameters(predecessor)[i] + '=' + parameters(actual)[i])
        if eval(condition)==True:
            return True
    return False


#apply production to a matching module
def apply(module,production,alphabet):
    '''parameters : module( a matching module) , production (strings)
       return : result, a parametric word (string)'''
    [predecessor,condition,successor]=split_production(production)
    result=''
    for i in range(n_parameters(module)):
            exec(parameters(predecessor)[i] + '=' + parameters(module)[i])
    successor_modules = word_to_modules(successor,alphabet) #modules in the successor
    for module in successor_modules:
        if module in ['[',']','{','}','°']:
            actual=module
        else:
            actual=module[0]+'('
            for parameter in parameters(module):
                if parameter !='':
                    actual=actual+str(eval(parameter))+','
            if actual[-1]==',':
                actual=actual[:-1] #delete last comma
            actual=actual + ')'
        result=result+ actual
    
    return result


#next word after productions
def next(word,productions,alphabet):
    '''apply production to a parametric word if conditions are met
    parameters : word (string), productions(list of strings)
    return : a parametric word(string)'''
    modules=word_to_modules(word,alphabet)
    result=''
    for module in modules :
        i=0
        for production in productions:
            if match(module,production):
                result=result+apply(module,production,alphabet)
                i=i+1
        if i==0 or module in ['[',']','{','}','°']:
                result=result+module
        
    return result



# parametric word after n steps
def parametric_word(axiome,productions,alphabet,n):
    '''write the parametric word after n steps of productions'
    parameters : axiome(string),productions(list of strings),
                 alphabet (list of strings)
                 n (integer)
    return : word, a paramtric word (string)
    '''
    word = axiome
    for i in range(n):
        word=next(word,productions,alphabet)
    return word


