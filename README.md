# rat-sci-locomotion
Data and analysis of results presented in:
Danner SM, Shepard CT, Hainline C, Shevtosva NA, Rybak IA, Magnuson DSK. Spinal control of locomotion before and after spinal cord injury. bioRxiv 2023.03.22.533794; doi: [10.1101/2023.03.22.533794][https://doi.org/10.1101/2023.03.22.533794]

Run in [Analysis.ipynb][binder-link] in binder [![Binder](https://mybinder.org/badge_logo.svg)][binder-link]

Run in [Analysis.ipynb][colab-link] in Google Colab
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)][colab-link]

[colab-link]: https://colab.research.google.com/github/dannerlab/rat-sci-locomotion/blob/master/Analysis.ipynb
[binder-link]: https://mybinder.org/v2/gh/dannerlab/rat-sci-locomotion/HEAD?labpath=Analysis.ipynb

## Files

`data/*/*.xlsx`: Raw footprint data

`data/df_raw.h5`: Raw data as table with meta data

`data/df_phases.h5`: Table of processed data, includes phase differences and other locomotion parameters as well as gait classifcation

`read_data.py`: Reads raw data files and creates `data/df_raw.h5`

`calc_phases.py`: Reads `data/df_raw.h5` and calculates phase differences etc. and creates `data/df_phases.h5`

`classify_gaits.py`: Calculates gait classifiction based on phase differences and duty factors

`Analysis.ipynb`: Notebook containing all data analysis. Creates plots and calculates statistics included in the paper. Can be run on [Colab][colab-link]  or [binder][binder-link].


## Licenses
Data licensed under Creative Commons Attribution-ShareAlike 4.0 International License [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

Source code licensed under GNU GPL v3 [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)][gpl3]

[gpl3]: https://www.gnu.org/licenses/gpl-3.0
[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

