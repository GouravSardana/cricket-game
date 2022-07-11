from prettytable import PrettyTable

from scorecard import Scorecard


class Over:
    def __init__(self, no_of_overs, batting_order, team, team1_scored):
        self.no_of_overs = no_of_overs
        self.batting_order = batting_order
        self.team = team
        self.team1_scored = team1_scored

    def start_the_over(self):

        # base case
        if len(self.batting_order) < 2:
            print("There must be more than 2 players for batting. Cancelling the match...")
            return

        runs_per_player = {}
        next_batsman_index = 2
        striker = self.batting_order[0]
        striker_runs = 0
        non_striker = self.batting_order[1]
        non_striker_runs = 0
        extras = 0
        is_non_striker_batting = False
        wickets = 0
        no_of_four_per_player = {}
        no_of_six_per_player = {}
        ball_faced_per_player = {}
        total_score = 0
        team2_win = False
        all_out = False
        scored_per_team = 0

        for over in range(1, self.no_of_overs + 1):
            ball_count = 1
            over_arr = []
            print("Over " + str(over) + ": ")
            while ball_count <= 6:
                # base case
                # there must be two players for batting
                if wickets > len(self.batting_order) - 2:
                    print("No more players available for batting. It seems to be All OUT")
                    all_out = True
                    break
                if self.team == 2 and scored_per_team > self.team1_scored:
                    break
                ball = input()
                if ball == "Wd" or ball == "wd" or ball == "Nb" or ball == "nb":
                    scored_per_team += 1
                    over_arr.append(ball)
                    continue
                elif ball == "W" or ball == "w":
                    wickets += 1
                    over_arr.append(ball)
                    ball_count += 1
                elif ball.isdigit():
                    if int(ball) > 6:
                        print(
                            "Please enter a valid score. It should be lesser or equal to 6. Otherwise please input "
                            "'Nb' for no ball and 'wd' for wide ")
                        continue
                    over_arr.append(ball)
                    scored_per_team += int(ball)
                    ball_count += 1
                else:
                    print("Please enter a Valid Value")

            scorecard_object = Scorecard(self.batting_order,
                                         over_arr, runs_per_player, next_batsman_index, striker, striker_runs,
                                         non_striker, non_striker_runs, extras, is_non_striker_batting,
                                         no_of_four_per_player, no_of_six_per_player, ball_faced_per_player,
                                         total_score, self.team1_scored, team2_win, self.team, all_out)

            runs_per_player, next_batsman_index, striker, striker_runs, non_striker, non_striker_runs, extras, \
            is_non_striker_batting, no_of_four_per_player, no_of_six_per_player, ball_faced_per_player, total_score, \
            team2_win, team, all_out = scorecard_object.score_card_per_over()

            if is_non_striker_batting:
                pass
            else:
                striker, non_striker = non_striker, striker
                # temp = striker
                # striker = non_striker
                # non_striker = temp

                # temp_run = striker_runs
                # striker_runs = non_striker_runs
                # non_striker_runs = temp_run

            is_non_striker_batting = False

            print("Scorecard of team : " + str(self.team) + " for over: " + str(over))

            fields = ["Player Name", "Score", '4s', "6s", "Balls"]
            self.print_score_card(runs_per_player, fields, over, "scorecard", no_of_four_per_player,
                                  no_of_six_per_player, ball_faced_per_player, total_score, extras, wickets, striker, non_striker)

            fields = ["total score", "Over"]
            self.print_score_card(runs_per_player, fields, over, "over", no_of_four_per_player, no_of_six_per_player,
                                  ball_faced_per_player, total_score, extras, wickets, striker, non_striker)

            if team2_win:
                return total_score + extras, team2_win, wickets, all_out
            if self.team == 2 and self.no_of_overs == over:
                if team2_win:
                    print("Team 2 wins")
                elif self.team1_scored == total_score + extras:
                    print("Match Tie")
                else:
                    winning_runs = self.team1_scored - (total_score + extras)
                    print("Team 1 wins by " + str(winning_runs) + " runs")
        return total_score + extras, team2_win, wickets, all_out

    @staticmethod
    def print_score_card(runs_per_player, fields, over_count, what_to_print, no_of_four_per_player,
                         no_of_six_per_player, ball_faced_per_player, total_score, extras, wickets,
                         striker, non_striker):
        form_table = PrettyTable()
        form_table.field_names = fields

        if what_to_print == "scorecard":
            for data in runs_per_player:
                no_of_four = 0 if data not in no_of_four_per_player else no_of_four_per_player[data]
                no_of_six = 0 if data not in no_of_six_per_player else no_of_six_per_player[data]
                no_of_ball_faced = 0 if data not in ball_faced_per_player else ball_faced_per_player[data]
                if striker == data or non_striker == data:
                    player = str(data) + "*"
                else:
                    player = data
                form_table.add_row([player, runs_per_player[data], no_of_four, no_of_six, no_of_ball_faced])
            print(form_table)
        else:
            total_score = total_score + extras
            total_score = str(total_score) + "/" + str(wickets)
            form_table.add_row([total_score, over_count])
            print(form_table)
