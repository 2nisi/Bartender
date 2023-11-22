//Global Variabels
var OSName = "MacOS";



//JavaScript functions of main page.

//Reports the Operating System that the page is loaded
function findOperatingSytem() {  
   
  if (navigator.appVersion.indexOf("Win")!=-1) OSName="Windows"; 
  if (navigator.appVersion.indexOf("Mac")!=-1) OSName="MacOS"; 
  if (navigator.appVersion.indexOf("X11")!=-1) OSName="UNIX"; 
  if (navigator.appVersion.indexOf("Linux")!=-1) OSName="Linux";
}



document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems);

    findOperatingSytem();
    console.log(OSName);  
    
  });


var slide = document.getElementById('alchoholStrength');

slide.onchange = function() {

      document.getElementById("drinkType").name = document.getElementById("drinkType").name + " " + document.getElementById("alchoholStrength").value;
      console.log(document.getElementById("alchoholStrength").value);
};