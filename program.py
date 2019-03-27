def hanoi_test(quantity,pile_from,pile_to,pile_aux)
    if quantity ==1:
        print "Mueve disco 1 de torre",pile_from," a torre ", pile_to
        return
    hanoi_test(quantity-1, pile_from,pile_aux,pile_to)
        print "Mueve disco ",quantity," de torre",pile_from," a torre ", pile_to
    hanoi_test(quantity-1, pile_aux,pile_to,pile_from)


    


