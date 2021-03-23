
state = 'led=on&motor=off&switch=off'
sensor = []
mode = {}
sensor = state.split("&")

for s in sensor:
    a, b= (s.split("="))
    mode[a] = b

print(mode)

