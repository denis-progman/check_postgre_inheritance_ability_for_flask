from services import LoserService
from flask import request, jsonify


class LoserController:
    def get_losers():
        from_number = request.args.get('from', default=0, type=int)
        count = request.args.get('count', default=100, type=int)
        return jsonify(LoserService.get_by(None, None, from_number, count))

    def get_losers_by(field, field_value):
        from_number = request.args.get('from', default=0, type=int)
        count = request.args.get('count', default=100, type=int)
        return jsonify(LoserService.get_by(field, field_value, from_number, count))
    
    def get_loser_by_id(id):
        return jsonify(LoserService.get_by_id(id))
    
    def create_loser():
        return jsonify(LoserService.create(request.json))
    
    def update_loser(id):
        return jsonify(LoserService.update(id, request.json))
    
    def delete_loser(id):
        return jsonify(LoserService.delete(id))