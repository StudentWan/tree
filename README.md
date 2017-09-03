## 生成文件夹树形结构

### 运行
```
python tree.py $1 $2 $3 ...
```
`$n`为需要忽略的文件或文件夹

### 适用

`MAC OSX `

### python版本

`2.7.13`

### 举例

对于： https://github.com/ecomfe/san/tree/master/example/todos-esnext
这个项目

使用：
```
python tree.py ./node_modules ./dist *.DS_Store
```

得到结果：
```
.
|_ .babelrc
|_ .gitignore
|_ build
|  |_ build.js
|  |_ dev-client.js
|  |_ dev-server.js
|  |_ utils.js
|  |_ webpack.base.conf.js
|  |_ webpack.dev.conf.js
|  |_ webpack.prod.conf.js
|_ config
|  |_ dev.env.js
|  |_ index.js
|  |_ prod.env.js
|  |_ test.env.js
|_ index.html
|_ package-lock.json
|_ package.json
|_ README.md
|_ src
|  |_ category
|  |  |_ Add.san
|  |  |_ Edit.san
|  |_ data.js
|  |_ filters.js
|  |_ main.css
|  |_ main.js
|  |_ service.js
|  |_ todo
|  |  |_ Form.san
|  |  |_ List.san
|  |_ ui
|  |  |_ Calendar.san
|  |  |_ CalendarLayer.san
|  |  |_ CategoryPicker.san
|  |  |_ ColorPicker.san
|  |  |_ TimePicker.san
|  |  |_ TimePickerLayer.san
```