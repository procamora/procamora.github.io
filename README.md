

# Wiki-Personal


Blog personal usado por el generador de código estático Pelican, escrito en Python.



## TODO

- [ ] Cambiar imagenes png por svg en fritzing
- [ ] Actualizar Tipue Search de la version 5 a la 7 si no lo actualizan en el tema
- [x] Meter un boton en los articulos para descargarse el articulo en formato pdf. (script que meta el hash de todos los ficheros md en una bd sqlite y luego compruebe si ha cambiado alguno, generando el pdf)


## Requisitos

Para instalar Pelican con los plugins y el tema utilizado hay que realizar los siguientes comandos:


```bash
sudo dnf -y install optipng.x86_64       # OptiPNG (Plugin optimize_images)
sudo dnf -y install libjpeg-turbo-utils  # jpegtran (Plugin optimize_images)
sudo dnf -y install librsvg2-tools       # rsvg-convert (generate_pdf, convierte svg a pdf)

pip3 install -r requirements.txt --user

git -C theme/plumage pull  # actualizamos tema
python3 modify_plumage.py  # modificamos tema con nuestro formato para editar articulos

#git clone --recursive https://github.com/getpelican/pelican-plugins
git -C pelican-plugins pull --recurse-submodules
```


> Cada cierto tiempo descomentar el plugin 'optimize_images' para que optimice las imágenes usadas, ya que tarda tiempo y no merece la pena que se este ejecutando en cada compilación.




## Customizacion del tema plumage



El tema usado [plumage][plumage], aunque es necesario hacer una modificación en los artículos para que podamos editarlo según mi estructura. Esta modificación manual no es necesaria realizarla, ya que se realiza con el script en python `modify_plumage.py` ejecutando anteriormente.



En el fichero `theme/plumage/templates/article.html` hay que buscar este bloque:

```html
    {% if ARTICLE_EDIT_LINK %}
      <p>Found a typo ? Want to fix it ?</p>
      <a class="btn btn-info btn-block" href="{{ ARTICLE_EDIT_LINK % {'slug': article.slug} }}"><i class="fa fa-random fa-white fa-fw"></i> Edit article on GitHub</a>
      <hr/>
    {% endif %}
```



Y sustituir por esto:

```html
    {% if ARTICLE_EDIT_LINK %}
      <p>Found a typo ? Want to fix it ?</p>
      <a class="btn btn-info btn-block" href="{{ ARTICLE_EDIT_LINK % {'category': category.name, 'slug': article.slug} }} " target="_blank" ><i class="fa fa-random fa-white fa-fw"></i> Edit article on GitHub</a>
      <a class="btn btn-info btn-block" href="{{ ARTICLE_PDF_LINK % {'slug': article.slug} }} " target="_blank" ><i class="fa fa-file-pdf-o"></i> Download article PDF</a>
      <hr/>
    {% endif %}
```


### Crear nuevos iconos



En el fichero _theme/plumage/templates/macros.html_ hay que añadir la relación entre el nombre y la url (aprox linea 18):

```
, 'linkedin': ['linkedin.com']
```



En el fichero _theme/plumage/templates/projects.html_ hay que modificar dos listas. Primero hay que indicar la relación que hay entre un dominio y el tag que nos proporciona la web [https://fontawesome.com/icons?d=gallery][fontawesome].
En segundo lugar hay que establecer el label del dominio creado.

```
# {% set ICONS =
, 'linkedin.com': 'fa-linkedin'

# {% set LABELS =
, 'fa-linkedin': 'Social networking service'
```


[fontawesome]: https://fontawesome.com/icons?d=gallery




> Usar Tipue Search 5.0 ya que la version 7 ha cambiado y no funcionan las busquedas sin modificar el tema.




[plumage]: https://github.com/kdeldycke/plumage


## Tareas pendientes


* [] Averiguar porque no funciona el sitemap en google search
* https://www.google.com/webmasters/tools/dashboard?utm_source=wnc_376106&utm_medium=gamma&utm_campaign=wnc_376106&utm_content=msg_743502&hl=es&siteUrl=http%3A%2F%2Fprocamora.github.io%2F


## Cron

La forma mas fácil de automatizar el sincronizado de los repositorios es creando un Personal access tokens y modificando la ruta del config de git: `vim .git/config` quedando así el fichero:

http://superuser.com/questions/199507/how-do-i-ensure-git-doesnt-ask-me-for-my-github-username-and-password

```
[core]
        repositoryformatversion = 0
        filemode = true
        bare = false
        logallrefupdates = true
[remote "origin"]
        url = https://procamora:TOKEN@github.com/procamora/Wiki-Pelican.git
        fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
        remote = origin
        merge = refs/heads/master
```

Habría que hacer esto en ambos directorios git para que podemos primero actualizar el directorio, generar la nueva pagina y después enviar el hrml de la nueva pagina a github.io para actualizar mi web

El cron se ejecutaría cada 2 horas pero tiene le inconveniente de que por culpa de los Related posts siempre haríamos un commit ya que los artículos son aleatorios.

`* */2   * * *   pi      cd /home/pi/wiki/ && bash pushgit.sh >> /tmp/wiki_cont 2>&1 && cd /home/pi/wiki/output/ && bash pushgit.sh >> /tmp/wiki_out.log 2>&1`
