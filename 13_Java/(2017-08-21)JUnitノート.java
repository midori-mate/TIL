
/**
 * JUnitノート
 *
 * 目次
 *     ■ テスト命名規則
 *     ■ テスト作成手順
 *     ■ カバレッジのとりかた
 *     ■ 最初に書いたほうがいいimport
 *     ■ 実例1: テスト対象が public static
 *     ■ 実例2: ひたすらたくさんの入力値、期待値パターンを書く
 *     ■ 実例3: テスト対象が private
 *     ■ 実例4: テスト対象が protected
 *     ■ 実例5: 例外を出すテスト
 *     ■ 実例6: モック対象が public
 *     ■ 実例7: モック対象が public static
 *     ■ 実例8: Listの検証方法
 *     ■ 実例9: モック対象が 対象クラス内のprivate
 *     ■ 実例10: モック対象が 対象クラス内のprivate かつ テスト対象が private *
 *     ■ 実例11: 中々使いやすいと思ったテストメソッドの書き方
 *     ■ 実例12: モック対象が voidを返すメソッド
 *     ■ 実例13: ひたすらたくさんの入力値、期待値パターンを書く + 例外パターンを含む場合の書き例
 *     ■ 実例14: テスト対象が private static で、かつ例外テストをしたいとき
 *     ■ 実例15: PowerMockとParameterizedを同時に使いたい
 */


// ■ テスト命名規則
//     ● ひとつのメソッドにつきひとつのテストクラス。
//         名前は {対象クラス名}_{対象メソッド名}Test。
//         CsvCreator_GetContentTest等。


// ■ テスト作成手順
//     ● 普通に作ると実ファイルと同じトコにテストjavaファイルが作られて邪魔い。テスト用フォルダを作る。
//         プロジェクト右クリック > New > SourceFolder
//     ● JUnitファイルの作成
//         テストしたいjavaファイル右クリック > New > JUnit Test Case
//         > SourceFolderを上で作ったトコに > 名前決めてNext (★★)
//         > テストを作りたいメソッドにチェック(必須ではない) > 完了
//         ★ ダイアログにあるsetUpBeforeClassとかは何?
//             setUpBeforeClass   いっちばん最初に実行される。
//             tearDownAfterClass いっちばん最後に実行される。
//             setUp              各テスト実行前に実行される。
//             tearDown           各テスト実行後に実行される。
//     ● 検証ソースを書く
//         下のテスト例を参考にどうぞ。
//     ● テスト実行方法
//         Run as > JUnit Test(Shift+Alt+X,T)
//     ● JUnitファイルを個別にちまちま実行するのは面倒なので、一括で実行
//         プロジェクト右クリック > New > Other,JUnit,JUnit Test Suite > 一括実行するものをチェックする
//         > {クラス名}AllTestsって名前で保存
//         作ったファイルを JUnit Test 実行すれば全部まとめてテストされる。


// ■ カバレッジのとりかた
//     ● EclEmmaを使うパターン
//         EclipseのHelp > Eclipse Marketplace からインストール。
//         ファイル右クリック > Coverage as > JUnit でカバレッジ実行ができます。
//         ★ ただし不具合アリ
//             EclEmmaはEclipse4.4だとカバレッジの表示が出ない不具合あり。
//             だいたいは出るが、細かいところが出なかったり、PowerMockito.spy()を使うとまるきり出なくなる。
//     ● IDE:IntelliJ IDEAを使うパターン
//         この記事に従ってインストール。
//             参考:http://qiita.com/kobake@github/items/71e3a57f971ba6771356
//         Eclipseと同じ感じにテストファイル右クリック > Run '...Test' with Coverage で見れる。
//         色がちょっと見づらいので File > Settings > EditorとかFontとかそのへん
//         からSchemeをDarculaにするのおすすめ。


// ■ 最初に書いたほうがいいimport
import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.*;
import static org.hamcrest.Matchers.*;
import static org.mockito.Mockito.*;
import java.util.Arrays;
import org.junit.Rule;
import org.junit.rules.ExpectedException;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;
import org.junit.runners.Parameterized.Parameters;


// ==============================================================================
// ■ 実例1: テスト対象が public static
//


  // テスト対象。
  public class Target {
    public static int foo(int x) {
      return x;
    }
  }

  // テストクラス。
  public class Target_FooTest {
    @Test
    public void ユニットテストPublicStaticメソッド() {
      // 入力値。
      int x = 1;
      // 期待値。
      int expected = 1;
      // 検証。
      int actual = Target.foo(x);
      assertThat(actual, is(expected));
    }
  }

