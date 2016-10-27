# Try Repy!

Try Repy is a web-based software development and execution environment for Repy. It lets you experiment with Repy code from within your web browser. Just point your browser at a Try Repy server -- you don't need to install Seattle on your local machine. Behind the scenes, Try Repy leverages Seattle's [wiki:RepyV2API#createvirtualnamespacecodename VirtualNamespaces] to provide Repy sandboxes for users. The web frontend is based on [Cloud9](https://c9.io/), an AJAX (Asynchronous JavaScript and XML) source code editor / IDE.

Below we will give a user-oriented introduction to Try Repy, and then talk about deploying one's own Try Repy server. More details are available  [here](http://seattle.poly.edu/static/try_repy_thesis.pdf) (Lukas Pühringer: Try Repy! A web-based Development and Execution Environment for Restricted Python. Bachelor's thesis, University of Vienna, 2011).




 




## Usage

Here is how Try Repy works for a user: Navigate your browser to a Try Repy server. The page you arrive at (see below) is an Integrated Development Environment (IDE) for Repy. The left half of the page is the Repy source code editor, complete with syntax highlighting and configurable auto-indent. Once started using the "Submit code" button at the bottom, output and error messages of the code are displayed.

[[Image(try-repy.png)]]

### Details

**Editor**: 
The editor is always displayed on the left side. You can write Repy code here, and evaluate it on the server. To submit the code press `cmd + return` (mac), `ctrl + return` (win), or the `submit` button beneath the editor window. Further code submission is locked until the code has been evaluated.

**Callargs**: 
You can append space separated call arguments in the input line beneath the editor window, when submitting code.

**Standard Output**: 
This displays the output of your submitted program. It gives "real time" feedback.

**Session Log**: 
This retrieves and displays the entire log for every submitted and evaluated code of a session.

**Insert Files**: 
Insert files to the editor window, whether at cursor position or at the top of the editor window. 

**Insert Characters**: 
Insert special characters at cursor position.

**Code Snippets**: 
Insert code snippets at cursor position.

**Editor Options**: 
Options to customize the editor window.

------





## Installation & Usage
 1. Check out a copy of [source:seattle/trunk/repy/apps/tryrepy Try Repy] from the Seattle repository.
 1. Make sure, the file `restrictions.tryrepy` contains a line with the serverport where you are going to run Try Repy: `resource connport <serverport>`.
 1. Run the following commands inside the `tryrepy` directory.
```
./tr_build.sh
./tr_run.sh </abspath/to/seattle_repy> <serverport>
```





## Known issues
 * `print` does not work, use `log()` instead.
 * Infinity loops can only be stopped by shutting down the entire server
 * `exitall()` does not work
 * Thread Exceptions: A thread exception in one thread does not exit the entire evaluation in a Virutal Namespace. So far exceptions in a thread are caught and logged but the execution of other healthy threads continues.
 *  TCP/UDP listeners are not isolated
 * A listener registered on one `IP:PORT` will override another listener previously registered on this `IP:PORT`





## Future work
 * Syntax highlighting should recognize Repy functions, and possibly highlight unwanted constructs, too.
 * Network ressource scheduling
 * Isolation of UDP and TCP listener
 * Repy preprocessing
 * Thread Exceptions should stop entire program




## Credits

Christian Schwartz (University of Wüzrburg) -- concept; [http://tryruby.org] aficionado

Albert Rafetseder (University of Vienna) -- proof of concept

Lukas Pühringer (University of Vienna) -- this implementation
