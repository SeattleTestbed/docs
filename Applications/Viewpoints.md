# Viewpoints

Viewpoints allows a user to view the web from different Seattle proxies.   The user can choose a country and a page and then see how the page differs when viewed from that location.

This software was developed by Yafete Yemuru: yemuru@gmail.com

## LICENSE
Legal Statement:

Copyright (c) 2009 The University of Washington

Permission is hereby granted, free of charge, to any person obtaining a copy ofthis software
and/or hardware specification (the "Work") to deal in the Work without restriction, including
without limitation the rights to use, copy, modify, merge, publish, distribute,sublicense, and/or
sell copies of the Work, and to permit persons to whom the Work is furnished todo so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Work.

THE WORK IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE WORK OR THE USE OR OTHER DEALINGS
IN THE WORK.


## Install/Setup of Viewpoints

1.      If you do not have a Seattle Clearinghouse account, go to https://seattleclearinghouse.poly.edu and register.

2.      Log on to Seattle Clearinghouseand acquire 10 WAN VMs.  

3.      Download the demokit form Seattle Clearinghouse

4.      Download your private and public keys from Seattle Clearinghouse and save them into the demokit folder.

5.      Unzip ```viewpoints.zip``` and copy all the files and documents from the viewpoints folder to the demokit. There will be files that overlap; these are the files that need to be updated. Thus, copy and replace them with the files from the viewpoints folder.

6.      Run ```python viewpoints.py 'username' 'geniport'``` with arguments of your Seattle Clearinghouse username followed by your port from Seattle Clearinghouse.  Make sure it says waiting. This indicates that the server is ready for requests.

7.      Now go over to your browser and type in http://127.0.0.1:12345/. You should retrieve the display of the viewpoints webpage.

8.      Click on the acquire VMs show button. This will generate the possible viewpoint locations using your available Seattle Clearinghouse nodes.(Note: this will take a few seconds, please wait)

9.      When you have the available locations. Copy over one location to the Viewpoints Location field.

10.     In the Viewpoints URL, Insert the URL you intend to display at this location. Click show.

11.     If you want to check another location repeat step 10 and 11.



## Known Issues & Limitations

(Note: The program is not yet at its best. So keep posted for updates. This is just a demo version of viewpoints. We are currently working on a lot of refinements to minimize the failure rate.)

## Improvement Schedule

1. UI
   The user interface will be updated soon.

2. Stability
   We will focus on stability improvement to increase the success rate of Viewpoints browsing.