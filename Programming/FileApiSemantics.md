# File API call semantics

Note: This is a working draft, and may be incomplete or incorrect in some places.

----

----



## Introduction and Purpose
----

This page is designed to specify, in detail, the behavior of File API calls under various circumstances.  For each call a list of argument and behavioral semantics is provided, along with a snippet of test code that shows how each case is verified -- hopefully in much the same style as the NetworkApiSemantics page.

Note: In order to make file operations more defined across threads, we have per-file locks that each file operation will block on.


----





## fobj.close()
----

### Interacts with:

All fobj methods that require a file to be open.

### Argument Semantics:

None.

### Behavioral Semantics:

1

Action: Close is called on an open file object.

Result: The file obj is closed. Read and write operations can no longer be performed.

(tested - z_testfileclosecloses.py)
Test Snippet:

```
fobj = open(filename)
fobj.close()
try:
  fobj.read(1)
except:
  pass
else:
  test_fail()
```

2

Action: Close is called on an already closed file object.

Result: False is returned, no exception occurs.

(tested - z_testfilecloseduplicate.py)

Test Snippet:

```
fobj = open("junk_test.out")
fobj.close()
if fobj.close():
  print "a duplicate fobj.close() should return false
```

3

Action: Close is called and attempts are made to read or write from the file.

Result: An exception occurs.

(tested under other file_object methods)

----


## fobj.flush()
----

### Interacts with:

fobj.write(data)
fobj.writelines(lines)

### Argument Semantics:

None.

### Behavioral Semantics:

1

Action: flush is called on a file object in read-only mode
Result: noop
(tested - z_testfileflushnooponreadonly.py)

Test Snippet:

```
fobj = open(filename,'r')
fobj.flush()
```

2

Action: flush is called on a file object that has write capability
Result: Buffers are written to disk.
(tested - z_testfileflushwrite.py)

Test Snippet:

```
fobj = open(filename,mode)
fobj.write(num)
fobj.flush()
reader = open(filename,'r')
if reader.read(1) != num:
  print ' write did not flush to disk on mode: '+mode
```

----


## fobj.next()
----

### Interacts With:

fobj.close()
fobj.read()
fobj.readline()
fobj.readlines()

### Argument Semantics:

None.

### Behavioral Semantics:

StopIteration is raised when EOF is hit.

1

Action: next() is called on a file object that is opened for writing.

Result: IOError is raised.

Test Snippet (z_testfilenextwrite.py):

```
fobj = open("junk_test.out", 'r+')
try:
  fobj.next()
except IOError:
  pass
else:
  fail('Supposed to throw exception!')
```

2

Action: next is called on a file object to get each line of the file, then next is called one additional time.

Result: Each line of the file is returned. When the additional call to next is made a StopIteration exception is thrown.
(tested - z_testfilenextloop.py)

Test Snippet:

```
fobj = open(filename)
for line in fobj:
  #process each line
  pass

try:
  fobj.next()
except StopIteration:
  pass
else:
  fail('no exception')
```

----


## fobj.read(size)
----

### Interacts With:

fobj.close()
fobj.next()
fobj.readline()
fobj.readlines()
fobj.write(data)
fobj.writelines(lines)

### Argument Semantics:

Takes one optional argument -- the length to read, in bytes. If that argument is omitted or a negative integer, read() returns the entire contents of the file from wherever the file handle is currently in the file. If that argument is a positive integer, read() returns at most that many bytes from the current position of the file handle. If the argument is not an integer, read() throws TypeError.

### Behavioral Semantics:

1

Action: read() is called on a file object that is closed.

Result: A ValueError exception is thrown.

Test Snippet:

```
fobj = open(filename, 'rb')
fobj.close()
try:
  fobj.read()
except ValueError:
  pass
```

2

Action: read() is called on a file object that is newly opened with no argument or a negative argument.

Result: The contents of the file are returned.

Test Snippet (z_testfilereadbasic.py):

```
fobj = open(filename, 'rb')
fobj.read()
fobj.seek(0)
fobj.read(-1)
```

3

Action: read() is called with a positive 'len' argument.

Result: At most that many bytes of the file's contents are returned.

Test Snippet (z_testfilereadlength.py):

```
fobj = open(filename, 'rb')
str = fobj.read(5)
if len(str) > 5:
  fail("fobj.read() should read no more than len bytes!")
```

4

Action: read() is called with a len argument that is not an integer at all.

Result: TypeError is raised.

Test Snippet (z_testfilereadbadarg.py):

```
fobj = open(filename, 'rb')
for arg in [3.0, "hi"]:
  try:
    fobj.read(arg)
  except TypeError:
    pass
  else:
    fail("fobj.read() should raise TypeError when given a bad len argument")
```

----


## fobj.readline(size)
----

### Interacts With:

fobj.close()
fobj.next()
fobj.read(size)
fobj.readlines(size)
fobj.write(data)
fobj.writelines(lines)

### Argument Semantics:

Optional non-negative integer argument 'size' limits the number of bytes to return.

### Behavioral Semantics:

1

Action: User calls readline on a closed file.

Result: ValueError is raised.

Test Snippet:

```
fobj = open(filename, 'rb')
fobj.close()
try:
  fobj.readline()
except ValueError:
  pass
```

2

Action: User calls readline with no argument or a negative argument.

Result: The next line is returned in its entirety. (Lines are LF-delimited.)

Test Snippet:

```
fobj = open(filename, 'rb')
line = fobj.readline()
if len(line) > 0 and not line.endswith("
n"):
  fail("readline() with no arguments should return an entire line")
```

3

Action: User calls readline with a positive integer argument.

