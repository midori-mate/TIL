Imports System.Text
Imports Microsoft.VisualStudio.TestTools.UnitTesting

<TestClass()> Public Class UnitTest1

    ' これをテストする TestMethod0
    ' 引数0 のとき ArgumentException
    <TestMethod()> Public Sub TestMethod0()

        ' 引数
        Dim x As Integer
        x = 0

        ' 検証
        Try
            ConsoleApplication1.Class1.TestTarget(x)
        Catch ex As Exception
            Assert.AreEqual("System.ArgumentException", ex.GetType().FullName)
            Return
        End Try
        Assert.Fail("Exceptionが出なかった!")

    End Sub

    ' これをテストする TestMethod1
    ' 引数1 のとき ArgumentOutOfRangeException
    <TestMethod()> Public Sub TestMethod1()

        ' 引数
        Dim x As Integer
        x = 1

        ' 検証
        Try
            ConsoleApplication1.Class1.TestTarget(x)
        Catch ex As Exception
            Assert.AreEqual("System.ArgumentOutOfRangeException", ex.GetType().FullName)
            Return
        End Try
        Assert.Fail("Exceptionが出なかった!")

    End Sub

    ' これをテストする TestMethod2
    ' 引数2 のとき そのまま2
    <TestMethod()> Public Sub TestMethod2()

        ' 引数
        Dim x As Integer
        x = 2

        ' 期待値
        Dim expected As Integer
        expected = 2

        ' 検証
        Dim actual As Integer
        actual = ConsoleApplication1.Class1.TestTarget(x)
        Assert.AreEqual(expected, actual)

    End Sub

    ' これのテストをする TestMethod3
    ' 引数その他 のとき 100
    <TestMethod()> Public Sub TestMethod3()

        ' 引数
        Dim x As Integer
        x = 3

        ' 期待値
        Dim expected As Integer
        expected = 100

        ' 検証
        Dim actual As Integer
        actual = ConsoleApplication1.Class1.TestTarget(x)
        Assert.AreEqual(expected, actual)

    End Sub

End Class