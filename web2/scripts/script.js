$(document).ready(function() {

	var game = {};
	var player_cards = [];

	function js_start_game() {
	    eel.start_game()(function (_game) {
		    game = JSON.parse(_game);
		    parse_player_cards();
		    set_draggable();
		});
	}

	function parse_player_cards() {
		player_cards = game.players[0].cards;

		jQuery.each(player_cards, function(i, cardRow) {
			jQuery.each(cardRow, function(i, _card) {
				var card = $("<div class='card'></div>");
				card.css('background-image', 'url(\'/images/cards/'+ _card[4] +'\')');
				
				console.log('url(\'/images/cards/'+ _card[4] +'\')');
				$('.player-hand').append(card);
			});
		});
	}

	js_start_game();

	function set_draggable() {
		$('.card:not(.in-play)').draggable({
			revert: 'invalid',
			start: function(event, ui) {
				$(this).addClass('dragging'); 
				// $(this).css("position", "absolute");
			},
			stop: function(event, ui) {
				$(this).removeClass('dragging'); 
				// $(this).css("position", "static");
			},
		});

		$('.player-hand').droppable({
			accept: ".card",
			hoverClass: "drop-hover",
			tolerance: "pointer",
			drop: function(event, ui) {
				$(ui.draggable).css({left: '', top: ''}); 
			}
		});

		$('.player-board .cards-in-play-container').droppable({
			accept: ".card",
			hoverClass: "drop-hover",
			tolerance: "pointer",
			drop: function(event, ui) {
				$(ui.draggable).addClass('in-play').css({position: 'static'}).draggable('destroy'); 
				$(this).append(ui.draggable);
			}
		});
	}

});