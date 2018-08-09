const state = {
    gameId: '',
    game: false,
    playerHand: [],
    computerHand: [],
    focusedCardId: null,
    notification: null,
    notificationVisible: false,
    currentRound: 0,
    currentPlayer: 0,
    cardSelectorVisible: false,
    cardSelectorType: null,
    cardSelectorCards: [],
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
    },
    currentRound: state => {
        return state.currentRound;
    },
    currentPlayer: state => {
        return state.currentPlayer;
    },
    cardSelectorVisible: state => {
        return state.cardSelectorVisible;
    },
    cardSelectorType: state => {
        return state.cardSelectorType;
    },
    cardSelectorCards: state => {
        return state.cardSelectorCards;
    },

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
    },
    SET_CURRENT_ROUND(state, currentRound) {
        state.currentRound = currentRound;
    },
    SET_CURRENT_PLAYER(state, currentPlayer) {
        state.currentPlayer = currentPlayer;
    },
    SET_CARD_SELECTOR_VISIBLE(state, cardSelectorVisible) {
        state.cardSelectorVisible = cardSelectorVisible;
    },
    SET_CARD_SELECTOR_TYPE(state, cardSelectorType) {
        state.cardSelectorType = cardSelectorType;
    },
    SET_CARD_SELECTOR_CARDS(state, cardSelectorCards) {
        state.cardSelectorCards = cardSelectorCards;
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
    },
    setCurrentRound(context, currentRound) {
        context.commit('SET_CURRENT_ROUND', currentRound);
    },
    setCurrentPlayer(context, currentPlayer) {
        context.commit('SET_CURRENT_PLAYER', currentPlayer);
    },
    setCardSelectorVisible(context, cardSelectorVisible) {
        context.commit('SET_CARD_SELECTOR_VISIBLE', cardSelectorVisible);
    },
    setCardSelectorType(context, cardSelectorType) {
        context.commit('SET_CARD_SELECTOR_TYPE', cardSelectorType);
    },
    setCardSelectorCards(context, cardSelectorCards) {
        context.commit('SET_CARD_SELECTOR_CARDS', cardSelectorCards);
    }
};

const GameState = {
    state,
    getters,
    mutations,
    actions
};

export default GameState;
