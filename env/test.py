from flask import request, jsonify
from app import app
from app.recommendation import llm_recommendation

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    user_id = data['user_id']
    recommendations = llm_recommendation(user_id)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)