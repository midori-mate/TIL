Public Class Class1

    ' このよっつをユニットテストでテストするよ～
    ' 引数0 のとき ArgumentException
    ' 引数1 のとき ArgumentOutOfRangeException
    ' 引数2 のとき そのまま2
    ' 引数その他 のとき 100
    Shared Function TestTarget(ByVal x As Integer) As Integer

        If x = 0 Then
            Throw New ArgumentException
        ElseIf x = 1 Then
            Throw New ArgumentOutOfRangeException
        ElseIf x = 2 Then
            TestTarget = x
            Exit Function
        Else
            TestTarget = 100
            Exit Function
        End If

    End Function

End Class
