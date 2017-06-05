// ESYSプログラムTIPS

// ==================================================
// 画面から値を取得する。
public String get_value_from_rakrak(PtnParam g_pp, String dd_name) {
  PmsFormValue p_fv = PtnComponent.get(g_pp, "COMPONENT1_1").getFv();
  return p_fv.getValue(dd_name);
}

// ==================================================
// セッションから値を取得する。
public String get_value_from_session(SeiServletParam g_ssp, String name) {
  SeiSess p_sess = g_ssp.g_ss;
  return p_sess.getValue(name);
}

// ==================================================
// プレースホルダを使ったSELECT。
public String select_constr_fr_dt(
    SeiServletParam g_ssp,
    String constr_no) {
  PmsSql p_sql = new PmsSql(g_ssp);
  p_sql.setField("t_constr_summary.constr_fr_dt");
  p_sql.setFrom("r_constr_summary")
    .join("t_constr_summary",
        "r_constr_summary.constr_cd = t_constr_summary.constr_cd"
        + " AND r_constr_summary.chief_cd = t_constr_summary.chief_cd"
        + " AND r_constr_summary.s_constr_no = t_constr_summary.s_constr_no");
  p_sql.setWhere(" r_constr_summary.constr_no = %r_constr_summary.constr_no% ");
  p_sql.addParamValue("r_constr_summary.constr_no", constr_no);
  p_sql.execQuery();
  List<HashMap<String, String>> lis = convert_pmssql_to_list(
      p_sql, new String[] { "constr_fr_dt" });
  if (lis.size() != 1) {
    return "";
  }
  return lis.get(0).get("constr_fr_dt");
}

// ==================================================
// SELECT済みのPmsSqlをHashMapのListにする便利関数。
public List<HashMap<String, String>> convert_pmssql_to_list(
    PmsSql p_sql, String[] fields) {
  List<HashMap<String, String>> lis = new ArrayList<HashMap<String,String>>();
  try {
    while (p_sql.next()) {
      HashMap<String, String> hm = new HashMap<String, String>();
      for (String f: fields) {
        // メソッド外でアクセスしようとしてエラーになったりするから空文字列にしとく。
        String value = (
            SeiUtil.isEmpty(p_sql.getString(f)) ? "" : p_sql.getString(f));
        hm.put(f, value);
      }
      lis.add(hm);
    }
  } finally {
    p_sql.close();
  }
  return lis;
    }

// ===========================================
// DELETEとINSERTを含むメソッド。
public int overwrite_t_cre_file_capture(
    SeiServletParam g_ssp,
    String site_no,
    String csv_file_cl,
    List<String[]> csv_content) {
  // 既存であればそれを削除します。
  PmsTable p_table = g_ssp.getTable("t_cre_file_capture");
  SeiValue p_sv = new SeiValue(g_ssp);
  p_sv.addValue("site_no", site_no);
  p_sv.addValue("csv_file_cl", csv_file_cl);
  p_table.setKeyValue(p_sv);
  if (p_table.existRowByKey()) {
    if (!p_table.delete()) {
      return 1;
    }
  }
  // 新規登録します。
  for (String[] row: csv_content) {
    p_sv = new SeiValue(g_ssp);
    p_sv.addValue("site_no", site_no);
    p_sv.addValue("csv_file_cl", csv_file_cl);
    String csv_1rec = "";
    for (int i = 0; i < row.length; i++) {
      csv_1rec += row[i];
      if (i != row.length - 1) {
        csv_1rec += ",";
      }
    }
    p_sv.addValue("csv_1rec", csv_1rec);
    p_table.setValue(p_sv);
    if (!p_table.insert()) {
      return 2;
    }
  }
  p_table.close();
  return 0;
}

// ==================================================
// テーブルにその行があるかどうかの存在チェック。
PmsTable p_table = g_ssp.getTable("t_cre_file_capture");
SeiValue p_sv = new SeiValue(g_ssp);
p_sv.addValue("site_no", site_no);
p_sv.addValue("csv_file_cl", csv_file_cl);
p_table.setKeyValue(p_sv);
if (p_table.existRowByKey()) {
  // ある
} else {
  // ない
}

// ==================================================
// PmsSqlの実行結果を画面に表示する
// このメソッドは execQuery() をやる前に使わないとダメ。
PmsResult2 p_rs2 = new PmsResult2(g_ssp);
p_rs2.setParamByURL();
if (p_rs2.getSqlNo() < 0) {
  PmsSql p_sql = new PmsSql(g_ssp);

  // ...SQLを作る部分
  p_sql.setField("sum(t_billing_dtl.billing_amount) sum");
  p_sql.setFrom("t_constr")
    .join("t_billing_dtl",
        "t_constr.constr_no = t_billing_dtl.constr_no")
    .join("m_waste",
      "t_billing_dtl.waste_cd = m_waste.waste_cd");
  p_sql.setWhere(" t_constr.site_no = %site_no% "
      + " AND m_waste.jwn_waste_cd IN ('0810','1501','1502')");
  p_sql.addParamValue("site_no", site_no);
  // ...ここまで

  p_rs2.setSql(p_sql);
}
p_rs2.print();


// ===========================================
// CSVファイルを上書きで開いて、ヘッダだけ書き込みます。
public boolean write_csv_header(
    String dirpath, String csvname, String[] csv_header) throws IOException {
  File file = new File(dirpath + "\\" + csvname);
  PrintWriter pw = (
      new PrintWriter(
          new BufferedWriter(
              new OutputStreamWriter(
                  new FileOutputStream(file), "SJIS"))));
  // ヘッダを書き込みます。
  for (int i = 0; i < csv_header.length; i++) {
    pw.print(csv_header[i]);
    if (i == csv_header.length - 1) {
      pw.println();
    } else {
      pw.print(",");
    }
  }
  pw.close();
  return true;
}

// ===========================================
// CSVファイルを追記で開いて、内容を書き込みます。
public boolean write_csv_content(
    String dirpath, String csvname, List<String[]> csv_content) throws IOException {
  File file = new File(dirpath + "\\" + csvname);
  PrintWriter pw = (
      new PrintWriter(
          new BufferedWriter(
              new OutputStreamWriter(
                  new FileOutputStream(file, true), "SJIS"))));
  // 内容を書き込みます。
  for (String[] row: csv_content) {
    for (int i = 0; i < row.length; i++) {
      pw.print(row[i]);
      if (i == row.length - 1) {
        pw.println();
      } else {
        pw.print(",");
      }
    }
  }
  pw.close();
  return true;
}



















