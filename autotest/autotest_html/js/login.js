// alert('ok');


$(function () {

    $('#subbtn').click(function () {
        var username = $('#username').val();
        var pwd = $('#pwd').val();
        var data = {
            'username':username,
            'password':pwd,
        };
        $.ajax({
            type:'POST',
            url:'http://127.0.0.1:8000/users/authorizations/',
            contentType:'application/json;charset=UTF-8',
            data:JSON.stringify(data),
            success:function (data) {
                localStorage.token = data.token;
                console.log('登陆成功');
                console.log(data);
                location.href = '/userinfo.html'

            },
            error:function () {
                console.log('登陆失败')
                // location.href = '/register.html'
            }

        })
    })
});
