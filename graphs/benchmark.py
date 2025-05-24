import subprocess


cmd = ['python3', 'main.py', '--graphs', '--generate']

file = open("results/list-find.csv", "w")
file.write("InputSize,Memory,Time\n")  # MEM IN KB, TIME IN SEC

for i in range(2, 14):
    input_data = f"{2**i}\n70\nlist\nfind\n{2**i - 2}\n{2**i - 1}\nexit"

    # Run /usr/bin/time with -f option to get memory and time info
    time_cmd = ['/usr/bin/time', '-f', '%M\n%e'] + cmd

    proc = subprocess.Popen(time_cmd,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True)

    stdout, stderr = proc.communicate(input=input_data)

    # print("Program output:")
    # print(stdout)
    
    mem, time, _ = stderr.split("\n")

    print(f"Input Size: {2 ** i}; Resource usage: MEM={mem} TIME={time}")
    file.write(f"{2**i},{mem},{time}\n")

file.close()
