import sys

file = sys.argv[1]
line_size = int(sys.argv[2])
line_buffer = ""
with open(file, "r") as inFile:
  for line in inFile:
    if len(line) > 0 and line[0] != '>':
      line = line.strip()
      if len(line_buffer) < line_size:
        line_buffer += line
      if len(line_buffer) >= line_size:
        print(line_buffer[0:line_size])
        line_buffer = line_buffer[line_size:]
print(line_buffer)
