"""Lantern: a tiny command-line task tracker."""
import argparse
import tasks

def main():
    parser = argparse.ArgumentParser(prog="lantern")
    sub = parser.add_subparsers(dest="command", required=True)

    add_parser = sub.add_parser("add")
    add_parser.add_argument("title")

    list_parser = sub.add_parser("list")
    list_parser.add_argument("--done",action="store_true",help="show only completed tasks")
    args = parser.parse_args()

    if args.command == "add":
        task = tasks.add_task(args.title)
        print(f"Added task: {task['title']}")
    elif args.command == "list":
        if not tasks.list_tasks():
            print("No tasks found.")
        else:
            for task in tasks.list_tasks():
                print(f"- {task['title']}")

            print(f"{len(tasks.list_tasks())} task(s)")

        all_tasks = tasks.list_tasks()
        if args.done:
            all_tasks = [t for t in all_tasks if t.get("done", False)]
        for t in all_tasks:
            print(t["title"])
        print(f"{len(all_tasks)} task(s)")

if __name__ == "__main__":
    main()

