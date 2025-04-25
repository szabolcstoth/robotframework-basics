# 5.1. Libdoc

## Goal

* If you have large test libraries, it is good to have all the keywords well documented so that you can create keyword documentation for the libraries that can be shared among developers.
* Generate documentation for `JSONLibrary`.

## Solution

!!! info "Hints"
    Robot Framework has a built-in tool named `Libdoc` for generating keyword documentation.

    [Click here to learn more about how to use `Libdoc`](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#library-documentation-tool-libdoc).

## Results

In the `tests` folder, execute the following command.

``` bash
python -m robot.libdoc ./libraries/JSONLibrary.py ./JSONLibrary.html
```

You can check the generated `JSONLibrary.html` file to see the keyword documentation.
