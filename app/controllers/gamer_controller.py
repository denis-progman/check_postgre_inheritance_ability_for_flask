from services import GamerService
from flask import request, jsonify


class GamerController:
    def get_gamers():
        from_number = request.args.get('from', default=0, type=int)
        count = request.args.get('count', default=100, type=int)
        return jsonify(GamerService.get_by(None, None, from_number, count))

    def get_gamers_by(field, field_value):
        from_number = request.args.get('from', default=0, type=int)
        count = request.args.get('count', default=100, type=int)
        return jsonify(GamerService.get_by(field, field_value, from_number, count))
    
    def get_gamer_by_id(id):
        return jsonify(GamerService.get_by_id(id))
    
    def create_gamer():
        return jsonify(GamerService.create(request.json))
    
    def update_gamer(id):
        return jsonify(GamerService.update(id, request.json))
    
    def delete_gamer(id):
        return jsonify(GamerService.delete(id))

