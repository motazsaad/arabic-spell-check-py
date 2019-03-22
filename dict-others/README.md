# Generate words from hunspell/aspell Arabic dictionaries 


```
aspell -d ar-large dump master | aspell -l ar-large expand > ar-aspell-large.dict
aspell -d ar dump master | aspell -l ar expand > ar-aspell.dict
```