// ==============================================================================
// ■ 実例2: ひたすらたくさんの入力値、期待値パターンを書く
//     対象は上のTarget.foo()とする。

  // 1. これを書きます。
  @RunWith(Parameterized.class)
  public class Target_FooTest2 {

    // 2. 入力値とか期待値をインスタンス変数にしときます。
    private final int x;
    private final int expected;

    // 3. コンストラクタを書きます。
    public Target_FooTest2(int x, int expected) {
      this.x = x;
      this.expected = expected;
    }

    // 4. 入力値、期待値とかのリストを作ります。
    @Parameters(name = "No.{index} x({0}) expected({1})")  // nameのとこは別に書かなくてもいい。好きなフォーマットでどうぞ。
    public static Iterable<Integer[]> list() {             // Object[]でもいいので型が混成してても大丈夫。
      return Arrays.asList(new Integer[][] {               // なお、intはダメ。Integerでないとダメ。
        // ここにコンストラクタ引数の順番に書きまくってください。
        {1, 1},
        {2, 2},
        {3, 3},
      });
    }

    // 5. 検証メソッドだけ書けばよい。
    @Test
    public void 入力値がそのまま返ってくれば成功() {
      int actual = Target.foo(x);
      assertThat(actual, is(expected));
    }
  }

// ==============================================================================
// ■ 実例3: テスト対象が private
//

  // テストクラス。
  public class Target_BarTest {

    private static Method method;

    @BeforeClass
    public static void setUpBeforeClass() throws Exception {
      method = EU03.class.getDeclaredMethod("bar", int.class);
      method.setAccessible(true);
    }

    @Test
    public void ユニットテストPrivateAndProtectedメソッド() throws Exception {
      // 入力値。
      int x = 1;
      // 期待値。
      int expected = 1;
      // 検証。
      int actual = (int)method.invoke(new Target(), x);
      // 対象が private static の場合は
      // (int)method.invoke(Target.class, x);
      // こうです。
      // nullでもよさげ!?
      assertThat(actual, is(expected));
    }
  }

// ==============================================================================
// ■ 実例4: テスト対象が protected
//

  public class EU06Test {

    // protectedメソッドをテストするときのテンプレ
    private EU02 eu;
    @Before
    public void setUp() throws Exception {
      this.eu02 = new EU02();
    }
    @After
    public void tearDown() throws Exception {
      this.eu02 = null;
    }

    @Test
    public void testGetContent() throws Exception {
      // 実行するときこうする。
      List<String[]> actual = this.eu.getContent();
    }
  }

// ==============================================================================
// ■ 実例5: 例外を出すテスト
//     私はパターン3を使っています。

  // テストクラス。
  public class Target_BazTest {

    @Test(expected = IllegalArgumentException.class)
    public void 例外のテストパターン1() throws Exception {
      // 例外が飛ぶが、expectedを指定してるのでテストが成功する。
      Target.baz(false);
      // このあとに何か書いても実行されない。
    }

    @Test
    public void 例外のテストパターン2() throws Exception {
      try {
        Target.baz(false);
        fail();
      } catch (IllegalArgumentException e) {
        // IllegalArgumentExceptionが出なければfail()になるっていう書き方。
      }
      // このあとに何か書けばそれも実行される。
    }

    @Rule
    public ExpectedException thrown = ExpectedException.none();
    @Test
    public void 例外のテストパターン3() throws Exception {
      // 期待されるExceptionの指定。
      thrown.expect(IllegalArgumentException.class);
      Target.baz(false);
      // このあとに何か書いても実行されない。
    }
  }

// ==============================================================================
// ■ 実例6: モック対象が public
//

  // テスト対象。
  public class Target {
    public int qux(int x) {
      return forMock.hoge(x);
    }

    // モック対象に使うクラス。0を返すけど、それをモックして差し替える。
    public ForMock forMock = new ForMock();
    public class ForMock {
      public int hoge(int y) {
        return 0;
      }
    }
  }

  // テストクラス。
  public class TargetTest_Qux {

    // モック対象。
    @Mock
    private ForMock forMock;

    // モックを挿入する対象。
    @InjectMocks
    private Target target = new Target();

    @Test
    public void forMockインスタンスのモック作成テスト() {
      // 入力値。
      int x = 1;
      // モックの設定。初期化->差し替え。
      MockitoAnnotations.initMocks(this);
      // anyInt()のとこにはフツーに1とか2とかにしてもOK。
      when(forMock.hoge(anyInt())).thenReturn(1);
      // 期待値。
      int expected = 1;
      // 検証。
      int actual = target.qux(x);
      assertThat(actual, is(expected));
    }
  }

