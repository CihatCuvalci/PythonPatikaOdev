l = [[1, 2], [3, 4], [5, 6, 7]]
for i in range(len(l)):
        if type(l[i]) == type([]):
            l[i].reverse()
        
l.reverse()
print(l)
