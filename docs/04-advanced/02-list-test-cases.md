# 4.2. List test cases

## Goal

* Write a new Python script that lists the test cases in a given suite.
    * Create a new folder named `tools` in the `tests` folder and save your script in that folder as `test_case_list.py`.
    * The script should take the path to the suite as a command line argument (the path can point to a folder or to a `.robot` file).
    * The script should iterate through each suite in the specified path.

## Solution

!!! info "Hints"
    It is recommended to use the `argparse` module from the Python standard library to process command line arguments.

    [Click here to learn more about the `argparse` module](https://docs.python.org/3/library/argparse.html).

    You can use the `TestSuiteBuilder` class from the `robot.api` package to parse the test data in the given path.

    [Click here to learn more about using the `TestSuiteBuilder` class](https://robot-framework.readthedocs.io/en/latest/autodoc/robot.running.builder.html#robot.running.builder.builders.TestSuiteBuilder).

    You can create your own child class of `SuiteVisitor` and override the `visit_suite` function to collect necessary information about test cases.

    [Click here to learn more about using the `SuiteVisitor` class](https://robot-framework.readthedocs.io/en/latest/autodoc/robot.model.html#robot.model.visitor.SuiteVisitor).

??? success "Solution: `tests/tools/test_case_list.py`"
    ``` python
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
    ```

## Results

In the `tests` folder, execute the following command.

``` bash
python ./tools/test_case_list.py --suite .
```

The output should look similar to the following:

    Test Case: Tests.01-Greetings.01-Greetings.Original Greetings
    Tags: [ubuntu]
    Documentation: This test case verifies that the Print Your Name keyword works as expected.

    Test Case: Tests.01-Greetings.01-Greetings.Greetings Again
    Tags: [centos]
    Documentation: This test case proves that we can import variables from resource files.

    ...

    Test Case: Tests.03-Remote.01-Connection.Test Package Management
    Tags: no tags were set
    Documentation: no documentation available

You can also list the test cases of a single `.robot` file.

``` bash
python ./tools/test_case_list.py --suite ./02-classroom/01-lists.robot
```

The output should look similar to the following:

    Test Case: 01-Lists.Greetings Everyone
    Tags: [loop]
    Documentation: This test case verifies the functionality of the 'Print Multiple Names' keyword.

    Test Case: 01-Lists.Students
    Tags: no tags were set
    Documentation: This test case logs the names from students.txt to the console.
