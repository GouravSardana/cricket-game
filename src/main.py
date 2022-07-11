from over import Over

def main():
    no_of_players = int(input("Enter No. of players for each team: "))
    no_of_overs = int(input("No. of overs: "))
    team1_scored = 0
    for team in range(1, 3):
        print()
        print("Batting Order for team " + str(team) + " : ")
        batting_order = []
        for input_player in range(no_of_players):
            batting_order.append(input())
        

        over_object = Over(no_of_overs, batting_order, team, team1_scored)
        total_score, team2_wins, wickets, all_out = over_object.start_the_over()
        if team == 1:
            team1_scored = total_score
            print("Team 2 needs " + str(team1_scored + 1) + " to win")
        elif team == 2:
            if team2_wins:
                print("Team 2 wins by " + str(len(batting_order) - wickets) + " wickets")
        

if __name__ == "__main__":
    main()