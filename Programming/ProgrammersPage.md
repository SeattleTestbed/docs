# Programmer Portal

This page features information and references regarding how to use write programs on Seattle. Seattle nodes run code written in a special language called Repy. Repy is a subset of the [Python language](http://www.python.org/) (version 2.5 / version 2.6) invented specifically for Seattle.  



## Before You Begin
Make sure you have all the necessary tools installed:

 * **Step 1**: Python2.5 or Python2.6 must be installed in order to use Repy.  [Download Python2.6](http://www.python.org/download/releases/2.6.4/) **WINDOWS USERS:** For instructions on how to check if you already have the correct version of Python installed, and for directions on how to install Python2.6, [wiki:InstallPythonOnWindows click here]

 * **Step 2**: You will have to download and install repy before starting the tutorials below: **[Download repy!](https://seattleclearinghouse.poly.edu/download/flibble/)**

## Tutorials
You can start with several different tutorials depending on your background.

 * [PythonTutorial All of the Python You Need to Understand Repy (and None You Don't)](PythonTutorial.md) Start here if you're new to Python and Repy!

 * [PythonVsRepy All of the Python You Need to Forget to Use Repy](PythonVsRepy.md) Use this tutorial if you already know Python.
 * [All of the Python You Need to Forget to Use RepyV2](PythonVsRepyV2.md)

After doing one of the above tutorials, do the following tutorial to learn how to use Repy specific features and functionality:

 * [RepyTutorial Repy Tutorial](RepyTutorial.md) Try this tutorial to learn more about Repy features and the language API.
 * [RePyV2 Tutorial](RepyV2Tutorial.md)

If you would prefer to use Repy V2, it is worthwhile to read through the following tutorials:

 * [RepyV2CheckoutAndUnitTests Checking out Repy V2 and Running the included unit tests](../Contributing/BuildInstructions.md)
 * [RepyV2SecurityLayers How to use Security Layers with Repy V2](RepyV2SecurityLayers.md)

## Other Resources
 * An easy way to start learning Seattle is to watch our [UnderstandingSeattle/DemoVideo five-minute demo](https://seattle.poly.edu/static/demo.mov).

 * Use the [RepyApi Repy API Reference](RepyApi.md) as a quick guide to Repy's API once you are comfortable with the language.

 * Programmers writing code for Repy V2 may want to read about the [RepyV1vsRepyV2 differences between Repy V1 and Repy V2](RepyV1vsRepyV2.md).

 * There is a growing list of library code you can download and use with Repy (see [seattlelib](http://seattle.poly.edu/svn/seattle/trunk/seattlelib/) in the Seattle repository for examples). Read more about RepyHelper for the details of how to include Repy code in Python programs.

 * Documentation about the Seattle Standard Library can be seen at [SeattleLib](SeattleLib_v1/ProgrammerResources.md)
<!--
Much of this code uses a Repy Pre-Processor (repypp).  To "include" a repy file in your source file **source.repy**, at the top of your code include ```include filename.repy```.   Then run ```python repypp.py source.repy out.repy```.   The **filename.repy** file does not need to be pre-processed. The file **out.repy** will contain the code for **filename.repy** included inside the code for **source.repy** at the appropriate place.
-->

 * Continuous Integration Guide for Seattle Projects: [ContinuousIntegrationGuide](../Contributing/ContinuousIntegration.md)

## Editing Repy files
### Vim
João Moreno has also provided a [VIM syntax file](http://www.vim.org/scripts/script.php?script_id=2546) for Repy that will syntax color Repy programs.

You can also choose to automatically color Repy code with python-mode in emacs.  In your .emacs file, add the following line:

```
(add-to-list 'auto-mode-alist '("

.repy$" . python-mode))
```

### gedit
In order to have proper syntax highlighting for Repy, `repy.lang` needs to be moved into the folder that stores the defined languages. It is a slightly modified version of the python language spec.

 * For system-wide changes, move it to: `/usr/share/gtksourceview-3.0/language-specs/repy.lang`
 * For a single user, move it to: `~/.local/share/gtksourceview-3.0/language-specs/repy.lang`

You can download `repy.lang` [raw-attachment:repy.lang here]
