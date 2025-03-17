states_needed = set([
    "mt", "wa", "or", "id", "nv", "ut", "ca", "az",
    "nm", "tx", "ok", "ks", "co", "ne", "sd", "wy",
    "nd", "ia", "mn", "mo", "ar", "la"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])
stations["ksix"] = set(["nm", "tx", "ok"])
stations["kseven"] = set(["ok", "ks", "co"])
stations["keight"] = set(["ks", "co", "ne"])
stations["knine"] = set(["ne", "sd", "wy"])
stations["kten"] = set(["nd", "ia"])
stations["keleven"] = set(["mn", "mo", "ar"])
stations["ktwelve"] = set(["la"])
stations["kthirteen"] = set(["mo", "ar"])

final_stations = set()

def Minglobal(stations, states_needed):

    while states_needed:
        best_station = None
        states_covered = set()

        for station, states_for_station in stations.items():
            
            covered = states_needed & states_for_station
            
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered

        states_needed -= states_covered            
        final_stations.add(best_station)

    return final_stations

def main():
    global_result = Minglobal(stations.copy(), states_needed.copy())
    print(f"Las estaciones a comprar con minimo global serian: {"-".join(sorted(global_result))}")
    
if __name__ == "__main__":
    main()