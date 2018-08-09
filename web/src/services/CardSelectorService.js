import store from '../vuex/store';

const CardSelectorService = {
    open(type, cards) {
        return new Promise((resolve, reject) => {
            console.log(cards);
            store.dispatch('setCardSelectorType', type);
            store.dispatch('setCardSelectorCards', cards);
            store.dispatch('setCardSelectorVisible', true);

            resolve();
        });
    }
};

export default CardSelectorService;
