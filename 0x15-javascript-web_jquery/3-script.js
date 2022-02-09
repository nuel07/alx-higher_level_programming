/*
adds class red to <header> element when user
clicks DIV#red_header 
*/
$('DIV#red_header').on('click', function(){
    $('header').addClass('red');
});
