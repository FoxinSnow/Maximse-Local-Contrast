# Local-Contrast-Maxmize

![](https://img.shields.io/apm/l/vim-mode.svg)

This code is used for locally contrast of a signal.\
\
For every fringe of the signal, their peaks is increased to a max value, and their valleys is decerased to a min value.\
The middle signal values will be automaticly modifies to meet the new signal shape.\
\
Current version is used for 1D signal.

Run `demo.py` to check the effect.\
Incluse both `findExtremums.py` and `maxContrast.py` in the code.\
(But if you only want to find all peaks and valleys of your signal, the `findExtremums.py` can also be used independently.)
