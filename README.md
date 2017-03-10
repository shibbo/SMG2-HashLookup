# SMG2-HashLookup
A python program that helps look up hashes in Super Mario Galaxy 2. However, it is not perfect and won't find all of them. strings.txt is an extracted part from the DOL that contains every string in the game, with ones that can't possibly be used as a field, but whatever.

It runs on Python 3.

```
python checkHashes.py <hash>
```

Hash has to be in hex/integer form. It will automatically convert hex -> integer because for some reason the string comparisons don't work. yay.

-shibboleet