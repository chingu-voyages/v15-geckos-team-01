//testing JavaScript routing in Django
let test_item;

function set_DOM() {
  test_item = document.getElementById('test_js');
  test_item.innerHTML = "Django path to JS file successful.";
}

window.onload = function load() {
  set_DOM();
}
