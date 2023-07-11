import time

brotato_dir = "C:/Users/s/AppData/Roaming/Brotato/76561197960788425/"
logfile = brotato_dir + "log.txt"
tracking_file = "obs_streak_track.txt"

#todo: call this
def format_time(start_time):
    if start_time is None:
        return ""
    duration = int(time.time() - start_time)
    hours, remainder = divmod(duration, 3600)
    minutes, seconds = divmod(remainder, 60)
    output = "{:02}:{:02}".format(int(minutes), int(seconds))
    if hours > 0:
        output = str(int(hours)) + output
    return "--" + output

old_wave = ""
new_char = ""
new_wave = ""
starting_weapons = ""
finished_logging_run = False
start_time = None
with open(tracking_file, "r") as outputfile:
    out_lines = outputfile.read().splitlines(keepends=True)
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
                finished_logging_run = False
                starting_weapons = line[len("Weapons: "):].strip()
                starting_weapons = starting_weapons.replace("weapon_", "")
                starting_weapons = starting_weapons.replace("_1", "")
                starting_weapons = starting_weapons.replace("jousting_", "")
                starting_weapons = starting_weapons.replace("double_barrel_", "")
                starting_weapons = starting_weapons.replace("minigun_3", "")
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
            start_time = time.time()
            out_lines.insert(0, new_char + ", " + starting_weapons + "\n")
            change = True
        elif run_won:
            out_lines[0] = new_char + ", " + starting_weapons + ": Won" + "\n"
            change = True
        elif run_lost:
            out_lines[0] = new_char + ", " + starting_weapons + ": w" + new_wave + "\n"
            change = True

        if change and not finished_logging_run:
            finished_logging_run = True
            with open(tracking_file, "w") as outputfile:
                outputfile.writelines(out_lines)

        old_wave = new_wave

           