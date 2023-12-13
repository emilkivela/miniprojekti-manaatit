*** Settings ***
Resource  resource.robot
Suite Setup  Run Keywords  Open And Configure Browser  AND  Register Test User And Login  AND  Create Test References
Suite Teardown  Run Keywords  Close Browser  AND  Clear Database

*** Variables ***
&{TEST_REF1} =  type=book  key=ERDS  title=Sefrverij  author=Gewfj Oewjif  year=908  publisher=Oefhi
&{TEST_REF2} =  type=article  key=WEF  title=Qtherok  author=Eqweji  journal=Ewfddf
...             year=1598  volume=4  pages=5
&{TEST_REF3} =  type=article  key=OGV  title=Iefwfeqp  author=Pjwreif  journal=Vfjew
...             year=234  volume=18  pages=567--569

*** Test Cases ***
#Try To Remove A Reference That Does Not Exist
#    Remove Reference  key=GRER
#    Reference Should Exist  &{TEST_REF1}
#    Reference Should Exist  &{TEST_REF2}
#    Reference Should Exist  &{TEST_REF3}

#Remove One Of Multiple References
#    Remove Reference  &{TEST_REF2}
#    Reference Should Exist  &{TEST_REF1}
#    Reference Should Exist  &{TEST_REF3}
#    Reference Should Not Exist  &{TEST_REF2}


*** Keywords ***
Create Test References
    Add Reference  &{TEST_REF1}
    Adding Reference Should Succeed
    Add Reference  &{TEST_REF2}
    Adding Reference Should Succeed
    Add Reference  &{TEST_REF3}
    Adding Reference Should Succeed
