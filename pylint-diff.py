import os

from git_functions import get_file_contents_from_branch, get_current_branch_name
from pylint_functions import get_pylint_score


def main():
    branch = get_current_branch_name()
    print(branch)
    if branch == 'master':
        print("Cannot run on master.")

    output = get_file_contents_from_branch("contacts/queries.py", "master")
    with open('contacts_queries.py', mode='w') as fh:
        fh.write(output)

    score1 = get_pylint_score('contacts_queries.py')
    os.remove('contacts_queries.py')
    score2 = get_pylint_score('contacts/queries.py')

    print('Master score: %s' % score1)
    print('Modified score: %s' % score2)
    print('Score diff: %s' % (score2 - score1))


if __name__ == "__main__":
    main()