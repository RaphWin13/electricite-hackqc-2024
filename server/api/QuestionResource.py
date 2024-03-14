from flask import Flask, jsonify, request
from domain.data_accessors import get_question, log_answer

class QuestionResource:

    def __init__(self, app: Flask) -> None:
        self.__app = app
        self.__register_routes()

    def __register_routes(self) -> None:
        
        @self.__app.route('/question', methods=['GET'])
        def get_random_question():
            quest, quest_type, quest_id = get_question()
            return jsonify({"question": quest, "type": quest_type, "id": quest_id})
        
        @self.__app.route('/question', methods=['POST'])
        def log_answer_to_file():
            data = request.json
            success = log_answer(data["id"], data["answer"])
            return jsonify({"status":success})