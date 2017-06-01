# Extensions Module Implementation
With the expansion of Repy and addition of new extensions like IPv6 support, https, sensibility or any future possible extensions, it would be benificial to structure these extensions into python modules. Various current and upcoming extenstions can be structured into modules. For more information on the modules can be created in python, [click here](https://docs.python.org/2/tutorial/modules.html)

# Understanding Modules for IPv6
Current and any upcoming extensions can be structured as modules in python. Let us discuss this module structure with an example of IPv6 extension, similar steps can be followed for other extensions. We assume you have been through build instructions of Repy_V2 and have clear understanding of how build process works, if not [click here](https://github.com/SeattleTestbed/docs/blob/master/Contributing/BuildInstructions.md) and then try to comprehend the following steps given as follows:
  1. First of all it is important to understand modules given in python documenatation given [here](https://docs.python.org/2/tutorial/modules.html). Understand how you want to structure modules. We have structured our IPv6 extension as follows:

               ```extensions/                  Top-level package
      					__init__.py            Initialize the package
      					ipv6/                  Subpackage 
              				  __init__.py
              				  emulcomm_ipv6.py```

  As we can see we have "extensions" as a top level module/package then inside we have "ipv6" in which finally we have our IPv6 python script which we need. This strcuture is given [here](https://github.com/ankitbhatia32/repy_v2/tree/repy_extensions). Go through the extensions module and it will be similar to the given above. 