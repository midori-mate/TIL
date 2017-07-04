
// JUnit、Mockito、PowerMockノート

// 目次
// ■ テストファイル作成手順
// ■ テストファイルの命名規則とか作成単位
// ■ テストファイルに自分で書いたほうがよさげなimport
// ■ ちょっとした疑問点
// ■ 実例1-1: staticメソッドをテストしたいとき
// ■ 実例1-2: ひたすらたくさんの入力値・期待値パターンを書く
// ■ 実例2: privateメソッドをテストしたいとき
// ■ 実例3: 例外を出すメソッドをテストしたいとき
// ■ 実例4: publicなインスタンスメソッドのモック
// ■ 実例5: publicな外部staticメソッドのモック
// ■ 実例6: privateなインスタンスメソッドのモック
// ■ 実例7: 二次元配列のテスト方法(主にList<String[]>)
// ■ 実例8: 同じクラスの中のprivateメソッドをモック
// ■ 実例9: 対象がprivateメソッドで、かつその中のprivateメソッド呼出をモック
// ■ オマケ: よく使うテンプレート


// ■ 手順
//     ● 普通に作ると実ファイルと同じトコにテストjavaファイルが作られて邪魔いのでテスト用フォルダを作る
//         プロジェクト右クリック > New > SourceFolder
//     ● JUnitファイルの作成
//         テストしたいjavaファイル右クリック > New > JUnit Test Case
//         > SourceFolderを上で作ったトコに > 名前決めてNext
//         > テストを作りたいメソッドにチェック(いちばん下の実例で触れてるけどこれは必須じゃない) > 完了
//         ★ ダイアログにあるsetUpBeforeClassとかは何?
//             setUpBeforeClass   いっちばん最初に実行される。
//             tearDownAfterClass いっちばん最後に実行される。
//             setUp              各テスト実行前に実行される。
//             tearDown           各テスト実行後に実行される。
//     ● JUnitファイルの中に検証スクリプトを書く
//         ★ 検証って実際どう書くの?
//             ナウいシリーズ
//                 assertThat(method, is(expected));              みたまんま
//                 assertThat(method, is(not(expected)));         否定
//                 assertThat(method, is(nullValue()));           null
//                 assertThat(method, is(instanceOf(Foo.class))); そのクラスのインスタンスである
//                 その他使えるもの(参考:http://qiita.com/opengl-8080/items/e57dab6e1fa5940850a3)
//             ナウくないシリーズ
//                 assertEquals(expected, method);
//                 assertEquals(message, expected, method);
//                 assertTrue(method);
//                 assertFalse(message, method);
//                 assertNull(method);
//                 assertNotNull(message, method);
//                 fail(message);
//     ● テスト方法
//         Run as > JUnit Test(Shift+Alt+X,T)
//     ● JUnitファイルを個別にちまちま実行するのは面倒なので、一括で実行する。
//         プロジェクト右クリック > New > Other,JUnit,JUnit Test Suite > 作ったテスト全部チェック
//         > AllTestsって名前で保存(AllTestsって名前が一般的らしい)
//         作ったファイルを JUnit Test 実行すれば全部まとめてテストされる。

// ■ テストファイル作成の単位(後述しますって書いたもの)
//     ● テストクラスはメソッド単位で作る。名前は"対象クラス名_メソッド名Test"。例:Klass_FooTest
//     ● テスト一括実行はクラス単位で作る。名前は"対象クラス名AllTests"。例:KlassAllTests

// ■ 自分で書いたほうがよさげなimport
//     import static org.junit.Assert.*;
//     import static org.hamcrest.CoreMatchers.*;
//     import static org.hamcrest.Matchers.*;
//     import static org.mockito.Mockito.*;

// ■ 疑問点
//     問題:JUnitファイルを作ったあとで本体クラスにメソッドが増えたら、その分のメソッドはどうやって増やすの? 手動なの?
//         んー手動しか見つけられなかった。最初メソッドにチェックつけたダイアログみたいなのをもう一度出して、
//         増えたメソッドにチェックして反映〜みたいなのを期待してたんだけれど。
//         未解決
//     問題:AllTests作ったあとでテストを追加したいときは? また作り直すの?
//         AllTests右クリック > Recreate Test Suite
//         そう、こういうものを期待してたんだよ。

// ==============================================================================
// ■ 実例1-1: staticメソッドをテストしたいとき

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
// ■ 実例1-2: ひたすらたくさんの入力値・期待値パターンを書く

// テスト対象。
public class Target {
  public static int foo(int x) {
    return x;
  }
}

