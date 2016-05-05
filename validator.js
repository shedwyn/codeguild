"use strict";

function checkFieldEmpty(anyObject){
    if (anyObject !== "") {
        return false
    }
    else {
        return true
    }
    // can I use jQuery.isEmptyObject($("#fullName"))?
}
function checkNameCount(namesList){
    if (namesList.length !== 2) {
        return false
    }
    else {
        return true
    }
}
function checkNameCapital(namesList){
    // but what about triple last names? de Hoya, de Graf 
    // people who type only first initial
    var firstName = namesList[0];
    var lastName = namesList[1];
    if (checkNameCount(namesList) !== true || 
        firstName[0] !== firstName[0].toUpperCase() ||
        lastName[0] !== lastName[0].toUpperCase()
        ){
        return false
    }
    else {
        return true
    }
}
function checkFullName(fullName){
    var namesList = fullName.split(" ");
    var fieldName = "Full Name"
    if (checkFieldEmpty(fullName) === false && checkNameCount(namesList) === false || 
        checkFieldEmpty(fullName) === false && checkNameCapital(namesList) === false) {
        return false
    }
    else {
        return true
    }
}
function updateFullNameWarning(boolVal){
    if (boolVal === false) {
        $("#fullName").css("background-color", "yellow");
        // $("#warnings").append(formatWarningNotice(fieldName));
    }
    else {
        $("#warnings").empty();
        $("#fullName").css("background-color", "initial")
    }
}
function fetchFullNameInput(){
    return $("#fullName").val()
}
function runNameCheckMain(){
    var fullName = fetchFullNameInput();
    var nameCheckResult = checkFullName(fullName);
    updateFullNameWarning(nameCheckResult)
}
function updateBirthDateWarning(boolVal){
    if (boolVal === false) {
        $("#birthDate").css("background-color", "yellow");
        // $("#warnings").append(formatWarningNotice(fieldName));
    }
    else {
        $("#warnings").empty();
        $("#birthDate").css("background-color", "initial")
    }
}
function fetchBirthDateInput(){
    return $("#birthDate").val()
}    
function checkBirthDate(){
    var regexLayout = /^(\d{4})(\-)(\d{2})(\-)(\d{2})$/
    var birthDate = fetchBirthDateInput()
    // var regexLayout = /(\d{4})-(\d{2})-(\d{2})/
    if (checkFieldEmpty(birthDate) === true || 
        !(birthDate.match(regexLayout))){
        return false
    }
    else {
        return true
    }
}
function runBirthDateCheckMain(){
    var birthDate = fetchBirthDateInput();
    var birthDateCheckResult = checkBirthDate();
    updateBirthDateWarning(birthDateCheckResult)
}
function registerInitialCallback(){
    $("#fullName").on("change", runNameCheckMain);
    $("#birthDate").on("change", runBirthDateCheckMain);
}
registerInitialCallback()



// function checkPhoneNum(){
//     // 555-555-5555
//     //^(\d{3})(\-)(\d{3})(\-)(\d{4})$
// }
// function formatWarningNotice(fieldName){
//     var warningNotice = $("<p></p>").text("WARNING!  You are in danger! The " + fieldName +
//         " field you have been editing is incorrect.  Take a look at the example given " +
//         "and try again, mmm-Kay?  What are you waiting for?  GO NOW!")
//         .css("background-color", "yellow")
//     return warningNotice
// }
// function formatApprovalNotice(){
//     var approvalNotice = $("<p></p>").text("CONGRATULATIONS!  Your data has been " +
//         "accepted.  Unfortunately, you are now above the age of mandatory death.  " +
//         "A team of mutant giraffes has been deployed to your present location to " +
//         "terminate you.  Have a nice day.")
//         .css("background-color", "green")
//     return approvalNotice
//     //approvalNotice.css("background-color", "green")
// }
// function formatMalformNotice(){
//     var malformNotice = $("<p></p>").text("WARNING!  Malformed information has " +
//         "been presented to your evil overlords!  This kind of egregious mistake " +
//         "cannot be ignored.  A team of ninjas ('assassin' being redundant) is now " +
//        "being deployed to your location and death will come on swift sword, or " +
//         "nunchucks, we do not like to micro-manage.  END OF WARNING STATEMENT." +
//         " Oh, and please take a few moments to fill out the exit survey before dying.")
//         .css("background-color", "red")
//     return malformNotice
//     //malformNotice.css("background-color", "red")
// }
// function validateForm(){
//     // posts a success or error notice
//     $("#warnings").empty();
//     if (checkFieldsNotEmpty() === false) {
//         $("#warnings").append(formatMalformNotice())
//     }
//     else if (checkFullName() === false) {
//         $("#warnings").append(formatMalformNotice())
//     }
//     // else if (checkBirthDate() === false) {
//     //     $("#warnings").append(formatMalformNotice())
//     // }
//     // else if (checkPhoneNum() === false) {
//     //     $("#warnings").append(formatMalformNotice())
//     // }
//     else {
//         $("#warnings").append(formatApprovalNotice())
//     }
// }