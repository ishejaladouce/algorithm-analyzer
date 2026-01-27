# Algorithm Time Complexity Analyzer

A Flask application that analyzes algorithm performance and generates graphs.

## Installation
1. Create virtual environment: \`python -m venv venv\`
2. Activate it: \`venv\\Scripts\\Activate\` (Windows)
3. Install dependencies: \`pip install -r requirements.txt\`

## Usage
Run the app: \`python main_app.py\`

Visit: \`http://localhost:3000/analyze?algo=bubble&n=100&steps=10\`

## API Endpoint
\`GET /analyze\`
- \`algo\`: algorithm name (bubble, linear, binary, nested, exponential)
- \`n\`: number of items
- \`steps\`: number of measurement points

## Response Format
\`\`\`json
{
    \"algo\": \"bubble\",
    \"items\": [10, 20, 30, ...],
    \"steps\": 10,
    \"start_time\": 123456789,
    \"end_time\": 987654321,
    \"total_time_ms\": 3.456,
    \"time_complexity\": \"O(n²)\",
    \"path_to_graph\": \"data:image/png;base64,...\"
}
\`\`\`
