import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64


def create_performance_graph(input_sizes, execution_times, algorithm_name):
    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, execution_times, 'b-', linewidth=2, label='Actual Time')
    plt.scatter(input_sizes, execution_times, color='red', s=50)

    plt.title(f'{algorithm_name.capitalize()} Algorithm Performance', fontsize=14)
    plt.xlabel('Input Size (n)', fontsize=12)
    plt.ylabel('Time (milliseconds)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()

    return convert_to_base64(plt)


def convert_to_base64(plot):
    buffer = io.BytesIO()
    plot.savefig(buffer, format='png', dpi=100)
    plt.close()

    buffer.seek(0)
    image_bytes = buffer.getvalue()
    base64_string = base64.b64encode(image_bytes).decode('utf-8')

    return f"data:image/png;base64,{base64_string}"
