class Scorecard:

    def __init__(self, batting_order, over, runs_per_player, next_batsman_index, striker, striker_runs, non_striker,
                 non_striker_runs, extras, is_non_striker_batting,
                 no_of_four_per_player, no_of_six_per_player, ball_faced_per_player, total_score, team1_scored,
                 team2_win, team, all_out):
        self.batting_order = batting_order
        self.over = over
        self.runs_per_player = runs_per_player
        self.next_batsman_index = next_batsman_index
        self.striker = striker
        self.striker_runs = striker_runs
        self.non_striker = non_striker
        self.non_striker_runs = non_striker_runs
        self.extras = extras
        self.is_non_striker_batting = is_non_striker_batting
        self.no_of_four_per_player = no_of_four_per_player
        self.no_of_six_per_player = no_of_six_per_player
        self.ball_faced_per_player = ball_faced_per_player
        self.total_score = total_score
        self.team1_scored = team1_scored
        self.team2_win = team2_win
        self.team = team
        self.all_out = all_out

    def score_card_per_over(self):
        runs_per_player, next_batsman_index, striker, striker_runs, non_striker, non_striker_runs, extras, \
        is_non_striker_batting, no_of_four_per_player, no_of_six_per_player, ball_faced_per_player, total_score, \
        team2_win, team, all_out = self.add_runs_and_display_scorecard(
            self.over, self.striker, self.non_striker, self.is_non_striker_batting,
            self.striker_runs, self.non_striker_runs, self.next_batsman_index, self.batting_order, self.runs_per_player,
            self.extras,
            self.no_of_four_per_player, self.no_of_six_per_player, self.ball_faced_per_player, self.total_score,
            self.team1_scored, self.team2_win, self.team, self.all_out)

        return runs_per_player, next_batsman_index, striker, striker_runs, non_striker, non_striker_runs, extras, \
               is_non_striker_batting, no_of_four_per_player, no_of_six_per_player, ball_faced_per_player, \
               total_score, team2_win, team, all_out

    def add_runs_and_display_scorecard(self, over, striker, non_striker, is_non_striker_batting, striker_runs,
                                       non_striker_runs, next_batsman_index, batting_order, runs_per_player, extras,
                                       no_of_four_per_player, no_of_six_per_player, ball_faced_per_player, total_score,
                                       team1_scored, team2_win, team, all_out):
        for runs in over:
            print("Striker", striker)
            print("Non striker", non_striker)
            if runs.isdigit():
                runs = int(runs)
                total_score += runs
                if total_score > team1_scored and team == 2:

                    if runs == 1 or runs == 2 or runs == 3:
                        if is_non_striker_batting:
                            non_striker_runs += runs
                            if non_striker not in ball_faced_per_player:
                                ball_faced_per_player[non_striker] = 1
                            else:
                                ball_faced_per_player[non_striker] += 1
                        else:
                            striker_runs += runs
                            if striker not in ball_faced_per_player:
                                ball_faced_per_player[striker] = 1
                            else:
                                ball_faced_per_player[striker] += 1
                        if runs % 2 == 1:
                            is_non_striker_batting = not is_non_striker_batting

                    runs_per_player[striker] = striker_runs
                    runs_per_player[non_striker] = non_striker_runs
                    team2_win = True
                    # self.add_boundaries_sixes_ball_faced_to_player_dict(ball_faced_per_player, 1, striker)
                    if runs == 4:
                        self.add_boundaries_sixes_ball_faced_to_player_dict(no_of_four_per_player, 4, striker)
                    elif runs == 6:
                        self.add_boundaries_sixes_ball_faced_to_player_dict(no_of_six_per_player, 6, striker)

                    return runs_per_player, next_batsman_index, striker, striker_runs, non_striker, non_striker_runs, \
                           extras, is_non_striker_batting, no_of_four_per_player, no_of_six_per_player, \
                           ball_faced_per_player, total_score, team2_win, team, all_out
                
                who_scored = non_striker if is_non_striker_batting else striker
                self.add_boundaries_sixes_ball_faced_to_player_dict(ball_faced_per_player, 1, who_scored)
            if runs == 1 or runs == 2 or runs == 3 or runs == 5:
                if is_non_striker_batting:
                    non_striker_runs += runs
                    # self.add_boundaries_sixes_ball_faced_to_player_dict(ball_faced_per_player, 1, non_striker)
                else:
                    striker_runs += runs
                    # self.add_boundaries_sixes_ball_faced_to_player_dict(ball_faced_per_player, 1, striker)
                if runs == 1 or runs == 3 or runs == 5:
                    is_non_striker_batting = not is_non_striker_batting
            elif runs == 4 or runs == 6:
                # who_scored = non_striker if is_non_striker_batting else striker
                # self.add_boundaries_sixes_ball_faced_to_player_dict(ball_faced_per_player, 1, who_scored)
                if runs == 4:
                    four_or_six = no_of_four_per_player
                else:
                    four_or_six = no_of_six_per_player

                if is_non_striker_batting:
                    self.add_boundaries_sixes_ball_faced_to_player_dict(four_or_six, "4/6", non_striker)
                    non_striker_runs += runs
                else:
                    striker_runs += runs
                    self.add_boundaries_sixes_ball_faced_to_player_dict(four_or_six, "4/6", striker)
            elif runs == "w" or runs == "W":
                if (len(batting_order) - 1) < next_batsman_index:
                    print("No More Batsman Available")
                    runs_per_player[striker] = striker_runs
                    return runs_per_player, next_batsman_index, striker, striker_runs, non_striker, non_striker_runs, \
                           extras, is_non_striker_batting, no_of_four_per_player, no_of_six_per_player, \
                           ball_faced_per_player, total_score, team2_win, team, all_out
                
                who_scored = non_striker if is_non_striker_batting else striker
                self.add_boundaries_sixes_ball_faced_to_player_dict(ball_faced_per_player, 1, who_scored)
                
                runs_per_player[striker] = striker_runs
                striker_runs = 0
                striker = batting_order[next_batsman_index]
                next_batsman_index += 1
            elif runs == "Wd" or runs == "wd" or runs == "nb" or runs == "Nb":
                extras += 1

        runs_per_player[striker] = striker_runs
        runs_per_player[non_striker] = non_striker_runs

        return runs_per_player, next_batsman_index, striker, striker_runs, non_striker, non_striker_runs, \
               extras, is_non_striker_batting, no_of_four_per_player, no_of_six_per_player, ball_faced_per_player, \
               total_score, team2_win, team, all_out

    @staticmethod
    def add_boundaries_sixes_ball_faced_to_player_dict(runs_dict, run_scored, who_scored):
        if who_scored in runs_dict:
            runs_dict[who_scored] += 1
        else:
            runs_dict[who_scored] = 1
