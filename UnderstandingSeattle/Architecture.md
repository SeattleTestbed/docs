## Nodemanager / Repy Architecture
This diagram illustrates the multi-process/multi-thread architecture of a Seattle node executing Repy code in a sandbox.
<br>
*Note: The nodemanager is shown here running in `--foreground` mode. In a default install, it runs without that option and thus daemonizes (i.e. it `forks` twice to detach from its ancestor processes and any controlling TTY).*
<br><br><br>

![Multi-process/-thread Architecture of Nodemanager and Repy sandbox](https://github.com/lukpueh/docs/raw/multi-process-thread-arch/ATTACHMENTS/Architecture/nm_repy_arch.png)
