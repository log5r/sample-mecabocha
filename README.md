# sample-mecabocha

[Technical Writing Meetup vol.36](https://tw-meetup.connpass.com/event/330008/) で用いたサンプルです。

30分くらいで作ったのでいろいろ不備があるかもしれません...🙏

## How to use

1. cabocha-pythonのインストールを成功させるために、環境変数をセットします
   * ```shell
        export LIBRARY_PATH=/opt/homebrew/Cellar/cabocha/0.69/lib:/opt/homebrew/Cellar/mecab/0.996/lib:/opt/homebrew/Cellar/crf++/0.58/lib
        export CPLUS_INCLUDE_PATH=/opt/homebrew/Cellar/cabocha/0.69/include:/opt/homebrew/Cellar/mecab/0.996/include:/opt/homebrew/Cellar/crf++/0.58/include
        ```
2. Homebrewを用いて cabochaを、 `pip` を用いてcabocha-pythonをインストールします。
   * `brew install cabocha`
   * `pip install cabocha-python` 
   * Apple Silicon 搭載の Mac の場合は以下のようにソースからビルドする必要があるかもしれません。
     * ```shell
        brew install -s cabocha
        ARCHFLAGS='-arch arm64' pip install --compile --use-pep517 --no-cache-dir --force cabocha-python
       ``` 
3. graphvizをインストールします
   * `pip install graphviz`
4. `main.py` を実行します。
5. `out/graph/` 以下にグラフの画像が生成されます。