// ==============================================================================
// ■ 実例7: モック対象が public static
//

  // PowerMockを使う準備と、PowerMockでモックするクラスを羅列します。
  // PowerMockで囲うものをPrepareForTestしておかないと、ClassNotPreparedExceptionが出る。
  @RunWith(PowerMockRunner.class)
  @PrepareForTest({EsysBatchUtils.class,})
  public class EU02Test {

    @Test
    public void testGetContent() throws Exception {

      // モックして差し替えたい値。
      List<String[]> returnSelectCsv1Rec = new ArrayList<String[]>();

      // 差し替えます。引数のとこは全部anyObject()でもいい。
      PowerMockito.mockStatic(EsysBatchUtils.class);
      when(EsysBatchUtils.selectCsv1Rec(anyObject(), anyString(), anyString())).thenReturn(returnSelectCsv1Rec);

      // 入力値。

      // 期待値。
      List<String[]> expected = returnSelectCsv1Rec;

      // 検証。
      //     対象がprotectedメソッドのときの書き方だけどここでは重要じゃないのでeuの準備は省略してる。
      //     Listの検証については下の例を見てください。
      List<String[]> actual = eu.getContent();
      for (int i = 0; i < actual.size(); i++) {
        assertThat(actual.get(i), is(expected.get(i)));
      }
    }
  }

// ==============================================================================
// ■ 実例8: Listの検証方法
//

    @Test
    public void Listの中身がString配列のテスト() {

      // 期待値。
      List<String[]> expected = new ArrayList<String[]>();
      expected.add(new String[] {"foo", "FOO"});
      expected.add(new String[] {"bar", "BAR"});
      expected.add(new String[] {"baz", "BAZ"});

      // 検証。Listをそのまま比較するとヘンなことになります。Stringとか、配列単位で比較すること。
      List<String[]> actual = Target.abc();
      for (int i = 0; i < actual.size(); i++) {
        assertThat(i + "項目めで失敗。", actual.get(i), is(expected.get(i)));
      }
    }

// ==============================================================================
// ■ 実例9: モック対象が 対象クラス内のprivate
//     これを使ったテストクラスでEclEmmaのカバレッジが表示されない不具合が出てます。

  // テストクラス。
  @RunWith(PowerMockRunner.class)
  @PrepareForTest({EU02.class,})
  public class EU02_GetKeikakuTest {

    @Test
    public void test() throws Exception {

      // 以下のprivateメソッドをモックします。
      // HashMap<String, String> hm = this.fetchForKeikakuAndJisshi();

      // 置き換えるモノを準備。とりあえずカラッポのHashMapってことにしとく。
      HashMap<String, String> returnFetchForKeikakuAndJisshi = new HashMap<String, String>();

      // 置き換え。
      EU02 eu02Mock = PowerMockito.spy(new EU02());
      PowerMockito.doReturn(returnFetchForKeikakuAndJisshi).when(eu02Mock, "fetchForKeikakuAndJisshi");

      // だいぶはまったところ。置き換えは以下の書き方では失敗する。
      //    PowerMockito.when(this.eu02, "fetchForKeikakuAndJisshi")
      //      .thenReturn(returnFetchForKeikakuAndJisshi);

      // 引数のあるprivateメソッドをモックする場合。
      HashMap<String, String> returnCreateOtherData = new HashMap<String, String>();
      PowerMockito.doReturn(returnCreateOtherData).when(eu02Mock, "createOtherData", {引数はここへ  });

      // 検証。
      List<String[]> actual = eu02Mock.getKeikaku();
    }
  }

// ==============================================================================
// ■ 実例10: モック対象が 対象クラス内のprivate かつ テスト対象が private
//     例では、privateOuter()メソッドの中で呼び出されるprivateInner()メソッドをモックします。
//     モックに焦点を絞るためassertThatらへんは省略。

  @RunWith(PowerMockRunner.class)
  @PrepareForTest({EU02.class, })
  public class EU02_PrivateOuterTest {

    @Test
    public void test() throws Exception {

      // 差し替えたい値を準備します。
      String returnPrivateInner = "privateInnerの返り値がStringだとする。";

      // 差し替えます。
      EU02 eu02Mock = PowerMockito.spy(new EU02);
      PowerMockito.doReturn(returnPrivateInner).when(eu02Mock, "privateInner");

      // privateOuter()のアクセス許可を得ます。
      Method method = EU02.class.getDeclaredMethod("privateOuter");
      method.setAccessible(true);

      // 検証。マジでビックリなことに、以下のふたつどちらで実行しても、オッケーである。
      method.invoke(eu02Mock);
      method.invoke(new EU02());

    }
  }

