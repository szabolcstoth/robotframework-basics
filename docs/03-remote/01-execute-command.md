# 3.1. Execute Command

## Goal

* Create a new test suite named `03-Remote`, which has a suite named `01-connection`.
* Create a new keyword named `Open Connection And Log In With Password` that will connect to the remote host.
* Create a new test case named `Get Date From Remote Host` that executes the `date` command on the remote host and logs the output to the console.

## Solution

!!! info "Hints"
    You can use `SSHLibrary` to open a connection to a remote host using `SSH`.

    [Click here to learn more about `SSHLibrary` and its keywords.](https://marketsquare.github.io/SSHLibrary/SSHLibrary.html).

??? success "Solution: `tests/03-remote/01-connection.robot`"
    ``` robotframework
    *** Test Cases ***
    Get Date From Remote Host
        Switch Connection    ${HOST}[alias]
        ${date}=    Execute Command    date

        Log To Console    ${date}

    *** Keywords ***
    Open Connection And Log In With Password
        Open Connection
        ...    ${HOST}[name]
        ...    port=${HOST}[port]
        ...    alias=${HOST}[alias]

        Login
        ...    ${AUTH}[username]
        ...    ${AUTH}[password]

    *** Settings ***
    Library        SSHLibrary
    Suite Setup    Open Connection And Log In With Password

    *** Variables ***
    &{HOST}    name=localhost    port=2222    alias=openssh-server-for-robot
    &{AUTH}    username=robotdev    password=Hn7c5%lyBpIn8*8Z
    ```

## Results

In the `tests` folder, execute the following command to execute the `03-Remote` suite.

``` bash
robot --suite 03-remote .
```

The output should look similar to the following:

    ==============================================================================
    Tests.03-Remote                                                               
    ==============================================================================
    Tests.03-Remote.01-Connection                                                 
    ==============================================================================
    Get Date From Remote Host                                             ..Sun Jun 14 21:13:28 CEST 2020
    Get Date From Remote Host                                             | PASS |

You can check the generated `log.html` file to see how your test cases worked.
