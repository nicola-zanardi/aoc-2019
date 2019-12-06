with open("input.txt") as f:
    data = [l.strip() for l in f.readlines()]

orbits = {}
planets = set()
for orbit in data:
    a = orbit.split(")")
    orbits[a[1]] = a[0]
    for p in a:
        planets.add(p)


def orbit_walker(planet, nr=0):
    if planet == "COM":
        return nr
    parent = orbits[planet]
    return orbit_walker(parent, nr + 1)


checksum = sum(list(map(orbit_walker, planets)))
print(checksum)
