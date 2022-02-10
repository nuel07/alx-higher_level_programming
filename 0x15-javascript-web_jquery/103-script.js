$('document').ready(function () {
    $('INPUT#btn_translate').click(translate);
    $('INPUT#language_code').focus(function () {
	$(this).keydown(function (ent) {
	    if (ent.keyCode === 13) {
		translator();	
	    } 
	});	
    });    
});

function translator () {
    const url = 'https://www.fourtonfish.com/hellosalut/hello/';
    $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (info) {
	$('DIV#hello').html(info.hello);	
    });   
}
