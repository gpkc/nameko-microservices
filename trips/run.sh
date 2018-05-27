#!/bin/bash

until nc -z ${RABBIT_HOST} ${RABBIT_PORT}; do
    echo "$(date) - waiting for rabbitmq..."
    sleep 1
done

until nc -z ${REDIS_HOST} ${REDIS_PORT}; do
    echo "$(date) - waiting for redis..."
    sleep 1
done

nameko run --config config.yml trips
