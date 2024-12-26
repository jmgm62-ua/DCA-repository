# DCA-repository

## Alias globales 

git config --global alias.s status
git config --global alias.c "commit -m"
git config --global alias.ch checkout

## Alias locales 
git config alias.br branch
git config alias.r "remote -v"

## Ramas creadas
git checkout -b rama1
git push

git checkout -b rama2
git push

git checkout -b rama3
git push

git checkout -b rama4
git push

## Git bisect
Tras realizar 5 revisiones de bisect encontramos el commit que introduce el fallo que hacía que las operaciones de 
suma resultasen en un resultado numéricamente erróneo.

```
17:37 DCA-repository ((no hay rama, comenzando biseccón en main)) $ git bisect bad
fd01f4348d4881bb964006c763221e839822309f is the first bad commit
commit fd01f4348d4881bb964006c763221e839822309f
Author: Jose Megía Guillén <jmgm62@alu.ua.es>
Date:   Tue Dec 24 17:06:35 2024 +0100

    Añadido un fallo en la suma para detectarlo con bisect

 calculadora.py | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)
```

## Hooks
Se ha añadido dos hooks.

El primero es "pre-commit" en la carpeta ".git/hooks". Este hook lista todos los ficheros incluidos en el commit a
realizar.

El segundo es "post-commit" en la carpeta ".git/hooks". Este hook muestra por pantalla un mensaje indicando que el 
commit ha sido realizado con éxito en el repositorio.

