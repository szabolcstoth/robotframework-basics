import argparse
from robot.api import TestSuiteBuilder


def get_command_line_arguments():
    parser = argparse.ArgumentParser(
        prog='Test Case List',
        description='Lists the test cases in a specific test suite.'
    )
    parser.add_argument(
        '-v', '--version',
        action='version',
        version=f'{parser.prog} 1.0.0'
    )
    parser.add_argument(
        '-s', '--suite',
        type=str,
        help='Path to the root folder (or file) of the test suite.'
    )
    return parser.parse_args()


def list_test_cases_from_suite(parent_suite, full_path_to_suite):
    for test_case in parent_suite.tests:
        print(f'Test Case: {full_path_to_suite}.{test_case.name}')
        print(f'Tags: {test_case.tags}')
        print(f'Documentation: {test_case.doc}\n-')


def visit_test_suites(parent_suite, full_path_to_suite):
    list_test_cases_from_suite(parent_suite, full_path_to_suite)

    for suite in parent_suite.suites:
        new_path = f'{full_path_to_suite}.{suite.name}'
        if suite.tests:
            list_test_cases_from_suite(suite, new_path)
        if suite.suites:
            visit_test_suites(suite, new_path)


def main():
    root_suite = TestSuiteBuilder().build(CLI_ARGS.suite)
    print(f'Root Suite: {root_suite.name}\n-')
    visit_test_suites(root_suite, root_suite.name)


if __name__ == '__main__':
    CLI_ARGS = get_command_line_arguments()
    main()
