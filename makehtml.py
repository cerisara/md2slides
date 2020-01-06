import codecs
import os

def newslide(g):
  global ns
  g.write('<section>\n')
  g.write('  <div class="wrap">\n')
  ns+=1
def endslide(g):
  g.write('  </div>\n')
  g.write('</section>\n')
def strong(s):
  i=0
  ss=""
  while True:
    j=s.find('*',i)
    if j<0: break
    if j>0 and s[j-1]=='\\':
        ss+=s[i:j-1]+'*'
        i=j+1
    else:
        k=s.find('*',j+1)
        if k<0: break
        ss+=s[i:j]+"<strong>"+s[j+1:k]+"</strong>"
        i=k+1
  ss+=s[i:]
  return ss
def getText_(s,http):
  i=s.find(http)
  if i>=0:
    part1=s[0:i]
    j=s.find(' ',i)
    url=s[i:j]
    part2=s[j:]
    return part1+'<a href="'+url+'">'+url+'</a>'+getText(part2)
  else: return s
def getText(s):
  s=getText_(s,'http://')
  s=getText_(s,'https://')
  s=strong(s)
  return s

# MAIN

ftemp = open("template.html","r")
fout  = open("slides.html","w")

for l in ftemp:
    if l.find("xtofcontent")>=0: break
    fout.write(l)

# insert markdown content here
with codecs.open("src.md","r","utf-8") as f: src=f.readlines()
inul=False
incol=False
inquote=False
ns=0

newslide(fout)
for line in src:
    # for headings, support both standard Markdown and ..TITLE
    if line.startswith("..TITLE"):
      lev=line[7]
      fout.write('    <div class="aligncenter">\n')
      fout.write('    <h'+lev+'>'+getText(line[9:].strip())+'</h'+lev+'>\n')
      fout.write('    </div>\n')
    elif line.startswith("######"):
      fout.write('    <div class="aligncenter">\n')
      fout.write('    <h6>'+getText(line[7:].strip())+'</h6>\n')
      fout.write('    </div>\n')
    elif line.startswith("#####"):
      fout.write('    <div class="aligncenter">\n')
      fout.write('    <h5>'+getText(line[6:].strip())+'</h5>\n')
      fout.write('    </div>\n')
    elif line.startswith("####"):
      fout.write('    <div class="aligncenter">\n')
      fout.write('    <h4>'+getText(line[5:].strip())+'</h4>\n')
      fout.write('    </div>\n')
    elif line.startswith("###"):
      fout.write('    <div class="aligncenter">\n')
      fout.write('    <h3>'+getText(line[4:].strip())+'</h3>\n')
      fout.write('    </div>\n')
    elif line.startswith("##"):
      fout.write('    <div class="aligncenter">\n')
      fout.write('    <h2>'+getText(line[3:].strip())+'</h2>\n')
      fout.write('    </div>\n')
    elif line.startswith("#"):
      fout.write('    <div class="aligncenter">\n')
      fout.write('    <h1>'+getText(line[2:].strip())+'</h1>\n')
      fout.write('    </div>\n')

    # slide separator
    elif line.startswith("---"):
      endslide(fout)
      newslide(fout)

    # just an horizontal line
    elif line.startswith("--"):
      fout.write('<hr>\n')

    # items list
    elif line[0]=='-':
      if not inul:
        inul=True
        fout.write('<ul class="description">\n')
      txti=2
      pref=""
      if not line[1]==' ':
        txti=3
        pref=' style="text-indent:'+line[1]+'cm"'
      fout.write('<li'+pref+'>'+getText(line[txti:].strip())+'</li>\n')
    elif line.startswith('..QUOTE') or line.startswith('```'):
      if not inquote: fout.write('<pre>')
      else: fout.write('</pre>')
      inquote=not inquote
    elif line.startswith('..INDENT'):
      idt=line[8]
      fout.write('<div syle="text-indent: '+idt+'cm">' + line[10:]+'</div>')
    elif line.startswith('..HIDE'):
      step=line[6]
      nsteps=line[8]
      if step=='1': fout.write('<span data-step-count='+nsteps+'></span>')
      fout.write('<div class="animate-show-visibility" data-step='+step+'>')
    elif line.startswith('..ENDHIDE'):
      fout.write('</div>')

    # the Markdown way for images ![](img.jpg) is not enough: we require an additional mandatory parameter: the height %
    elif line.startswith('![]('):
      # assume it's an image
      i=line.find(')')
      im=line[4:i].strip()
      fout.write('<div class="aligncenter"><img src="'+im+'" style="height:50vh"></div><br>\n')
    elif line.startswith('..IMG'):
      h=line[5:7]
      im=line[8:].strip()
      fout.write('<div class="aligncenter"><img src="'+im+'" style="height:'+h+'vh"></div><br>\n')

    # columns
    elif line.startswith('..COL'):
      if not incol:
        fout.write('<div class="grid">\n')
        incol=True
      else:
        fout.write('</div>\n')
      fout.write('<div class="column">\n')
      hd=getText(line[5:].strip())
      if len(hd)>0: fout.write('<h6>'+hd+'</h6>\n')
    elif line.startswith('..ENDCOL'):
      assert incol
      fout.write('</div></div>\n')
      incol=False

    # Just standard text
    else:
      if inul:
        inul=False
        fout.write('</ul>\n')
      fout.write(getText(line))
