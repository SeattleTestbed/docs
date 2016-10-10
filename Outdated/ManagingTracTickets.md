# Managing Trac Tickets
With so many options, fields, and dropdown boxes, trac tickets can be confusing. This is a description of how to get the most out of the powerful and convenient tools that trac gives you. After the description, there are a few hints and recommended best practices.
----

----


## Introduction
----
One of the most important features of trac is its ticketing system. Developers can use this to keep track of tasks to complete and bugs to fix. trac works best when everybody tickets all of their bugs and all of their tasks, including as much metadata as possible. But not all of the fields are self-explanatory, and many of them could allow for multiple interpretations. In order for us to get the most out of it, it helps if we follow certain common practices.


## The life of a ticket
----
These are the various stages that every ticket should pass through.
 1. **Creation:** Whether you are creating a ticket for yourself or for someone else, it should contain certain information:
  1. Summary - a brief but descriptive summary of the ticket which will show up in searches.
  1. Description - a full description of the ticket, ideally including everything that anyone on the project would need to know about the assignment or bug. You can and should use wiki formatting here where it would be helpful.
  1. Assign to - the person for whom the ticket would be most relevant. Tickets that are not assigned will often be orphaned and forgotten, so you should almost always fill in this field. If it turns out that you got the wrong person, they can always reassign it with no harm done.
  1. Type - should be filled in; mostly self-explanatory.
  1. Priority - should be filled in; mostly self-explanatory.
  1. Milestone - if the task is related to a certain strike force's upcoming sprint, it should be assigned to that milestone. If that milestone doesn't exist yet, it can be created by going to Roadmap. If the ticket is a bug that should be fixed by a certain release, it should be assigned to the corresponding milestone.
  1. Component - something of a judgment call. If it's done for a particular strike force, it should probably be classified with that strike force. Otherwise, it should be classified with the area of the project that seems most relevant.
  1. Version - should probably be filled in with the version of the code it is for.
  1. Keywords - can be used to improve searchability.
  1. Cc - since you can only have one owner of a particular ticket, it can help to use this field to keep others posted on it. They will get emails whenever the ticket has changes.
  1. Severity - used to specify how severe the problem is. By default this is set to 'Medium' but its range is Highest - High - Medium - Low - Lowest.
  1. Blocking and Blocked by -- using these fields you can specify some number of space/comma delimited ticket numbers. Naturally, the Blocking list is a set of tickets that are blocking progress on this ticket, and the Blocked by are the tickets being blocked by the resolution of this ticket. After you do this, the ticket ids will be linked in the summary display for the ticket at the top of the page (and the other tickets will reflect a consistent blocking direction). Additionally in the top right corner you can click on 'Depgraph' to see a visual graph of ticket dependencies. See ticket #103 for an example of these features.

 1. **Acceptance:** When you are assigned a ticket, you should as soon as possible either accept it, close it if it is invalid, or reassign it to someone else if it doesn't belong to you. This way the reporter knows that you've at least looked at the ticket.
 1. **Modification:** Actually, the description of a ticket can't be modified, so if you need to make any significant modifications to the ticket, it's usually best to close the old one and open a new one with the modified description, since people are apt to overlook comments when looking at a ticket. Tickets closed for this reason should generally be resolved as invalid.
 1. **Closing:** Once you've fixed the problem or completed the task described in the ticket, you need to close the ticket, marking it as "fixed". If you fixed part of the problem and are not immediately planning to fix the whole thing, you might consider closing the ticket and reopening a new one with the part of the problem that you still have to fix. Anytime you close a ticket you should leave a comment. If you're reopening a new one that is closely related, go ahead and link to it (which you can do in wiki formatting by prefacing the ticket number with a pound sign; !#42 -> #42). If you've completed a task or fixed a bug that involved checking code into the repository, then you should provide a link to the changeset (which you can do in wiki formatting by prefacing the revision number with the letter r: !r1313 -> r1313). That's really handy for people browsing the wiki to quickly see exactly what changes you made.



## A few hints
----
The art of ticket management is not a strict art. But there are a few hints that you can use along the way. Here are some of these (feel free to add more!):

 * Use the right task granularity. If the ticket is too specific and documents a spelling error then the granularity is too small -- the overhead of creating/closing the ticket is higher than that of the actual task -- avoid this case. On the other hand a ticket could specify a very large task that has multiple sub-tasks -- avoid these as well because its much better to have a ticket for each sub-task so that progress can be made and each task has its own space where relevant details could be assembled.

 * Be verbose -- describe the problem in the ticket with as much detail as possible -- e.g. attach screenshots, or code that triggers the problem. A ticket should strive to convey everything one needs to start addressing the problem.

 * Use a milestone to organize your work. If none exists -- create one in the roadmap (see left bar of the wiki). Milestones make it easy to find tickets later and to track your progress on a number of related  tickets

 *  Use the correct component for the ticket. Remember that the component owner will be notified on ticket creation. You don't want to bother people unnecessarily.

 * Use comments to reply to tickets / update tickets as you make progress. Reference other tickets related to the issue. Its important to specify how the ticket fits in with the rest of the project. For example, a ticket could be blocking a release, or it could be a minor issue that's orthogonal to the priority areas of the project.

 * Use the CC field to reference other users who need to know about the ticket. Often a ticket will require team effort -- reference anyone who needs to know about the ticket.

 * Use ticket numbers in SVN comments when committing code (e.g. Worked on Ticket #92) -- the #92 is the format that will cause trac to understand that this refers to a ticket.

 * Use revision numbers in ticket comments when closing tickets (e.g. fixed in r101) -- the r101 is the format that will cause trac to understand that this refers to a commit.

 * Use the Trac [timeline](https://seattle.poly.edu/timeline) to track what has been happening recently -- to see new tickets, new commits, etc.
