"""
Main Flask application with single endpoint.
"""

from flask import Flask, request, jsonify
import time
from algorithm_implementations import get_algorithm_function, get_time_complexity
from graph_generator import create_performance_graph

app = Flask(__name__)


def validate_inputs(algorithm_name, item_count, step_count):
    """Validate all input parameters."""

    errors = []

    valid_algorithms = ['bubble', 'linear', 'binary', 'nested', 'exponential']
    if algorithm_name not in valid_algorithms:
        errors.append(f"Algorithm must be one of: {', '.join(valid_algorithms)}")

    if item_count < 1:
        errors.append("Item count must be at least 1")
    elif item_count > 100000:
        errors.append("Item count cannot exceed 100,000")

    if step_count < 1:
        errors.append("Step count must be at least 1")
    elif step_count > 50:
        errors.append("Step count cannot exceed 50")

    if algorithm_name == 'exponential' and item_count > 25:
        errors.append("For exponential algorithm, maximum n is 25")

    return errors


def measure_time(algorithm_name, item_count):
    """Measure execution time of algorithm."""

    algorithm_func = get_algorithm_function(algorithm_name)
    if not algorithm_func:
        return 0, 0, 0

    start_ns = time.perf_counter_ns()
    algorithm_func(item_count)
    end_ns = time.perf_counter_ns()

    elapsed_ms = (end_ns - start_ns) / 1_000_000

    return start_ns, end_ns, elapsed_ms


@app.route('/analyze', methods=['GET'])
def analyze():
    try:
        algorithm = request.args.get('algo', 'bubble').lower()
        n = request.args.get('n', type=int)
        steps = request.args.get('steps', type=int)

        if n is None or steps is None:
            return jsonify({
                "error": "Missing parameters. Required: algo, n, steps"
            }), 400

        errors = validate_inputs(algorithm, n, steps)
        if errors:
            return jsonify({
                "error": "Invalid parameters",
                "details": errors
            }), 400

        if steps == 1:
            sizes = [n]
        else:
            min_size = max(10, n // steps)
            sizes = []
            for i in range(steps):
                size = min_size + (i * max(1, (n - min_size) // (steps - 1)))
                if size > n:
                    size = n
                sizes.append(size)
            sizes[-1] = n

        times_ms = []
        for size in sizes:
            _, _, time_ms = measure_time(algorithm, size)
            times_ms.append(round(time_ms, 3))

        start_ns, end_ns, final_ms = measure_time(algorithm, n)

        graph_data = create_performance_graph(sizes, times_ms, algorithm)

        response = {
            "algo": algorithm,
            "items": n,
            "steps": steps,
            "start_time": int(start_ns),
            "end_time": int(end_ns),
            "total_time_ms": round(final_ms, 3),
            "time_complexity": get_time_complexity(algorithm),
            "path_to_graph": graph_data,
            # "download_url": f"http://localhost:3000/download-graph?algo={algorithm}&n={n}"

        }

        return jsonify(response)

    except Exception as e:
        return jsonify({
            "error": "Internal error",
            "message": str(e)
        }), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
