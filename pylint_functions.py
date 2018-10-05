from pylint.lint import Run


def get_pylint_score(filename):
    """
    Gets the pylint score for a file.
    :param filename: Name of the file
    :return: Pylint score
    """
    result = Run([filename, "--reports=n"], do_exit=False)
    return result.linter.stats["global_note"]
