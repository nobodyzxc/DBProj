# DB final project - markdown blog builder

## Start

To run this project, you need

```
pip install flask
pip install flask_login
```

### Material

[flask](https://spacewander.github.io/explore-flask-zh/index.html)
[flask-login](http://www.pythondoc.com/flask-login/)

### Based On

[Editor.md](https://github.com/pandao/editor.md/)

### TODO

> 模板使用的語言為 Jinja，大夥開幹啦～

- `index.html`
我們的主頁，希望可以連結到註冊及登入頁面
加上一些 Project 介紹，還可以 Show 一些用戶的 Blog。

- `login.html`
登入及註冊頁面
必須實作 login 功能，可以先用個簡單的 Form
希望可以參考 [flask-login](http://www.pythondoc.com/flask-login/) 及 [flask-wtf](https://spacewander.github.io/explore-flask-zh/11-handling_forms.html)。
登入後跳轉到 console.html

- `console.html`
希望可以放已經存在的 posts，做簡單管理，
然後可以轉跳到 editor.html, 及 config.html

- `editor.html`
接上 [Editor.md](https://github.com/pandao/editor.md/)
然後存 md 到資料庫。
（還要提供 render，可將 db 的 md render 成 html。)

- `config.html`
可以配置一些 user 的東西。
例如 markdown 的渲染方法及 layout。

- `blog/<user>`
實作從資料庫參考 user 的 config 及動態渲染 user blog
