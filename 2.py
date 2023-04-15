from collections import Counter
dictionary_of_symbol_price = {'AEIOULNSTRАВЕИНОРСТ':1, 'DGДКЛМПУ':2, 'BCMPБГЁЬЯ':3, 'FHVWYЙЫ':4, 'KЖЗХЦЧ':5, 'JXШЭЮ':8, 'QZФЩЪ':10} 
print("Please input a world that you want:")
world = dict(Counter(input()))
result = 0
for i,j in world.items():
    for x,y in dictionary_of_symbol_price.items():
        if i in x:
            result += y*j
            break
print(result)