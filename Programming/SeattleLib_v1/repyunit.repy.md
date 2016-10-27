# repyunit.repy

A unit testing suite for repy. Based on JUnit in java and the Python unittest suite. See http://docs.python.org/library/unittest.html for more information.


### Classes & Functions

```
class repyunit_TestResult(object):
```
   Hold test result statistics and process test outcomes. Subclasses may extend this class to provide additional functionality, like printing output.

   The test_count instance member holds the number of tests executed; success_count holds the number of tests executed that were successful,    failure_count holds the number of tests executed that have failed, error_count holds the number of tests executed that resulted in an error.

 

 
```
class repyunit_TestCase(object):
```
   Encapsulate a test case. This class is the workhorse of the module. It defines the methods required to run tests by extending the class. 

   Under regular Python, the class name would be extracted automatically, but this is not possible in Repy. Thus, subclasses must override the    get_class_name method. For the same reasons, subclasses must also override the get_test_method_names method if run_test is not overwritten or when additional tests are defined.




```
class repyunit_TestSuite(object):
```
   Encapsulate a collection of unit tests. This class is used to group together repyunit_TestCase instances for execution.




```
def repyunit_load_tests_from_test_case(test_case):
```
   Populate a repyunit_TestSuite with all tests from a repyunit_TestCase to run all the tests automatically.

   Notes:

   * test_case is the repyunit_TestCase from which to populate the repyunit_TestSuite.
   * Returns a repyunit_TestSuite loaded with all the tests from the given test case.




```
def repyunit_text_test_run(test_case):
```
   Run all tests given in test and print statistical information in textual format.

   Notes: 

   * test_case is a repyunit_TestCase or repyunit_TestSuite to run the test(s).
   * Prints in the following form:
   ``` Ran %d tests: %d successes, %d failures, %d errors ```



### Usage

To get the testing results.
```
   test = FoobarTestSuite()
   test.run(repyunit_TestResult())
```



To run testing cases.
```
    class FooTestCase(repyunit_TestCase):
      def get_class_name(self):
        return "FooTestCase"
      def run_test(self):
        self.assert_true(True)

    test = FooTestCase()
    test.run()
```



To run a testing suite.
```
suite = repyunit_TestSuite().
suite.add_test(FoobarTest())
suite.add_test(FoobarTest("test_baz"))
suite.run(CustomTestResult())
```