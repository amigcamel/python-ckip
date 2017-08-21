# python-ckip 

(支援Python2 / Python3)  
想要使用CKIP Chinese Parser 進行小規模的斷詞測試  
毋需登入即可使用  
  
基本上它就是幫你方送HTTP request  
然後把結果撈出來  


## 安裝

    pip install ckippy

## 使用

    from ckippy import parse_tree

    parse_tree('中研院斷詞器真是好棒棒')
