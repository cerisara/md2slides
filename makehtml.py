import codecs
import os

def newslide(g):
  g.write('<section>\n')
  g.write('  <div class="wrap">\n')
def endslide(g):
  g.write('  </div>\n')
  g.write('</section>\n')
def getText_(s,http):
  i=s.find(http)
  if i>0:
    part1=s[0:i]
    j=s.find(' ',i)
    url=s[i:j]
    part2=s[j:]
    return part1+'<a href="'+url+'">'+url+'</a>'+getText(part2)
  else: return s
def getText(s):
  s=getText_(s,'http://')
  s=getText_(s,'https://')
  return s

os.system("cp skel0.html slides.html")
with codecs.open("src.md","r","utf-8") as f: src=f.readlines()
inul=False
incol=False
inquote=False
with codecs.open("slides.html","a","utf-8") as g:
  newslide(g)  
  for line in src:
    if line.startswith("..TITLE"):
      lev=line[7]
      g.write('    <div class="aligncenter">\n')
      g.write('    <h'+lev+'>'+getText(line[9:].strip())+'</h'+lev+'>\n')
      g.write('    </div>\n')
    elif line.startswith("---"):
      endslide(g)
      newslide(g)
    elif line.startswith("--"):
      g.write('<hr>\n')
    elif line[0]=='-':
      if not inul:
        inul=True
        g.write('<ul class="description">\n')
      g.write('<li>'+getText(line[2:].strip())+'</li>\n')
    elif line.startswith('..QUOTE'):
      if not inquote: g.write('<pre>')
      else: g.write('</pre>')
      inquote=not inquote
    elif line.startswith('..IMG'):
      h=line[5:7]
      im=line[8:].strip()
      g.write('<div class="aligncenter"><img src="'+im+'" style="height:'+h+'vh"></div><br>\n')
    elif line.startswith('..COL'):
      if not incol:
        g.write('<div class="grid">\n')
        incol=True
      else:
        g.write('</div>\n')
      g.write('<div class="column">\n')
      hd=getText(line[5:].strip())
      if len(hd)>0: g.write('<h6>'+hd+'</h6>\n')
    elif line.startswith('..ENDCOL'):
      assert incol
      g.write('</div></div>\n')
      incol=False
    else:
      if inul:
        inul=False
        g.write('</ul>\n')
      g.write(getText(line))
      
  endslide(g)
os.system("cat skel1.html >> slides.html")

