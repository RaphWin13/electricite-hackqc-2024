from flask import Flask, jsonify


class HealthResource:

    def __init__(self, app: Flask) -> None:
        self.__app = app
        self.__register_routes()

    def __register_routes(self) -> None:
        
        @self.__app.route('/health', methods=['GET'])
        def health():
            return jsonify({"health": "OK"})