#This defines the function "pretty_print" which is a function that will print the lists I will be using a much nicer and easier to read way
def pretty_print(data):
    import json
    print(json.dumps(data, sort_keys=True, indent=4))

team_list = []
individual_list = []
team_id = 0
individual_id = 0
events = ["Maths challenge", "Football", "Basketball", "Egg and spoon race"]

#This is used to create a maximum 4 teams limited to 5 members each
while True:
    if len(team_list) != 4:
        team_names = input("Enter a team name: ")
        team_id = team_id + 1
        team_members = input("Enter the names of the team members on each team using a comma to seperate the names. Each team must have at least 5 members: ").split(",")
        if len(team_members) != 5:
            print("A team can only have 5 members.")
            continue
        team_list.append({
            "TeamID": team_id,
            "TeamNames": team_names,
            "TeamMembers": team_members,
        })
        pretty_print(team_list)
    else:
        break

#This is used to enter the names 20 individuals that will be taking part in the events
for b in range (20):
    individual_names = input("Enter an individual's name: ")
    individual_id = individual_id + 1
    individual_list.append({
        "IndividualNames": individual_names,
        "IndividualID": individual_id,
    })
pretty_print(individual_list)

#This is used to select the event and which teams you would like to review the scores of
while True:
    pretty_print(events)
    event_select = input("Which event would you like to select? ")
    events_lower = []
    for c in events:
        events_lower.append(c.lower())
    if event_select.lower() in events_lower:
        indteam = input("Would you like to view the points for individuals or teams? ")
        if indteam.lower() == "individuals":
            print("Here is a list of the individuals:")
            pretty_print(individual_list)
            break
        elif indteam.lower() == "teams":
            print("Here is a list of the teams:")
            pretty_print(team_list)
            break
    else:
        pretty_print("Error, please try again.")

#This is used for displaying the scores for the individuals/teams participating
indselect = input("Please select which individual you would like to see the scores of ")