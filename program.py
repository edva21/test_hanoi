def hanoi_test( quantity, pile_from, pile_to, pile_aux):
    if quantity ==1:
        print ("Mueve disco 1 de torre",pile_from," a torre ", pile_to)
        return
    hanoi_test(quantity-1, pile_from,pile_aux,pile_to)
    print ("Mueve disco ",quantity," de torre",pile_from," a torre ", pile_to)
    hanoi_test(quantity-1, pile_aux,pile_to,pile_from)

def hanoi_test2( quantity, pile_from, pile_to, pile_aux):
    if quantity ==1:
        pile_to.append(pile_from.pop())
        return
    hanoi_test(quantity-1, pile_from,pile_aux,pile_to)
    pile_to.append(pile_from.pop())
    hanoi_test(quantity-1, pile_aux,pile_to,pile_from)


    
if __name__ == '__main__':
    #hanoi_test(4,'Borigen','Bdestino','Bintermedia')
    Borigen=[4,3,2,1]
    Bdestino=[]
    Bintermedia=[]
    hanoi_test2(4,Borigen,Bdestino,Bintermedia)
    print (Borigen)
    print (Bdestino)
    print (Bintermedia)


