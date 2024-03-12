from flask import Flask, jsonify
from domain.fichierDeCalcul import get_question

class QuestionResource:

    def __init__(self, app: Flask) -> None:
        self.__app = app
        self.__register_routes()

    def __register_routes(self) -> None:
        
        @self.__app.route('/question', methods=['GET'])
        def get_random_question():
            quest, quest_type = get_question()
            return jsonify({"question": quest, "type": quest_type})