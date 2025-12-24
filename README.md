# IoT Mailbox Simulator (Python CLI)

This project simulates an Internet of Things (IoT)–enabled physical mailbox that detects when the mailbox door is opened or closed based on changes in internal light levels.

The simulator is implemented as a **Python command-line application** and focuses on core systems concepts such as callbacks, background monitoring, and clean start/stop control.

---

## Project Overview

A real IoT mailbox might contain a light sensor that detects when the door is opened.  
This simulator models that behavior by:

- Periodically sampling a simulated light level
- Using a callback function to notify other parts of the system
- Running monitoring logic in a background thread
- Allowing the user to start and stop monitoring via a CLI

Positive light levels represent an **open** mailbox door, while negative values represent a **closed** door.

---

## Key Concepts Demonstrated

- Callback-based communication between components
- Background execution using threads
- Clean start/stop lifecycle management
- Separation of concerns (sensor logic vs. control logic)
- CLI-driven testing of asynchronous systems

These concepts closely mirror patterns used in embedded systems, monitoring IP, and verification tooling.

---

## Project Structure
iot_mailbox_sim/
├── src/
│ ├── init.py
│ └── mailbox.py # IoT mailbox sensor logic
├── scripts/
│ └── run_sim.py # CLI entry point
├── README.md
└── .gitignore


---

## How to Run

From the project root:

```bash
python3 -m scripts.run_sim

Available commands:
- start — begin monitoring the mailbox
- stop — stop monitoring
- quit — exit the program

Example Output
Commands: start | stop | quit
> start
Light level: 0.62 -> Door OPEN
Light level: -0.41 -> Door CLOSED
> stop
Monitoring stopped

## Future Improvements 
Event-based notifications instead of per-sample printing
Logging to file for regression-style analysis
Configurable alert thresholds (e.g., door left open)
Web-based dashboard frontend

Author
Taha Iqbal
Electrical Engineering Student
University of Saskatchewan