valves = """Valve OA has flow rate=0 tunnels lead to valves VP VM
Valve GA has flow rate=13 tunnel leads to valve KV
Valve WD has flow rate=0 tunnels lead to valves SH XQ
Valve TE has flow rate=0 tunnels lead to valves OY DO
Valve JR has flow rate=0 tunnels lead to valves TR LY
Valve JQ has flow rate=0 tunnels lead to valves TD DZ
Valve VH has flow rate=6 tunnels lead to valves WY YQ NU
Valve NX has flow rate=0 tunnels lead to valves XQ MN
Valve XL has flow rate=0 tunnels lead to valves AA FA
Valve QY has flow rate=0 tunnels lead to valves NU DO
Valve KV has flow rate=0 tunnels lead to valves GA XQ
Valve NK has flow rate=0 tunnels lead to valves XW XQ
Valve JU has flow rate=0 tunnels lead to valves QH TB
Valve XZ has flow rate=0 tunnels lead to valves AA SH
Valve XQ has flow rate=18 tunnels lead to valves GK NX WD KV NK
Valve VM has flow rate=19 tunnels lead to valves LY OA OY AE
Valve LE has flow rate=0 tunnels lead to valves MN NS
Valve HO has flow rate=0 tunnels lead to valves GO QH
Valve PX has flow rate=0 tunnels lead to valves MN VP
Valve MN has flow rate=4 tunnels lead to valves LE UX TB NX PX
Valve VB has flow rate=0 tunnels lead to valves XM AA
Valve VP has flow rate=21 tunnels lead to valves XM WT BG PX OA
Valve KI has flow rate=15 tunnels lead to valves XU MT
Valve NU has flow rate=0 tunnels lead to valves QY VH
Valve WT has flow rate=0 tunnels lead to valves SH VP
Valve OY has flow rate=0 tunnels lead to valves VM TE
Valve VS has flow rate=0 tunnels lead to valves QH SH
Valve XM has flow rate=0 tunnels lead to valves VB VP
Valve HI has flow rate=17 tunnel leads to valve TD
Valve TB has flow rate=0 tunnels lead to valves JU MN
Valve BG has flow rate=0 tunnels lead to valves VP GK
Valve HN has flow rate=16 tunnel leads to valve BO
Valve MT has flow rate=0 tunnels lead to valves KI BO
Valve OX has flow rate=0 tunnels lead to valves DZ ZF
Valve QH has flow rate=5 tunnels lead to valves FA DW VS JU HO
Valve YQ has flow rate=0 tunnels lead to valves VH AE
Valve DW has flow rate=0 tunnels lead to valves ML QH
Valve WY has flow rate=0 tunnels lead to valves HS VH
Valve GO has flow rate=0 tunnels lead to valves HO DO
Valve UX has flow rate=0 tunnels lead to valves AA MN
Valve AE has flow rate=0 tunnels lead to valves YQ VM
Valve DZ has flow rate=9 tunnels lead to valves HS OX JQ
Valve NS has flow rate=0 tunnels lead to valves SH LE
Valve LY has flow rate=0 tunnels lead to valves JR VM
Valve BO has flow rate=0 tunnels lead to valves HN MT
Valve HS has flow rate=0 tunnels lead to valves WY DZ
Valve XW has flow rate=0 tunnels lead to valves NK AA
Valve DO has flow rate=11 tunnels lead to valves TE XU ZF QY GO
Valve FA has flow rate=0 tunnels lead to valves XL QH
Valve AA has flow rate=0 tunnels lead to valves VB XL XZ XW UX
Valve VW has flow rate=14 tunnel leads to valve ML
Valve SH has flow rate=8 tunnels lead to valves NS WT XZ VS WD
Valve XU has flow rate=0 tunnels lead to valves DO KI
Valve ZF has flow rate=0 tunnels lead to valves OX DO
Valve GK has flow rate=0 tunnels lead to valves XQ BG
Valve ML has flow rate=0 tunnels lead to valves VW DW
Valve TD has flow rate=0 tunnels lead to valves HI JQ
Valve TR has flow rate=25 tunnel leads to valve JR"""  # commas and semi colons have been omitted

valves = """Valve AA has flow rate=0 tunnels lead to valves DD II BB
Valve BB has flow rate=13 tunnels lead to valves CC AA
Valve CC has flow rate=2 tunnels lead to valves DD BB
Valve DD has flow rate=20 tunnels lead to valves CC AA EE
Valve EE has flow rate=3 tunnels lead to valves FF DD
Valve FF has flow rate=0 tunnels lead to valves EE GG
Valve GG has flow rate=0 tunnels lead to valves FF HH
Valve HH has flow rate=22 tunnel leads to valve GG
Valve II has flow rate=0 tunnels lead to valves AA JJ
Valve JJ has flow rate=21 tunnel leads to valve II"""

valves = valves.split("\n")
adjecency_dict = dict()
flow_dict = dict()
for valve in valves[:]:
    valve = valve.split(" ")
    adjecency_dict[valve[1]] = valve[9:]
    flow_dict[valve[1]] = int(valve[4].split("=")[1])
valves = adjecency_dict.keys()

from collections import deque
def get_distance_dict(node):
    distance = {node: 1}
    queue = deque([node])
    while queue:
        current = queue.popleft()
        for valve in adjecency_dict[current]:
            if valve not in distance:
                distance[valve] = distance[current] + 1
                queue.append(valve)
    return distance
        
distance_dict = {valve: get_distance_dict(valve) for valve in valves if (flow_dict[valve] or valve == "AA")}  # the amount of minutes to go to AND open a valve
max_pressure = 0
current_valve = "AA"
current_pressure = 0
minutes_left = 30
open_valve_dict = {valve: False for valve in valves}
nums = set()
queue = deque([(current_valve, current_pressure, minutes_left, open_valve_dict)])
while queue:
    current_valve, current_pressure, minutes_left, open_valve_dict = queue.popleft()
    if minutes_left not in nums:
        print(minutes_left)
        nums.add(minutes_left)

    pressure_per_minute = sum([flow_dict[valve]*open_valve_dict[valve] for valve in valves])
    if minutes_left == 0:
        max_pressure = max(max_pressure, current_pressure)
        continue
    
    remaining = False
    for valve in distance_dict[current_valve]:
        if distance_dict[current_valve][valve] <= minutes_left and not open_valve_dict[valve] and valve != current_valve and flow_dict[valve]:
            remaining = True
            current_pressure += distance_dict[current_valve][valve]*pressure_per_minute
            new_open = open_valve_dict.copy()
            new_open[valve] = True
            queue.append((valve, current_pressure, minutes_left-distance_dict[current_valve][valve], new_open))

    if not remaining:
        current_pressure += minutes_left*pressure_per_minute
        max_pressure = max(max_pressure, current_pressure)
    

print(max_pressure)