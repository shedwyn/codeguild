"use strict";
//If field is valid or empty, remain blue, otherwise chg to yellow
function checkNameEmpty(fullName){
    if (fullName === "") {
        return true
    }
    else {
        return false
    }
    // can I use jQuery.isEmptyObject($("#fullName"))?
}
function checkNameLength(fullName){
    var namesList = fullName.split(" ");
    if (namesList.length === 2) {
        return true
    }
    else {
        return false
    }
}
function checkNameCapital(fullName){
    var namesList = fullName.split(" ");
    // but what about triple last names? de Hoya, de Graf 
    // people who type only first initial
    return true
}
function checkFullName(){
    var fullName = $("#fullName").val();
    var nameConditions = [
        checkNameEmpty(fullName), 
        checkNameLength(fullName),
        checkNameCapital(fullName)
    ]
    console.log(nameConditions)
    console.log("checkFullName was run")
    if (nameConditions[0] === true){
        return true
    }
    else if (nameConditions[1] === false) {
        return false
    }
    else if (nameConditions[2] === false) {
        return false
    }
    else {
        console.log("Final else statement which is true")
        return true
    }
    console.log("if statements were skipped")
}
function checkNameOnChange() {
    $("#fullName").on("change", function(event){
        event.preventDefault();
        if (checkFullName() === false) {
            $("#fullName").css("background-color", "red")
        }
        else {
            $("#fullName").css("background-color", "#ABE6FF")
        }
        console.log("Ran the stuff")
    })
}
function checkBirthDate(){
    // YYYY-MM-DD
    //return true or false
}
function checkPhoneNum(){
    // 555-555-5555
    //return true or false
}
function formatApprovalNotice(){
    var approvalNotice = $("<p></p>").text("CONGRATULATIONS!  Your data has been " +
        "accepted.  Unfortunately, you are now above the age of mandatory death.  " +
        "A team of mutant giraffes has been deployed to your present location to " +
        "terminate you.  Have a nice day.")
    //approvalNotice.css("background-color", "green")
}
function formatMalformNotice(){
    var malformNotice = $("<p></p>").text("WARNING!  Malformed information has " +
        "been presented to your evil overlords!  This kind of egregious mistake " +
        "cannot be ignored.  A team of ninjas ('assassin' being redundant) is now " +
       "being deployed to your location and death will come on swift sword, or" +
        "nunchucks, we do not like to micro-manage.  END OF WARNING STATEMENT.")
    //malformNotice.css("background-color", "red")
}
function formatSubmitButton(){
    
}
function validateForm(){
    // posts a success or error notice
    if (checkFullName === false) {

    }
    else if (checkBirthDate === false) {

    }
    else if (checkPhoneNum === false) {
        $("#warnings").append(formatMalformNotice())
    }
    else {
        $("#warnings").append(formatApprovalNotice())
    }
}
checkNameOnChange();
console.log(checkFullName());
$("#birthDate");
$("#phoneNum");
$("form").on("submit", function (event){
    event.preventDefault();
    validateForm();
})
// As the user is typing, you should validate that the fields are filled 
    // in the correct format. 
        // If the content is not currently valid, the field 
//              box should be yellow and a yellow warning notice describing which field 
//              is malformed displayed atop the form. 
        // If multiple forms are invalid, just 
//              show one. I don't care which. 
        // Otherwise, if valid or empty, the fields 
//              should be default and no warning notice displayed.

// If the user submits with valid info, display a green success notice atop 
//     the form, otherwise a red error notice.