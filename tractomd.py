"""
Transform trac wiki markup file(s) to GitHub markdown markup and write it to
new file with .md extension

Usage:
  python tractomd.py <trac markup>.wiki ...

!!!
This is not a fully fledged converter! It only takes over some repetitive tasks.
I strongly recommend to also compare both documents and adjust manually. See 
reasons below.
!!!

On the one hand implementing an isolated trac syntax parser is not something you
do in a couple of hours. The guys at trac seem to have been working on this
for quite some time: https://trac.edgewall.org/wiki/WikiEngine

Additionally, we want to seize the opportunity of this conversion, to 
update the documentation, i.e. each document needs to be reviewed 
manually anyways.

Nevertheless, contribution to this collection of regexes are most definitely 
appreciated.

Following trac syntac elements are ignored: 
 - discussion
 - citation
 - macros
 - macro lists
 - list escaping
 - headings without closing `=`
 - bold italic
 - color
 - underline (because there is no underline in md)
 - escaping with preceding !
 - monospace escaping: `{{{` or {{{`}}}
 - list continuation
 - table headers
 - table row continuation
 - complex tables
 - table cell alignment
 - embedded images
 - wiki links
 - special links
"""

import sys, os, re

def main(argv):
  for wiki_filename in argv:
    if (os.path.isfile(wiki_filename) and wiki_filename.endswith(".wiki")):
      md_filename = os.path.splitext(wiki_filename)[0] + ".md"

      text = ""
      with open(wiki_filename, "r") as wiki_file:
        for line in wiki_file:
          # HEADINGS
          line = re.sub(r'(?m)^======\s+(.*?)\s+======\s*$', r'###### \1\n', line)
          line = re.sub(r'(?m)^=====\s+(.*?)\s+=====\s*$', r'##### \1\n', line)
          line = re.sub(r'(?m)^====\s+(.*?)\s+====\s*$', r'#### \1\n', line)
          line = re.sub(r'(?m)^===\s+(.*?)\s+===\s*$', r'### \1\n', line)
          line = re.sub(r'(?m)^==\s+(.*?)\s+==\s*$', r'## \1\n', line)
          line = re.sub(r'(?m)^=\s+(.*?)\s+=\s*$', r'# \1\n', line)

          # LINKS
          line = re.sub(r'\[(https?://[^\s\[\]]+)\s([^\[\]]+)\]', r'[\2](\1)', line)
          # Strip trac internal link escapes
          line = re.sub(r'!([A-Z])', r'\1', line)

          # EMPHASIS
          line = re.sub(r' \'\'\'(.*?)\'\'\' ', r' **\1** ', line) # bold
          line = re.sub(r' //(.*?)// ', r' *\1* ', line) # italic
          line = re.sub(r'\^(.*?)\^', r'<sup>\1</sup>', line) # superscript
          line = re.sub(r',,(.*?),,', r'<sub>\1</sub>', line) # subscript

          # MONOSPACE
          line = re.sub(r'\{\{\{(.*?)\n?\}\}\}', r'```\1```', line) # any code

          # LISTS
          line = re.sub(r'^(\s*)a\. (\w.*?)$', r'\g<1>1. \2', line)
          # Strip definition lists
          line = re.sub(r'::', r'', line)

          # TABLES
          line = re.sub(r'\|\|', r'|', line)

          # Strip TOC
          line = re.sub(r'\[\[TOC\(inline\)\]\]', r'', line)

          # LINEBREAKS
          line = re.sub(r'\\', r'\n', line)
          line = re.sub(r'\[\[BR\]\]', r'\n', line)

          text += line

        # Multiline replacing 
        # CODE
        # http://stackoverflow.com/questions/4823468/comments-in-markdown
        comments = re.compile(r'\{\{\{\s*#!comment(.*?)\}\}\}', re.DOTALL)
        text = re.sub(comments, r'<!--\1-->', text)

        language = re.compile(r'\{\{\{\s*#!(\w*)(.*?)\}\}\}', re.DOTALL)
        text = re.sub(language, r'```\1\2```', text)

        anycode = re.compile(r'\{\{\{(.*?)\}\}\}', re.DOTALL)
        text = re.sub(anycode, r'```\1```', text)


      with open(md_filename, "w") as md_file:
        md_file.write(text)

if __name__ == '__main__':
  main(sys.argv[1:])


