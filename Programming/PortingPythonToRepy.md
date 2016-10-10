# Porting Guide

Porting existing code into REPY.



### Removing imports
----

Since importing is not permitted in REPY it will be necessary to eventually remove any ```import``` statements and use an **include** statement instead. Since for large files this may be difficult to attempt all at once, it can be approached in several stages.

#### Stage 1
Given a simple example:

```
from foo import *

squid(x)
```

Or the more specific import: 

```
from foo import squid

squid(x)
```


The specified names from foo will be imported (except for those starting with an underscore when using ```import *```). The first stage in transitioning to using an include statement will consist of importing the module name into the importing module's symbol table.

```
import foo

foo.squid(x)
```

Now we use the module name to access the desired functions.

#### Stage 2

To complete our transition, we will ```include``` the module instead of importing it. The [/wiki/PythonVsRepy#Importstatements Import statements guide] has more information on the functionality of the includes feature. To avoid collisions in the name space, an appropriate naming convention will be needed since the contents of the foo module will be inlined into the module using the ```include``` statement.

```
include foo.repy

foo_squid(x)
```

In this example we have used foo and an underscore as a convention to help avoid a collision.

