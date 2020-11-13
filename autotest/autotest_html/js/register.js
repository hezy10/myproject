// alert('ok');


$(function () {

    $('#subbtn').click(function () {
        var username = $('#username').val();
        var pwd = $('#pwd').val();
        var cpwd = $('#cpwd').val();
        var data = {
            'username':username,
            'password':pwd,
            'cpwd':cpwd
        };
        $.ajax({
            type:'POST',
            url:'http://127.0.0.1:8000/users/register/',
            contentType:'application/json;charset=UTF-8',
            data:JSON.stringify(data),
            success:function (data) {
                // location.href = '/'
                console.log(data);
                // 浏览器关闭就失效
                sessionStorage.token = data.token;
                //长期有效
                localStorage.token = data.token;
                console.log(sessionStorage.token);
                location.href = '/'

            },
            error:function () {
                location.href = '/register.html'
            }

        })
    })
});
