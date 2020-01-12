# Pythonのimportについて

pythonのimportが把握できていなかったので調べてみた。（特に親階層や別階層にあるモジュールの使い方）
簡単なサンプルコードも追加しています。

## import文
二つの処理を連続して行っている
- ある名前のモジュールを探し、
- 検索結果をローカルスコープの名前に束縛？する

モジュールが初めてインポートされる時、Pythonはそのモジュールを検索→見つかったらモジュールオブジェクトを作成し、初期化する。

モジュールが見つからなければ、 ModuleNotFoundErrorを送出する。

## パッケージ
モジュールオブジェクトの種類は1つしかなく、PythonでもCでも、それ以外の実装でも関係なく全て一種類。

パッケージはファイルシステムのディレクトリ、
モジュールはディレクトリにあるファイル、

と考えることができるが、パッケージやモジュールはファイルシステムから生まれる必要はない（完全に一致するとは限らないし必要性はない）

全てのパッケージはモジュールだが、
全てのモジュールがパッケージとは限らない

パッケージには、以下の二種類がある。
- 通常のパッケージ
- 名前空間パッケージ

### 通常のパッケージ

`__init__.py`を含むディレクトリとして実装される。
通常のパッケージがインポートされた時、__init__.pyが暗黙的に実行され、そこで定義しているオブジェクトがパッケージ名前空間の名前に束縛される。

例：
以下のファイルシステム配置は、3つのサブパッケージを持つ最上位の`parent`パッケージを定義する。

```
parent/
 __init__.py
 one/
  __init__.py
 two/
  __init__.py
 three/
  __init__.py
```

parent.oneをインポート→ parent/__init__.py, parent/one/__init__.pyが実行される。
その後two,threeのものをインポートすると、まだ読み込まれていない__init__.pyが実行される

### 名前空間パッケージ

様々なポーションを寄せ集めたもので、ポーションはサブパッケージを親パッケージに提供する。
ポーションは、
- ファイルシステムの別の場所にあることも
- zipファイルの中
- ネットワーク上
その他の箇所にあるかも。
それらは実際の実体のない**仮想モジュール**

仮想モジュールには、 `__init__.py`は存在しない。
階層は通常のようになっているとも限らない。

## 検索
`import モジュール名`：
モジュール名.関数名やモジュール名.変数名
のように使うことがdケイル

```
import math
print(type(math)) # <class 'module'>

print(math) # <module 'math' from ////>


print(math.radians(1))
print(math.pi)
```

### インポート順
1. 標準ライブラリ
2. サードパーティライブラリ
3. 自作ライブラリ

### from
fromを使って、モジュールで定義されたオブジェクト（関数、変数、クラスなど）を指定してインポートできる。

インポートしたオブジェクトは、"オブジェクト名"で直接利用できる。
インポートされるのは指定したオブジェクトだけでモジュール自体はインポートsれない。
やろうとすると NameErrorになる。

例：
```
from math import pi

print(pi) # mathをつけなくて良い
#print(math.radians(100)) # NameError: name 'math' is not definedになる
```

アスタリスク（ワイルドカード）を使うと全てのオブジェクトがインポートされる。

```
from math import *

print(pi)
print(cos(0))
```

### 実例
__init__.pyにちゃんと記述がなければ、import urllib などだけでは配下の parse, requestなどは使うことができない。

## 親階層や別階層にあるモジュールのimport

様々な方法があるが、ここでは`sys.path.append('[パス]')`の方法を採用しています。
sys.pathは単なるリストなので、このようにすることで検索対象を追加することができる。

``` folder21.py
import sys
sys.path.append("../")
from folder1 import folder11
```

## 参考
- [https://docs.python.org/ja/3/reference/import.html](https://docs.python.org/ja/3/reference/import.html)
- [https://note.nkmk.me/python-import-usage/](https://note.nkmk.me/python-import-usage/)