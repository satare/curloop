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

You can download binaries via the releases page.

Or...

    curl https://raw.githubusercontent.com/satare/curloop/master/install.sh | bash

## Build from source

I packaged this application using pyinstaller
    
    pyinstaller curloop.py -F
