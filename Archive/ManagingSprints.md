# Managing Sprints

The [milestones.txt file](http://seattle.poly.edu/svn/seattle/trunk/milestones.txt) located in /seattle/trunk/milestones.txt maintains sprint information for Seattle strike forces.

## milestones.txt format

The milestones.txt file is composed of sprint snippets that are separated by newlines and have the following format:
```
:sprint
strikeforce
date
name1 task1
name2 task2
``` 

Where:
 * strikeforce is the name of the strike force
 * date is in mm/dd/yyyy format
 * names are person names of those involved in the sprint
 * tasks are short descriptions of the task corresponding to each person

You can add comments to the file, and possibly comment out old sprints by using the '#' symbol. **Note: right now the parser ignores all lines containing #, not just lines that start with #.**


At the end of your development cycle for the sprint, your should pre-append an svn revision number that contains all your committed files to the line with your name. For example, change this line:
```
name1 task1
```
to this line (if your svn revision is rev1):
```
rev1 name1 task1
```

## Example

Here is an example of a completed sprint snippet:
```
:sprint
01/01/2009
eye candy
807 alper
810 sean
```