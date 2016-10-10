# Code Safety

Maintaining a safe environment for execution of untrusted Repy code is fundamental to Seattle.
Seattle securely isolates Repy programs in multiple ways, including performing analysis of the
program's abstract syntax tree, maintaining a small and secure API through which programs can
interact with the outside world, and implementing strong isolation between untrusted code and the
rest of the execution environment.

## Program Analysis

When Seattle runs any Repy program, the program is first parsed and its syntax tree analyzed.
As Repy is largely a subset of Python, we leverage the Python interpreter but disallow anything in
Python that could allow the program direct access system resources. We therefore look through
the program's syntax tree to ensure that only the Python functionality we have specifically allowed exists
in the program. If Seattle encounters anything forbidden, it refuses to run the program.

## Secure API

As we've stripped away any other method by which the program can access resources such as the
computer's hard drive and networking, in order to make Repy a useful programming environment we
need to add a few things back in. What we add in, however, is a clean and minimal API for using
a restricted subset of the computer's resources. As all access to these resources goes through
our API, we can ensure that only allowed resources are accessed as well as limit the frequency
and quantity of any resource that a program uses.

## Code Isolation

As our safe API runs in the same Python interpreter as the untrusted program code, we must ensure that
the untrusted code has no way to manipulate the trusted code or access privileged functionality
that only our own trusted API code should be able to access. We do this in multiple ways. First,
we leverage Python's ability to execute code in a separate context from the rest of the program.
By doing this, we have complete isolation but a program that can't access our trusted API at all.
From there, we then provide the untrusted program access to our API functions.

In fact, we also take extra precautions at the point where we provide access to our API functions.
Instead of providing direct access, we provide access to function wrappers that, when called,
carefully check arguments to the program as well as ensuring that data returned from the function
is the correct type of data (to protect against, for example, leaking object references from trusted
to untrusted contexts). These wrapper functions also further wrap any object instances returned
by those function, such as objects that represent files, sockets, and locks. This ensures that methods
called on those objects have the same namespace protection as the API functions themselves.