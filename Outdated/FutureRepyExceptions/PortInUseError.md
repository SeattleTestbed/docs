In the FutureRepyExceptionHierarchy, PortInUseError is a network exception raised when another program is using a port that a repy program wants to bind to. It is distinguished from AddressBindingError in that it is expected to happen and user programs should handle it.

Conrad: I'm not sure if AddressBindingError should be a subclass of this, or vice versa, or if they should remain distinct.