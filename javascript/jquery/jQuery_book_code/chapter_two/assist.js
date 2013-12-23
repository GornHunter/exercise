/**
 * Created with IntelliJ IDEA.
 * User: nancy
 * Date: 11/18/13
 * Time: 4:09 PM
 * To change this template use File | Settings | File Templates.
 */

$(document).ready(function(){
    $("#reset").click(function(){
        $("*").removeAttr("style");
        $("div[class=none]").css({"display":"none"})
    });

    $("input[type=button]").click(function(){
        if($("#isreset").is(":checked")){
            $("#reset").click();
        }
    });
    function animateIt(){
        $("#mover").slideToggle(1000,"linear",animateIt)
    }
    animateIt();
});