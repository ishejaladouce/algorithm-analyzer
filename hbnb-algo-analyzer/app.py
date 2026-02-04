from flask import Flask, request, jsonify
from database import SessionLocal
from models import AlgoAnalysis

app = Flask(__name__)


# 🔹 Health check endpoint
@app.route("/", methods=["GET"])
def health_check():
    return jsonify({
        "status": "API is running"
    }), 200


# 🔹 Save analysis endpoint
@app.route("/api/save_analysis", methods=["POST"])
def save_analysis():
    data = request.get_json()

    if not data:
        return jsonify({
            "status": "error",
            "message": "Invalid or missing JSON payload"
        }), 400

    session = SessionLocal()

    try:
        analysis = AlgoAnalysis(
            algo=data["algo"],
            items=data["items"],
            steps=data["steps"],
            start_time=data["start_time"],
            end_time=data["end_time"],
            total_time_ms=data["total_time_ms"],
            time_complexity=data["time_complexity"],
            path_to_graph=data.get("path_to_graph")
        )

        session.add(analysis)
        session.commit()
        session.refresh(analysis)

        return jsonify({
            "status": "success",
            "id": analysis.id
        }), 201

    except KeyError as e:
        session.rollback()
        return jsonify({
            "status": "error",
            "message": f"Missing required field: {str(e)}"
        }), 400

    except Exception as e:
        session.rollback()
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

    finally:
        session.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888, debug=True)
