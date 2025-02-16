import time
import os
import signal

class PomodoroTimer:
    def __init__(self, work_time=25, break_time=5, long_break_time=15, sessions=4):
        self.work_time = work_time * 60
        self.break_time = break_time * 60
        self.long_break_time = long_break_time * 60
        self.sessions = sessions
        self.current_session = 1
        self.running = True

    def start_timer(self):
        def signal_handler(sig, frame):
            self.running = False
            print("\nTimer interrupted. Exiting gracefully.")

        signal.signal(signal.SIGINT, signal_handler)  # Handle Ctrl+C

        while self.running and self.current_session <= self.sessions:
            print(f"Session {self.current_session}/{self.sessions}: Work time!")
            self.run_timer(self.work_time)
            if not self.running: break

            if self.current_session < self.sessions:
                print("Break time!")
                self.run_timer(self.break_time)
                if not self.running: break
            else:
                print("Long break time!")
                self.run_timer(self.long_break_time)
                if not self.running: break

            self.current_session += 1

        if self.running:
            print("Pomodoro complete!")

    def run_timer(self, duration):
        start_time = time.time()
        end_time = start_time + duration

        while self.running and time.time() < end_time:
            remaining_time = int(end_time - time.time())
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            print(f"{minutes:02d}:{seconds:02d}", end="\r")
            time.sleep(1)

if __name__ == "__main__":
    work_minutes = int(input("Enter work time (minutes): ") or 25)
    break_minutes = int(input("Enter break time (minutes): ") or 5)
    long_break_minutes = int(input("Enter long break time (minutes): ") or 15)
    num_sessions = int(input("Enter number of sessions: ") or 4)

    timer = PomodoroTimer(work_minutes, break_minutes, long_break_minutes, num_sessions)
    timer.start_timer()
