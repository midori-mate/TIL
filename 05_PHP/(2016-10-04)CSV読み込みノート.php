<?php

# windows上では日本語入ってるとエラー出る。
$path = 'SampleFrameCSVtest.csv';

$file = new SplFileObject($path);
$file->setFlags(SplFileObject::READ_CSV);

$lineArray = [];
foreach ($file as $line) {
    $cellArray = [];
    foreach ($line as $cell) {
        $cellArray[] = mb_convert_encoding($cell, 'UTF-8', 'SJIS-WIN');
    }
    $lineArray[] = $cellArray;
}

print('<pre>');print_r($lineArray);print('</pre>');





