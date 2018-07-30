// import Cookie from "js-cookie";
import store from '../vuex/store';
import DataService from './DataService';

// const CookieKey = 'publistry_cart';
// const CookieDomain = process.env.MIX_COOKIE_DOMAIN;
// const CookieVersion = '3';

const GameService = {
    startGame() {
        return DataService.startGame().then(response => {
            const game = response.data;

            store.dispatch('setGameId', game.id);
            store.dispatch('setGame', game);

            let cards = [];
            game.players[0].cards.forEach(row => {
                row.forEach(card => {
                    cards.push(card);
                });
            });

            store.dispatch('setPlayerHand', cards);
        }).catch(err => {
            console.log(err);
        });
    },

    playCard(cardId) {
        const gameId = store.getters.gameId;

        return DataService.playCard(gameId, cardId).then(response => {
            const game = response.data;

            store.dispatch('setGame', game);

            let cards = [];
            game.players[0].cards.forEach(row => {
                row.forEach(card => {
                    cards.push(card);
                });
            });

            console.log(game);

            store.dispatch('setPlayerHand', cards);
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

    // addItemToCart: (token, item, quantity) => {
    //     let cookie = CartService.getCookie();
    //     let cart = {};
    //     let _quantity = quantity;

    //     if (cookie[token]) {
    //         for (let key in cookie[token]) {
    //             if (cookie[token].hasOwnProperty(key)) {
    //                 cart[key] = cookie[token][key];
    //             }
    //         }

    //         if (cookie[token][item.id]) {
    //             _quantity += cookie[token][item.id].quantity;
    //         }
    //     } else {
    //         cookie[token] = {};
    //         cart = {};
    //     }

    //     cart[item.type +'_'+ item.id] = {
    //         item_id: item.id,
    //         item_type: item.type,
    //         title: item.title,
    //         quantity: _quantity,
    //         unit_price: item.price
    //     };

    //     cookie[token] = cart;

    //     Cookie.set(CookieKey, cookie, { domain: CookieDomain });

    //     return CartService.setupCart(cart);
    // },

    // removeItemFromCart: (token, item_type, item_id) => {
    //     let cookie = CartService.getCookie();
    //     let cart = null;

    //     if (cookie && cookie[token]) {
    //         cart = {};

    //         for (let key in cookie[token]) {
    //             if (cookie[token].hasOwnProperty(key)) {
    //                 cart[key] = cookie[token][key];
    //             }
    //         }
    //     }

    //     if (cart && cart[item_type +'_'+ item_id]) {
    //         delete cart[item_type +'_'+ item_id];
    //     }

    //     cookie[token] = cart;

    //     Cookie.set(CookieKey, cookie, { domain: CookieDomain });

    //     return CartService.setupCart(cart);
    // },

    // setupCart: (cart) => {
    //     let totalItems = 0;
    //     let totalPrice = 0;

    //     if (cart) {
    //         for (let item in cart) {
    //             if (cart.hasOwnProperty(item)) {
    //                 totalItems += cart[item].quantity;
    //                 totalPrice += cart[item].quantity * cart[item].unit_price;
    //             }
    //         }
    //     }
    //     return {
    //         items: cart,
    //         total_items: totalItems,
    //         total_price: totalPrice,
    //     };
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




