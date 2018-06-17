# Typographeur

> Faire respecter les règles typographiques françaises en HTML.

Status: Pre-Alpha

[![Build Status](https://travis-ci.org/brunobord/typographeur.svg?branch=master)](https://travis-ci.org/brunobord/typographeur)

## Utilisation

```python
>>> from typographeur import typographeur
>>> typographeur('<p>Exemple : <em>Salut ! ça va ?</em></p>')
"<p>Exemple&nbsp;: <em>Salut&nbsp;! ça va&nbsp;?</em></p>"
>>> typographeur('<strong>et , entre ( parenthèses  ...) les points sans espace  .</strong>')
"<strong>et, entre (parenthèses…) les points sans espace.</strong>"
```

## Origine

Cette bibliothèque a pour but de faire appliquer les règles de base de la typographie française sur des documents au format HTML. Elle s'inspire du projet SmartyPants, et lui emprunte une partie du code.

* [SmartyPants, le projet initial](https://daringfireball.net/projects/smartypants/)
* [smartypants.py, le fork le plus à jour](https://pypi.org/project/smartypants/)

## Tester

Pour tester, lancer (de préférence dans un virtualenv):

```sh
make test
```

Un exemple complet des correctifs que peut produire `typographeur` est disponible dans le dossier `tests/examples/`. On y trouve un fichier `input.html`, qui contient de nombreuses fautes de typographie, et `expected.html`, qui est le résultat attendu après corerection.

## Règles implémentées

* les signes `:`, `!`, `?` et `;` doivent être précédés d'une (et une seule) espace insécable.
* pas d'espace après une parenthèse ouvrante, ni avant une parenthèse fermante.
* les points de suspension `...` sont remplacés par le caractère `…` ; de même, on *nettoie* les doubles, triples, quadruples, n-uples points. Ça n'existe pas, c'est tout.
* pas d'espace avant un point (simple `.` ou `…`) ou une virgule (`,`).
* les guillemets doubles classiques ("") sont remplacés par des chevrons («»). À noter l'utilisation d'espaces insécables à l'intérieur des guillemets français.

Pour votre plaisir, un document HTML qui respecte les règles énoncées ci-dessus restera inchangé.

Bien que non-testée, la bibliothèque est supposée corriger les textes « bruts » (markdown, par exemple) aussi bien que le HTML.

## Autres implémentations

Des fonctionnalités similaires ont été implémentées dans d'autres langages de programmation. À noter :

* [JoliTypo](https://github.com/jolicode/JoliTypo), en PHP,
* [Cette extension pour Jekyll](https://github.com/borisschapira/jekyll-microtypo/blob/master/lib/jekyll/microtypo.rb), en Ruby.

*Autre ressource :*

[Grammalecte](https://www.dicollecte.org/) est une extension pour LibreOffice, Firefox et Thunderbird pour aider à corriger (entre autres) les fautes de typographie.

## Licence

Ce projet est librement utilisable, publié sous licence MIT.

-----

In *English*, now: this library tries to apply basic French typography rules. It's vastly inspired by SmartyPants, and borrows a lot of code from it.

* [Initial SmartyPants project](https://daringfireball.net/projects/smartypants/)
* [Current smartypants.py code](https://pypi.org/project/smartypants/)

MIT License.
