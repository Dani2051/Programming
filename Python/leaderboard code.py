def leaderboard(score1,score2,user1,user2):
        
    winner = ''
    
    #######FINGING HIGEST SCORE IN CURRENT MATCH########

    if score1 > score2:
        highestscore = score1
        winner = (user1)
        loser = (user2)
    elif score1 < score2:
        highestscore = score2
        winner = (user2)
        loser = (user1)

    highest1 = open('Highest Score1.txt','w')
    highest2 = open('Highest Score2.txt','w')
    highest3 = open('Highest Score3.txt','w')
    highest4 = open('Highest Score4.txt','w')
    highest5 = open('Highest Score5.txt','w')
    if highest1 != '':
        if int(highestscore) >= int(highest1):
            edit_board(highestscore,winner,loser,highest1,highest_n1,highest_opp1,highest2,highest_n2,highest_opp2,highest3,highest_n3,highest_opp3,highest4,highest_n4,highest_opp4)
    elif highest2 != '':
        if int(highestscore) >= int(highest2):
            edit_board(highest1,highest_n1,highest_opp1,highestscore,winner,loser,highest2,highest_n2,highest_opp2,highest3,highest_n3,highest_opp3,highest4,highest_n4,highest_opp4)
    elif highest3 != '':
        if int(highestscore) >= int(highest3):
            edit_board(highest1,highest_n1,highest_opp1,highest2,highest_n2,highest_opp2,highestscore,winner,loser,highest3,highest_n3,highest_opp3,highest4,highest_n4,highest_opp4)
    elif highest4 != '':
        if int(highestscore) >= int(highest4):
            edit_board(highest1,highest_n1,highest_opp1,highest2,highest_n2,highest_opp2,highest3,highest_n3,highest_opp3,highestscore,winner,loser,highest4,highest_n4,highest_opp4)
    elif highest5 != '':
        if int(highestscore) >= int(highest5):
           edit_board(highest1,highest_n1,highest_opp1,highest2,highest_n2,highest_opp2,highest3,highest_n3,highest_opp3,highest4,highest_n4,highest_opp4,highestscore,winner,loser,)
