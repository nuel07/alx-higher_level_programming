$('document').ready(function(){
    const url = 'https://www.fourtonfish.com/hellosalut/hello/';
    $('INPUT#btn_translate').on('click', function(){
	$.get(url + $.param({ lang: $('INPUT#language_code').val()}),
	  function(info){
	      $('DIV#hello').html(info.hello);
	  });
    });
});
