import argparse

from robot.api import TestSuiteBuilder
from robot.model import SuiteVisitor, TestSuite


class TestCaseCollector(SuiteVisitor):
    def visit_suite(self, suite: TestSuite) -> None:
        for test in suite.tests:
            print(
                f"Test Case: {test.full_name}\n"
                f"Tags: {test.tags if test.tags else 'no tags were set'}\n"
                f"Documentation: {test.doc if test.doc else 'no documentation available'}\n"
            )
        for s in suite.suites:
            self.visit_suite(s)


def get_command_line_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="Test Case List",
        description="Lists the test cases in a specific test suite.",
    )
    parser.add_argument(
        "-v", "--version", action="version", version=f"{parser.prog} 1.0.0"
    )
    parser.add_argument(
        "-s",
        "--suite",
        type=str,
        required=True,
        help="Path to the test suite (folder or file).",
    )
    return parser.parse_args()


def collect_test_cases_from_suite(suite: str) -> None:
    root_suite = TestSuiteBuilder().build(suite)
    collector = TestCaseCollector()
    root_suite.visit(collector)


def main(suite: str) -> None:
    collect_test_cases_from_suite(suite)


if __name__ == "__main__":
    cli_args = get_command_line_arguments()
    main(cli_args.suite)
