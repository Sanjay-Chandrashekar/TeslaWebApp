$(document).ready(function () {

	$('.hamburger-button').click(function(){
		if($('.model-pop-up').css('visibility') == 'visible')
			$('.model-pop-up').css('visibility', 'hidden');
		else
			$('.model-pop-up').css('visibility', 'visible');
	})
});