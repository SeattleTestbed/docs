"""
repy_www_sandbox.py - a Repy sandbox running in a Repy web server.

Author:
  Albert Rafetseder, University of Vienna, Austria

Change log:
v 0.1.1, 20100914 2319 AR
"""

"""
Depending on the URL, the user
  . GETs /index.html,
  . POSTs code he put into the HTML form, command line arguments, and 
    a session identifier, or
  . is served the HTMLized log of his experiment.

Here is what we will probably get in the http_request_dict:
  {
    'datastream': <._httpserver_bodystream instance at 0x10065a998>,
    'querydict': None,
    'remoteipstr': '131.130.175.5',
    'remoteportnum': 53869,
    'httpdid': 0,
    'headers': {
      'Origin': ['http://131.130.175.5:12345'],
      'Content-Length': ['0'],
      'Accept-Language': ['de-de'],
      'Accept-Encoding': ['gzip, deflate'],
      'Connection': ['keep-alive'],
      'Accept': ['application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5'],
      'User-Agent': ['Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; de-de) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8'],
      'Host': ['131.130.175.5:12345'],
      'Referer': ['http://131.130.175.5:12345/'],
      'Content-Type': ['application/x-www-form-urlencoded']
    },
    'verb': 'POST',
    'version': '1.1',
    'querystr': None,
    'path': '/131.130.175.5:12345'
  }


Here is what we should return from our callback function:
  {
    'version': '0.9' or '1.0' or '1.1',
    'statuscode': any integer from 100 to 599,
    'statusmsg' (optional): an arbitrary string without newlines,
    'headers': { 'Server': mycontext['server_string'] },
    'message': arbitrary string
  }
"""



######
# Preliminaries
#
# Copy the current (clean) context before including any libraries. 
# Afterwards we can modify getruntime etc. for each sandbox.

mycontext['clean_user_context'] = _context.copy()





#####
# Includes

include httpserver.repy
include urllib.repy
include random.repy
# end includes
#####





# Strings used in HTTP headers and HTML title tags
mycontext['server_string_short'] = 'Repy WWW sandbox'
mycontext['server_string'] = mycontext['server_string_short'] + ' server v 0.1.0'

# Footer
mycontext['footer'] = '<hr>' + mycontext['server_string'] + \
  ', <a href="http://www.univie.ac.at">University of Vienna, Austria</a>. ' + \
  '<a href="mailto:albert.rafetseder you-know-what-goes-here univie.ac.at">' + \
  'Contact us</a> with bug reports, feature requests etc.'
 

mycontext['random_user_id_list'] = [] # Record of ID's I handed out so far





def initialize_clean_user_context():
  """
  Remove the host's mycontext and callargs from the otherwise clean 
  user context we copied earlier.
  """
  mycontext['clean_user_context']['mycontext'] = {}
  mycontext['clean_user_context']['callargs'] = []




def my_log(random_user_id, *args):
  """
  Per-sandbox 'print' surrogate (we can't override the builtin 
  'print'). Wrapped by get_user_context to include random_user_id, 
  thus creating per-user logs. Since Repy v2 is going to use log() 
  instead of print, we should be forward compatible.

  XXX The last arg given will also be followed by a space.

  XXX No care is taken to sanitize what the user prints, i.e. it 
  XXX could be HTML, JavaScript, ... so expect the worst to happen 
  XXX to your browser.
  """
  for this_arg in args:
    mycontext[random_user_id, 'pseudo_stdout'] += \
      str(this_arg) + ' '

  mycontext[random_user_id, 'pseudo_stdout'] += "\n"




def my_getruntime(runtime_at_sandbox_invocation):
  """
  Per-sandbox getruntime(). Wrapped by get_user_context to adjust 
  the runtime_at_sandbox_invocation, so the sandbox does not see 
  the host's runtime.
  """
  now = getruntime()-runtime_at_sandbox_invocation
  return now




def get_user_context(base_context, random_user_id):
  """
  Extend a given base_context to form a new user_context including 
  log() and an adjusted version of getruntime(). Furthermore, 
  set up a per-user pseudo_stdout in the host's mycontext.
  """
  user_context = base_context.copy()

  mycontext[random_user_id, 'pseudo_stdout'] = ""

  def wrapped_log(*args):
    return my_log(random_user_id, *args)
  user_context['log'] = wrapped_log

  runtime_at_sandbox_invocation = getruntime()
  def wrapped_getruntime():
    return my_getruntime(runtime_at_sandbox_invocation)
  user_context['getruntime'] = wrapped_getruntime

  return user_context





