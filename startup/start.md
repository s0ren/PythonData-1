<style>
    .reveal section p {
    display: inline-block;
    font-size: 0.8em;
    line-height: 1.2em;
    vertical-align: top;
  }
  .reveal th, .reveal td {
    font-size: 0.5em;
  }
  .reveal li, .reveal ul, .reveal ol {
    font-size: 0.8em
  }
</style> 
---
# pandoc -s --mathjax -t revealjs start.md -o start.html --slide-level=2
title: Python
author: Søren Magnusson, TEC
date: Februar 2023
theme: white
slide-level: 2 
...

_-- et valgfag på TEC_

# Python

Med fokus på datastrukturer

. . . 

men hvad mener jeg med datastrukturer?

## Datastrukturer er

- lister `[1,2,'tre', ...]`
- tupler `(1,2,'tre')`
- dictionaries `{key1: value1, 'key2': 'value2'}`
- mængder `set`

## og - i høj grad - kombinationer af disse

- Lister af dicts
- Dicts med lister
- Lister af lister af dicts med lister

# Men Aller-Først, 

__*installering*__

## python.org

![](2023-02-05-23-26-28.png)

## Kildekode til opgaver, med git

* bliv meldt ind
  * Hvad er dit brugernavn på github?
* lav en `fork` af https://github.com/TEC-Prog-Stud/PythonData-1
* lav en klon på din computer
  * `git clone https://github.com/<dit-brugernavn ... nej ikke "dit-brugernavn" ... >/PythonData-1`

# Og så i gang...