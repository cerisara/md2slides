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
  return s

def skel0():
    entete = ('<!doctype html>',
        '<html lang="en" prefix="og: http://ogp.me/ns#">',
        '  <head>',
        '    <meta charset="utf-8">',
        '    <meta name="viewport" content="width=device-width, initial-scale=1">',
        '',
        '    <!-- SEO -->',
        '    <title>Presentation</title>',
        '    <meta name="description" content="Presentation">',
        '',
        '    <!-- URL CANONICAL -->',
        '    <!-- <link rel="canonical" href="http://your-url.com/permalink"> -->',
        '',
        '    <!-- CSS Base -->',
        '    <link rel="stylesheet" type="text/css" media="all" href="webslides.css">',
        '    <link rel="stylesheet" type="text/css" media="all" href="svg-icons.css">',
        '    <link rel="stylesheet" type="text/css" media="all" href="custom.css">',
        '',
        '    <!-- SOCIAL CARDS (ADD YOUR INFO) -->',
        '',
        '    <!-- FACEBOOK -->',
        '    <meta property="og:url" content="http://your-url.com/permalink"> <!-- EDIT -->',
        '    <meta property="og:type" content="article">',
        '    <meta property="og:title" content="Make a Keynote presentation using HTML"> <!-- EDIT -->',
        '    <meta property="og:description" content="WebSlides is the easiest way to make HTML presentations. 120+ free slides ready to use."> <!-- EDIT -->',
        '    <meta property="og:updated_time" content="2017-01-04T17:32:14"> <!-- EDIT -->',
        '',
        '    <!-- TWITTER -->',
        '    <meta name="twitter:card" content="summary_large_image">',
        '    <meta name="twitter:site" content="@webslides"> <!-- EDIT -->',
        '    <meta name="twitter:creator" content="@jlantunez"> <!-- EDIT -->',
        '    <meta name="twitter:title" content="Make a Keynote presentation using HTML"> <!-- EDIT -->',
        '    <meta name="twitter:description" content="WebSlides is the easiest way to make HTML presentations. 120+ free slides ready to use."> <!-- EDIT -->',
        '',
        '    <!-- FAVICONS -->',
        '    <link rel="shortcut icon" sizes="16x16" href="../static/images/favicons/favicon.png">',
        '    <link rel="shortcut icon" sizes="32x32" href="../static/images/favicons/favicon-32.png">',
        '    <link rel="apple-touch-icon icon" sizes="76x76" href="../static/images/favicons/favicon-76.png">',
        '    <link rel="apple-touch-icon icon" sizes="120x120" href="../static/images/favicons/favicon-120.png">',
        '    <link rel="apple-touch-icon icon" sizes="152x152" href="../static/images/favicons/favicon-152.png">',
        '    <link rel="apple-touch-icon icon" sizes="180x180" href="../static/images/favicons/favicon-180.png">',
        '    <link rel="apple-touch-icon icon" sizes="192x192" href="../static/images/favicons/favicon-192.png">',
        '',
        '    <!-- Android -->',
        '    <meta name="mobile-web-app-capable" content="yes">',
        '    <meta name="theme-color" content="#333333">',
        '',
        '    <script type="text/javascript" async',
        '      src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?config=TeX-MML-AM_CHTML">',
        '    </script>',
        '',
        '  </head>',
        '  <body>',
        '',
        '    <main role="main">',
        '      <article id="webslides">')
    with codecs.open("slides.html","w","utf-8") as g:
        for l in entete: g.write(l+'\n')

def skel1():
    pied = ('</article>',
        '</main>',
        '<script src="https://rawgithub.com/webslides/WebSlides/master/static/js/webslides.js"></script>',
        '<script src="webslides-animation.js"></script>',
        '<script>',
        '  window.ws = new WebSlides();',
        '  new WebSlidesAnimation(window.ws);',
        '</script>',
        '<script defer src="svg-icons.js"></script>',
        '</body>',
        '</html>')
    with codecs.open("slides.html","a","utf-8") as g:
        for l in pied: g.write(l+'\n')

skel0()
with codecs.open("src.md","r","utf-8") as f: src=f.readlines()
inul=False
incol=False
inquote=False
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
      lev=line[7]
      g.write('    <div class="aligncenter">\n')
      g.write('    <h6>'+getText(line[9:].strip())+'</h6>\n')
      g.write('    </div>\n')
    elif line.startswith("#####"):
      lev=line[6]
      g.write('    <div class="aligncenter">\n')
      g.write('    <h5>'+getText(line[9:].strip())+'</h5>\n')
      g.write('    </div>\n')
    elif line.startswith("####"):
      lev=line[5]
      g.write('    <div class="aligncenter">\n')
      g.write('    <h4>'+getText(line[9:].strip())+'</h4>\n')
      g.write('    </div>\n')
    elif line.startswith("###"):
      lev=line[4]
      g.write('    <div class="aligncenter">\n')
      g.write('    <h3>'+getText(line[9:].strip())+'</h3>\n')
      g.write('    </div>\n')
    elif line.startswith("##"):
      lev=line[3]
      g.write('    <div class="aligncenter">\n')
      g.write('    <h2>'+getText(line[9:].strip())+'</h2>\n')
      g.write('    </div>\n')
    elif line.startswith("#"):
      lev=line[2]
      g.write('    <div class="aligncenter">\n')
      g.write('    <h1>'+getText(line[9:].strip())+'</h1>\n')
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
    elif line.startswith('..QUOTE'):
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

