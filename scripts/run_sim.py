from src.mailbox import IOTMailbox


def handle_light_level(light_level):
    if light_level >= 0:
        state = "OPEN"
    else:
        state = "CLOSED"

    print(f"Light level: {light_level:.2f} -> Door {state}")


def main():
    mailbox = IOTMailbox(
        interval_ms=1500,
        signal_callback=handle_light_level
    )
    
    print("Commands: start | stop | quit")

    while True:
        cmd = input("> ").strip().lower()

        if cmd == "start":
            mailbox.start()
            print("Monitoring started")

        elif cmd == "stop":
            mailbox.stop()
            print("Monitoring stopped")

        elif cmd == "quit":
            mailbox.stop()
            print("Exiting...")
            break

        else:
            print("Unknown command")


if __name__ == "__main__":
    main()
