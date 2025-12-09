from prometheus_api_client import PrometheusConnect
prom = PrometheusConnect(url="http://localhost:9090", disable_ssl=True)
data = prom.get_current_metric_value("metric_pzem")

print(data)