// JS code for hamburger icon

let nav_div;
let hamburg;


function set_DOM(){
    nav_div = document.getElementById("links_list")
    hamburg = document.getElementById("hamburger_icon")
}

function show(element){
    element.style.display = 'flex';
}

function hide(element){
    element.style.display = 'none';
}

function toggle_burger(){
    current = hamburg.getAttribute("value")
    if(current == "ON"){
        hamburg.setAttribute("value", "OFF")

        show(nav_div)
    }
    else{
        hamburg.setAttribute("value", "ON")

        hide(nav_div)
    }

}


function set_listener(){
    hamburg.addEventListener('click', toggle_burger)
}


window.onload = function(){
    set_DOM()
    set_listener()
}
