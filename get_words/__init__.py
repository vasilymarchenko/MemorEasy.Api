import azure.functions as func
import json
from shared_code.word_service import word_service

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Get query parameters with defaults
    try:
        page = int(req.params.get('page', 1))
        page_size = int(req.params.get('pageSize', 20))
    except ValueError:
        return func.HttpResponse(
            json.dumps({"error": "Invalid page or pageSize parameter"}),
            status_code=400,
            mimetype="application/json"
        )
    
    search = req.params.get('search')
    
    # Validate parameters
    if page < 1 or page_size < 1:
        return func.HttpResponse(
            json.dumps({"error": "Page and pageSize must be positive integers"}),
            status_code=400,
            mimetype="application/json"
        )
    
    result = word_service.get_translations(page, page_size, search)
    
    return func.HttpResponse(
        json.dumps(result.to_dict()),
        mimetype="application/json"
    )
