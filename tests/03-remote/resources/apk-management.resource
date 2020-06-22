*** Keywords ***
APK Search
    [Documentation]    This keyword searches package(s) by the given `pattern`
    ...    on the given `remote_host`.
    [Arguments]    ${remote_host}    ${package_name}

    Switch Connection    ${remote_host}
    ${stdout}    ${rc}=    Execute Command
    ...    apk search ${package_name}
    ...    return_rc=${TRUE}

    Should Be Equal As Integers    ${rc}    0
    Log To Console    ${\n}The following packages were found: ${stdout}
