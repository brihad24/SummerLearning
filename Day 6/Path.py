from calendar import firstweekday
from pathlib import Path

path = Path("Day 1")
print(path.exists())

path1 = Path("Temp")
print(path1.mkdir()) # Creates a folder 
print(path1.rmdir()) # Deletes a folder

path2 = Path()
for file in path2.glob('*'):
    print(file)