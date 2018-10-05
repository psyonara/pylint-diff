import subprocess


def is_branch_merged(branch):
    """
    Checks if given branch is merged into current branch.
    :param branch: Name of branch
    :return: True/False
    """
    proc = subprocess.Popen(["git", "branch", "--merged"], stdout=subprocess.PIPE)
    result = proc.stdout.read().decode()
    return branch in result.strip().split("\n")


def get_file_contents_from_branch(filename, branch_name):
    """
    Gets the contents of a file from a specific branch.
    :param filename: Name of the file
    :param branch_name: Name of the branch
    :return: Contents of the file
    """
    proc = subprocess.Popen(
        ["git", "show", "%s:%s" % (branch_name, filename)], stdout=subprocess.PIPE
    )
    return proc.stdout.read().decode()


def get_current_branch_name():
    """
    Gets the name of the current git branch in the working directory.
    :return: Name of the branch
    """
    proc = subprocess.Popen(["git", "rev-parse", "--abbrev-ref", "HEAD"], stdout=subprocess.PIPE)
    return proc.stdout.read().decode()


def get_changed_files(branch1, branch2):
    """
    Gets a list of changed files between two branches.
    :param branch1: name of first branch
    :param branch2: name of second branch
    :return: A list of changed files
    """
    proc = subprocess.Popen(
        ["git", "diff", "--name-only", branch1, branch2], stdout=subprocess.PIPE
    )
    return proc.stdout.read().decode()
