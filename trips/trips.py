import uuid

from nameko.rpc import rpc
from nameko_redis import Redis


class TripsService:
    name = "trips_service"

    redis = Redis('development')

    @rpc
    def get(self, trip_id):
        trip = self.redis.get(trip_id)
        return trip

    @rpc
    def create(self, airport_from_id, airport_to_id):
        trip_id = uuid.uuid4().hex
        self.redis.set(trip_id, {
            "from": airport_from_id,
            "to": airport_to_id
        })
        return trip_id
