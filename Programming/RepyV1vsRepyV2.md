# Difference between Repy V1 and Repy V2

This page describes following : 

 * Existing features which are available in Repy V1 and modified in Repy V2.

 * Improved features of Repy V2



## Existing features which are available in Repy V1 and modified in Repy V2

### File Functions

#### Opening File
```open``` command in Repy V1 is replaced by ```openfile``` command in Repy V2. 

Repy V1
```python
file file_object = open(file_name [, access_mode])

Parameter details:
 file_name: It is a string value that contains the name of the file that you want to access.
 access_mode: The access_mode determines the mode in which the file has to be opened,
  - r    : Opens file for readonly.
  - r+   : Opens file for read and write both. File would not be created if it does not exist
  - w/w+ : Opens file for read and write both.File would be created if it does not exist
  - a/a+ : Opens file for append.File would be created if it does not exist.
```
Repy V2
```python
file file_object =  openfile(file_name,create)
 
Parameter details:
 file_name: String value that contains the name of the file that you want to access.
 create   : Bool value, that specifies if the file should be created if it does not exist. If the file  
            exists, this flag has no effect.
 Note: By default each file is opened in both read and write mode.
```

For details on exceptions raised by RepyV2 ```openfile``` function,please refer  [wiki:RepyV2API#openfilefilenamecreate Repy V2 API openfile section]

#### Closing file

Syntax for closing a file remains same in Repy V1 and Repy V2. 
```python
file_object.close()
```

Only difference is, in Repy V1 after closing the file if any input/output operations are performed which requires that the file be opened would raise a general ```Exception``` with a message indicating that given operation is not allowed. Whereas, in Repy V2 a more specific exception ```FileClosedError``` would be raised. This will help user to easily debug his issue.

For details on exceptions raised by RepyV2 ```close``` function,please refer  [wiki:RepyV2API#file.close Repy V2 API close section]

#### Reading File
```read``` command used in Repy V1 to read data from a file, is replaced by ```readat``` in Repy V2

Repy V1
```python
fileObject.read(size)
  size : Optional numeric argument. If size is not specified then
         entire contents of the file are read. If size is specified than equivalent number of bytes are  
         returned.By default bytes are always read from the beginning of the file.
```
Repy V2
```python
fileObject.readat(size,offset)
  size   : Mandatory numeric argument. None, indicates read the entire contents of the file.
  offset : Mandatory numeric argument.Indicates seek to a specific offset before reading. '0' indicates start  
           reading from the beginning of the file 
```

In Repy V1, for reading a file from a specific offset, user would first need to call following function: 
```python
fileObject.seek(offset, from_what)
   offset    : The offset into the file
   from_what : The position is computed from adding offset to a reference point; the reference point is 
               selected by the from_what argument
               0 : Indicates beginning of the file
               1 : Indicates current file position
               2 : Indicates end of the file 
                   Its an optional argument. By default it uses 0 i.e. beginning of the file

```

For details on exceptions raised by RepyV2 ```readat``` function,please refer  [wiki:RepyV2API#file.readatsizelimitoffset Repy V2 API readat section]

#### Writing to File
```write``` command used in Repy V1 to write data to a file, is replaced by ```writeat``` in Repy V2.

Repy V1
```python
fileObject.write(data)
  data : Data to be written in the file
```
Repy V2
```python
fileObject.writeat(data,offset)
  data  : Data to be written in the file
  offset: Indicates seek to a specific offset before writing. '0' indicates start writing  
          from the beginning of the file. 
```

In Repy V1, for writing to a file from a specific offset, user would first need to call ```seek(offset, from_what)``` function.

For details on exceptions raised by RepyV2 ```writeat``` function,please refer  [wiki:RepyV2API#file.writeatdataoffset Repy V2 API writeat section]

### Network functions

#### Getting host by name

```gethostbyname_ex``` in Repy V1 is replaced by ```gethostbyname``` in Repy V2

Repy V1
```python
gethostbyname_ex(hostname)
 hostname : The hostname to translate
 returns  : A tuple containing (hostname, aliaslist, ipaddrlist).
            hostname: Primary host name responding to the given ip_address
            aliaslist:(possibly empty) list of alternative host names for the same address
            ipaddrlist: list of IPv4 addresses for the same interface on the same host 
            See the python docs for socket.gethostbyname_ex()
     
```

Repy V2
```python
gethostbyname(hostname)
 hostname : The hostname to translate
 returns  : The IPv4 address as a string.  If the host name is an
            IPv4 address itself it is returned unchanged. 
            See the python docs for socket.gethostbyname()
```

For details on exceptions raised by RepyV2 ```gethostbyname``` function,please refer  [wiki:RepyV2API#gethostbynamename Repy V2 API gethostbyname section]

#### Sending message to destination host/port
```sendmess``` in Repy V1 is replaced by ```sendmessage``` in Repy V2

Repy V1
```python
sendmess(desthost, destport, message, localip, localport)
   desthost: The host to send a message to.
   destport: The port to send the message to.
   message : The message to send.
   localhost : (optional)The local IP to send the message from. 
   localport : (optional)The local port to send the message from (0 for a random port).

```

Repy V2
```python
sendmessage(destip, destport, message, localip, localport)
   desthost: The host to send a message to.
   destport: The port to send the message to.
   message : The message to send.
   localhost : (optional)The local IP to send the message from. 
   localport : (optional)The local port to send the message from (0 for a random port).
```

For details on exceptions raised by RepyV2 ```sendmessage``` function,please refer  [wiki:RepyV2API#sendmessagedestipdestportmessagelocaliplocalport Repy V2 API sendmessage section]

### Threading functions


### Miscellaneous functions

#### Printing standard output

```print``` command in RepyV1 is replaced by ```log``` command in Repy V2.

Repy V1
```python
    print "By default print adds new line character"
    print "Two string messages" , "can be concatenated using comma(,)"
    print "Two string messages" + " can be concatenated using plus(+) sign too"
    print "Message can be enclosed in double quotes."
    print ("Message can be enclosed in parentheses followed by double quotes too")

Output:
    By default print adds new line character
    Two string messages can be concatenated using comma(,)
    Two string messages can be concatenated using plus(+) sign too
    Message can be enclosed in double quotes.
    Message can be enclosed in parentheses followed by double quotes too
 ```

Repy V2
```python
    log ("log does not add new line character by default.")
    log ("Explicitly line feed character should be used. 
n")
    log ("Two string messages" , "can be concatenated using comma(,) 
n")
    log ("Two string messages" + " can be concatenated using plus(+) sign too 
n")
    log ("Message can be enclosed only within parentheses followed by double quotes")

Output:
    log does not add new line character by default. Explicitly line feed character should be used. 
    Two string messages can be concatenated using comma(,) 
    Two string messages can be concatenated using plus(+) sign too 
    Message can be enclosed only within parentheses followed by double quotes
 ```

For more details on RepyV2 ```log``` function,please refer  [wiki:RepyV2API#logargs Repy V2 API log section]


## Improved Features of Repy V2

 * Improved "Write once, run anywhere".

 * Improved performance.
   
 * Simpler API.

 * Better performance isolation.

 * Easier to extend.
 
 * Enhanced Security







 
 