In the FutureRepyExceptionHierarchy, AddressBindingError is an error that occurs when a low level bind() call fails. It is distinguished from PortInUseException in that the cause isn't something else using the service (perhaps a low-numbered (reserved) port?).

Conrad: I'm not sure this distinction is valuable; perhaps removing PortInUseException is a good idea.