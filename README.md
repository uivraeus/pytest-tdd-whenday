# Simple TDD Example in python (with pytest)

## The task

Create a CLI tool `whenday` that will take a date (or date/time) string as input and output when that is relative the current date/time.
 
### Examples:

```console
$ date
Sun Jun 19 11:53:35 CEST 2022

$ whenday 2022-06-18
Yesterday

$ whenday 2022-06-17
Two days ago

$ whenday 2022-06-07
12 days ago

$ whenday 2022-06-19 09:00
Earlier today

$ whenday 2022-06-19 19:00
Later today

$ whenday 2022-06-20 11:00
Tomorrow

$ whenday 2022-06-21 11:00
In two days

$ whenday 2022-06-30 11:00
In 11 days
```
