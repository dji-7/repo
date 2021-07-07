# coding: utf-8 

from markdown2 import markdown 
from html2text import *

# echo, html makeup() 

TEMPLATE = ''' 

<!doctype html> 

<html> 

<head> 

<meta charset="utf-8"> 

<meta name="viewport"  

<content="width=device-width"> 

<title>https://dji-7.github.io/dji7.github.io/<title> 

<meta name="author=content"> 

<link src="realsheet"> 

<style rel 

''' 

 

def page(render):
  
  if render:
    print('<p>echo, If none make up language blueprint found in: create your own and save it in local repository as sheet.txt.</p>')
    return render.markdown({{page}}) 

  elif not render:
    print('<p>echo, If none master plan for local project pages in: create your own and save it in local repository as sheet.txt.</p>')
    return render.markdown({{page}})

  else:
    print({{page}})
    
html2text = TEMPLATE.get(page)
html.markdown = html2text.get(render.pages("<form>{{CONTENT}}</form>"))

main = page.html()
print(main)
