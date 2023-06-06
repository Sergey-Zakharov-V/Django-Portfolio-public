function hide (id){
    var element = document.getElementById(id);
    var element2 = document.getElementById("test-button");
    console.log(element, element2.style.backgroundColor)
    if (element && element2){
        if (element2.style.backgroundColor === "blue"){
            element2.style.backgroundColor = "red";
        } else {
            element2.style.backgroundColor = "blue";
        }
    }
}