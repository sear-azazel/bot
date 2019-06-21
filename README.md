# Botサーバ
Slack Bot API用サーバ


## 開発環境構築
### 共通
- ローカル環境設定
    1. `src/bot/local_settings.py`を作成
    1. `src/bot/settings.py`から上書きする設定を記載
        - 例）DBの設定を上書き
            ```
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                }
            } 
            ```

### Anacondaの場合
1. Anaconda Navigatorの起動
1. 仮想環境作成
    - EnvironmentsタブからCreate
    - python 3.7を選択
    - 作成した環境に変更
1. ライブラリのインストール
    - Environmentsタブで下記ライブラリを選択
        - django
        - mysqlclient
        - sqlparse
1. Terminalを起動
    - Environmentsタブの仮想環境からOpen Terminalを選択
    - プロジェクトフォルダへ移動
1. DBの指定
    - `src\bot\settings.py`の`DATABASES`を環境に合わせて修正
1. サーバ起動
    - Terminal上で下記コマンドを実行
        ```
        python src\manage.py runserver 0.0.0.0:8000
        ```

### Dockerの場合
1. コンテナ起動
    ```
    docker-compose up -d
    ```

## DBマイグレーション
1. DB作成
    `docker\mysql\sql\init.sql`を実行
1. マイグレーションコマンドの実行
    ```
    python src\manage.py makemigrations
    python src\manage.py migrate
    ```
