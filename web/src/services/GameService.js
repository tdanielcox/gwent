// import Cookie from "js-cookie";
import store from '../vuex/store';
import DataService from './DataService';
import NotificationService from './NotificationService';

// const CookieKey = 'publistry_cart';
// const CookieDomain = process.env.MIX_COOKIE_DOMAIN;
// const CookieVersion = '3';

const parseGame = (game) => {
    store.dispatch('setGame', game);

    let playerCards = [];
    game.players[0].cards.forEach(row => {
        row.forEach(card => {
            playerCards.push(card);
        });
    });
    store.dispatch('setPlayerHand', playerCards);

    let currPlayer = '', plural = '';
    switch (game.current_player) {
        default:
        case 0:
            currPlayer = 'You';
            plural = 'r';
            break;
        case 1:
            currPlayer = 'Gw[Ai]nt';
            plural = '\'s';
            break;
    }

    return { currPlayer, plural };
};

const GameService = {
    startGame() {
        return DataService.startGame().then(response => {
            const game = response.data;

            const info = parseGame(game);
            store.dispatch('setGameId', game.id);

            return NotificationService.setNotification(info.currPlayer + ' will go first').then(() => {
                if (game.current_player === 1) {
                    return GameService.aiTurn().then(_response => {
                        const game = _response.data;
                        const info = parseGame(game);
                        const player = info.currPlayer + '' + info.plural;

                        return NotificationService.setNotification(player + ' turn');
                    });
                }
            });
        }).catch(err => {
            console.log(err);
        });
    },

    playCard(cardId) {
        const gameId = store.getters.gameId;

        return DataService.playCard(gameId, cardId).then(response => {
            const game = response.data;
            const info = parseGame(game);
            const player = info.currPlayer + '' + info.plural;

            return NotificationService.setNotification(player + ' turn').then(() => {
                GameService.aiTurn().then(_response => {
                    const game = _response.data;
                    const info = parseGame(game);
                    const player = info.currPlayer + '' + info.plural;

                    return NotificationService.setNotification(player + ' turn');
                });
            });
        }).catch(err => {
            console.log(err);
        });
    },

    aiTurn() {
        const gameId = store.getters.gameId;

        return DataService.aiTurn(gameId).then(response => {
            const game = response.data;
            const info = parseGame(game);
            const player = info.currPlayer + '' + info.plural;

            return NotificationService.setNotification(player + ' turn');
        }).catch(err => {
            console.log(err);
        });
    }

    // getCart: token => {
    //     let cookie = CartService.getCookie();
    //     let cart = {};

    //     if (cookie && cookie[token]) {
    //         for (let key in cookie[token]) {
    //             if (cookie[token].hasOwnProperty(key)) {
    //                 cart[key] = cookie[token][key];
    //             }
    //         }
    //     }

    //     return CartService.setupCart(cart);
    // },

    // getCookie: () => {
    //     let cookie = Cookie.get(CookieKey);

    //     if (cookie) {
    //         cookie = JSON.parse(cookie);
    //     } else {
    //         cookie = {};
    //     }

    //     if (!cookie.version || cookie.version !== CookieVersion) {
    //         cookie = { version: CookieVersion };
    //         Cookie.set(CookieKey, cookie, { domain: CookieDomain });
    //     }

    //     return cookie;
    // }
};

export default GameService;




