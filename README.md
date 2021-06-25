# repotemplate



## developing stuff in this repo

clone this repo and use:

    pip install -e .

to import normally its packages anywhere in your system, virtual env, notebooks, etc.

see the example notebook under `notebooks`

if you modify any file under `src` use the following in your code

   
   from importlib import reload
   reload(...) # whatever module imported from the package

to reload any module within the same python process (no need to restart)

## using this repo packages

just install it with `pip` as with any github repo



