$(".nav .navbar-nav .nav-item .nav-link").on("click", function(){
   $(".nav").find(".active").removeClass("active");
   alert($(this).addClass("active"));
});
