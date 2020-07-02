#legenda
# 0: boundaries
# 1: in
# 2: out
# 3: road
# 4: trafficlight/stop

map = [

    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,   1,1,2,2,    0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,   3,3,3,3,    0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,   3,3,3,3,    0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,   3,3,3,3,    0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,   3,3,3,3,    0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,6,   3,3,3,3,    0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,   4,4,3,3,    0,6,0,0,0,0,0,0,0,0,0,0,0,0],

    [2,3,3,3,3,3,3,3,3,3,3,3,3,3,   5,5,5,5,    4,3,3,3,3,3,3,3,3,3,3,3,3,1],
    [2,3,3,3,3,3,3,3,3,3,3,3,3,3,   5,5,5,5,    4,3,3,3,3,3,3,3,3,3,3,3,3,1],
    [1,3,3,3,3,3,3,3,3,3,3,3,3,4,   5,5,5,5,    3,3,3,3,3,3,3,3,3,3,3,3,3,2],
    [1,3,3,3,3,3,3,3,3,3,3,3,3,4,   5,5,5,5,    3,3,3,3,3,3,3,3,3,3,3,3,3,2],

    [0,0,0,0,0,0,0,0,0,0,0,0,6,0,   3,3,4,4,    0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,   3,3,3,3,    6,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,   3,3,3,3,    0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,   3,3,3,3,    0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,   3,3,3,3,    0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,   3,3,3,3,    0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,   2,2,1,1,    0,0,0,0,0,0,0,0,0,0,0,0,0,0],

]

