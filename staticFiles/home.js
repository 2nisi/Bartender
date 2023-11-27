//Global Variabels
var OSName = "MacOS";
var selected_drink = ""; // This variable holds the latest selected coctail type.


//JavaScript functions of main page.

//Reports the Operating System that the page is loaded
function findOperatingSytem() {  
   
  if (navigator.appVersion.indexOf("Win")!=-1) OSName="Windows"; 
  if (navigator.appVersion.indexOf("Mac")!=-1) OSName="MacOS"; 
  if (navigator.appVersion.indexOf("X11")!=-1) OSName="UNIX"; 
  if (navigator.appVersion.indexOf("Linux")!=-1) OSName="Linux";
}


// Creating DOMContentLoader
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems);

    findOperatingSytem();
    console.log(OSName);  
    
  });


// Updating the global variable selected_drink with the latest choosen coctail.
function update_drink_selection(selected_coctail){
    console.log(selected_coctail);
    selected_drink = selected_coctail;
};


// Updating the slider value and making it more visually appealing.
const slider = document.getElementById('alchoholStrength');
document.getElementById('alchoholStrength').oninput = function() {

    var alchohol_strength = slider.value;
    var alchohol_strength_text = "";

    // Reseting all fonts to default
    document.getElementById("lab_void").style.fontSize = "0.8rem";
    document.getElementById("lab_soft").style.fontSize = "0.8rem";
    document.getElementById("lab_medium").style.fontSize = "0.8rem";
    document.getElementById("lab_strong").style.fontSize = "0.8rem";

    // Depending on the alchohol strength value, the strength name is updated
    if (alchohol_strength == 0) { alchohol_strength_text = "Void"; document.getElementById("lab_void").style.fontSize = "1.2rem";}
    else if (alchohol_strength <= 45) { alchohol_strength_text = "Soft"; document.getElementById("lab_soft").style.fontSize = "1.2rem"; }
    else if (alchohol_strength <= 85) { alchohol_strength_text = "Medium"; document.getElementById("lab_medium").style.fontSize = "1.2rem"; }
    else if (alchohol_strength <= 100) { alchohol_strength_text = "Strong"; document.getElementById("lab_strong").style.fontSize = "1.2rem"; }

    // Updating the shown strength name
    document.getElementById("strength_text").innerHTML = 'Drink strength: <i> ' + alchohol_strength_text + '<i></h5>';
};

window.onload = function (){

    // This is being activated once the form is being submited. Here the coctail type and alchohol content are defined.
    document.getElementById("order_form").onsubmit = function(){
        var order_drink = document.getElementById("submit_button");
        order_drink.name = selected_drink + ";" + slider.value; // This is the text command that is send over Post method to ROS server
    };

};

