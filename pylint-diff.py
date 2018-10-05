import argparse
import os

from git_functions import get_file_contents_from_branch, get_current_branch_name
from pylint_functions import get_pylint_score


def main():
    parser = argparse.ArgumentParser(
        description="Calculate the pylint score difference between two branches for a particular file."
    )
    parser.add_argument(
        "file_name", help="The path to the file name that should be compared across two branches."
    )
    args = parser.parse_args()
    branch = get_current_branch_name()
    print(branch)
    if branch == "master":
        print("Cannot run on master.")

    if not os.path.isdir("temp"):
        os.makedirs("temp")

    output = get_file_contents_from_branch(args.file_name, "master")
    with open(f"temp/{args.file_name}", mode="w") as fh:
        fh.write(output)

    score1 = get_pylint_score(args.file_name)
    os.remove(f"temp/{args.file_name}")
    score2 = get_pylint_score(args.file_name)

    print("Master score: %s" % score1)
    print("Modified score: %s" % score2)
    print("Score diff: %s" % (score2 - score1))


if __name__ == "__main__":
    main()
