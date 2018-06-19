
$(document).ready(function(){
  $.ajax({url:"/message/2?next=" + encodeURIComponent(document.URL),success:function(result){
    $("#comment").html(result);
  }});
});
