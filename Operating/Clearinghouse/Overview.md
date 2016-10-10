# How SeattleGENI Works

This page describes how the clearinghouse (SeattleGENI) is constructed using the node manager API.   It heavily utilizes the [wiki:UnderstandingSeattle/NodeManagerDesign#NodeManagerInterface Node Manager API], so it is important to understand this document before reading further.

We first describe how the specific tasks are performed by SeattleGENI and then describe the key use overall.

## Acquiring and releasing resources

The basic idea behind SeattleGENI controlling resources is that it possesses the owner private key for all donated resources.   When it provides resources to a user, it adds their user key to the VM.   When a user releases resources, their key is removed from the user list.   A ResetVessel operation is also performed on the VM to clear any state.   

## Finding donations

The SeattleGENI server needs to be able to find new donations.   To do this, the installer that SeattleGENI provides on behalf of the user has a special user key inside that indicates the node is in the 'donation state'.   This user key has no corresponding private key and is only used by SeattleGENI to look up new donations (i.e. nodes in the 'donation state').

## Attributing donations to the correct user

Each donation's VM has a donation key that is unique to the donating user.   When the SeattleGENI site configures the VM, it creates a new, per node owner key and creates a database entry linking the node ID and donating user.

## Finding nodes

After a node is correctly configured a VM on the node is given a special user key that corresponds to the 'ready state'.   SeattleGENI looks up this key and then in a local database marks any nodes that it can contact as ready (which means the VMs are eligible to be acquired by interested users).


## Overall

When an installer is downloaded from SeattleGENI, the owner key is a private key that is specific to the donating user (but is different than the user's private key they use to access resources).   The user key is the special 'donation state' key.   The SeattleGENI server runs a script that looks for nodes in the 'donation state' and then changes the VM owner to be a newly generated, per-node key, while linking the node ID and donating user in a local database.   SeattleGENI then splits the VM into pieces of the correct size and changes the user key on the leftover resources to be the 'ready state' key.   Another script finds nodes in the 'ready state' and then marks them as available in a local database (incrementing the number of credits for the donating user).   When a user clicks to acquire resources on a node, SeattleGENI looks up the VMs owner's private key, and then changes the user of the VM to include the requesting user.   When a user releases a vessel (or it expires), the user's key is removed from the vessel and the VM is reset.