from flask import Flask
from domain.scoring import getJsonPostionAndScoreLetter, getJsonPodiumScore

class ScoreResource:

    def __init__(self, app: Flask) -> None:
        self.__app = app
        self.__register_routes()

    def __register_routes(self) -> None:
        
        @self.__app.route('/score/letters', methods=['GET'])
        def getScoreLetters():
            return getJsonPostionAndScoreLetter(), 200
        
        @self.__app.route('/score/podium', methods=['GET'])
        def getScorePodium():
            return getJsonPodiumScore(), 200