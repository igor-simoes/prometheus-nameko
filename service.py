from nameko.rpc import rpc
from nameko.web.handlers import http
from nameko_prometheus import PrometheusMetrics
from prometheus_client import Counter


work_units = Counter(
    "my_service_work_units_total", "Total number of work units", ["work_type"]
)

class ExampleService:
    name = "example_service"
    metrics = PrometheusMetrics()

    @http("GET", "/metrics")
    def endpoint(self, request):
        return self.metrics.expose_metrics(request)

    @rpc
    def example(self):
        work_units.labels(work_type="hard").inc()
        return {"hello": "world"}
