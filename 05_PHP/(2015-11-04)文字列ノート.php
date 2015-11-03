<?php

$string = "midori";

# sは文字列として、dは整数として扱う
print(sprintf("%010s\n", $string));
print(sprintf("%10s\n", $string));
print(sprintf("%-10s\n", $string));