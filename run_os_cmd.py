def run_os_cmd(cmd: str, *args: str) -> list:
    cmdOut: list
    output: list = []
    if os_command_check(cmd):
        if args:
            cmdOut = subprocess.run([cmd, *args], capture_output=True, text=True)
        else:
            cmdOut = subprocess.run(cmd, capture_output=True, text=True)
        for line in cmdOut.stdout.split("\n"):
            output.append(line.strip())
        return output
    return None
