"""Lantern: a tiny command-line task tracker."""
import argparse

import tasks


def main():
    parser = argparse.ArgumentParser(prog="lantern")
    sub = parser.add_subparsers(dest="command", required=True)

    add_parser = sub.add_parser("add")
    add_parser.add_argument("title")

    list_parser = sub.add_parser("list")

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


if __name__ == "__main__":
    main()

