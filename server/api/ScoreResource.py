from flask import Flask
from domain.building_scoring import get_json_position_and_score_letter, get_json_podium_score

class ScoreResource:

    def __init__(self, app: Flask) -> None:
        self.__app = app
        self.__register_routes()

    def __register_routes(self) -> None:
        
        @self.__app.route('/score/letters', methods=['GET'])
        def getScoreLetters():
            return get_json_position_and_score_letter(), 200
        
        @self.__app.route('/score/podium', methods=['GET'])
        def getScorePodium():
            return get_json_podium_score(), 200