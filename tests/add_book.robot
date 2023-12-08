*** Settings ***
Resource  book_resource.robot
Suite Setup  Run Keywords  Open And Configure Browser  AND  Register Test User And Login
Suite Teardown  Close Browser And Clear Database
Test Setup  Go To Book Adding Page And Clear Database

*** Test Cases ***
Add Book With Valid Info
    Add Reference  type=book  key=XXX  title=Jdsfh Yeshd  author=Ewdkos Kdiffs  year=1876  publisher=Rwjfiji
    Adding Reference Should Succeed

Add Book With Key Missing
    Add Reference  type=book  title=Jdsfh Yeshd  author=Ewdkos Kdiffs  year=1876  publisher=Rwjfiji
    Adding Reference Should Fail With Message  All fields must be filled

Add Book With Title Missing
    Add Reference  type=book  key=BBB  author=Ewdkos Kdiffs  year=1876  publisher=Rwjfiji
    Adding Reference Should Fail With Message  All fields must be filled

Add Book With Author Missing
    Add Reference  type=book  key=CCC  title=Jdsfh Yeshd  year=1876  publisher=Rwjfiji
    Adding Reference Should Fail With Message  All fields must be filled

Add Book With Year Missing
    Add Reference  type=book  key=DDD  title=Jdsfh Yeshd  author=Ewdkos Kdiffs  publisher=Rwjfiji
    Adding Reference Should Fail With Message  All fields must be filled

Add Book With Publisher Missing
    Add Reference  type=book  key=DDD  title=Jdsfh Yeshd  author=Ewdkos Kdiffs  year=1876
    Adding Reference Should Fail With Message  All fields must be filled

Add Book With Non-Numeric Year
    Add Reference  type=book  key=EEE  title=Jdsfh Yeshd  author=Ewdkos Kdiffs  year=18r6  publisher=Rwjfiji
    Adding Reference Should Fail With Message  Year must be a number
