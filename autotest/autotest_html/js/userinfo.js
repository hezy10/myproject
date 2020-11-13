// alert('ok')
//celery




$(function () {
    var token = localStorage.token;
    $.ajax({
        url:'http://127.0.0.1:8000/users/userinfo/',
        method:'GET',
        headers:{'Authorization':'JWT '+token},
        success:function (data) {
            console.log('请求成功');
            console.log(data);
            var  username = data['username'];
            var email = data['email'];
            var id = data['id'];
            var phone = data['phone'];
            $('#username').val(username)
        },
        error:function (data) {
            console.log('失败')
        }
    });

    // 修改手机号码
    // 1.0 校验当前手机号码是否能接收验证码
    var phoneBtn = $('#phone');
    console.log('http://127.0.0.1:8000/verifi/mobile/'+phoneBtn.val()+'/');
    phoneBtn.focus(function () {
        // alert('得到焦点')
        //将验证码发送给用户
        $.ajax({
            'url':'http://127.0.0.1:8000/verifi/mobile/'+phoneBtn.val()+'/',
            'method':'GET',
            headers:{'Authorization':'JWT '+token},
            success:function () {
                console.log('ok')
            },
            error:function (data) {
                console.log('error');
                console.log(data);
                console.log(typeof (data.status));
                // 判断当前的路径,如果是404状态码,说明手机号码出错
                if(data.status==404){
                    console.log('进入');
                    console.log($('#showerror').css('display','block'))
                }

            }
        })
    });
    phoneBtn.blur(function () {
        console.log('失去焦点')
    })






    // todo 为按钮添加单击事件
    $('#subbtn').click(function () {
    //    todo 获取当前的数据
    //     $('')
    })


})