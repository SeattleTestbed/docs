# SeattleBot: The Seattle IRC Bot
SeattleBot is an instance of ```supybot``` running on ```seattle.cs``` which logs the Freenode ```#seattle``` channel and provides information from Trac when tickets or changesets are mentioned.

**Note:** This service is not related to the IRC messages that will get posted by the [wiki:Local/MonitorProcessService Monitor Process Service] in the event of a service failure.


## Log storage
SeattleBot is configured to log to ```/home/seattlebot/logs/ChannelLogger/freenode/#seattle/``` on ```seattle.cs```. The logs can also be [viewed online](https://seattle.poly.edu/irclogs/).


## Trac info in IRC
When a user in ```#seattle``` mentions ticket numbers or changeset numbers, SeattleBot tries to grab relevant information from Trac and deliver it to the channel. For example, including the following text in a message should cause SeattleBot to speak up:

```
#100
ticket 100
ticket:100
```

```
r200
changeset 200
changeset:200
```

See the regular expressions used in SupyTrac/plugins.py for more specifics. Notably, single-digit tickets as well as single- and double-digit changesets are currently ignored.

## Installation Instructions

A user account on ```seattle.cs``` was created which has ```supybot``` installed from the Ubuntu repositories. Installation instructions are as follow:

```
mkdir /home/seattlebot/plugins
touch /home/seattlebot/plugins/__init__.py
cd /home/seattlebot/plugins
svn co http://svn.aminus.net/misc/supybot/plugins/SupyTrac/
```

In order to work with the installed version of Trac, the following changes were made to /home/seattlebot/plugins/SupyTrac/plugins.py:

```
--- plugin.py   (revision 173)
+++ plugin.py   (working copy)
@@ -104,10 +104,14 @@
             site = g[0]
         ticketURL = self.private_uri(channel, '/'.join(('ticket', ticketNumber)))
         soup = self.getSoupFromTracUrl(ticketURL)
-        title = soup.findAll(attrs={'class': 'summary'})[0].string
+        # jsamuel: changed this to just get the second h2, as "summary" was changed
+        # to "summary searchable" and BeautifulSoup doesn't want to find that.
+        #title = soup.findAll(attrs={'class': 'summary'})[0].string
+        title = soup.findAll('h2')[1].string
         tag = soup.findAll(attrs={'class': 'status'})[0]
-        status = tag.findChild('strong')
-        status = status.string
+        #status = tag.findChild('strong')
+        #status = status.string
+        status = tag.string
         ticketURL = self.public_uri(channel, '/'.join(('ticket', ticketNumber)))
         irc.reply('%s - %s - %s' % (ticketURL, status, title), prefixNick=False)
     ticketSnarfer = urlSnarfer(ticketSnarfer)
@@ -124,7 +128,9 @@
             site = g[0]
         changesetURL = self.private_uri(channel, '/'.join(('changeset', revisionNumber)))
         soup = self.getSoupFromTracUrl(changesetURL)
-        p = soup.findAll('dd', attrs={'class': 'message'})[0]
+        # jsamuel
+        #p = soup.findAll('dd', attrs={'class': 'message'})[0]
+        p = soup.findAll('dd')[2]
         message_tags = p.findAll(text=lambda text: isinstance(text, NavigableString))
         message = ''.join([tag for tag in message_tags]).replace('
n', ' ')
         author = soup.findAll('dd', attrs={'class': 'author'})[0].string
```

All plugins besides ChannelLog and SupyTrac were disabled in the ```/home/seattlebot/seattlebot.conf```. 

The following was added to ```/etc/rc.local``` to start ```supybot``` on startup:

```
sudo -u seattlebot supybot /home/seattlebot/seattlebot.conf >>/home/seattlebot/stdout-stderr.log 2>&1 &
```

To make the logs available through the website, the following was added to /etc/apache2/sites-available/default's https vhost:

```
    Alias /irclogs /home/seattlebot/logs/ChannelLogger/freenode/#seattle
    <Location /irclogs>
      SetHandler None
    </Location>
    <Directory "/home/seattlebot/logs/ChannelLogger/freenode/#seattle">
      Options +Indexes
      Order allow,deny
      Allow from all
    </Directory>
```