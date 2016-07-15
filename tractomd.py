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
 - macros (it does strip TOC)
 - macro lists
 - list escaping
 - headings and font markup without closing tag
 - bold italic
 - color
 - underline (because there is no underline in md)
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

def main(wiki_filenames_list):
  for filename in wiki_filenames_list:
    if (not os.path.isfile(filename) or not filename.endswith(".wiki")):
      # I cannot convert things that aren't files, and will not 
      # convert non-".wiki" type files.
      print "NOTE: Skipping", filename, "-- this is not a '.wiki' file,",
      print "not a regular file, or does not exist."
    else:
      # This is a regular file with ".wiki" extension. Convert it.
      md_filename = os.path.splitext(filename)[0] + ".md"

      # Don't overwrite existing ".md" files!
      if os.path.exists(md_filename):
        print "NOTE: Skipping conversion of", filename, "to", md_filename,
        print "-- the destination file already exists!"
        continue

      print "Converting", filename, "to", md_filename

      text = ""
      with open(filename, "r") as wiki_file:
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
          line = re.sub(r'\'\'\'(.*?)\'\'\'', r'**\1**', line) # bold
          # Messy Magic:
          # (?<!:) is a `negative lookbehind assertion` that ensures that the ...
          # between two urls on a line (http:// ... http://) is not italicezed
          line = re.sub(r'(?<!:)//(.*?)//', r'*\1*', line) # italic
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
  if len(sys.argv) > 1:
    # We seem to have at least one file to convert.
    main(sys.argv[1:])
  else:
    # No file names were supplied. Print usage information.
    print
    print sys.argv[0],
    print """converts files from Trac wiki markup to GitHub Markdown and 
saves them using a file extension of '.md'. You may supply multiple 
files for conversion at once.

Usage:"""
    print "  python " + sys.argv[0] + " TRAC_MARKED_UP_FILE.wiki [...]"
    print

