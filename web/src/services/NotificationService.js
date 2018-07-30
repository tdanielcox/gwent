import store from '../vuex/store';

const NotificationService = {
    setNotification(notification) {
        return new Promise((resolve, reject) => {
            store.dispatch('setNotification', notification);
            store.dispatch('setNotificationVisible', true);

            setTimeout(() => {
                store.dispatch('setNotificationVisible', false);
            }, 2600);

            setTimeout(() => {
                store.dispatch('setNotification', null);
                resolve();
            }, 3000);
        });
    }
};

export default NotificationService;




