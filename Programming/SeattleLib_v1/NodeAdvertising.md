### Description

Seattle uses a node based service where available resources are stored by value and key pairs. All available resources (otherwise known as nodes) are thus hashed to a global store (otherwise known as advertising). The Seattle Standard Library provides three different methods of advertising nodes: [SeattleLibcentralizedadvertise.repy](centralizedadvertise.repy.md), [openDHTadvertise.repy](openDHTadvertise.repy.md), or [DORadvertise.repy](DORadvertise.repy.md).

[SeattleLibcentralizedadvertise.repy](centralizedadvertise.repy.md) uses a centralized hash table to store all the values, which runs on the main Seattle server. This may be desirable to users who do not want to depend on the OpenDHT client in case of failure, etc.

[openDHTadvertise.repy](openDHTadvertise.repy.md) uses the OpenDHT client to store key value pairs.

[DORadvertise.repy](DORadvertise.repy.md). uses the CNRI service.

One of these services may be chosen for exclusive use, but [advertise.repy](advertise.repy.md) is the most common choice, as it combines all three services and allows the user to pick a specific implementation of node advertising.

[Back to SeattleLibWiki](../)
