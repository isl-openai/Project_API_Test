from flask import Flask, jsonify

app = Flask(__name__)

users = {
    1:{"id":1, "name":"홍길동", "age":30},
    2:{"id":2, "name":"김철수", "age":30}
}

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    
    if user is None:
        return jsonify({"error":"User not found"}), 404
    
    return jsonify(user), 200


if __name__ == "__main__":
    app.run(debug=True)