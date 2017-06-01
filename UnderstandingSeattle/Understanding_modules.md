# Extensions Module Implementation
With the expansion of Repy and addition of new extensions like IPv6 support, https, sensibility or any future possible extensions, it would be benificial to structure these extensions into python modules. Various current and upcoming extenstions can be structured into modules. For more information on the modules can be created in python, [click here](https://docs.python.org/2/tutorial/modules.html)

## Understanding Modules for IPv6
Current and any upcoming extensions can be structured as modules in python. Let us discuss this module structure with an example of IPv6 extension, similar steps can be followed for other extensions. Our example involves the use of module called ```extensions``` with its subpackages, this is given [here](https://github.com/ankitbhatia32/repy_v2/tree/repy_extensions). We assume you have been through build instructions of Repy_V2 and have clear understanding of how build process works, if not [click here](https://github.com/SeattleTestbed/docs/blob/master/Contributing/BuildInstructions.md) and then try to comprehend the following steps given as follows:
  1. First of all it is important to understand modules given in python documenatation given [here](https://docs.python.org/2/tutorial/modules.html). Understand how you want to structure modules. We have structured our IPv6 extension as follows:

               ```extensions/                  		Top-level package
      					__init__.py            		Initialize the package
      					ipv6/                  		Subpackage 
              				  __init__.py
              				  emulcomm_ipv6.py```

  As we can see we have "extensions" as a top level module/package then inside we have "ipv6" in which finally we have our IPv6 python script i.e. ```emulcomm_ipv6.py``` which we need, this python file contains the IPv6 API functions defined. This structure is given [here](https://github.com/ankitbhatia32/repy_v2/tree/repy_extensions) Go through the extensions module and it will be similar to the given above. 

  2. One of the key asspects of running Repy_V2 involves the building process which involves two things i.e. the initializing and building, also their corresponding "config" txt file. Initialize as we know fetch the dependencies defined. So in our case we need to define dependent repositories in ```config_initialize.txt```. The dependent repository is given [here](https://github.com/ankitbhatia32/repy_v2/tree/repy_extensions), this involves the repository on which we have added our modules. Update in the ```config_initialize.txt``` file is given [here](https://github.com/ankitbhatia32/repy_v2/blob/repy_extensions/scripts/config_initialize.txt#L7)

  Note: If the dependent repository is a branch, the address should be given accordingly.

  Now for building, the ```config_build.txt``` provides ```build_component.py``` with the names and paths of necessary files that are to be copied over from the cloned repos to the target directory to build the required Seattle component. In our case the path name for building components is the following:
                  
                  ```./extensions/ipv6/* extensions/ipv6```

  This is also given [here](https://github.com/ankitbhatia32/repy_v2/blob/repy_extensions/scripts/config_build.txt#L8-L9). Build file need to have path name for the Repy runtime that the custominstallerbuilder requires. Now with understanding of the build process the above path names represents the extensions module with sub module, on building will add that module to the ```RUNNABLE``` directory or the Target directory created for execution in the Repy.

  3. Now coming onto running our API function we need to import our module in our ```namespace.py```. You can clearly understand how to import module in python. This for our IPv6 implementation is given as follows:

                 ```import extensions.ipv6.emulcomm_ipv6```
  
  This is represented [here](https://github.com/ankitbhatia32/repy_v2/blob/repy_extensions/namespace.py#L125). This imports our extension module and its subpackages and file i.e. here ```extensions``` is module with ```ipv6``` as subpackage containing our ```emmulcomm_ipv6.py``` which is a python file containing all our IPv6 API functions, in our implementation for IPv6 we need to use these functions given in ```emulcomm_ipv6.py```. 

  4. On importing the module and its subpackage we need to define these function calls in User context Wrapper information according to our modules implementation of IPv6. For example, "sendmessage_ipv6" is function defined in ```emulcomm_ipv6.py```, so for our module implementation we should define this function as follows:

                ```
                  'sendmessage_ipv6' :
           				{'func' : extensions.ipv6.emulcomm_ipv6.sendmessage_ipv6,
       					'args' : [Str(), Int(), Str(), Str(), Int()],
       					'return' : Int()}
       			``` 
  We need to define our module and its subpackage to call this function. Similar update need to be done every function call that need to be added in wrapper info. Again similar update need to carried out when implementing modules for any other extensions of Repy. This also give [here](https://github.com/ankitbhatia32/repy_v2/blob/repy_extensions/namespace.py#L667)

