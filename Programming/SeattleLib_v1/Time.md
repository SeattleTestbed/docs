### Description

Like many services, Seattle contains its own time module, which provides various time related functions like getting the time and updating the time.

Seattle provides both TCP and NTP time services. TCP, otherwise known as Transmission Control Protocol, utilizes timestamps to keep track of time. NTP, or Network Time Protocol, synchronizes clocks on different machines by using various jitter buffers.

In any case, all programmers should include [wiki:SeattleLib/time.repy], which ties both services into one.