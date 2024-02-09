from services import ViewerService
from flask import request, jsonify

class ViewerController:
    def get_viewers():
        from_number = request.args.get('from', default=0, type=int)
        count = request.args.get('count', default=100, type=int)
        return jsonify(ViewerService.get_by(None, None, from_number, count))

    def get_viewers_by(field, field_value):
        from_number = request.args.get('from', default=0, type=int)
        count = request.args.get('count', default=100, type=int)
        return jsonify(ViewerService.get_by(field, field_value, from_number, count))
    
    def get_viewer_by_id(id):
        return jsonify(ViewerService.get_by_id(id))
    
    def create_viewer():
        return jsonify(ViewerService.create(request.json))
    
    def update_viewer(id):
        return jsonify(ViewerService.update(id, request.json))
    
    def delete_viewer(id):
        return jsonify(ViewerService.delete(id))
    