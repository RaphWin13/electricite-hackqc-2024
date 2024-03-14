from flask import Flask, jsonify
from domain.data_accessors import get_fun_fact

class FunFactResource:

    def __init__(self, app: Flask) -> None:
        self.__app = app
        self.__register_routes()

    def __register_routes(self) -> None:
        
        @self.__app.route('/funfact', methods=['GET'])
        def get_funfact():
            fact, conversion = get_fun_fact()
            return jsonify({"fact": fact, "equivalence": conversion})