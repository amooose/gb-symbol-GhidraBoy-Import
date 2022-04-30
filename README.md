# gb-symbol-GhidraBoy-Import
Takes the symbol file generated from rgblink (any similarly formatted) and imports it into Ghidra for use with [GhidraBoy](https://github.com/Gekkio/GhidraBoy) extension

Accepted Symbol format:
`XX:XXXX LABEL`
```
;comments allowed
00:ABCD wTestVar
0a:DED3 hTestVar2 ;comment
00:080A FUNC_TEST
```
Run script after importing+analyzing rom with [GhidraBoy](https://github.com/Gekkio/GhidraBoy)  
(To run Ghidra scripts, go to Window->Script Manager)
