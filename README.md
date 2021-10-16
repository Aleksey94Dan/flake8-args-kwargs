# flake8-args-kwargs

A Flake8 plugin for checking arguments in a function

>The  ideal  number  of  arguments  for  a  function  is
>zero (niladic). Next comes one (monadic), followed
>closely  by  two  (dyadic). Three  arguments  (triadic)
>should be avoided where possible. More than three
>(polyadic)  requires  very  special  justification—and
>then shouldn’t be used anyway.
>
> -- <cite>Robert C. Martin</cite> "Clean Code"

## Installation

Install from pip with:

```
$ pip install flake8-args-kwargs

```

## Testing

flake8-args-kwargs uses pytest for tests. To run them use:

```
$ make test

```

## List of Rules

| Rule | Description |
| ---- | ----------- |
| AK001| The function has more than 2 arguments |
| AK002| The order of the arguments in the called function does not match in the declared function |