// ==============================================================================
// ■ 実例11: 中々使いやすいと思ったテストメソッドの書き方

  @RunWith(PowerMockRunner.class)
  @PrepareForTest({EsysBatchUtils.class, SurplusSoilPlanUtils.class})
  public class Test {

    // ここに対象クラスとprivate用Methodの宣言。
    private static EU03 euMock;
    private static Method method;

    // BeforeClassにはprivateメソッドアクセスの許可を書く。
    @BeforeClass
    public static void setUpBeforeClass() throws Exception {
      method = EU03.class.getDeclaredMethod("selectForKeikaku");
      method.setAccessible(true);
    }

    // Beforeには対象クラスのモック作成を書く。あと全テストメソッドで共通に使うメソッドの作成。
    @Before
    public void setUp() throws Exception {
      euMock = PowerMockito.spy(new EU03());

      PmsSql returnPmsSql = PowerMockito.mock(PmsSql.class);
      PowerMockito.doReturn(returnPmsSql).when(euMock, "createSelectForKeikakuPmsSql");
    }

    // Afterには対象クラスモックの削除。
    @After
    public void tearDown() throws Exception {
      euMock = null;
    }

    @Test
    public void test() throws Exception {
      // ここにモック作成を書く。

      // 入力値。

      // 期待値。

      // 検証。
    }

  }

// ==============================================================================
// ■ 実例12: モック対象が voidを返すメソッド

  // モック対象
  //     EsysBatchUtils.deleteInsertTCreFileCapture(x_ssp, siteNo, csvFileCl, csvContent)
  PowerMockito.spy(EsysBatchUtils.class);
  PowerMockito.doNothing().when(EsysBatchUtils.class, "deleteInsertTCreFileCapture", anyObject(),
      anyObject(), anyObject(), anyObject());

// ==============================================================================
// ■ 実例13: ひたすらたくさんの入力値、期待値パターンを書く + 例外パターンを含む場合の書き例
  @RunWith(Parameterized.class)
  public class EsysBatchFileUtils_ConvertZipCodeWithHyphenTest {

    @Rule
    public ExpectedException thrown = ExpectedException.none();

    private final String zipCodeWithoutHyphen;
    private final String expected;
    private final boolean expectException;

    public EsysBatchFileUtils_ConvertZipCodeWithHyphenTest(
        String zipCodeWithoutHyphen, String expected, boolean expectException) {

      this.zipCodeWithoutHyphen = zipCodeWithoutHyphen;
      this.expected = expected;
      this.expectException = expectException;
    }

    @Parameters(name = "zipCodeWithoutHyphen:{0}, expected:{1}, expectException:{2}")
    public static Iterable<Object[]> data() {
      return Arrays.asList(new Object[][] {
          // 正常系。
          {"0000000", "000-0000", false,},
          // 正常系。
          {"1234567", "123-4567", false,},
          // 正常系。
          {"１２３４５６７", "１２３-４５６７", false,},
          // IllegalArgumentException
          {"郵便番号", "", true,},
          // 正常系。
          {"一二三四五六七", "一二三-四五六七", true,},
        });
    }


    @Test
    public void test() {
      if (expectException) {
        thrown.expect(IllegalArgumentException.class);
        EsysBatchFileUtils.convertZipCodeWithHyphen(zipCodeWithoutHyphen);
      } else {
        String actual = EsysBatchFileUtils.convertZipCodeWithHyphen(zipCodeWithoutHyphen);
        assertThat(actual, is(expected));
      }
    }

  }

// ==============================================================================
// ■ 実例14: テスト対象が private static で、かつ例外テストをしたいとき
// method.invoke()が例外を出すと本来の例外がInvocationTargetExceptionに覆い隠されちゃって
// thrown.expect(期待してたException.class)で受け止められない。

  @Test
  public void test() throws Throwable {
    // 検証。
    if (this.expectIllegalArgumentException) {
      try {
        method.invoke(AddConstrUtils.class, this.deptCl, this.constrCl);
      } catch (InvocationTargetException e) {
        // 投げられたInvocationTargetExceptionから本来のExceptionをほじくりだす。
        thrown.expect(IllegalArgumentException.class);
        throw e.getCause();
      }
    } else {
      String actual = (String) method.invoke(AddConstrUtils.class, this.deptCl, this.constrCl);
      assertThat(actual, is(this.expected));
    }
  }

// ==============================================================================
// ■ 実例15: PowerMockとParameterizedを同時に使いたい

  @RunWith(PowerMockRunner.class)
  @PowerMockRunnerDelegate(Parameterized.class)








@BeforeClass
public static void setUpBeforeClass() throws Exception {}

@Before
public void setUp() throws Exception {}

@After
public void tearDown() throws Exception {}









