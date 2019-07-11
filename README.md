# curLoop

Little tool for performing curl loop

## Syntax

    curloop <URL> -n99 -t99 [-vvv]

## Parameters

- -n (--number)
  - Number of iterations.
- -t (--time)
  - time  to wait between iterations, in seconds.
- [-v (--verbose)]
  - Level of verbosity, can be :
    - -v
    - -vv

## Installation

Download last release
Un-compress it and move it to your /usr/local/bin
chmod +x curloop

Ex:

## Build from source

I packaged this application using pyinstaller : pyinstaller curloop.py -F
