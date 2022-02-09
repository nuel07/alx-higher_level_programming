/*
updates text of <header> element when user
clicks on DIV#update_header tag
*/
$('DIV#update_header').on('click', function(){
    $('header').text('New Header!!!');
});
