import influxdb
import random

dbClient = influxdb.InfluxDBClient(host='localhost', port=8086, username='root', password='root', database='test')

def writer_N(things_to_write_N):
    
    json_body_N = [
        {
            "measurement": "Vehicles",
            "tags": {
                "host": "server_main",
                "region": "it"
            },
            "fields": {
                "Spawn_N": Spawn_N,
            }
        }
    ]

    try:
        dbClient.write_points(json_body_N)
    except:
        print("nope!")

    result = dbClient.query('SELECT * from Vehicles;')
    print("Result: {0}".format(result))

def writer_S(things_to_write_S):
    
    json_body_S = [
        {
            "measurement": "Vehicles",
            "tags": {
                "host": "server_main",
                "region": "it"
            },
            "fields": {
                "Spawn_N": Spawn_S,
            }
        }
    ]

    try:
        dbClient.write_points(json_body_S)
    except:
        print("nope!")

    result = dbClient.query('SELECT * from Vehicles;')
    print("Result: {0}".format(result))

Spawn_N = 0
Spawn_N += random.random()

Spawn_S = 0
Spawn_S += random.random()

writer_N(Spawn_N), 
writer_S(Spawn_S),