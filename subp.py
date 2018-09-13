import subprocess
p = subprocess.Popen(["cat","/proc/cpuinfo"],stdout=subprocess.PIPE)
text = p.stdout.read().decode()
for line in text.splitlines():
   if line[:3] == "CPU":
    print(line)
