from lib.cli2 import CLI

if __name__ == "__main__":
    cli = CLI()
    cli.show_help()
    print("#############################################")
    while True:
        command = input("<Enter command or 'help' for options. Type 'exit' to quit> ")
        if command.lower() in ["exit", "quit"]:
            break
        cli.process_command(command)


