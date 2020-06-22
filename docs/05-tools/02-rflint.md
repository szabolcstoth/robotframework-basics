# 5.2. RFlint

## Goal

* It is always good to have an automated tool to check the syntax of your test code.
* Run `RFlint` to check all your files.

## Solution

!!! info "Hints"
    `RFlint` is a static analysis tool which can be used to check your Robot Framework related files.

    [Click here to learn more about `RFlint`](https://github.com/boakley/robotframework-lint).

## Results

Inside the `tests` folder, execute the following command.

``` bash
rflint --recursive .
```

You can list all the available rules by executing the following command.

``` bash
rflint --list
```

You can check the details of a rule by executing the following command.

``` bash
rflint --describe RequireKeywordDocumentation
```