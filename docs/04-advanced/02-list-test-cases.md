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

    You can use the `TestSuiteBuilder` class from the `robot.running` package to parse the test data in the given path.

    [Click here to learn more about using the `TestSuiteBuilder` class](https://robot-framework.readthedocs.io/en/latest/autodoc/robot.running.html#examples).

??? success "Solution: `tests/tools/test_case_list.py`"
    ``` python
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
    ```

## Results

In the `tests` folder, execute the following command.

``` bash
python ./tools/test_case_list.py --suite .
```

The output should look similar to the following:

    Root Suite: Tests
    -
    Test Case: Tests.01-Greetings.01-Greetings.Original Greetings
    Tags: [ubuntu]
    Documentation: This test case verifies that the Print Your Name keyword works as expected.
    -
    Test Case: Tests.01-Greetings.01-Greetings.Greetings Again
    Tags: [centos]
    Documentation: This test case proves that we can import variables from resource files.
    -
    ...

You can also list the test cases of a single `.robot` file.

``` bash
python ./tools/test_case_list.py --suite ./02-classroom/01-lists.robot
```

The output should look similar to the following:

    Root Suite: 01-Lists
    -
    Test Case: 01-Lists.Greetings Everyone
    Tags: [loop]
    Documentation: This test case verifies the functionality of the 'Print Multiple Names' keyword.
    -
    Test Case: 01-Lists.Students
    Tags: []
    Documentation: This test case logs the names from students.txt to the console.
    -