// テストクラス。1~5の手順で。
// 1. これを書きます。
@RunWith(Parameterized.class)
public class Target_FooTest2 extends Target {

  // 2. 入力値とか期待値をインスタンス変数にしときます。
  private final int x;
  private final int expected;

  // 3. コンストラクタを書きます。
  public Target_FooTest2(int x, int expected) {
    this.x = x;
    this.expected = expected;
  }

  // 4. 入力値、期待値とかのリストを作ります。
  //     nameのとこは書かなくてもいい。好きなフォーマットでどうぞ。
  //     Integer[]とかnew Integer[][]のところは入力値の型にあわせて。
  //     Object[]でも大丈夫だからString Integer混成でもOK。
  //     ここ、IntegerをintにしたらinitializationErrorになります。
  @Parameters(name = "No.{index} x({0}) expected({1})")
  public static Iterable<Integer[]> 入力値と期待値のリスト() {
    return Arrays.asList(new Integer[][] {
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
// ■ 実例2: privateメソッドをテストしたいとき

// テスト対象。
public class Target {
  private int bar(int x) {
    return x;
  }
}

// テストクラス。
public class TargetTest_Bar {
  @Test
  public void ユニットテストPrivateAndProtectedメソッド() throws Exception {
    // 入力値。
    int x = 1;
    // 期待値。
    int expected = 1;
    // privateメソッドへのアクセス許可を得ます。
    Method method = Target.class.getDeclaredMethod("bar", int.class);
    method.setAccessible(true);
    // 検証。
    int actual = (int)method.invoke(new Target(), x);
    assertThat(actual, is(expected));
  }
}

// ==============================================================================
// ■ 実例3: 例外を出すメソッドをテストしたいとき

// テスト対象。
public class Target {
  public static boolean baz(boolean x) throws Exception {
    if (!x) {
      throw new IllegalArgumentException();
    }
    return x;
  }
}

// テストクラス。
public class TargetTest_Baz {
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
      // IllegalArgumentExceptionが出たときだけテストが成功する、という書き方。
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
// ■ 実例4: publicなインスタンスメソッドのモック

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
// ■ 実例5: publicな外部staticメソッドのモック
// テスト対象は省略。EU06.getContentのテストを例にします。
// powermockに関係あるところは★で囲ってある。

// ★ PowerMockでEsysBatchUtilsのstaticメソッドをモックする準備 ★
@RunWith(PowerMockRunner.class)
@PrepareForTest({EsysBatchUtils.class,})
public class EU06Test {

  // ========== protectedメソッドをテストするときのテンプレ ==========
  private EU06 eu;
  @Before
  public void setUp() throws Exception {
    this.eu = new EU06();
  }
  @After
  public void tearDown() throws Exception {
    this.eu = null;
  }
  // ========== ここまで ==========

  @Test
  public void testGetContent() throws Exception {

    // モックして差し替えたい値。
    List<String[]> returnSelectCsv1Rec = new ArrayList<String[]>();

    // ★ EsysBatchUtils.selectCsv1Recのモックを作成する箇所。 ★
    PowerMockito.mockStatic(EsysBatchUtils.class);
    // ★ anyなんちゃらの部分には目当てのメソッドの引数に該当するものを書く。ぶっちゃけ全部anyObject()でいいんじゃね? ★
    when(EsysBatchUtils.selectCsv1Rec(anyObject(), anyString(), anyString())).thenReturn(
        returnSelectCsv1Rec);

    // 入力値。

    // 期待値。
    List<String[]> expected = returnSelectCsv1Rec;

    // 検証。
    List<String[]> actual = eu.getContent();
    for (int i = 0; i < actual.size(); i++) {
      assertThat(actual.get(i), is(expected.get(i)));
    }
  }
}


// ==============================================================================
// ■ 実例6: privateなメソッドのモック
// PowerMock必要。
// 今のところ出てきていないが、実例8や実例9のを応用できそう。

// ==============================================================================
// ■ 実例7: 二次元配列のテスト方法(主にList<String[]>)

// テスト対象。
public class Target {
  // List<String[]>を返すメソッド。こっちがモンダイ。
  public static List<String[]> abc() {
    List<String[]> ret = new ArrayList<String[]>();
    ret.add(new String[] {"foo", "FOO"});
    ret.add(new String[] {"bar", "BAR"});
    ret.add(new String[] {"baz", "BAZ"});
    return ret;
  }

  // String[][]を返すメソッド。こっちはフツーに比較してOK。
  public static String[][] xyz() {
    String[][] ret = new String[][] {
        {"foo", "FOO"},
        {"bar", "BAR"},
        {"baz", "BAZ"},
    };
    return ret;
  }
}

// テストクラス。
public class Target_XyzTest {
  @Test
  public void Listの中身がString配列のテスト() {

    // 期待値。
    List<String[]> expected = new ArrayList<String[]>();
    expected.add(new String[] {"foo", "FOO"});
    expected.add(new String[] {"bar", "BAR"});
    expected.add(new String[] {"baz", "BAZ"});

    // 検証。Listをそのまま比較するとヘンなことになるみたいです。
    List<String[]> actual = Target.abc();
    for (int i = 0; i < actual.size(); i++) {
      assertThat(actual.get(i), is(expected.get(i)));
    }
  }

  @Test
  public void String２次元配列のテスト() {

    // 期待値。
    String[][] expected = new String[][] {
        {"foo", "FOO"},
        {"bar", "BAR"},
        {"baz", "BAZ"},
    };

    // 検証。
    String[][] actual = Target.xyz();
    assertThat(actual, is(expected));
  }

}

// ==============================================================================
// ■ 実例8: 同じクラスの中のprivateメソッドをモック
//     テスト対象: protectedメソッド
//     モック対象: テスト対象とおんなじクラスのprivateメソッド

// 注意: これを使ったテストクラスで、EclEmmaのカバレッジが表示されないって不具合が出てます。

// テストクラス。
// テスト対象も例を書きたいところだが、mavenプロジェクト外で作ると依存関係がちゃんと解決できなかった。
// だから実例にはEU02を使う。
@RunWith(PowerMockRunner.class)
@PrepareForTest({EU02.class,})
public class EU02_GetKeikakuTest {

  // ========== protectedメソッドをテストするときのテンプレ ==========
  private EU02 eu;
  @Before
  public void setUp() throws Exception {
    this.eu = new EU02();
  }
  @After
  public void tearDown() throws Exception {
    this.eu = null;
  }

  @Test
  public void test() throws Exception {

    // 以下のprivateメソッドをモックします。
    // HashMap<String, String> hm = this.fetchForKeikakuAndJisshi();

    // 置き換えるモノを準備。とりあえずカラッポのHashMapってことにしとく。
    HashMap<String, String> returnFetchForKeikakuAndJisshi = new HashMap<String, String>();

    // 置き換え。
    EU02 eu02Mock = PowerMockito.spy(eu);
    PowerMockito.doReturn(returnFetchForKeikakuAndJisshi).when(eu02Mock, "fetchForKeikakuAndJisshi");

    // だいぶはまったところ。以下の書き方では失敗する。
    //    PowerMockito.when(this.eu02, "fetchForKeikakuAndJisshi")
    //      .thenReturn(returnFetchForKeikakuAndJisshi);

    // 引数のあるprivateメソッドをモックする場合。
    HashMap<String, String> returnCreateOtherData = new HashMap<String, String>();
    PowerMockito.doReturn(returnCreateOtherData).when(eu02Mock, "createOtherData",
        {ここに引数});
  }
}

// ==============================================================================
// ■ 実例9: 対象がprivateメソッドで、かつその中のprivateメソッド呼出をモック
//     例では、privateOuter()メソッドの中で呼び出されるprivateInner()メソッドをモックします。
//     モックに焦点を絞るためにassertThatらへんは省略。

// PowerMockでモックするクラスを並べておきます。
@RunWith(PowerMockRunner.class)
@PrepareForTest({EU02.class, })
public class EU02_PrivateOuterTest {

  @Test
  public void test() throws Exception {

    // 差し替えたい値を準備します。
    String returnPrivateInner = "privateInnerの返り値がStringの場合。";

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
// よく使うテンプレート。

// まず書く
import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.*;
import static org.hamcrest.Matchers.*;
import static org.mockito.Mockito.*;

// PowerMock準備
@RunWith(PowerMockRunner.class)
@PrepareForTest({SeiServletParam.class})

public class Test {

  // 一時ディレクトリ
  @Rule
  public TemporaryFolder junitTempFolder = new TemporaryFolder();

  // 例外
  @Rule
  public ExpectedException thrown = ExpectedException.none();

  @Before
  public void setUp() throws Exception {
  }

  @After
  public void tearDown() throws Exception {
  }

  @Test
  public void testGetFileName() {
    // 入力値。

    // 期待値。
    String expected = "";

    // 検証。
    String actual = method();
    assertThat(actual, is(expected));
  }
}








