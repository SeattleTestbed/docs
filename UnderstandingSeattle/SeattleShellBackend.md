Seash (also known as Seattle Shell) is the command line interface for interacting with Seattle VMs.  This will describe how seash is designed.  If you are a user interested in learning how to use Seash, please go to the [SeattleShell main Seattle Shell page].





## Command Dictionary
----

The command dictionary contains command nodes that determine how seash responds to various input. Each command node represents a recognized command keyword, and may have child command nodes that represent keywords that should come after that command. Seash will use this dictionary to check if an input string matches a path through the command dictionary, and if it does, executes the command at the terminating node.

Each command node is defined in the following manner:

```python
command_dict = { 
  'mycommandtoken': {
    'name': 'tokenname',
    'callback': command_callback,
    'summary': 'summary text for the command',
    'help_text': 'comprehensive help text for the command',
    'display_keyword': 'display this command in the list of commands when the help command contains this display keyword.',
    'children': {} # command dictionaries of subsequent child commands
  }
}
```

 * mycommandtoken: What the user should input to use this command. This should be a single word. If the user should type in 'browse', then this should be 'browse'. This can also be a user-entered argument. These arguments include [TARGET], [FILENAME], [KEYNAME], and [ARGUMENT]. 
 * name: A unique tag that can be used in the callback function to identify a specific token.
 * callback: The callback function to run if this command was entered. It should take two parameters: an input_dict that contains the parsed input as a command dictionary, as well as an environmentdict that describes seash's current state.
 * summary: A short summary of what the command does.
 * help_text: A detailed explanation of what the command should do and can do.
 * display_keyword: When showing help for a command, the summaries of any sub-commands are shown. This is the keyword that should be specified in order for this summary to show. Omit this if a command should be shown by default.
 * children: A dictionary containing command tokens that map to command nodes for subsequent commands.

The root dictionary is treated as a list of children. Therefore, the command dictionary should be as such (everything except for the command names are hidden for ease of reading):
```python
command_dictionary = {
  'show': {
    ...
    'users': {...}
    ...
  },
  'add': {
    ...
    '[GROUP]': {...}
    ...
  },
  ...
}
```


## Defining New Modules
----

Seash has support for adding additional commands via modules that are imported on startup. These modules should be placed in a subdirectory within the /modules/ folder. These modules are standard python packages.



### Creating a Module
Defining a module is relatively straightforward.  First, create the ```__init__.py``` file that contains the ```moduledata``` dictionary in the module namespace that is loaded by the module importer.  It should look like the following:

```python
# The actual definitions of command_dict, module_help, and input_preprocessor are in 
# subsequent sections to improve readability of this example.
moduledata = {
  'command_dict': command_dict,
  'help_text': module_help,
  'url': "http://update.url/",
  'input_preprocessor': input_preprocessor,
}
```


#### The Command Dictionary

The command_dict defines all the commands that are to be part of the module.  These command_dicts should be specified in a similar manner as described in the command dictionary section above.

```python
command_dict = {
  'show': {'children': {
    'location':{
      'name':'location',
      'callback': show_location_callback,
      'summary': "Display location information (countries) for the nodes",
      'help_text':"""...""",}},
    'coordinates':{
      'name':'coordinates',
      'callback': show_coordinates_callback,
      'summary':'Display the latitude & longitude of the node',
      'help_text':"""...""",}
```


#### Module Level Documentation
You must also have module-level documentation.

```python
module_help = """
GeoIP Module

This module includes commands that provide information regarding VMs' geographical 
locations.  To get started using this module, acquire several VMs through the Seattle
Clearinghouse, use the 'browse' command, and then in any group, run either 'show location' 
or 'show coordinates'.
"""
```


#### Automatic Updating
You must also specify an update URL to where your module can be found.  This will be used with the updater to automatically update the module.  To disable this feature, set the URL to ```None```.  Note, this is not functional yet.  All modules should not have this set until then.
```python
# This is already set in the moduledata above so this is no longer needed.
# It is only shown as an example.  Set it to None if you do not want to 
# support updating.
moduledata['url'] = "http://update.url/"
```



#### Input Preprocessor
The input preprocessor is available for modules to tap into raw input from the command line to perform initial preprocessing.  This is used especially in the variables module.  This preprocessor will be given one string as input, and must return one string representing the results of the preprocessing.  

This example is a simple example that replaces every instance of $USERPORT with a user's port.
```python
def input_preprocessor(user_input):
  port_token = '$USERPORT'
  retstr = ''
  # Hardcoded for now, probably should be looked up
  # through SeattleClearinghouseClient
  user_port = 63100
  while port_token in user_input:
    before, port_token, user_input = user_input.partition(port_token)
    retstr += before + user_port
  else:
    retstr += user_input
  return retstr
```