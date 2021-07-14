# Anki scritpts

## Set up
### Configuration
if needed, copy file BoringStuff.ini from root of the project to the user HOME directory.

### Python 
Necessary packages, that need to be installed into python:
- ankipandas   '''pip3 install --user --upgrade ankipandas''' 
- regex 

### JUPYTER
To work with ankipandas in jupyter, would be nice to start jupyter notebook over borring-stuff space in Anaconda. 

## Scripts
### Removing tags from cards
Next command will ask you what you want to do with anki - it's just a basic entry point 
```
anki
```

Next command asked user, which deck he wants to clean up according to html tags and then perform the tasks:
- remove br tags
- remove span tags
- handling html special chars
```
anki ct
```

