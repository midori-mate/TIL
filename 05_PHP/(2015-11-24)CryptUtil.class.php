<?php
//==============================================================================
// 暗号・復号クラス
//==============================================================================

class CryptUtil
{
    // アカウントパスワードは暗号化して保存するか
    protected $encrypt_enabled = true;
    
    // openssl_encryptで使うメソッドとパスワード
    protected $encrypt_method = 'aes-256-ecb';
    protected $encrypt_password = 'aaaK8fLj';
    
    //--------------------------------------------------------------------------
    // 暗号化
    //--------------------------------------------------------------------------
    public function encrypt($str)
    {
        if ($this->encrypt_enabled && function_exists('openssl_encrypt')) {
            $return = openssl_encrypt($str, $this->encrypt_method, $this->encrypt_password);
            if ($return === false) {
                return $str;
            }
            return $return;
        }
        return $str;
    }
    
    //--------------------------------------------------------------------------
    // 復号化
    //--------------------------------------------------------------------------
    public function decrypt($str)
    {
        //if ($this->encrypt_enabled && function_exists('openssl_decrypt')) {
        if (strlen($str) > 16 && function_exists('openssl_decrypt')) {
            $return = openssl_decrypt($str, $this->encrypt_method, $this->encrypt_password);
            if ($return === false) {
                return $str;
            }
            return $return;
        }
        return $str;
    }
}