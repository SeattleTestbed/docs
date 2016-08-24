## Nodemanager / Repy Architecture
This diagram illustrates the multi-process/multi-thread architecture of a Seattle node exectuing Repy code in a sandbox.
*Note: for simplicity, the two initial daemonizing forks of the nodemanager are omitted, which is equivalent to running the nodemanager with the `--foreground` option.*
<br><br><br>

![Multi-process/-thread Architecture of Nodemanager and Repy sandbox](https://github.com/lukpueh/docs/raw/multi-process-thread-arch/ATTACHMENTS/Architecture/nm_repy_arch.png)