# XXX Deserves a better name
def evaluate_namespace_verbosly(user_namespace, user_context, random_user_id):
  """
  Evaluate user_namespace, and update the host's mycontext to reflect 
  the current status of the user's sandbox.
  XXX Should we store the post-run user context as returned by .evaluate?
  """
  mycontext[random_user_id, 'sandbox_status'] = "is running"
  try:
    print 'Started sandbox ' + random_user_id + '.'
    user_namespace.evaluate(user_context) # XXX This can run forever
  except Exception, e:
    mycontext[random_user_id, 'sandbox_status'] = \
      'has crashed with exception "' + str(e) + '"'
    print 'ERROR: Sandbox ' + random_user_id + \
      ' crashed with exception "' + str(e) + '".'
  else:
    mycontext[random_user_id, 'sandbox_status'] = "has finished"
    print 'Sandbox ' + random_user_id + ' has finished.'
  








#####
# HTTP server callback

def switch_request(http_request_dict):
  """This takes the decision on which site to serve, based on the 
  verb and path of the HTTP command sent by the user."""
  try:
    if (http_request_dict['verb'].upper() == 'GET' and 
      http_request_dict['path'] == '/'):
      return serve_index(http_request_dict)

    if http_request_dict['verb'].upper() == 'POST':
      return run_repy_code(http_request_dict)

    if (http_request_dict['verb'].upper() == 'GET' and 
      http_request_dict['path'] == '/log.html'):
      return serve_log(http_request_dict)

    if True: # E.g. for favicon
      return serve_error(http_request_dict, 500,
        'switch_request() failed to match verb/path on ' + str(http_request_dict))

  except Exception, e:
      return serve_error(http_request_dict, 500, 'Error "' + str(e) + 
      '" in ' + str(http_request_dict) + '.')






def serve_index(http_request_dict):
  """Serve an individual index.html file, including a random user ID 
  by which the experiment will be identified."""

  random_user_id = str(random_randint(0, 2**30))
  mycontext['random_user_id_list'].append(random_user_id)

  open_form = '<form action="http://' + getmyip() + ':' + \
    str(mycontext['port']) + '/log.html?id=' + random_user_id + \
    '&logstyle=fancy" method="POST">'

  sample_code = '# This sample code snippet shows you how to print ' + \
    'to your sandboxes\n' + \
    '# log (You will see the log once you run the sample code). The program\n' + \
    '# pauses for a second between each line it prints.\n' + \
    'i=1\nwhile i<=10:\n  log(\'This is iteration\', ' + \
    'str(i) + \'.\')\n  i += 1\n  sleep(1)'

  index_html = html(head(title('Repy WWW Sandbox')) + 
    body(h(1,mycontext['server_string_short']) + 
    para('Put the Repy code you want to try out into the form below and '
    'click the &quot;Run my code&quot; button, or ' +
    '<a href="#samples">go to the samples section</a> for inspiration.') +
    para('Note: Please use <em>log()</em> instead of ' +
    '<em>print</em> to write to your sandboxes log.') + 
    open_form + 
    '<textarea name="user_repy_code" rows=24 cols=80 tabindex="0"></textarea>' +
    '<br><label for="user_callargs">Your callargs: </label>' +
    '<input type="text" name="user_callargs">' +
    '<input type="submit" value="Run my code">' + 
    '<input type="reset" value="Clear form">' +
    '<input type="hidden" name="random_user_id" value="' + 
    random_user_id + '">' + '</form>') + 
    h(2, '<a name="samples">Want to try out some sample code?</a>') + 
    para('Click on the button below the code snippet to run it.') +
    open_form + pre(sample_code) +
    '<input type="hidden" name="user_repy_code" value="' + sample_code + '">' + 
    '<input type="hidden" name="user_callargs" value="">' + 
    '<input type="hidden" name="random_user_id" value="' + random_user_id + '">' + 
    '<input type="submit" value="Run sample code">' + '</form>' +
    mycontext['footer']
    ) 
  # The hidden input is a random user ID to keep parallel users from 
  # overwriting their mutual namespaces. No, that's not quite secure.

  return {'version': '1.1',
    'statuscode': 200,
    'statusmsg': 'OK',
    'headers': {'Server': mycontext['server_string']},
    'message': index_html}



