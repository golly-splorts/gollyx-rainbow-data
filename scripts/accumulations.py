import json
import os
import copy


def main():
    #for which in [0, 1, 2]:
    for which in range(24):
        fix_season(which)

def fix_season(which_season0):
    print(f"\naccumulations script is now repairing season0={which_season0}...")

    nteams = 4

    f_rainbows = lambda x: 11*x[0] + 7*x[1] + 3*x[2]
    rainbow_values = [11, 7, 3, 0]

    postseason_json_file = os.path.join(f'season{which_season0}', 'postseason.json')
    if not os.path.exists(postseason_json_file):
        raise Exception(f"Error: could not find json file: {postseason_json_file}")
    with open(postseason_json_file, 'r') as f:
        post = json.load(f)

    # Initialize new postseason data structure
    new_post = {}

    # Initialize new W23L/points accumulators
    lcs_sw23l = {}
    rcs_sw23l = {}
    lcs_points = {}
    rcs_points = {}
    # Loop over all teams involved
    last_day = post['LCS'][-1]
    for game in last_day:
        for i in range(nteams):
            abbr_key = f"team{i+1}Abbr"
            abbr_val = game[abbr_key]
            lcs_sw23l[abbr_val] = [0, 0, 0, 0]
            rcs_sw23l[abbr_val] = [0, 0, 0, 0]
            lcs_points[abbr_val] = 0
            rcs_points[abbr_val] = 0

    # Iterate through LCS, filtering games as we go
    miniseason = []
    for day in post['LCS']:
        new_day = []
        for game in day:
            # Scores and ranks are ok,
            # SeriesW23L and SeriesTotalPoints are not
            new_game = copy.deepcopy(game)

            # First, fix the incorrect fields
            for i in range(nteams):
                abbr_key = f"team{i+1}Abbr"
                abbr_val = team_abbr = game[abbr_key]
                
                this_sw23l = copy.deepcopy(lcs_sw23l[team_abbr])

                sw23l_key = f"team{i+1}SeriesW23L"
                #del new_game[sw23l_key]
                new_game[sw23l_key] = []

                stp_key = f"team{i+1}SeriesTotalPoints"
                #del new_game[stp_key]
                new_game[stp_key] = 0

                new_game[sw23l_key] = this_sw23l
                new_game[stp_key] = lcs_points[team_abbr]

            new_day.append(new_game)

            # Now accumulate W23L and points (correctly)
            for i in range(nteams):
                abbr_key = f"team{i+1}Abbr"
                abbr_val = game[abbr_key]

                rank_key = f"team{i+1}Rank"
                rank_val = game[rank_key]

                score_key = f"team{i+1}Score"
                score_val = game[score_key]

                tmp = lcs_sw23l[abbr_val]
                tmp[rank_val] += 1
                lcs_sw23l[abbr_val] = tmp
                lcs_points[abbr_val] += score_val

        miniseason.append(new_day)
    new_post['LCS'] = miniseason

    # Iterate through RCS, filtering games as we go
    miniseason = []
    for day in post['RCS']:
        new_day = []
        for game in day:
            # Scores and ranks are ok,
            # SeriesW23L and SeriesTotalPoints are not
            new_game = copy.deepcopy(game)

            # First, fix the incorrect fields
            for i in range(nteams):
                abbr_key = f"team{i+1}Abbr"
                abbr_val = team_abbr = game[abbr_key]

                this_sw23l = copy.deepcopy(rcs_sw23l[team_abbr])

                sw23l_key = f"team{i+1}SeriesW23L"
                #del new_game[sw23l_key]
                new_game[sw23l_key] = []

                stp_key = f"team{i+1}SeriesTotalPoints"
                #del new_game[stp_key]
                new_game[stp_key] = 0

                new_game[sw23l_key] = this_sw23l
                new_game[stp_key] = rcs_points[team_abbr]

            new_day.append(new_game)

            # Now accumulate
            for i in range(nteams):
                abbr_key = f"team{i+1}Abbr"
                abbr_val = game[abbr_key]

                rank_key = f"team{i+1}Rank"
                rank_val = game[rank_key]

                score_key = f"team{i+1}Score"
                score_val = game[score_key]

                tmp = rcs_sw23l[abbr_val]
                tmp[rank_val] += 1
                rcs_sw23l[abbr_val] = tmp
                rcs_points[abbr_val] += score_val

        miniseason.append(new_day)
    new_post['RCS'] = miniseason

    with open(postseason_json_file, 'w') as f:
        json.dump(new_post, f, indent=4)

    print(f"Done repairing {postseason_json_file}.")



if __name__=="__main__":
    main()

