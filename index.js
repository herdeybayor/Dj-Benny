$(".nav-bugger").click(()=>{
    var className = $(".nav-bugger i").attr("class");
    switch (className) {
        case "fas fa-bars":
            $(".nav-bugger i").attr("class", "fas fa-times");
            break;
        case "fas fa-times":
            $(".nav-bugger i").attr("class", "fas fa-bars");
            break;
    }
    $(".nav-bar").toggleClass("right");
    $(".nav-bugger").toggleClass("bugger-change");
})