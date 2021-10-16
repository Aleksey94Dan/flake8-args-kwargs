[![Maintainability](https://api.codeclimate.com/v1/badges/9490f1466ac93407443d/maintainability)](https://codeclimate.com/github/Aleksey94Dan/flake8-args-kwargs/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/9490f1466ac93407443d/test_coverage)](https://codeclimate.com/github/Aleksey94Dan/flake8-args-kwargs/test_coverage)
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
$ pip install -i https://test.pypi.org/simple/ flake8-args-kwargs 

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
| AK002| The function contains a boolean variable|



