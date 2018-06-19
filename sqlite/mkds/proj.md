# DB final project

> markdown blog builder

### Start

To run this project, you need

```
pip install flask
pip install flask_login
pip install markdown2
```

### Material

- [flask](https://spacewander.github.io/explore-flask-zh/index.html)
- [flask-login](http://www.pythondoc.com/flask-login/)

### Based On

[Editor.md](https://github.com/pandao/editor.md/)

### TODO

> 模板使用的語言為 [Jinja](http://docs.jinkan.org/docs/jinja2/)，請大家熟悉

- `/index`

   我們的主頁，希望可以連結到註冊及登入頁面

   加上一些 Project 介紹，還可以 Show 一些用戶的 Blog。

- `/login`

   登入及註冊頁面

   必須實作 login 功能，可以先用個簡單的 Form

   希望可以參考 [flask-login](http://www.pythondoc.com/flask-login/) 及 [flask-wtf](https://spacewander.github.io/explore-flask-zh/11-handling_forms.html)。

   登入後跳轉到 manage.html

- `/manage`

   希望可以放已經存在的 posts，做簡單管理，

   然後可以轉跳到 editor.html, 及 config.html

- `/editor`

   接上 [Editor.md](https://github.com/pandao/editor.md/)

   然後存 md 到資料庫。

   取消或儲存回到 manage.html

- `/config`

   可以配置一些 user 的東西。

   例如 markdown 的渲染方法及 layout。

   這裡有 css 供參考，你要提供一些 css 配置供使用者挑選，可將 db 的 md render 成 html。

   - [link1](http://markdowncss.github.io)
   - [link2](http://jasonm23.github.io/markdown-css-themes/)
   - [link3](https://sindresorhus.com/github-markdown-css/)

   儲存後回 manage.html

- `/blog/<user>`
- `/blog/<user>/<post>`

   提供 layout。

   實作從資料庫參考 user 的 config 及動態渲染 user blog

   使用 markdown [render](https://github.com/trentm/python-markdown2)

   注意他的 [Extra](https://github.com/trentm/python-markdown2/wiki/Extras) 用法，最重要的是 [code block](https://github.com/trentm/python-markdown2/wiki/fenced-code-blocks) 要有顏色！

   some render vars
   ```
   blog_name
   blog_href
   user_name
   post_title
   post_href
   post_time
   post_wedge
   post_content
   ```
