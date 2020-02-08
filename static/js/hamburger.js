// JS code for hamburger icon

let nav_div;
let hamburg;

//console.log("hamburger javascript file loaded.")
function set_BURGER_DOM(){
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
    //console.log("toggling burger")
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


function set_BURGER_listener(){
    hamburg.addEventListener('click', toggle_burger)
}

window.onload = function(){
    set_BURGER_DOM()
    set_BURGER_listener()

}



