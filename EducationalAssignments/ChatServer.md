# Chat Server Assignment
----
This assignment focuses on designing and implementing a chat service called Seattlechat. Seattlechat has three main components, a central Seattlechat server whose focus is to relay messages, a collection of Seattlechat translators that change messages into different formats for display, and a Seattlechat client which is will use a standard web browser for communicating with a user. Each Seattlechat client has its own translator, but many translators can connect to the same Seattlechat server.

----

----



## Step 1 : Seattlechat Server
----

Your Seattlechat server should accept connections on your GENI port using the waitforconn() call. Seattlechat is a multiway text conferencing system, and so the server must be able to accept and manage multiple connections simultaneously. Once two or more sources are connected, all bytes sent to the server are “relayed” to all other computers listening to the service. The server should separate text by source by sending it line by line (lines end with '
n'), labeling each line with the name of the client who sourced that particular message.



## Step 2 : Seattlechat Translator
----

The Seattlechat translator connects to a Seattlechat server and translates messages for the client. In all cases, the Seattlechat translator provides a web page that has the chat output and accepts incoming chat messages (in the form of HTTP POST messages). There are three translators you will need to implement: 

 * normal: This translator does not change incoming or outgoing data.

 * reverse: This translator reverses the order of all incoming and outgoing data streams (hint: data[-1] is the reverse of data). Names and other data should not be reversed. Note that input typed by a user behind the reverse translator will be backwards!

 * Pig Latin: This translator changes words to and from [Pig Latin](http://en.wikipedia.org/wiki/Pig_Latin). Your Pig Latin translator should use the hyphenated form and be able to reverse translate data from the client which is in hyphenated form.




## Step 3 : Chat web-browser client
----
In this step, you will build a chat client which will use a web-browser to communicate with the user. The client must interact with a translator instead of contacting the server directly.



## Strategy
----

To test your code, we suggest that you first build the server and test it using a simple program that opens connections and sends strings. Following this, build the normal translator using the webserver from the previous assignment to pass messages and display output. After this works, add the reverse and Pig Latin translators.