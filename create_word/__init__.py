import azure.functions as func
import json
from shared_code.word_service import word_service

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(
            json.dumps({"error": "Invalid request body"}),
            status_code=400,
            mimetype="application/json"
        )
    
    word = req_body.get('word')
    translation = req_body.get('translation')
    
    if not word or not translation:
        return func.HttpResponse(
            json.dumps({"error": "Both word and translation are required"}),
            status_code=400,
            mimetype="application/json"
        )
    
    new_translation = word_service.create_translation(word, translation)
    
    return func.HttpResponse(
        json.dumps(new_translation.to_dict()),
        status_code=201,
        mimetype="application/json"
    )
