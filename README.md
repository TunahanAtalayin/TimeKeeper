# TimeKeeper
Agent project

## Description
This project simulates a simple appointment system using **Python** and the **SPADE** library. It demonstrates how two autonomous agents communicate.

* **Scheduler Agent:** Holds the daily calendar. It checks if a requested time is free or busy.
* **Client Agent:** Sends a request for a specific time (e.g., 13:00) and waits for a reply.

## Installation
1.  You need Python installed.
2.  Install the library:
    ```bash
    pip install spade
    ```

## How to Run
1.  Open `main.py`.
2.  Enter your XMPP username and password in the top section:
    ```python
    Schedular_ID = "Scheduler@jabbim.com"
    CLIENT_ID = "RequestSender@jabbim.com"
    ```
3.  Run the code:
    ```bash
    python main.py
    ```

## Scenario
1.  The **Client** sends a message: *"13:00"*.
2.  The **Scheduler** checks its internal list.
3.  Since 13:00 is busy, the Scheduler replies: *"BUSY: That time slot is taken."*
