/**
 * Created by wangjj on 2017/1/12.
 */
$(document).ready(function () {
    $('#btn1').on('click',function (e) {
        debugger;
        alert('click');
        // $('#btn1').off('click');
    });
    // $('#btn1').trigger('click');
    $('#btn2').on('dblclick',function (e) {
        alert('double click');
    });
    $('#ip1').on('focus',function () {
        $('#result').html('focused');
    });
    $('#ip1').on('blur',function () {
        $('#result').html('blurred');
    });
    $('#btn3').on('mousedown',function () {
        $('#result2').append('&nbsp;mousedown');
    });
    $('#btn3').on('mouseup',function () {
        $('#result2').append('&nbsp;mouseup');
    });
    $('#btn3').on('click',function () {
        $('#result2').append('&nbsp;<b>clicked</b>');
    });

    $('#btn4').on('mouseover',function () {
        $('#result3').append('&nbsp; mouseover');
    });
    $('#btn4').on('mouseout',function () {
        $('#result3').append('&nbsp; mouseout');
    });
    // $('#btn4').on('mousemove',function () {
    //     $('#result3').append('&nbsp; mousemove');
    // });

    $('#ip2').on('keydown',function () {
        $('#result4').append('&nbsp; keydown');
    });

    $('#ip2').on('keyup',function () {
        $('#result4').append('&nbsp; keyup');
    });
    $('#ip2').on('keypress',function () {
        $('#result4').append('&nbsp; keypress');
    });

    $('#ip3').on('change',function () {
        $('#result5').html('changed');
    });
    $('#form1').on('submit',function () {
        alert('submit');
    })
})