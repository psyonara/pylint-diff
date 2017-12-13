import subprocess


def get_file_contents_from_branch(filename, branch_name):
    """
    Gets the contents of a file from a specific branch.
    :param filename: Name of the file
    :param branch_name: Name of the branch
    :return: Contents of the file
    """
    proc = subprocess.Popen(['git', 'show', '%s:%s' % (branch_name, filename)], stdout=subprocess.PIPE)
    return proc.stdout.read().decode()