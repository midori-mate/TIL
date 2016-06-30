
// C#とPHPのSHA256

// 結果はどちらも  0966c798f8e7623d8e66d76b72e4455164ab28d2eed108fad668e5fa168c872d

// C#
private string getSha256(string str)
{
    System.Security.Cryptography.SHA256 sha256 = System.Security.Cryptography.SHA256Managed.Create();
    byte[] byteValue = Encoding.UTF8.GetBytes(str);
    byte[] hash = sha256.ComputeHash(byteValue);
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < hash.Length; i++)
    {
        sb.AppendFormat("{0:x2}", hash[i]);
    }
    return sb.ToString();
}

// PHP
hash('sha256', $score.$player.$salt);