def read_and_decode_form_data(datastream):
  """Read the url-encoded posted user FORM (i.e. user_repy_code in the 
  HTML textarea) and decode it."""

  form_data_urlencoded = ''
  while True:
    new_chunk = datastream.read(4096)
    form_data_urlencoded += new_chunk
    if len(new_chunk) == 0:
      break

  form_data = urllib_unquote_parameters(form_data_urlencoded)
  return form_data




def run_repy_code(http_request_dict):
  """Reads the user_repy_code, sets up a virtual_namespace for the 
  current random user ID, """
  # Read in the user input from the HTML form
  user_input = read_and_decode_form_data(http_request_dict['datastream'])

  # Sanity check: I won't run code for ID's I didn't hand out
  random_user_id = user_input['random_user_id']
  if random_user_id not in mycontext['random_user_id_list']:
    return serve_error(http_request_dict, 400, 
      'Bad request in run_repy_code(): Unknown user ID in query.')

  # I know this ID
  user_repy_code = user_input['user_repy_code']
  user_callargs = user_input['user_callargs'].split()
  # Initialize sandbox_status and pseudo_stdout before serve_log 
  # tries to access it (and crashes)
  mycontext[random_user_id, 'sandbox_status'] = 'was just created'
  mycontext[random_user_id, 'pseudo_stdout'] = ''

  # Create a namespace and run the code inside, logging all activities 
  try:
    user_namespace = VirtualNamespace(str(user_repy_code),
      mycontext['server_string_short'] +' user code, ID '+random_user_id)
  except Exception, e:
    return serve_error(http_request_dict, 500, 
      'Error setting up a namespace for your code. If the safety ' +
      'check failed, please check for typos, missing parentheses ' +
      'and such. Here is the exception:\n'+str(e))
  else:
    try:
      user_context = get_user_context(mycontext['clean_user_context'], random_user_id)
      mycontext[random_user_id, 'sandbox_status'] = "is ready to run"
      user_context['callargs'] = user_callargs
      # XXX I don't think this timer handle is useful as we should 
      # XXX start right away with the evaluation of the namespace.
      mycontext[random_user_id, 'namespace_eval_timer_handle'] = \
       settimer(0.0, evaluate_namespace_verbosly, (user_namespace, 
        user_context, random_user_id))
    except Exception, e:
      return serve_error(http_request_dict, 500, 
        'Error evaluating your code. This is probably my fault, sorry.' +
        'Here is the exception:\n'+str(e))
  return {'version': '1.1',
    'statuscode': 200,
    'statusmsg': 'OK',
    'headers': {'Server': mycontext['server_string']},
    'message': html(head(title(mycontext['server_string_short'] + ': Yes, we run!')) +
    body(h(1,'Your code is running.') + 
    para('I\'ll redirect you to its log in couple of seconds.') +
    '<meta http-equiv="refresh" content="2;http://' + getmyip() + ':' +
    str(mycontext['port']) + '/log.html?id=' + random_user_id + 
    '&logstyle=fancy">' + mycontext['footer']))}





