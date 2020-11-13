// alert('ok');


window.onload = function(){
    var usernamebtn = document.getElementById('username');
    var pwdbtn = document.getElementById('pwd');
    var cpwdbtn = document.getElementById('cpwd');
    var subbtn = document.getElementById('subbtn');
    console.log(subbtn);
    subbtn.onclick = function () {
        // alert('ok')
        // alert(usernamebtn.value)

        // todo 获取数据
        var username = usernamebtn.value;
        var pwd = pwdbtn.value;
        var cpwd = cpwdbtn.value;
        console.log(username,pwd,cpwd);

        // todo 校验数据
        console.log(username.length)
    }


};

