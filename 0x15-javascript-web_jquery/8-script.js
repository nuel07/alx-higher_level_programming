$('document').ready(function(){
    $.get('https://swapi-api.hbtn.io/api/films/?format=json',
	  function(info, txtstatus){
	      if(txtstatus == 'success'){
		  const flicks = info.results;
		  flicks.forEach(flick => {
		      $('UL#list_movies').append('<li>' +
						 flick.title + '</li>');
		  });
	      }
	  });
});
