*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Run Keywords  Close Browser  AND  Clear Database
Test Setup  Run Keywords  Clear Database  AND  Register Test Users  AND  Create Test References

*** Variables ***
&{TEST_REF1} =  type=book  key=ERDS  title=Sefrverij  author=Gewfj Oewjif  year=908  publisher=Oefhi
&{TEST_REF2} =  type=article  key=WEF  title=Qtherok  author=Eqweji  journal=Ewfddf
...             year=1598  volume=4  pages=5
&{TEST_REF3} =  type=article  key=OGV  title=Iefwfeqp  author=Pjwreif  journal=Vfjew
...             year=234  volume=18  pages=567--569

*** Test Cases ***
Remove One Of Multiple References
    Log In With Credentials  kalle  kalle123
    Remove Reference  &{TEST_REF2}
    Reference Should Exist  &{TEST_REF1}
    Reference Should Exist  &{TEST_REF3}
    Reference Should Not Exist  &{TEST_REF2}
    Sign Out

Remove A Reference That Has The Same Key As Another User's Reference
    Log In With Credentials  kalle  kalle123
    Add Reference  &{Test Book}
    Sign Out
    Log In With Credentials  jussi  jussi456
    Add Reference  &{Test Book}
    Remove Reference  &{Test Book}
    Go To Home Page
    Wait Until Page Contains  Article references
    Page Should Not Contain  ${Test Book}[key]
    Sign Out
    Log In With Credentials  kalle  kalle123
    Go To Home Page
    Wait Until Page Contains  Article references
    Page Should Contain  ${Test Book}[key]
    Sign Out

*** Keywords ***
Register Test Users
    Register With Credentials  kalle  kalle123
    Register With Credentials  jussi  jussi456

Create Test References
    Log In With Credentials  kalle  kalle123
    Add Reference  &{TEST_REF1}
    Adding Reference Should Succeed
    Add Reference  &{TEST_REF2}
    Adding Reference Should Succeed
    Add Reference  &{TEST_REF3}
    Adding Reference Should Succeed
    Sign Out
