import html

def my_template(page, content, render):
  if render:
    my = html.str(render="page")
    print(template = html.render({{CONTENT}}))
  return f'render {render} content'

  if content:
    my = html.str(content="render")
    print(template = html.content({{CONTENT}}))
  return f'content {content} page'  

  if page:
    my = html.str(page="content")
    print(template = html.page({{CONTENT}}))
  return f'render {page} page'

def __init__(my):
    if (page == my.page) and (content == my.content) and (render == my.render):
      return True
    return False 

def __str__(self):
    print(self.content +"|"+ self.page +"|"+ self.render)    

      
def template(items):
    for items in my:
      print(items)

templates = my_tamplate()


