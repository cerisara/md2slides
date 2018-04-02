# From Markdown to Webslides in minutes

This is a very simple python script that compiles an easy-to-write markdown-like text file into
an html presentation based on [WebSlides](https://webslides.tv).

The objective is to write your presentation in no time in the *src.md* file, with an extremely simple syntax that looks like
Markdown.
You then just run the python script, which compiles *src.md* into the HTML file *slides.html*, which links to the WebSlides CSS
on the web.

This is just a simple python script: nothing to install, no dependency.
Download and start writing your presentation straight away.

The script is so simple that it is trivial to adapt it to your needs, if you want more fancy stuff.
You may also post-edit the HTML file to use more advanced WebSlides tricks if you want.

## Syntax

The easiest way is to start from the small example.
Otherwise, here is some syntax tricks:

- Every slide must end with
```
---
```
- A title starts with ..TITLE, followed by a title level (from 1 to 6)
- You can add latex-like equations (rendered with MathJax included by default), the only constraint is that the equation must be on its own line
- To add an image that occupies 60% vertically of the screen:
```
..IMG60 myimg.png
```
- It's super-easy to have 2 or 3 columns:
```
..COL optional column title
- text in col1

..COL another one
- text in col2
..ENDCOL
```
- If you find that the font size is too small or too large, remember that this is all HTML, so you can at any time press Ctrl+ or Ctrl- in the browser !

## Example

The given example compiles into the following [presentation](http://deeploria.gforge.inria.fr/pres/generative/slides.html)

Note that the images are not commited in this repository, to keep it as light as possible. But you can replace them with your own images if you want to try and compile the example yourself.

