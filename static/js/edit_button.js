/*
* Edit button in the django form will use this Javascript
* to load the present goal into the text-input, and focus the mouse into the text field.
* The current goal can then be editted and submitted upon completion.
* if a user is not authorized (logged in), These buttons and the django form are not
* available to users.
*/

let EDIT_one;
let EDIT_two;
let EDIT_three;
let goal1;
let goal2;
let goal3;
let goal1_btn;
let goal2_btn;
let goal3_btn;

// JS code for hamburger icon -removed-


function set_DOM(){
    EDIT_one = document.getElementById('goal_1_input')
    EDIT_two = document.getElementById('goal_2_input')
    EDIT_three = document.getElementById('goal_3_input')
    goal1 = document.getElementById('longtermgoal')
    goal2 = document.getElementById('threemonthgoal')
    goal3 = document.getElementById('shorttermgoal')
    goal1_btn = document.getElementById('goal1_edit')
    goal2_btn = document.getElementById('goal2_edit')
    goal3_btn = document.getElementById('goal3_edit')
}

function addListeners(){
    goal1_btn.addEventListener('click', edit_one)
    goal2_btn.addEventListener('click', edit_two)
    goal3_btn.addEventListener('click', edit_three)
}

function strip(astring){
    /* django add's newline characters to {{ variable }}
     Strip these out before assiging the value to text-input for edit*/
    max = astring.length
    var newstring;


    for(var i=0; i < max; i++){
        //console.log("what is it?")
        //console.log(astring.charCodeAt(i))
        character = astring.charAt(i)
        char_code = astring.charCodeAt(i)
        if(char_code != 10 && character != " "){
            newstring = astring.slice(i)
            break
        }

    }

    // Take of spaces newlines on tail of string
    new_max = newstring.length - 1
    for(var n = new_max; n >= 0 ; n--){
        character = newstring.charAt(n)
        char_code = newstring.charCodeAt(n)
        //console.log(character)
        //console.log(char_code)
        if(char_code != 10 && character != " "){
            if(n >= new_max){
            newstring = newstring.slice(0, n)

            break

            }

            else{
            newstring = newstring.slice(0, n+1)

            break

            }
        }


    }

    if(newstring.length > 0){
        return newstring
    }
    else {
        return " "
    }
}



function edit_one(){
    astring = goal1.textContent
    new_string = strip(astring)
    EDIT_one.value = new_string;
    EDIT_one.focus()
}

function edit_two(){
    astring = goal2.textContent
    new_string = strip(astring)
    EDIT_two.value = new_string
    EDIT_two.focus()
}

function edit_three(){
    astring = goal3.textContent
    new_string = strip(astring)
    EDIT_three.value = new_string
    EDIT_three.focus()
}

window.onload = function(){
    set_DOM();
    addListeners();


}