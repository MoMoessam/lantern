"""Lantern: a tiny command-line task tracker."""
import argparse
import tasks
import export

def main():
    parser = argparse.ArgumentParser(prog="lantern")
    sub = parser.add_subparsers(dest="command", required=True)

    add_parser = sub.add_parser("add")
    add_parser.add_argument("title")

    export_parser = sub.add_parser("export")
    export_parser.add_argument("--csv", action="store_true", help="print tasks as CSV")

    list_parser = sub.add_parser("list")

    args = parser.parse_args()

    if args.command == "add":
        task = tasks.add_task(args.title)
        print(f"Added task: {task['title']}")
    elif args.command == "list":
        print(f"{len(tasks.list_tasks())} task(s)")

    elif args.command == "export":
        if args.csv:
            export.export_csv(tasks.list_tasks())

if __name__ == "__main__":
    main()

