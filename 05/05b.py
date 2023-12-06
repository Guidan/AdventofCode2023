import multiprocessing
with open("./input.txt") as file:
    schematic = file.readlines()


def get_value(search: int, lookup: list):
    output = None
    for values in lookup:
        if values[1] <= search < values[1] + values[2]:
            output = values[0] + (search - values[1])
            break
    if output is None:
        output = search
    return output




def getlowestloc(schematic: list) -> int:
    seeds = []
    seed_map = []
    seeds_to_soil = []
    soil_to_fert = []
    fert_to_water = []
    water_to_light = []
    light_to_temp = []
    temp_to_hum = []
    hum_to_loc = []
    lowest_loc = 9999999999

    section = 0
    for lines in schematic:
        if lines.startswith("seeds:"):
            seed_map = list(map(int, lines[7::].split()))
        elif lines[0].isnumeric():
            match section:
                case 1:
                    seeds_to_soil.append(list(map(int, lines.split())))
                case 2:
                    soil_to_fert.append(list(map(int, lines.split())))
                case 3:
                    fert_to_water.append(list(map(int, lines.split())))
                case 4:
                    water_to_light.append(list(map(int, lines.split())))
                case 5:
                    light_to_temp.append(list(map(int, lines.split())))
                case 6:
                    temp_to_hum.append(list(map(int, lines.split())))
                case 7:
                    hum_to_loc.append(list(map(int, lines.split())))
                case _:
                    continue
        elif lines[0].isalpha():
            section += 1

    for i, seed in enumerate(seed_map):
        print(seed, seed_map[i+1])
        if (i % 2) == 0:
            for seed_num in range(seed, (seed + seed_map[i+1])):
                soil = get_value(seed_num, seeds_to_soil)
                fert = get_value(soil, soil_to_fert)
                water = get_value(fert, fert_to_water)
                light = get_value(water, water_to_light)
                temp = get_value(light, light_to_temp)
                hum = get_value(temp, temp_to_hum)
                loc = get_value(hum, hum_to_loc)
                if lowest_loc > loc:
                    lowest_loc = loc
    return lowest_loc


print(getlowestloc(schematic))