points = [  

    ###--------------------NORD----------------------###

    [840, 1020,   "start",      "nord",         "right",        "in" ],
    [900, 1020,   "start",      "nord",         "left" ,        "in" ],
    [960, 1020,   "exit",       "nord",         "left" ,        "out"],
    [1020, 1020,  "exit",       "nord",         "right",        "out"],
    [840, 660,    "semaforo",   "nord",         "right",        "in",       1],
    [900, 660,    "semaforo",   "nord",         "left" ,        "in",       1],
  
    [840,960,     "strada",     "nord",         "right",        "in" ],
    [900,960,     "strada",     "nord",         "left" ,        "in" ],
    [960,960,     "strada",     "nord",         "left" ,        "out"],
    [1020,960,    "strada",     "nord",         "right",        "out"],

    [840,900,     "strada",     "nord",         "right",        "in" ],
    [900,900,     "strada",     "nord",         "left" ,        "in" ],
    [960,900,     "strada",     "nord",         "left" ,        "out"],
    [1020,900,    "strada",     "nord",         "right",        "out"],
 
    [840,840,     "strada",     "nord",         "right",        "in" ],
    [900,840,     "strada",     "nord",         "left" ,        "in" ],
    [960,840,     "strada",     "nord",         "left" ,        "out"],
    [1020,840,    "strada",     "nord",         "right",        "out"],
 
    [840,780,     "strada",     "nord",         "right",        "in" ],
    [900,780,     "strada",     "nord",         "left" ,        "in" ],
    [960,780,     "strada",     "nord",         "left" ,        "out"],
    [1020,780,    "strada",     "nord",         "right",        "out"],
 
    [840,720,     "strada",     "nord",         "right",        "in" ],
    [900,720,     "strada",     "nord",         "left" ,        "in" ],
    [960,720,     "strada",     "nord",         "left" ,        "out"],
    [1020,720,    "strada",     "nord",         "right",        "out"],
 
    [960,660,     "strada",     "nord",         "left" ,        "out"],
    [1020,660,    "strada",     "nord",         "right",        "out"],
    [780, 720,    "semaforo",   "nord",         "Null",         "Null",     1],
 
    ###---------------------SUD-----------------------#

    [840, 0,      "exit",        "sud",         "right",        "out"],
    [900, 0,      "exit",        "sud",         "left" ,        "out"],
    [960, 0,      "start",       "sud",         "left" ,        "in" ],
    [1020, 0,     "start",       "sud",         "right",        "in" ],
    [960, 360,    "semaforo",    "sud",         "left" ,        "in",       3],
    [1020, 360,   "semaforo",    "sud",         "right",        "in",       3],
 
    [840, 60,     "strada",      "sud",         "right",        "out"],
    [900, 60,     "strada",      "sud",         "left" ,        "out"],
    [960, 60,     "strada",      "sud",         "left" ,        "in" ],
    [1020,60,     "strada",      "sud",         "right",        "in" ],
 
    [840, 120,    "strada",      "sud",         "right",        "out"],
    [900, 120,    "strada",      "sud",         "left" ,        "out"],
    [960, 120,    "strada",      "sud",         "left" ,        "in" ],
    [1020,120,    "strada",      "sud",         "right",        "in" ],
 
    [840, 180,    "strada",      "sud",         "right",        "out"],
    [900, 180,    "strada",      "sud",         "left" ,        "out"],
    [960, 180,    "strada",      "sud",         "left" ,        "in" ],
    [1020,180,    "strada",      "sud",         "right",        "in" ],
 
    [840, 240,    "strada",      "sud",         "right",        "out"],
    [900, 240,    "strada",      "sud",         "left" ,        "out"],
    [960, 240,    "strada",      "sud",         "left" ,        "in" ],
    [1020,240,    "strada",      "sud",         "right",        "in" ],
 
    [840, 300,    "strada",      "sud",         "right",        "out"],
    [900, 300,    "strada",      "sud",         "left" ,        "out"],
    [960, 300,    "strada",      "sud",         "left" ,        "in" ],
    [1020,300,    "strada",      "sud",         "right",        "in" ],
 
    [840, 360,    "strada",      "sud",         "right",        "out"],
    [900, 360,    "strada",      "sud",         "left" ,        "out"],
    [1080, 300,   "semaforo",      "sud",         "Null",         "Null",      3],

    ###--------------------OVEST----------------------###

    [0, 420,      "start",     "ovest",         "right",        "in" ],
    [0, 480,      "start",     "ovest",         "left" ,        "in" ],
    [0, 540,      "exit",      "ovest",         "left" ,        "out"],
    [0, 600,      "exit",      "ovest",         "right",        "out"],
    [780,420,     "semaforo",  "ovest",         "right",        "in",       4],
    [780,480,     "semaforo",  "ovest",         "left" ,        "in",       4],
    
    [60, 420,     "strada",    "ovest",         "right",        "in" ],
    [120,420,     "strada",    "ovest",         "right",        "in" ],
    [180,420,     "strada",    "ovest",         "right",        "in" ],
    [240,420,     "strada",    "ovest",         "right",        "in" ],
    [300,420,     "strada",    "ovest",         "right",        "in" ],
    [360,420,     "strada",    "ovest",         "right",        "in" ],
    [420,420,     "strada",    "ovest",         "right",        "in" ],
    [480,420,     "strada",    "ovest",         "right",        "in" ],
    [540,420,     "strada",    "ovest",         "right",        "in" ],
    [600,420,     "strada",    "ovest",         "right",        "in" ],
    [660,420,     "strada",    "ovest",         "right",        "in" ],
    [720,420,     "strada",    "ovest",         "right",        "in" ],
    
    [60, 480,     "strada",    "ovest",         "left" ,        "in" ],
    [120,480,     "strada",    "ovest",         "left" ,        "in" ],
    [180,480,     "strada",    "ovest",         "left" ,        "in" ],
    [240,480,     "strada",    "ovest",         "left" ,        "in" ],
    [300,480,     "strada",    "ovest",         "left" ,        "in" ],
    [360,480,     "strada",    "ovest",         "left" ,        "in" ],
    [420,480,     "strada",    "ovest",         "left" ,        "in" ],
    [480,480,     "strada",    "ovest",         "left" ,        "in" ],
    [540,480,     "strada",    "ovest",         "left" ,        "in" ],
    [600,480,     "strada",    "ovest",         "left" ,        "in" ],
    [660,480,     "strada",    "ovest",         "left" ,        "in" ],
    [720,480,     "strada",    "ovest",         "left" ,        "in" ],
    
    [60, 540,     "strada",    "ovest",         "left" ,        "out"],
    [120,540,     "strada",    "ovest",         "left" ,        "out"],
    [180,540,     "strada",    "ovest",         "left" ,        "out"],
    [240,540,     "strada",    "ovest",         "left" ,        "out"],
    [300,540,     "strada",    "ovest",         "left" ,        "out"],
    [360,540,     "strada",    "ovest",         "left" ,        "out"],
    [420,540,     "strada",    "ovest",         "left" ,        "out"],
    [480,540,     "strada",    "ovest",         "left" ,        "out"],
    [540,540,     "strada",    "ovest",         "left" ,        "out"],
    [600,540,     "strada",    "ovest",         "left" ,        "out"],
    [660,540,     "strada",    "ovest",         "left" ,        "out"],
    [720,540,     "strada",    "ovest",         "left" ,        "out"],
    [780,540,     "strada",    "ovest",         "left" ,        "out"],

    [60, 600,     "strada",    "ovest",         "right",        "out"],
    [120,600,     "strada",    "ovest",         "right",        "out"],
    [180,600,     "strada",    "ovest",         "right",        "out"],
    [240,600,     "strada",    "ovest",         "right",        "out"],
    [300,600,     "strada",    "ovest",         "right",        "out"],
    [360,600,     "strada",    "ovest",         "right",        "out"],
    [420,600,     "strada",    "ovest",         "right",        "out"],
    [480,600,     "strada",    "ovest",         "right",        "out"],
    [540,600,     "strada",    "ovest",         "right",        "out"],
    [600,600,     "strada",    "ovest",         "right",        "out"],
    [660,600,     "strada",    "ovest",         "right",        "out"],
    [720,600,     "strada",    "ovest",         "right",        "out"],
    [780,600,     "strada",    "ovest",         "right",        "out"],
    [720, 360,    "semaforo",     "ovest",         "Null",         "Null",     4],

    ###----------------------EST----------------------###

    [1860, 420,   "exit",        "est",         "right",        "out"],
    [1860, 480,   "exit",        "est",         "left" ,        "out"],
    [1860, 540,   "start",       "est",         "left" ,        "in" ],
    [1860, 600,   "start",       "est",         "right",        "in" ],
    [1080, 540,   "semaforo",    "est",         "left" ,        "in",       2],
    [1080, 600,   "semaforo",    "est",         "right",        "in",       2],
    
    [1800,420,     "strada",    "est",        "right",        "out"],
    [1740,420,     "strada",    "est",        "right",        "out"],
    [1680,420,     "strada",    "est",        "right",        "out"],
    [1620,420,     "strada",    "est",        "right",        "out"],
    [1560,420,     "strada",    "est",        "right",        "out"],
    [1500,420,     "strada",    "est",        "right",        "out"],
    [1440,420,     "strada",    "est",        "right",        "out"],
    [1380,420,     "strada",    "est",        "right",        "out"],
    [1320,420,     "strada",    "est",        "right",        "out"],
    [1260,420,     "strada",    "est",        "right",        "out"],
    [1200,420,     "strada",    "est",        "right",        "out"],
    [1140,420,     "strada",    "est",        "right",        "out"],
    [1080,420,     "strada",    "est",        "right",        "out"],
    
    [1800,480,     "strada",    "est",        "left" ,        "out"],
    [1740,480,     "strada",    "est",        "left" ,        "out"],
    [1680,480,     "strada",    "est",        "left" ,        "out"],
    [1620,480,     "strada",    "est",        "left" ,        "out"],
    [1560,480,     "strada",    "est",        "left" ,        "out"],
    [1500,480,     "strada",    "est",        "left" ,        "out"],
    [1440,480,     "strada",    "est",        "left" ,        "out"],
    [1380,480,     "strada",    "est",        "left" ,        "out"],
    [1320,480,     "strada",    "est",        "left" ,        "out"],
    [1260,480,     "strada",    "est",        "left" ,        "out"],
    [1200,480,     "strada",    "est",        "left" ,        "out"],
    [1140,480,     "strada",    "est",        "left" ,        "out"],
    [1080,480,     "strada",    "est",        "left" ,        "out"],
    
    [1800,540,     "strada",    "est",        "left" ,        "in" ],
    [1740,540,     "strada",    "est",        "left" ,        "in" ],
    [1680,540,     "strada",    "est",        "left" ,        "in" ],
    [1620,540,     "strada",    "est",        "left" ,        "in" ],
    [1560,540,     "strada",    "est",        "left" ,        "in" ],
    [1500,540,     "strada",    "est",        "left" ,        "in" ],
    [1440,540,     "strada",    "est",        "left" ,        "in" ],
    [1380,540,     "strada",    "est",        "left" ,        "in" ],
    [1320,540,     "strada",    "est",        "left" ,        "in" ],
    [1260,540,     "strada",    "est",        "left" ,        "in" ],
    [1200,540,     "strada",    "est",        "left" ,        "in" ],
    [1140,540,     "strada",    "est",        "left" ,        "in" ],

    [1800,600,     "strada",    "est",        "right",        "in" ],
    [1740,600,     "strada",    "est",        "right",        "in" ],
    [1680,600,     "strada",    "est",        "right",        "in" ],
    [1620,600,     "strada",    "est",        "right",        "in" ],
    [1560,600,     "strada",    "est",        "right",        "in" ],
    [1500,600,     "strada",    "est",        "right",        "in" ],
    [1440,600,     "strada",    "est",        "right",        "in" ],
    [1380,600,     "strada",    "est",        "right",        "in" ],
    [1320,600,     "strada",    "est",        "right",        "in" ],
    [1260,600,     "strada",    "est",        "right",        "in" ],
    [1200,600,     "strada",    "est",        "right",        "in" ],
    [1140,600,     "strada",    "est",        "right",        "in" ],
    [1140,660,    "semaforo",      "est",        "Null",         "Null",   2],

]