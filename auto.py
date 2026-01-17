import os
import shutil

source = os.path.expanduser("~/Downloads")

destination = os.path.expanduser("~/Pictures")

file_types = [".jpg", ".jpeg", ".png", ".gif"]

for f in os.listdir(source):

    if any(f.lower().endswith(e) for e in file_types):
        shutil.move(os.path.join(source, f), os.path.join(destination, f))

print("doneee")

