from datetime import datetime
import os


def initialize_file():
    if not os.path.exists("attendance.txt"):
        with open("attendance.txt", "w") as file:
            pass

def mark_attendance():
    initialize_file()
    date_str = datetime.now().strftime("%d-%m-%Y")
    print(f"\n  Attendance for {date_str}   ")


    with open("attendance.txt", "a") as file:
        while True:
            student = input("Enter student name  (or type 'done' to finish): ").strip()
            if student.lower()== 'done':
                break

            if not student:
                print("Name cannot  be empty")
                continue


            status = input(f"Is {student} Present?  (Y/N): ").strip().upper()
            while status not in ['Y', 'N']:
                status = input("Invalid input. Enter Y for Present or N for Absent: ").strip().upper()

            final_status = "Present" if status == 'Y' else "Absent"
            file.write(f"{date_str} | {student} | {final_status}\n")
            print(f"Recorded: {student} - {final_status}")

def view_attendance_summary():

    if not os.path.exists("attendance.txt")  or os.path.getsize("attendance.txt") == 0:
        print("\n No Attendance records found.")
        return

    summary = {}
    print("\n    Attendance Summary ")

    with open("attendance.txt", "r") as file:
        for line in file:
            if "|" in line:
                parts = line.strip().split(" | ")
                if len(parts) == 3:
                    _, student, status = parts
                    if student not in summary:
                        summary[student] = 0

                    if status == "Present":
                        summary[student] += 1


    print(f"{'Student':<20} | {'Days Present':<5}")
    print("-" * 30)
    for student, count in sorted(summary.items()):
        print(f"{student:<20} | {count:<5}")


def main():
    while True:
        print("\n==== ATTENDANCE TRACKING SYSTEM =====")
        print("1.  Mark Daily Attendance")
        print("2. View Presence Summary")
        print("3. Exit")

        choice = input("Select an option: ").strip()
        if choice == '1':
            mark_attendance()

        elif choice == '2':
            view_attendance_summary()

        elif choice == '3':
            print("Exiting")

        else:
            print("Invalid selection. Please choice 1, 2, or 3. ")


if __name__ == "__main__":
    main()



