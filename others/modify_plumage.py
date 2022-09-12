#!/bin/env python3
# -*- coding: utf-8 -*-

# Script que busca el string original del tema y lo modifica por el que usa mi plantilla
# ya que uso un arbol de directorios diferente al autor del tema

import re

article = 'theme/plumage/templates/article.html'

search = r'''{% if ARTICLE_EDIT_LINK %}\n\s*<p>Found a typo \? Want to fix it \?<\/p>\n\s*<a class="btn btn-info btn-block" href="{{ ARTICLE_EDIT_LINK % {'slug': article\.slug} }}"><i class="fa fa-random fa-white fa-fw"><\/i> Edit article on GitHub<\/a>\n\s*<hr\/>\n\s*{% endif %}'''

replace = '''{% if ARTICLE_EDIT_LINK %}
      <p>Found a typo ? Want to fix it ?</p>
      <a class="btn btn-info btn-block" href="{{ ARTICLE_EDIT_LINK % {'category': category.name, 'slug': article.slug} }} " target="_blank" ><i class="fa fa-random fa-white fa-fw"></i> Edit article on GitHub</a>
      <hr/>
    {% endif %}'''

update: bool = False
new_text: str

with open(article, 'r') as f:
    data = f.read()
    query = re.search(search, data)
    if query:
        print(f.read())
        update = True
        new_text = re.sub(search, replace, data)
# print(new_text)

if update:
    with open(article, 'w') as n:
        n.write(new_text)
