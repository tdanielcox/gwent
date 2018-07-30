import store from '../vuex/store';

const NotificationService = {
    setNotification(notification, timeout) {
        timeout = timeout || 2600;
        return new Promise((resolve, reject) => {
            store.dispatch('setNotification', notification);
            store.dispatch('setNotificationVisible', true);

            setTimeout(() => {
                store.dispatch('setNotificationVisible', false);
            }, timeout - 400);

            setTimeout(() => {
                store.dispatch('setNotification', null);
                resolve();
            }, timeout);
        });
    }
};

export default NotificationService;




