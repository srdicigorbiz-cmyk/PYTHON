def printCard(l_ranks, l_input_suit):
    suits = {
        "club":"♣", 
        "diamond":"♦", 
        "heart":"♥", 
        "spade":"♠"
        }
    top =    "╔═════════╗"
    body =   "║         ║"
    bottom = "╚═════════╝"
    rank = []
    suit = []
    for r in l_ranks:
        if r == 1:
            rank.append("A")
        elif 2 <= r <= 10:
            rank.append(r)
        elif r == 11:
            rank.append("J")
        elif r == 12:
            rank.append("Q")
        elif r == 13:
            rank.append("K")
        elif r > 13 or r == 0:
            rank.append(" ")
    for s in l_input_suit:
        if s in suits:
            suit.append(suits[s])
        else:
            suit.append(" ")
    
    # CARD
    # configuring card
    cb_top = []
    cb_body = []
    cb_1_rank = []
    cb_2_suit = []
    cb_3_rank = []
    cb_bottom = []
    
    for r in rank:
        cb_top.append(top)
        cb_body.append(body)
        cb_bottom.append(bottom)
    for r in rank:
        if r == 10:
            cb_1_rank.append(f"║ {r}      ║")
        else: 
            cb_1_rank.append(f"║ {r}       ║")
    
    for s in suit:
        cb_2_suit.append(f"║    {s}    ║")
    
    for r in rank:
        if r == 10:
            cb_3_rank.append(f"║      {r} ║")
        else:
            cb_3_rank.append(f"║       {r} ║")

    #PRINT
    for i in range(9):
        if i == 0:
            print(" ".join(cb_top))
        elif i == 1:
            print(" ".join(cb_1_rank))
        elif i == 4:
            print(" ".join(cb_2_suit))
        elif i == 7:
            print(" ".join(cb_3_rank))
        elif i == 8:
            print(" ".join(cb_bottom))
        else:
            print(" ".join(cb_body))
    
 

    
printCard([32, 2, 10],["null", "heart", "club"])