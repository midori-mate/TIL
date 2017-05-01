// JDBCノート

// えーっとね、これらimportはあとから「あっ javaのノートってimportも書いてないと役に立たないわ」と気づいて
// 書いたものだから(時間差があるから)チト間違ってるカモ。
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.HashMap;

public static void db_connect_base() throws Exception {
    String servername     = "localhost";
    String databasename   = "simple";
    String user           = "user";
    String password       = "pass";
    String serverencoding = "UTF-8";
    String url            = "jdbc:mysql://" + servername + "/" + databasename;
    Connection con = null;

    try {
        Class.forName("com.mysql.jdbc.Driver").newInstance();
        con = DriverManager.getConnection(url, user, password);
        System.out.println("Connected...");

        // ここにクエリ別メソッドを挟むよ。
        insert_method(con, "Sazai");
        update_method(con, 2, "Akoya");
        select_method(con);

        con.close();
    }
    catch (SQLException e) {
        System.out.println("Connection Failed. : " + e.toString());
        throw new Exception();
    }
    catch (ClassNotFoundException e) {
        System.out.println("ドライバを読み込めなかった. : " + e);
    }
    finally {
        try {
            if (con != null) {
                con.close();
            }
        }
        catch (Exception e) {
            System.out.println("Exception2! : " + e.toString());
            throw new Exception();
        }
    }
    System.out.println("おわり。");
}

public static void update_method(Connection con, int update_id, String update_name) throws Exception {
    String sqlStr = "UPDATE simple_table SET name=? WHERE id=?";
    PreparedStatement prpr = con.prepareStatement(sqlStr);
    prpr.setString(1, update_name);
    prpr.setInt(2, update_id);
    int resultInt = prpr.executeUpdate();
    System.out.println("UPDATE結果は " + resultInt + " だったよ.");
    prpr.close();
}

public static void insert_method(Connection con, String insert_name) throws Exception {
    String sqlStr = "INSERT INTO simple_table (name) VALUES (?)";
    PreparedStatement prpr = con.prepareStatement(sqlStr);
    prpr.setString(1, insert_name);
    int resultInt = prpr.executeUpdate();
    System.out.println("INSERT結果は " + resultInt + " だったよ.");
    prpr.close();
}

public static void select_method(Connection con) throws Exception {
    Statement st = con.createStatement();
    String sqlStr = "SELECT * FROM simple_table";
    ResultSet result = st.executeQuery(sqlStr);
    while (result.next()) {
        String str1 = result.getString("id");
        String str2 = result.getString("name");
        System.out.println(str1 + ", " + str2);
    }
    result.close();
    st.close();
}