endslide(fout)

# end of HTML file
for l in ftemp:
    fout.write(l)

fout.close()
ftemp.close()

"""
skel0()
with codecs.open("src.md","r","utf-8") as f: src=f.readlines()
inul=False
incol=False
inquote=False
ns=0
with codecs.open("slides.html","a","utf-8") as g:
  newslide(g)  
  for line in src:
    # for headings, support both standard Markdown and ..TITLE
    if line.startswith("..TITLE"):
      lev=line[7]
      g.write('    <div class="aligncenter">\n')
      g.write('    <h'+lev+'>'+getText(line[9:].strip())+'</h'+lev+'>\n')
      g.write('    </div>\n')
    elif line.startswith("######"):
      g.write('    <div class="aligncenter">\n')
      g.write('    <h6>'+getText(line[7:].strip())+'</h6>\n')
      g.write('    </div>\n')
    elif line.startswith("#####"):
      g.write('    <div class="aligncenter">\n')
      g.write('    <h5>'+getText(line[6:].strip())+'</h5>\n')
      g.write('    </div>\n')
    elif line.startswith("####"):
      g.write('    <div class="aligncenter">\n')
      g.write('    <h4>'+getText(line[5:].strip())+'</h4>\n')
      g.write('    </div>\n')
    elif line.startswith("###"):
      g.write('    <div class="aligncenter">\n')
      g.write('    <h3>'+getText(line[4:].strip())+'</h3>\n')
      g.write('    </div>\n')
    elif line.startswith("##"):
      g.write('    <div class="aligncenter">\n')
      g.write('    <h2>'+getText(line[3:].strip())+'</h2>\n')
      g.write('    </div>\n')
    elif line.startswith("#"):
      g.write('    <div class="aligncenter">\n')
      g.write('    <h1>'+getText(line[2:].strip())+'</h1>\n')
      g.write('    </div>\n')

    # slide separator
    elif line.startswith("---"):
      endslide(g)
      newslide(g)

    # just an horizontal line
    elif line.startswith("--"):
      g.write('<hr>\n')

    # items list
    elif line[0]=='-':
      if not inul:
        inul=True
        g.write('<ul class="description">\n')
      txti=2
      pref=""
      if not line[1]==' ':
        txti=3
        pref=' style="text-indent:'+line[1]+'cm"'
      g.write('<li'+pref+'>'+getText(line[txti:].strip())+'</li>\n')
    elif line.startswith('..QUOTE') or line.startswith('```'):
      if not inquote: g.write('<pre>')
      else: g.write('</pre>')
      inquote=not inquote
    elif line.startswith('..INDENT'):
      idt=line[8]
      g.write('<div syle="text-indent: '+idt+'cm">' + line[10:]+'</div>')
    elif line.startswith('..HIDE'):
      step=line[6]
      nsteps=line[8]
      if step=='1': g.write('<span data-step-count='+nsteps+'></span>')
      g.write('<div class="animate-show-visibility" data-step='+step+'>')
    elif line.startswith('..ENDHIDE'):
      g.write('</div>')
 
    # the Markdown way for images ![](img.jpg) is not enough: we require an additional mandatory parameter: the height %
    elif line.startswith('![]('):
      # assume it's an image
      i=line.find(')')
      im=line[4:i].strip()
      g.write('<div class="aligncenter"><img src="'+im+'" style="height:50vh"></div><br>\n')
    elif line.startswith('..IMG'):
      h=line[5:7]
      im=line[8:].strip()
      g.write('<div class="aligncenter"><img src="'+im+'" style="height:'+h+'vh"></div><br>\n')

    # columns
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

    # Just standard text
    else:
      if inul:
        inul=False
        g.write('</ul>\n')
      g.write(getText(line))
      
  endslide(g)
skel1()
"""

