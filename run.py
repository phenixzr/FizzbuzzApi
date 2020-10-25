from FizzbuzzApi.endpoints.fizzbuzzEP import FizzBuzzEP
from FizzbuzzApi.endpoints.metricsEP import MetricsEP
from FizzbuzzApi import db, app, api

# adding our endpoints
api.add_resource(FizzBuzzEP, '/v1/fizzbuzz')
api.add_resource(MetricsEP, '/v1/metrics')

if __name__ == '__main__':
    app.run()