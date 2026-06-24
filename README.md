# API Response Latency Benchmark

## The Goal
A side-by-side performance comparison between two popular public JSON APIs to establish a reproducible baseline for latency and payload structure. 

## The Rig
- **Language:** Python 3.x
- **Methodology:** 10 consecutive requests per endpoint with a 500ms delay between calls to simulate stable network conditions.
- **Metrics:** - **Latency (ms):** Total round-trip time per request.
    - **JSON Integrity:** Boolean check for valid JSON formatting (`clean_json`).

## The Results (Summary)
| API | Avg Latency (ms) | Success Rate |
| :--- | :--- | :--- |
| **JSONPlaceholder** | 202.02 ms | 100% |
| **DummyJSON** | 213.65 ms | 100% |

## Interpretation
The data shows that both APIs maintain highly consistent response times, with JSONPlaceholder showing a slightly lower median latency (approx. 5% faster in this sample). Both endpoints consistently returned valid JSON, confirming their reliability for integration testing.

## How to Reproduce
1. Clone this repository.
2. Ensure Python 3 is installed.
3. Run the benchmark script: `python benchmark.py`
4. The script will generate `resultados_benchmark.csv` with the raw data.
