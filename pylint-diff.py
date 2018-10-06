import argparse
import os

from git_functions import get_file_contents_from_branch, get_current_branch_name, is_branch_merged, \
    uncommitted_changes_present, get_changed_files
from pylint_functions import get_pylint_score


def main():
    parser = argparse.ArgumentParser(
        description="Calculate the pylint score difference between two branches for a particular file."
    )
    parser.add_argument(
        "-f", "--file_name", dest="file_name", help="The path to the file name that should be compared across two branches."
    )
    args = parser.parse_args()

    branch = get_current_branch_name()
    if branch == "master":
        print("Cannot run on master.")
        return

    if is_branch_merged("master") is False:
        print("Master must be merged into current branch")
        return

    if uncommitted_changes_present() is True:
        print("Warning: Uncommitted changes are present, and will not be included.")

    if args.file_name:
        file_names = [args.file_name] if args.file_name.endswith(".py") else []
    else:
        file_names = [file_name for file_name in get_changed_files("master", branch) if file_name.endswith(".py")]

    if not file_names:
        print("No valid files specified.")
        return

    if not os.path.isdir("temp"):
        os.makedirs("temp")

    for file_name in file_names:
        output = get_file_contents_from_branch(file_name, "master")
        with open(f"temp/{file_name}", mode="w") as fh:
            fh.write(output)

        score1 = get_pylint_score(file_name)
        os.remove(f"temp/{file_name}")
        score2 = get_pylint_score(file_name)

        print("Master score: %s" % score1)
        print("Modified score: %s" % score2)
        print("Score diff: %s" % (score2 - score1))


if __name__ == "__main__":
    main()
