# User sends a  request through Flask API, parameters are sent to api_functions which loads the csv files and create the objects.
# Objects are sent back to api_functions into Flask API and finally to the user in json format.

# Run flask_api.py
# A new tab will appear with 'Hello world' as a greeting.
# Add '/get_matches_by_tournament' to the URL path and specify the tournament you wish to filter from the results by adding '?' ,and the tournament name.
# You can add another filter to see if the match is 'upcoming' or 'played'

## Please see examples below:

# Example - http://127.0.0.1:5000/get_matches_by_tournament?tournament=premier-league
# Example - http://127.0.0.1:5000/get_matches_by_tournament?tournament=premier-league&status=played


# Add '/get_matches_by_team' to the URL path and specify the tournament you wish to filter from the results by adding '?' ,and the team name.
# You can add another filter to see if the match is 'upcoming' or 'played'

## Please see examples below:

# Example - http://127.0.0.1:5000/get_matches_by_team?team=Manchester%20United
# Example - http://127.0.0.1:5000/get_matches_by_team?team=Manchester%20United&status=upcoming