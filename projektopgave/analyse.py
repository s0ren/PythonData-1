# Her udleveres kode til løsning af opgave 1

def pace2velocity(p):
    return (1000/60)/p

assert pace2velocity(10) == 1.666666666666666666

def v2p(v):
    return (1000/60)/v

assert v2p(1.666666666666666666) == 10

# Her udleveres kode til at løse opgave 2
# virker med stien når du har mappen `projektopgave` aktiv`

def indlaes_fra_fit(fname = "data/hok_klubmesterskab_2022/CA8D1347.FIT"):
    from fit_file import read
    points = read.read_points(fname)
    return points

punkter = indlaes_fra_fit()

print(f"Der er indlæst {len(punkter)} punkter fra filen")
print(punkter[300])

def points2lines(points):
    from geopy.distance import distance
    L = []
    for i, p in enumerate(points[1:]):
        pp = points[i]
        dt = (p['timestamp'] - pp['timestamp']).seconds
        dd = distance( (p['latitude'], p['longitude']), (pp['latitude'], pp['longitude']) ).meters
        
        line = {
            'delta_time' : dt,
            'delta_distance' : dd,
            # 'velocity' : 
            'velocity' : dd/dt
        }

        L.append(line)
    return L

lines = points2lines(punkter)

def beregn_tempo_zoner(lines):
    run_dist = 0
    run_time = 0
    walk_dist = 0
    walk_time = 0
    idle_dist = 0
    idle_time = 0
    total_dist = 0
    total_time = 0
    
    for l in lines:
        if l['velocity'] > pace2velocity(10):
            run_dist += l['delta_distance'] 
            run_time += l['delta_time']
        elif l['velocity'] > pace2velocity(50):
            walk_dist += l['delta_distance'] 
            walk_time += l['delta_time']
        else:
            idle_dist += l['delta_distance'] 
            idle_time += l['delta_time']

        total_dist += l['delta_distance'] 
        total_time += l['delta_time']


    return {
            'run' : {'dist' : run_dist, 'time' : run_time},
            'walk': {'dist' : walk_dist, 'time' : walk_time},
            'idle': {'dist' : idle_dist, 'time' : idle_time},
            'total': {'dist': total_dist, 'time': total_time}
            }

t = beregn_tempo_zoner(lines) # alle tallene

print(t)
run_pct = t['run']['time']/t['total']['time']
walk_pct = t['walk']['time']/t['total']['time']
idle_pct = t['idle']['time']/t['total']['time']

print(f"{''      :10}{'meter'              :>10}{'seconds'            :>10}{'% of time' :>10}")

print(f"{'Run:'  :10}{t['run']['dist']  :10.1f}{t['run']['time']  :10.0f}{ run_pct  :10.0%}") 
print(f"{'Walk:' :10}{t['walk']['dist'] :10.1f}{t['walk']['time'] :10.0f}{ walk_pct  :10.0%}") 
print(f"{'Idle:' :10}{t['idle']['dist'] :10.1f}{t['idle']['time'] :10.0f}{ idle_pct  :10.0%}") 
print(f"{'Total:' :10}{t['total']['dist'] :10.1f}{t['total']['time'] :10.0f}{ 1  :10.0%}") 