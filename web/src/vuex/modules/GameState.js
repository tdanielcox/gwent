const state = {
    gameId: '',
    game: {},
    playerHand: [],
    computerHand: [],
    focusedCardId: null,
    notification: null,
    notificationVisible: false
};

const getters = {
    gameId: state => {
        return state.gameId;
    },
    game: state => {
        return state.game;
    },
    playerHand: state => {
        return state.playerHand;
    },
    computerHand: state => {
        return state.computerHand;
    },
    focusedCardId: state => {
        return state.focusedCardId;
    },
    notification: state => {
        return state.notification;
    },
    notificationVisible: state => {
        return state.notificationVisible;
    }
};

const mutations = {
    SET_GAME_ID(state, gameId) {
        state.gameId = gameId;
    },
    SET_GAME(state, game) {
        state.game = game;
    },
    SET_PLAYER_HAND(state, playerHand) {
        state.playerHand = playerHand;
    },
    SET_COMPUTER_HAND(state, computerHand) {
        state.computerHand = computerHand;
    },
    SET_FOCUSED_CARD_ID(state, cardId) {
        state.focusedCardId = cardId;
    },
    SET_NOTIFICATION(state, notification) {
        state.notification = notification;
    },
    SET_NOTIFICATION_VISIBLE(state, visible) {
        state.notificationVisible = visible;
    }
};

const actions = {
    setGameId(context, gameId) {
        context.commit('SET_GAME_ID', gameId);
    },
    setGame(context, game) {
        context.commit('SET_GAME', game);
    },
    setPlayerHand(context, playerHand) {
        context.commit('SET_PLAYER_HAND', playerHand);
    },
    setComputerHand(context, computerHand) {
        context.commit('SET_COMPUTER_HAND', computerHand);
    },
    setFocusedCardId(context, cardId) {
        context.commit('SET_FOCUSED_CARD_ID', cardId);
    },
    setNotification(context, notification) {
        context.commit('SET_NOTIFICATION', notification);
    },
    setNotificationVisible(context, visible) {
        context.commit('SET_NOTIFICATION_VISIBLE', visible);
    }
};

const GameState = {
    state,
    getters,
    mutations,
    actions
};

export default GameState;
