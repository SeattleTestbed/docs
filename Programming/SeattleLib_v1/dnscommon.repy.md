
## dnscommon.repy

This is a formatting tool for DNS queries. It has two public methods which are of primary concern:


convert_packet_to_dictionary(string arg)

convert_dictionary_to_packet(dictionary arg)

Which work exactly as you would expect. These two methods convert between bitstrings that can be used in DNS network operations and dictionary representations detailed within dnscommon itself. The dictionary format is complex, as you would expect for a direct DNS query construction. As way of compensation, you have total control over what your DNS packet looks like.

There is one additional public method,

generate_packet(dictionary arg)

which takes a dictionary identical in structure to the "questions" section of the larger dictionary below. It uses a default set of packet descriptors included in dnscommon.repy as "default_flags". This can be overridden as a second argument in the generate_packet method.


## Dictionary Format


```
{
160	    'raw_data':                <long string> (network raw)
161	    'remote_ip':               string (formatted unicode, IP Address)
162	    'remote_port':             integer
163	    'communication_id'         string (network raw)
164	    'query_response'           boolean
165	    'operation_code'           integer
166	    'authority_advisory'       boolean
167	    'truncation'               boolean
168	    'recursion_desired'        boolean
169	    'recursion_accepted'       boolean
170	    'z'                        boolean
171	    'authentic_data'           boolean
172	    'checking_disabled'        boolean
173	    'error_code'               integer (4 bit)
174	    'question_count'           integer (16 bit)
175	    'answer_count'             integer (16 bit)
176	    'authority_record_count'   integer (16 bit)
177	    'additional_record_count'  integer (16 bit)   )
178	    'questions': array of dictionaries containing:
179	        'name'                  string (formatted unicode, IP Address)
180	        'type'                  string (formatted unicode, eg A, AAAA, MX)
181	        'class'                 string (formatted unicode, eg IN, HE, CH)
182	    'answers': array of dictionaries containing:
183	    'name'                  string (formatted unicode, IP Address)
184	        'type'                  string (formatted unicode, eg A, AAAA, MX)
185	        'class'                 string (formatted unicode, eg IN, HE, CH)
186	        'time_to_live'          integer (seconds, 32 bit)
187	        'answer_data'           dictionary (format based on type)
188	
189	  }
```

Most of this is self-explanatory, but answer_data deserves a special mention.

If the packet has type SOA, answer_data takes on the following format:

{ mname, rname, serial, retry, refresh, expire, minimum } (Meanings are thoroughly explained in RFCs 1034 and 1035)

All other supported packets (A, NS, CNAME, MD, MB, MF, MG, MR, MX, PTR) have answer_data with the following format:

{ address }

In other words, unless you're dealing with SOA queries, there is no need to have more than one key-value pair in your dictionary's answer_data subdictionary.


## Location


This file can be found in the seattlelib directory of the repy v1 repository.