Result: The next line is returned in its entirety if its length (including trailing newline) is shorter than or equal to the integer passed.

Test Snippet:

```
fobj = open(filename, 'rb')
line = fobj.readline(5)
if len(line) > 5:
  fail("readline() with a positive size argument should return a truncated line")
```

----


## fobj.readlines(size)
----

### Interacts With:

fobj.close()
fobj.next()
fobj.read(size)
fobj.readline(size)
fobj.write(data)
fobj.writelines(lines)

### Argument Semantics:

Optional argument size approximately limits the amount of data returned (in bytes). If the argument is omitted or negative, the result size is unbounded. Note: the size argument is not a strict bound, as readlines() only returns whole lines. Thus, it is possible for readlines() to go over the size specified as an argument.

### Behavioral Semantics:

readlines() calls readline() repeatedly and returns a list of the lines read.

1

Action: User calls readlines() on a closed file.

Result: ValueError is raised.

Test Snippet:

```
fobj = open(filename, 'rb')
fobj.close()
try:
  fobj.readlines()
except ValueError:
  pass
```

2

Action: User calls readlines() with a negative or omitted size.

Result: All lines in a file are returned.

Test Snippet:

```
fobj = open("junk.out", "w+b")
fobj.write("line1
nline2
r
n")
fobj.flush()
fobj.seek(0)
expected = ["line1
n", "line2
r
n"]
results = fobj.readlines()
for i in xrange(0, len(expected)):
  assert expected[i] == results[i]
```

3

Action: User calls readlines() with a positive size argument.

Result: At most one line more than that amount is read.

Test Snippet:

```
fobj = open("junk.out", "w+b")
fobj.write("line1
nline2
r
nline3
n")
fobj.flush()
fobj.seek(0)
expected1 = ["line1
n", "line2
r
n", "line3
n"]
results1 = fobj.readlines(14)
fobj.seek(0)
expected2 = ["line1
n", "line2
r
n"]
results2 = fobj.readlines(7)
assert len(expected1) == len(results1)
assert len(expected2) == len(results2)
for i in xrange(0, len(expected1)):
  assert expected1[i] == results1[i]
for i in xrange(0, len(expected2)):
  assert expected2[i] == results2[i]
```

----


## fobj.seek(offset, whence=0)
----

### Interacts With:

fobj.close()
fobj.next()
fobj.read(size)
fobj.readline(size)
fobj.write(data)
fobj.writelines(lines)

### Argument Semantics:

Offset specifies how far to seek into the file. The optional argument whence specifies where to seek from; 0 is absolute position in the file, 1 is seek relative to the current position, and 2 is seek relative to the end of the file.

### Behavioral Semantics:

seek() adjusts the position in the file where the next read/write will occur.

1

Action: User calls seek() on a closed file.

Result: ValueError is raised.

Test Snippet:

```
fobj = open(filename, 'rb')
fobj.close()
try:
  fobj.seek(0)
except ValueError:
  pass
```

2

Action: User calls seek() with an offset outside the bounds of the file.

Result: Undefined behavior! Fun! (On POSIX, I think the call probably just fails, but the man/info pages don't say.)

Test Snippet:

```
???
```

3

Action: User calls seek() with a positive size argument.

Result: The next write()/read() call happens at this location. Note: there is currently no atomic "{read,write} at position X" method; you'll need to do your own locking if you're writing to specific locations in the file from multiple threads. This will be addressed in the future API changes.

Test Snippet:

```
f = open("filename", "w+b")
f.write("abcd")
f.seek(1)
assert f.read() == 'bcd'
```

----


## fobj.write(data)
----

### Interacts With:

fobj.close()
fobj.flush()
fobj.next()
fobj.read(size)
fobj.readline(size)
fobj.readlines(size)
fobj.writelines(lines)

### Argument Semantics:

Writes the (required) string argument to the (open) file handle. Due to buffering, it is necessary to call flush() on the object before the on-disk file contents are changed.

### Behavioral Semantics:

1

Action: User calls write() on a closed file, or a file opened in read-only mode.

Result: ValueError is raised.

Test Snippet:

```
fobj = open(filename, 'rb')
fobj.close()
try:
  fobj.write("hi")
except ValueError:
  pass
```

2

Action: User calls write() on a file opened in a write-enabled mode.

Result: Data is written to file. If two threads try to write at the same time, the behavior is the same as if the writes were sequential, though the order is undefined.

Test Snippet:

```
fobj = open(filename, 'r+b')
fobj.write("hi")
```

----


## fobj.writelines(lines)
----

### Interacts With:

fobj.close()
fobj.flush()
fobj.next()
fobj.read(size)
fobj.readline(size)
fobj.readlines(size)
fobj.write(data)

### Argument Semantics:

Takes any iterable object for the 'lines' argument, iterates over it, and calls write() on each individual string. In other words, it behaves exactly the same as:

```
for line in lines:
  fobj.write(line)
```

(Yes, this means no newlines are added.)

### Behavioral Semantics:

1

Action: User calls writelines() on a closed file, or a file opened in read-only mode.

Result: ValueError is raised.

Test Snippet:

```
fobj = open(filename, 'rb')
fobj.close()
try:
  fobj.writelines(["hi"])
except ValueError:
  pass
```

2

Action: User calls writelines() on a file opened in a write-enabled mode.

Result: No-op.

Test Snippet:

```
fobj = open(filename, 'r+b')
fobj.writelines(["hi"])
```

3

Action: User calls writelines(), passing a non-iterable argument.

Result: TypeError is raised.

Test Snippet:

```
fobj = open(filename, 'r+b')
try:
  fobj.writelines(5)
except TypeError:
  pass
```