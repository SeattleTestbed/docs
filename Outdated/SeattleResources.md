# Seattle Resources

## Hosts dedicated to the project and that we maintain

Accounts on these machines must be requested. These machines do not run NIS/NFS, so accounts/file-systems on these machines are independent.

| Type | Location | Purpose | Hostname | OS | Services | Monitoring |

| Production | ? | Runs production services that change infrequently. 
 No dev access. | seattleclearinghouse.poly.edu| Ubuntu | [wiki:MonitorProcess Monitoring service] 
 [wiki:Archive/SeattleGeniProductionHttp SeattleGENI HTTP] 
 [wiki:SeattleGeniProductionDB SeattleGENI SQL] 
 [wiki:SeattleGeniApi SeattleGENI XML-RPC] 
 [wiki:Local/SshService SSH] 
 [wiki:StateTransitionsService State transition daemons] | HTTP is monitored by a UW CSE [uptime service](http://weblogin.cs.washington.edu/www_is_up).

A GET request is generated every 20 minutes. Justin, Ivan, and Monzur are emailed in case of downtime.|

| Custombuilder | ? | Runs custom installer builder and associated services. 
 No dev access. | custombuilder.poly.edu| Ubuntu | [wiki:CustomInstallerBuilder Custom Installer Builder HTTP] 
 [wiki:CustomInstallerBuilderApi Custom Installer Builder XML-RPC]| ? |

| Beta | ? | Runs beta services that change frequently. 
 No dev access. This is the Seattle Clearinghouse home of our beta testbed and we want to keep it as stable as possible. | betaseattleclearinghouse.poly.edu| Red Hat | [wiki:Local/MonitorProcessService Monitoring service] 
 [wiki:Archive/SeattleGeniProductionHttp SeattleGENI HTTP] 
 [wiki:SeattleGeniProductionDB SeattleGENI SQL] 
 [wiki:SeattleGeniApi SeattleGENI XML-RPC] 
 [wiki:Local/SshService SSH] 
 [StateTransitionsService State transition daemons] | Needs monitoring |

| Stable | CSE 352 | Hosts basic dev services, and simple production services | seattle.cs 
 beraber.cs 
 satya.cs | Ubuntu | Beraber (HTTP) 
 [CentralizedAdvertiseService Centralized advertise server] 
 [wiki:SeattleIrcBot IRC bot] 
 [wiki:Local/MonitorProcessService Monitoring service] 
 SeattleGENI test (HTTP) 
 [SeattleSoftwareUpdaterService Software updater] 
 [wiki:Local/SshService SSH] 
 [wiki:Local/SvnService SVN] 
 [SeattleTracService Trac] | HTTP is monitored by a UW CSE [uptime service](http://weblogin.cs.washington.edu/www_is_up).

A GET request is generated every 20 minutes. Justin, Ivan, and Monzur are emailed in case of downtime.|


| Unstable | CSE 352 | Runs no production services. Used for monitoring, node deployment, and other distributed tasks. | blackbox.cs | Ubuntu | Autograder 
  [wiki:Local/RunningIntegrationTests Blackbox testing] 
 Deployment scripts 
 [wiki:Applications/GeoIpServer GeoIP server] 
 [wiki:Archive/SeattleGeniProductionHttp SeattleGENI HTTP] 
 [wiki:SeattleGeniProductionDB SeattleGENI SQL] 
 [wiki:SeattleGeniApi SeattleGENI XML-RPC] 
 [wiki:Local/SshService SSH] 
 [wiki:Zenodotus Zenodotus server] 
 | None |

| Developer Machine | Sieg Hall !#319 | Testing/Development | testbed-opensuse.cs | OpenSuse | [wiki:Local/SshService SSH] | None |

| Developer Machine | Sieg Hall !#319 | Testing/Development | testbed-mac.cs | OS X | [wiki:Local/SshService SSH] | None |

| Developer Machine | Sieg Hall !#319 | Testing/Development | testbed-vista1.cs | Vista | [wiki:RemoteTestingService Remote testing service] 
 [wiki:Local/SshService SSH] | None |

| Developer Machine | Sieg Hall !#319 | Testing/Development | testbed-xp2.cs | XP | [wiki:RemoteTestingService Remote testing service] 
 [wiki:Local/SshService SSH] | None |


## Seattle notification Gmail Account
We use a normal Gmail account seattle DOT devel -AT- gmail to send automatically generated emails regarding...

| **Service**                                  | **Subject Line Format**                                      |
| Unit test failures in the post-commit SVN hook | svn post-commit unit test hoook failed on rvn [RVN #]          |
| Integration test failures from blackbox.cs     | seattle test failed @ blackbox.cs.washington.edu : [TEST_PATH] |
| Trac ticket notifications                      | [Seattle] #[TICKET #]: [TICKET TITLE]                          |
| Django/SeattleGENI error                       | starts with "[seattlegeni]" or "[betabox]"                     |


## Mailing lists
We use the UW CSE mailing lists to coordinate developers, and to receive email from our users. These lists are configured to receive email from anyone, but require admin confirmation to subscribe, and only subscribers can view the list archives.

 * [Developers](https://mailman.cs.washington.edu/mailman/listinfo/seattle-devel) mailing list ([admin](https://mailman.cs.washington.edu/mailman/admin/seattle-devel) interface)
 * [Users](https://mailman.cs.washington.edu/mailman/listinfo/seattle-users) mailing list ([admin](https://mailman.cs.washington.edu/mailman/admin/seattle-users) interface)


## UW CSE Seattle account
We run Seattle on some of the machines in UW CSE labs. Seattle runs under the **justinc** username.


## Emulab accounts
We use [Emulab](http://www.emulab.net) for our autograder infrastructure. Our Emulab GID (group ID) is **Seattle**.


## PlanetLab accounts
We run Seattle on [PlanetLab](http://planet-lab.org/). Our PlanetLab slice is **uw_seattle**.