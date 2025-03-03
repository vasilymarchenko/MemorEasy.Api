import azure.functions as func
import json
from shared_code.word_service import word_service

def main(req: func.HttpRequest) -> func.HttpResponse:
    word_id = req.route_params.get('id')
    
    if not word_id:
        return func.HttpResponse(
            json.dumps({"error": "Word ID is required"}),
            status_code=400,
            mimetype="application/json"
        )
    
    success = word_service.delete_translation(word_id)
    
    if not success:
        return func.HttpResponse(
            json.dumps({"error": "Translation not found"}),
            status_code=404,
            mimetype="application/json"
        )
    
    return func.HttpResponse(status_code=204)
