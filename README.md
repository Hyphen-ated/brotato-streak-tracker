# brotato-streak-tracker
This is a streaming tool for the game Brotato. It reads the game's log file to see how your runs are going, and it puts
summaries of your runs into a text file, which you can display on your stream with OBS.

To use it, you currently need to edit tracker.py so that `brotato_dir` points to the correct location for your install.

Then do `python tracker.py`. Tested with python 3.8
