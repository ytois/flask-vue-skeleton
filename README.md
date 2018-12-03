# flask-vue-skeleton

## Project setup

```
npm install
pip install pipenv
pipenv install
```

## commands

```shell
# Compiles and hot-reloads for development
npm run serve

# Compiles and minifies for production
npm run build

# Run your tests
npm run test

# Lints and fixes files
npm run lint
```

## 構成

### バックエンド

|                  |           |
| ---------------- | --------- |
| メイン言語       | Python    |
| フレームワーク   | Flask     |
| テンプレート言語 | Pug(Jade) |
| パッケージ管理   | Pipenv    |

### フロントエンド

|                      |                  |
| -------------------- | ---------------- |
| モジュールバンドラー | Webpack(Vue-Cli) |
| JavaScript           | ES2015           |
| JS フレームワーク    | Vue.js           |
| HTML テンプレート    | Pug              |
| CSS                  | Stylus           |
| CSS フレームワーク   | Bulma / Buefy    |
| パッケージ管理       | npm              |

### ディレクトリ構成

```
- /backend
  - /config
  - /static
  - /templates
  - app.py
  - secrets.py

- /frontend
  - /assets
  - /components
  - /pages
  - /store
  - main.js
  - router.js

```

### ビルド

Webpack でビルド時に`/backend/static/`が一度初期化され、ビルド済みファイルが配置される。  
そのため`/backend/static/`配下に直接ファイルを配置せず、フロント周りのファイルは基本`/frontend/`配下で管理する。  
ただし、コンポーネント化していない HTML ファイルは`/backend/templates`配下に置く。(SPA のエントリーポイントとなる index.html など)  
→ 非 SPA ページを取り扱う可能性もあるため

1. Webpack でビルド
2. `/backend/static/`に`manifest.json`が生成される
3. `manifest.json`にかかれているパスを元に Flask で HTML テンプレートに js/css をインクルードする

## コーディング規約

- Python: flake8
- JavaScript: ESLint-Standard
