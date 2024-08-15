document.addEventListener('DOMContentLoaded', function() {
    function printHello() {
        console.log("hello");
    }
    const button = document.getElementById('myButton');
    if (button) {
        button.addEventListener('click', printHello);
    }
});


