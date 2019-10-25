# Рекламный агрегатор


### Авторизация:

- /login. В запрос входит два параметра: логин и пароль. Сейчас создан тестовый пользователь с логином: admin и паролем: admin. В ответ приходит json с уникальным токеном пользователя. В последующем все запросы к базе должны иметь этот token в качестве аргумента.

##### Пример:
```
var xhttp = new XMLHttpRequest();
xhttp.open("POST", "/login", true);
xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
xhttp.send("login=admin&password=admin");
```

##### Ответ:

```
{
  "token": "eyJhbGciOiJIUzUxMiIsImlhdCI6MTU3MTE2MjU1NCwiZXhwIjoxNTcxMTcyNTU0fQ.eyJpZCI6MTF9.lAU7dZkII6g3AY81cWDrFlDNCNc_IPQbCeIMR6UlJkozjC5VkOO0enrBW39sI6hEa5GYuatqFgZgaQN28JDnkg"
}
```


### Регистрация:

- /register. В запрос входит параметр email. Если пользователя с таким email не существует, то создается новый пользователь и на данный email отсылается письмо с логином и сгенерированным паролем. Если email существует возврашается ошибка 406

##### Пример:
```
var xhttp = new XMLHttpRequest();
xhttp.open("POST", "/register", true);
xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
xhttp.send('email=myemail@gmail.com');
```




#### Подключение к бд:

Логин: dbuser. Пароль: dbpassword. Таблица: advertisement.