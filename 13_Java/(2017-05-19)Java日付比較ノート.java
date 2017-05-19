// Java日付比較ノート

package org.mate;

import java.text.SimpleDateFormat;
import java.util.Date;

public class Jv {

    public static void main(String[] args) throws Exception {
        // 現在をDateインスタンスにする。
        Date date_now = new Date();

        // フォーマットを自分で決める。
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
        String before = "2000-01-01";
        // Dateを文字列にする。
        String today = sdf.format(date_now);
        String after = "2100-01-01";

        // 文字列をDateにする。
        Date date_before = sdf.parse(before);
        Date date_today = sdf.parse(today);
        Date date_after  =sdf.parse(after);

        // 比較する。
        int diff_before = date_today.compareTo(date_before);
        int diff_today = date_today.compareTo(date_today);
        int diff_after = date_today.compareTo(date_after);

        System.out.println(diff_before); // 1になる。
        System.out.println(diff_today); // 0になる。
        System.out.println(diff_after); // -1になる。


    }


}



