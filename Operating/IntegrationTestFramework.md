# Writing Integration Tests for Seattle

----

----



## Introduction
----
The purpose of this document is to guide any Seattle developers in how to create integration tests. These integrations will be used to run some sort of test and email the required people (usually the system admins) in case the tests fail. 



## Imports
----
These are the files that need to be imported in order to setup and run the integration tests properly. All these files are located in trunk/integrationtests/common/
 1. send_gmail.py
 1. integrationtestlib.py
 1. seattle_gmail_info
 1. irc_seattlebot.py (Optional - import this if you want to send messages on the irc)



## Initializing the Integration Tests
----
In order to set up the integration tests, we must first initialize the send_gmail so on failure the integration test emails the required developers. In the main function of the test have the following line of code before any testing is done:
```
success,explanation_str = send_gmail.init_gmail()

if not success:
  integrationtestlib.log(explanation_str)
  sys.exit(0)
```

This ensures that the gmail user name and password are set up.



## Key Functions
----
 1. integrationtestlib.py
  1. log(msg) - This function just prints a time stamp as well as the message that is passed along. This function is used when the developer wants to log some information.
  1. notify(text, subject) - This function is used to notify the required developers if the test fails. The <string> text that is passed in as input is the message that is emailed to the developers and the <string> subject is used as the subject of the email. Currently the emails that are notified are "ivan@cs.washington.edu", "justinc@cs.washington.edu" and "monzum@u.washington.edu". This email list resides in integrationtestlib.py. An example of usage would be:
```
#test_fail is a boolean
if test_fail:
  integrationtestlib.notify("Error: The test has failed!!", "test_fail notification")
```
  1. handle_exception(text, subject) - This function is used with a try and except block. This function should be called if you expect there to be some kind of error that will be printed in StdErr. This function sends an email to the developer as well as send them a traceback of the failure. An example of usage would be:
```
try:
  run_test()
except:
  integrationtestlib.handle_exception("run_test failed", "run_test fail notification")
  sys.exit(0)
```
 1. irc_seattlebot.py
  1. send_msg(message_string) - This function is used to send a message on irc on the server irc.freenode.net and on the channel #seattle. An example of use would be:
```
if test_fail:
  irc_seattlebot.send_msg("Error: The test has failed!!")  
```

If anyone has further questions or need help writing integration tests, please contact Monzur Muhammad at monzum@cs.washington.edu.