# sqlite3

## Sequence reset (pk reset?)
```
1. Table Sequence Check
$ select * from sqlite_sequence;

2. Table Sequence Initialzed
$ update SQLITE_SEQUENCE set seq=1 where name="{TABLE_NAME}";
```