def serve_log(http_request_dict):
  """Serve the log.html page for the current random user ID. Offer 
  fancy (HTML) or plain styles for viewing - handy for code that 
  outputs HTML/XML itself."""

  # Which user's log?
  random_user_id = http_request_dict['querydict']['id']

  if random_user_id not in mycontext['random_user_id_list']:
    return serve_error(http_request_dict, 400, 
      'Bad request in serve_log(): Unknown user ID ' + 
      random_user_id + ' in query.')

  try:
    if http_request_dict['querydict']['logstyle'] not in \
      ['fancy', 'plain', 'download']:
      return serve_error(http_request_dict, 400, 
        'Bad request: Unknown logstyle "' +
        http_request_dict['querydict']['logstyle'] +'".')

  except Exception, e:
      return serve_error(http_request_dict, 400, 
        'Bad request: Logstyle missing from query ("' + str(e) + '").')

  # What is the 'logstyle' specification?
  if http_request_dict['querydict']['logstyle'] == 'fancy':
    # Fancy logstyle returns an HTML page with the log inside <pre>.
    # This is problematic if the sandbox prints HTML itself, 
    # or prints characters the browser misinterprets, such as < and >.
    # In these cases, the user can switch to inornate and plaintext 
    # modes.
    current_url = 'http://' + getmyip()+':'+ str(mycontext['port']) + \
      '/log.html?id=' + random_user_id
    return {'version': '1.1',
      'statuscode': 200,
      'statusmsg': 'OK',
      'headers': {'Server': mycontext['server_string']},
      'message': html(
        head(title(mycontext['server_string_short'] + ': Sandbox log')) +
        body(h(1,'Your code ' + mycontext[random_user_id, 'sandbox_status'] +
        ' and printed to the log:') + 
        para('You might want to refresh this page to see additional output,' +
        ' or ' + '<a href="' + current_url + '&logstyle=fancy#endoflog">' + 
        'go to the tail of the log</a>).') + 
        para('If the log below looks scrambled or fragmentary, try to ' +
        '<a href="' + current_url + '&logstyle=plain">view</a> or ' +
        '<a href="' + current_url + '&logstyle=download">download</a> it '
        'as a plain text file.') + 
        pre(mycontext[random_user_id, 'pseudo_stdout']) +
        '<a name="endoflog"></a>' + mycontext['footer']))}

  if http_request_dict['querydict']['logstyle'] == 'download':
    return {'version': '1.1',
      'statuscode': 200,
      'statusmsg': 'OK',
      'headers': {'Content-Type': 'text/plain', 
        'Content-Disposition': 'attachment; filename="repy-www-sandbox.log"',
        'Content-Length': str(len(mycontext[random_user_id, 'pseudo_stdout'])),
        'Server': mycontext['server_string']}, 
      'message': mycontext[random_user_id, 'pseudo_stdout']}


  elif http_request_dict['querydict']['logstyle'] == 'plain':
    return {'version': '1.1',
      'statuscode': 200,
      'statusmsg': 'OK',
      'headers': {'Content-type': 'text/plain',
        'Server': mycontext['server_string']},
      'message': mycontext[random_user_id, 'pseudo_stdout']}
    






def serve_error(http_request_dict, error_number, error_string):
  """Helper function that serves configurable error pages, 
  e.g. '404 Not found: Your request for FOO did not match any BAR.'"""
  error_html = html(head(title(mycontext['server_string_short'] +
    ': Error '+str(error_number))) + 
    body(h(1, 'Error '+str(error_number)) + 
    para('Sorry, I could not handle your request.') + 
    pre('Server traceback:\n' + mycontext['server_string'] + '\n' + 
    error_string + '\n') + para('Consider going back to the page ' + 
    'you came from using your browser\'s "Back" button, or <a href="http://' +
    getmyip() + ':' + str(mycontext['port']) + '/">start over on the main page</a>.') + 
    para(str(http_request_dict)) + mycontext['footer']))

  return {'version': '1.1',
    'statuscode': error_number,
    'statusmsg': 'Sorry, I could not handle your request.',
    'headers': {'Server': mycontext['server_string']},
    'message': error_html}



#####
# HTML tag helper functions

# Meta-definition: This is a configurable tag
def tag(name, string):
  return '<' + name + '>' + string + '</' + name + '>\n'

# The special tags rely on the configurable tag, then.
def html(string):
  return tag('html', string)

def head(string):
  return tag('head', string)

def title(string):
  return tag('title', string)

def body(string):
  return tag('body', string)

def para(string): # XXX Should read 'p'
  return tag('p', string)

def h(level, string):
  return tag('h' + str(level), string)

def pre(string):
  return tag('pre', string)




def usage():
  print "Usage:"
  print "  repy_www_sandbox LISTENTCPPORT"
  print




#####
# main()

if callfunc == 'initialize':
  if len(callargs) not in [1]:
    usage()
    exitall()

  initialize_clean_user_context()

  mycontext['port'] = int(callargs[0])
  httpserver_registercallback((getmyip(), mycontext['port']), switch_request)
