### Create first user
```
docker-compose exec mosquitto mosquitto_passwd -c /mosquitto/conf/mosquitto.passwd mosquitto
```

### Create second user
```
docker-compose exec mosquitto mosquitto_passwd -b /mosquitto/conf/mosquitto.passwd seconduser shoaCh3ohnokeathal6eeH2marei2o
```

```
mosquitto_sub -h localhost -t mytopic
```

```
mosquitto_pub -h localhost -t mytopic -m "Hello, MQTT!"
```
