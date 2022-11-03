# stable-diffusion-without-gpu

[English version](README.md)
## インストール

Windowsの場合はWSL2上でUbuntuを利用することをお勧めします。

1. `docker`と`docker-compose`をインストールします。
2. Hugging Faceでアカウントを作成し、メール認証を済ませた後、モデルのダウンロードとトークンの取得を行います。
3. `docker-compose.yml`をエディタで開き、`HUGGING_FACE_TOKEN`の値をあなたのHugging Faceのトークン文字列に置き換えてください。
4. 以下のコマンドを実行してください。  

    ```sh
    $ git clone https://github.com/hidao80/stable-diffusion-without-gpu
    ```

## 使い方

1. ターミナルに次のコマンドを入力すると、stable diffusion環境が起動します。  

    ```sh
    $ cd stable-diffusion-without-gpu
    $ docker-compose up --build -d
    ```

2. 続けてターミナルに次のコマンドを入力すると、画像を作成します。  

    ```sh
    $ ./generate.sh "green apple"
    ```

3. `stable-diffusion-without-gpu/files/output.png`に画像がが生成されます。
