# argparse.repy

This module contains several functions to check for command line arguments. Similar to getopt()/getopts() in C. See http://docs.python.org/library/getopt.html for more details.

### Functions


```
def argparse_scan_bool(args_array, flag_name, default_value = False):
```
   This function checks to see if a FLAG (flag_name) was passed as an argument.

   Notes: 

   * Careful that another parameter will not have the same name as the flag you're looking for.
   * args_array is the complete array of arguments.
   * flag_name is the flag we're looking for. Can have any naming format, e.g.: --local or /local or -local
   * default_value is 'False' unless otherwise specified.
   * Returns True if the flag_name was found in the list of arguments. Returns default_value if it was not.
 

```
def argparse_scan_str(args_array, flag_name, default_value = False):
```
   This function checks to see if a FLAG (flag_name) exists, and then takes the very next "word" and returns it as the argument.

   Note:

   * Careful that another parameter will not have the same name as the flag you're looking for.
   * args_array is the complete array of arguments.
   * flag_name is the flag we're looking for. Can have any naming format, e.g.: --local or /local or -local
   * default_value is 'False' unless otherwise specified.
   * If the flag exists, then the value directly following it will be returned as a string. If the value does not exist, then the function returns the default_value.



```
def argparse_scan_int(args_array, flag_name, default_value = False):
```
   This function checks to see if a FLAG (flag_name) exists, and then takes the very next "word" and returns it as the argument. This function is    different from scan_str as it will expect an integer to follow the flag name, and will raise an error if the value following is NOT an integer.

   Note:

   * Careful that another parameter will not have the same name as the flag you're looking for.
   * args_array is the complete array of arguments.
   * flag_name is the flag we're looking for. Can have any naming format, e.g.: --local or /local or -local
   * default_value is 'False' unless otherwise specified.
   * If the flag exists, then the value directly following it will be returned as a string (but guarantee to be able to cast to integer type). If the value does not exist, then the function returns default_value. 


### Usage


```
 argparse_scan_str(callargs, '-ip')
    returns False if no -ip flag
    returns string containing ip (parameter following -ip flag)
  argparse_scan_bool(callargs, '--local')
    returns False if no --local flag is set
    returns True if --local flag is set
  argparse_scan_int(callargs, '/port')
    returns False if no /port flag is set
    returns a string (ensures castable to int) following the
    
  Note: False is the default return value for all the functions if a
    default return value is not specified on function call.
  Note: See individual functions for detailed information.
```


```
#scan boolean example
if scan_bool(callargs, '--local'): # we have the argument!
      ... your code ...
```


```
#scan string example
temp_ip = scan_str(callargs, '--ip'):
    if temp_ip: # we have an IP!
      ip = temp_ip
```