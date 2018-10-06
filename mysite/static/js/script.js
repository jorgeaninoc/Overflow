// $(".nav .navbar-nav .nav-item .nav-link").on("click", function(){
//    $(".nav").find(".active").removeClass("active");
//    alert($(this).addClass("active"));
// });

// alert("HEY THERE");
$(document).ready(function() {
  $('li.active').removeClass('active');
  $('a[href="' + location.pathname + '"]').closest('li').addClass('active'); 
});