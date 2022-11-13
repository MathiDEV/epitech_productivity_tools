if (window.chrome === undefined) {
    console.warn('EpiAuth: Chrome is required to use this library');
} else {
    const uuid = () => {
        return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
            const r = Math.random() * 16 | 0;
            const v = c == 'x' ? r : (r & 0x3 | 0x8);
            return v.toString(16);
        });
    }

    const browser = window.chrome;

    class EpiAuth {
        exists = false;

        onLoad(cb) {
            const listener = (message) => {
                if (message.data.type === 'EPIAUTH_INIT') {
                    this.exists = true;
                    if (cb) {
                        cb();
                    }
                    window.removeEventListener('message', listener);
                }
            };
            window.addEventListener('message', listener);
        }

        getUser() {
            return this.get('https://intra.epitech.eu/user/?format=json');
        }

        get(url) {
            const reqUUID = uuid();
            window.postMessage({ type: 'EPIAUTH_GET', data: { url, uuid: reqUUID } }, '*');
            return new Promise((resolve, reject) => {
                const listener = (message) => {
                    if (message.data.type === 'EPIAUTH_RESULT' && message.data.data.uuid === reqUUID) {
                        window.removeEventListener('message', listener);
                        resolve(message.data.data.response);
                    }
                }
                window.addEventListener('message', listener);
            });
        }
    }

    window.epiAuth = new EpiAuth();
}