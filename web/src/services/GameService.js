// import Cookie from "js-cookie";
import store from '../vuex/store';
import DataService from './DataService';
import NotificationService from './NotificationService';

// const CookieKey = 'publistry_cart';
// const CookieDomain = process.env.MIX_COOKIE_DOMAIN;
// const CookieVersion = '3';

const updateGame = (game) => {
    store.dispatch('setGame', game);
    store.dispatch('setCurrentPlayer', game.current_player);
    store.dispatch('setCurrentRound', game['round']);

    let playerCards = [];
    game.players[0].cards.forEach(row => {
        row.forEach(card => {
            playerCards.push(card);
        });
    });
    store.dispatch('setPlayerHand', playerCards);

    return game;
};

const showGameNotifications = (game) => {
    return new Promise((resolve, reject) => {
        if (game.status.length > 0) {
            let messages = [];
            let secMessages = [];
            let customTimeout = 1800;
            let secCustomTimeout = 3400;

            game.status.forEach(status => {
                switch (status) {
                    case 'round_0_start':
                        customTimeout = 3400;
                        return messages.push('Round 1');
                    case 'round_1_start':
                        return secMessages.push('Round 2');
                    case 'round_2_start':
                        return secMessages.push('Round 3');
                    case 'player_0_start':
                        return messages.push('You will start');
                    case 'player_1_start':
                        return messages.push('Opponent will start');
                    case 'player_0_passed':
                        return messages.push('You passed');
                    case 'player_1_passed':
                        return messages.push('Opponent passed');
                    case 'player_0_next':
                        customTimeout = 2600;
                        return messages.push('Your turn');
                    case 'player_1_next':
                        return messages.push('Opponent\'s turn');
                    case 'round_0_player_0_win':
                        customTimeout = 3400;
                        return messages.push('You won round 1');
                    case 'round_1_player_0_win':
                        customTimeout = 3400;
                        return messages.push('You won round 2');
                    case 'round_2_player_0_win':
                        customTimeout = 3400;
                        return messages.push('You won round 3');
                    case 'round_0_player_1_win':
                        customTimeout = 3400;
                        return messages.push('Opponent won round 1');
                    case 'round_1_player_1_win':
                        customTimeout = 3400;
                        return messages.push('Opponent won round 2');
                    case 'round_2_player_1_win':
                        customTimeout = 3400;
                        return messages.push('Opponent won round 3');
                }
            });

            if (messages.length) {
                const msgStr = messages.join(' - ');
                NotificationService.setNotification(msgStr, customTimeout).then(() => {
                    if (secMessages.length) {
                        const secondaryMsgStr = secMessages.join(' - ');
                        NotificationService.setNotification(secondaryMsgStr, secCustomTimeout).then(() => {
                            resolve();
                        });
                    } else {
                        resolve();
                    }
                });
            } else {
                resolve();
            }
        } else {
            resolve();
        }
    });

};

const GameService = {
    startGame() {
        return DataService.startGame().then(response => {
            const game = response.data;
            updateGame(game);
            store.dispatch('setGameId', game.id);

            console.log(game);

            return showGameNotifications(game).then(() => {
                if (game.current_player === 1) {
                    return GameService.aiTurn().then(_response => {
                        const game = _response.data;
                        updateGame(game);

                        console.log(game);
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
            updateGame(game);

            console.log(game);

            return showGameNotifications(game).then(() => {
                GameService.aiTurn();
            });
        }).catch(err => {
            console.log(err);
        });
    },

    passRound() {
        const gameId = store.getters.gameId;

        return new Promise((resolve, reject) => {
            DataService.passRound(gameId).then(response => {
                const game = response.data;
                updateGame(game);

                console.log(game);

                showGameNotifications(game).then(() => {
                    GameService.aiTurn().then(_response => {
                        const game = _response.data;
                        updateGame(game);

                        console.log(game);

                        resolve(_response);
                    });
                });
            }).catch(err => {
                reject(err);
            });
        });
    },

    aiTurn() {
        return new Promise((resolve, reject) => {
            const gameId = store.getters.gameId;

            return DataService.aiTurn(gameId).then(response => {
                const game = response.data;
                updateGame(game);

                console.log(game);

                showGameNotifications(game).then(() => {
                    if (game.current_player === 1) {
                        GameService.aiTurn().then(_response => {
                            const game = _response.data;
                            updateGame(game);

                            console.log(game);

                            resolve(_response);
                        });
                    } else {
                        resolve(response);
                    }
                });
            }).catch(err => {
                reject(err);
            });
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




