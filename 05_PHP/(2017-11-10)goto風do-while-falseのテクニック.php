<?php

$errors = [];
do {
    if (!something()) {
        $errors[] = "";
        break;
    }

    //上の処理でbreakしていた場合は実行されない。
    if (!something2()) {
        $errors[] = "";
        break;
    }

} while (false);

//breakするとここに飛ぶ