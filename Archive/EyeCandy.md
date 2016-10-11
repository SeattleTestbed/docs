# Eye candy

 * Seattle/GENI website
 * Web back end improvements.

# Overview

This force is concerned with the GENI web portal. This portal consists of html/css/javascript code that executes in the browser and web back end code that runs on the server and interacts with the database as well as Seattle nodes. There are numerous improvements that need to be implemented and various extensions that we are going to work on throughout the quarter.

There is a production server that runs the GENI portal, and test server that is used for development work. We will periodically push updates to the production server once the new code has been extensively tested and has been verified to work.

## Meetings

Wednesday 10:30-11:30pm in CSE 314.

# Coding Sprints
 * 1/22 (Sprint) 7PM, and 1/24 (Integration) 2-5 PM
   * Parallelism addition to resource acquisition/release in django
   * New design of the GENI portal

# Next Meeting
 * Set up a coding sprint date and deadlines
 * Current django back-end overview and tutorial
 * Review of new portal design

# Future

 * Testing django functionality using django's testing suite
 * Portal Ajaxification

# Ajax API

 * All Ajax calls are POSTs


# MyGENI Ajax calls

 * ajax_getcredits : returns list of credits
   * args {}
   * return : [{'username' : 'sean', percent : 16} ...]

 * ajax_getshares : returns list of shares
   * args {}
   * return : [{'username' : 'sean', percent : 16} ...]

 * ajax_editshare : modifies existing share
   * args : {username: "sean", percent : "17"}
   * return : {"success" : True/False, "error" : "" on success or string with explanation of error}
   * note: if percent is 0 then the action is to remove the share

 * ajax_createshare : creates a new share with some user
   * args : {username : "sean", percent : "17"}
   * return : {"success", "error"} just like above
   * note: percent must be > 0 (local js check as well as remote django check)

 * ajax_getvessels : gets more vessels/VMs
   * args : {numvessels : 16, env : 'LAN' or 'WAN' or 'Random'}
   * return : {"success" : True/False, "error" as above, "mypercent" : 50, "vessels" : [{"vesselid" : vid, "status" : status, "expiresin" : expirein}...]}

