import time
import random
import testbasic

Spawn_N = 0
Spawn_S = 0
Spawn_E = 0
Spawn_W = 0
Despawn_N = 0
Despawn_S = 0
Despawn_E = 0
Despawn_W = 0
Deaths = 0
Accidents = 0

while True:

    #N
    time.sleep(3)
    Spawn_N  += random.triangular(0.1, 15.0, 3)
    print(Spawn_N)
    testbasic.writer(Spawn_N)

    #E
    time.sleep(2)
    Spawn_E += random.triangular(0.1, 15.0, 3)
    print(Spawn_E)
    testbasic.writer(Spawn_E)

    #W
    time.sleep(1)
    Spawn_W += random.triangular(0.1, 15.0, 3)
    print(Spawn_W)
    testbasic.writer(Spawn_W)

    #S
    time.sleep(3)
    Spawn_S += random.triangular(0.1, 15.0, 3)
    print(Spawn_S)
    testbasic.writer(Spawn_S)