def tri_selection (tab):
 for i in range(len(tab)):
    min=i
    for j in range (i+1,len(tab)):
        if tab[j]<tab[min]:
            min=j

    temp=tab[i]
    tab[i]=tab[min]
    tab[min]=temp
    return tab
tab=[5,8,9,23,56] #un tableau aleatoire à titre d'exemple
tri_selection(tab)
print ("le tableau trié est:")
for i in range (len(tab)):
    print("%d"%tab[i])


