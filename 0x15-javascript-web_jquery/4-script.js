/*
toggles the class of the <header> element when the
user clicks on the DIV#toggle_header tag
*/
$('DIV#toggle_header').on('click', function(){
    $('header').toggleClass('red green');
});
