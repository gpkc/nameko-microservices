import uuid

from nameko.rpc import rpc
from nameko_redis import Redis


class AirportsService:
    name = "airports_service"

    redis = Redis('development')

    @rpc
    def get(self, airport_id):
        airport = self.redis.get(airport_id)
        return airport

    @rpc
    def create(self, airport):
        airport_id = uuid.uuid4().hex
        self.redis.set(airport_id, airport)
        return airport_id
