with open("input.txt") as f:
    image = f.readlines()[0].strip()

size = 25 * 6
layers = [image[i : i + size] for i in range(0, len(image), size)]

zeros = [l.count("0") for l in layers]
i = zeros.index(min(zeros))
checksum = layers[i].count("1") * layers[i].count("2")

print(f"PART 1: {checksum}")

image = [["2" for x in range(25)] for y in range(6)]
for layer in layers:
    x = 0
    for line in [layer[i : i + 25] for i in range(0, len(layer), 25)]:
        y = 0
        for pixel in line:
            if image[x][y] == "2":
                image[x][y] = pixel
            y += 1
        x += 1

print("PART 2:")
for line in image:
    print("".join(line).replace("0", " ").replace("1", "█"))
