# Generate words from hunspell/aspell Arabic dictionaries 


## Aspell Dictionary
```
aspell -d ar-large dump master | aspell -l ar-large expand > ar-aspell-large.dict
aspell -d ar dump master | aspell -l ar expand > ar-aspell.dict
```

## Hunspell Dictionary
```
unmunch dict-hunspell/ar.dic ar.aff > words.ar 
```

Note: Compile latest source of hunspell to avoid segmentation fault when run unmunch commad. 
