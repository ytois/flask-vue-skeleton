# db

## document

https://flask-migrate.readthedocs.io/en/latest/

## Database / User 作成

- Docker コンテナ立ち上げ時に`docker-entrypoint/initialize.sql`が実行されるため不要。
- ローカルの DB につなぐ場合は予め作成しておく。

```shell
psql -U postgres
CREATE DATABASE flask;
CREATE ROLL flask WITH LOGIN PASSWORD 'xxxx';
```

## マイグレーション手順

0. ※不要※

以下で`migrations`ディレクトリが作成される

```shell
python manage.py db init
```

1. マイグレーションファイルの作成

モデルの編集・作成  
新規モデルの場合は`app.py`に読み込まれるように`models/__init__.py`を編集する

```python
# models/__init__.py
__all__ = [
    User # 追加
]
```

以下コマンドで`migrations/versions`配下へマイグレーションファイルが作成される

```shell
python manage.py db migrate
```

3. マイグレーションの実行

```shell
python manage.py db upgrade
```

### ロールバック

一つ前に戻す

```shell
python manage.py db downgrade
```
