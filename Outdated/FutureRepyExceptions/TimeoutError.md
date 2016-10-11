In the FutureRepyExceptionHierarchy, there are many functions and methods that support (optionally) the ability to terminate themselves when continuing would mean exceeding some specified maximum run-time. In these cases, TimeoutError is raised.

Some of these include:
 * `openDHTadvertise_announce()`
 * `openDHTadvertise_lookup()`
 * `DORadvertise_announce()`
 * `DORadvertise_lookup()`
 * `centralized_announce()`
 * `centralized_lookup()`
 * many others...