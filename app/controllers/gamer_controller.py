from services import GamerService
from flask import request, jsonify


class GamerController:

    def get_all():
        from_number = request.args.get('from', default=0, type=int)
        count = request.args.get('count', default=100, type=int)
        return jsonify(GamerService.get_by(None, None, from_number, count))

    def get_by(field, field_value):
        from_number = request.args.get('from', default=0, type=int)
        count = request.args.get('count', default=100, type=int)
        return jsonify(GamerService.get_by(field, field_value, from_number, count))
    
    def get_by_id(id):
        return jsonify(GamerService.get_by_id(id))
    
    def create():
        return jsonify(GamerService.create(request.json))
    
    def update(id):
        return jsonify(GamerService.update(id, request.json))
    
    def delete(id):
        return jsonify(GamerService.delete(id))

