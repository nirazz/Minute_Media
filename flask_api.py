import flask
import apis_functions as f

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World'


@app.route('/get_matches_by_team', methods=['GET'])
def get_matches_by_team():
    team = flask.request.args.get('team')
    status = flask.request.args.get('status')
    return f.get_matches(team=team, status=status)


@app.route('/get_matches_by_tournament', methods=['GET'])
def get_matches_by_tournament():
    tournament = flask.request.args.get('tournament')
    status = flask.request.args.get('status')
    return f.get_matches(tournament=tournament, status=status)


if __name__ == '__main__':
    app.run()

