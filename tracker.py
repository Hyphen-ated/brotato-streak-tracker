import time
brotato_dir = "C:/Users/s/AppData/Roaming/Brotato/76561197960788425/"
logfile = brotato_dir + "log.txt"
tracking_file = "obs_streak_track.txt"

old_wave = ""
new_char = ""
new_wave = ""
starting_weapons = ""
with open(tracking_file, "r") as outputfile:
    out_lines = outputfile.read().splitlines()
    if len(out_lines) == 0:
        out_lines.append("\n")

print("Starting brotato tracker")
while True:
    time.sleep(1)
    with open(logfile, "r") as log_lines:
        run_won = False
        run_lost = False
        for line in log_lines:
            if line.startswith("Character: character_"):
                new_char = line[len("Character: character_"):].strip()
            if line.startswith("Wave: "):
                new_wave = line[len("Wave: "):].strip()
            if new_wave == "1" and old_wave != "1" and line.startswith("Weapons: "):
                starting_weapons = line[len("Weapons: "):].strip()
                starting_weapons = starting_weapons.replace("weapon_", "")
                starting_weapons = starting_weapons.replace("_1", "")
                if len(starting_weapons) > 0 and starting_weapons[-1] == ',':
                        starting_weapons = starting_weapons[0:-1]
            if line.startswith("is_run_won"):
                run_won = True
            if line.startswith("is_run_lost"):
                run_lost = True

        change = False
        # there are three reasons to edit the output: a new run started, a run ended in win, or a run ended in loss
        if new_wave == "1" and old_wave != "1":
            print("new run detected with " + new_char)
            out_lines.insert(0, new_char + ", " + starting_weapons + "\n")
            change = True
        elif run_won:
            out_lines[0] = new_char + ", " + starting_weapons + ": Won\n"
            change = True
        elif run_lost:
            out_lines[0] = new_char + ", " + starting_weapons + ": w" + new_wave + "\n"
            change = True

        if change:
            with open(tracking_file, "w") as outputfile:
                outputfile.writelines(out_lines)

        old_wave = new_wave

           