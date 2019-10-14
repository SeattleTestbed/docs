### Description

The parallelism services offered by Seattle are purely for the client's needs and not required in any way. Running parallel processes are more efficient and may be of interest to some users, but adds a certain amount of overhead since locking must be implemented to prevent crashes and errors in critical sections of code. For this reason, libraries like [wiki:SeattleLib/semaphore.repy] and [wiki:SeattleLib/cv.repy] to help the client implement locks.

Many modules here also have Python equivalents. These are linked appropriately.

[Back to SeattleLibWiki](../)
