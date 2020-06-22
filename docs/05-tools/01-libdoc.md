# 5.1. Libdoc

## Goal

* If you have large test libraries, it is good to have all the keywords well documented, so you can generate keyword documentation for the libraries which can be used among the developers.
* Generate documentation for `JSONLibrary`.

## Solution

!!! info "Hints"
    Robot Framework has a built-in tool named `Libdoc` for generating keyword documentation.

    [Click here to learn more about `Libdoc`](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#libdoc).

## Results

Inside the `tests` folder, execute the following command.

``` bash
python -m robot.libdoc ./libraries/JSONLibrary.py ./JSONLibrary.html
```

You can check the generated `JSONLibrary.html` file to see the keyword documentation.
