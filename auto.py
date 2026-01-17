import os

import shutil

src = os.path.expanduser("~/Downloads")

dst = os.path.expanduser("~/Pictures")

exts = [".jpg", ".jpeg", ".png", ".gif"]

for f in os.listdir(src):

    if any(f.lower().endswith(e) for e in exts):
        shutil.move(os.path.join(src, f), os.path.join(dst, f))

print("doneee")
