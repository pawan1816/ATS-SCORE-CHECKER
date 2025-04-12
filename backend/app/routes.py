from flask import Blueprint, request, jsonify
from app.utils.nlp_processor import calculate_ats_score

api = Blueprint('api', __name__)  # Note: 'api' not 'app'

@api.route('/check-score', methods=['POST', 'OPTIONS'])  # Add OPTIONS
def check_score():
    if request.method == 'OPTIONS':
        return {}, 200  # Return empty response for preflight
        
    # Your existing POST handling code
    data = request.json
    score, analysis = calculate_ats_score(data['resume'], data['job_description'])
    return jsonify({'score': score, 'analysis': analysis})


