var comments = [
    {
        'username': 'zhangsan',
        'comment': 'shafa'
    },
    {
        'username': 'lisi',
        'content': 'bandeng'
    },
    {
        'username': 'wangwu',
        'content': 'diban'
    }];

var html='';
$.each(comments,function(commentIndex,comment){
    html+="<div class='comment'><h6>"+comment['username']+":</h6><p class='para'>"+comment['content']+"</p> </div> "
});

$("#resText").html(html);