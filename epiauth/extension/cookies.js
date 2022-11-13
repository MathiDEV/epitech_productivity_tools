
function getCookie() {
    return new Promise((resolve, reject) => {
        chrome.cookies.get({ url: "https://intra.epitech.eu", name: "user" }, (cookie) => {
            if (cookie) {
                resolve(cookie.value);
            } else {
                resolve(undefined);
            }
        });
    });
}
function canRequestIt(url, cookie, cb) {
    const urlObj = new URL(url);
    if (urlObj.hostname !== "intra.epitech.eu") {
        cb({ success: false, err: "Can't request external websites" });
        return false;
    }
    if (!cookie || cookie.length < 10) {
        cb({ success: false, err: "User is not authentified on intranet" });
        return false;
    }
    return true;
}
async function getUrl(url, cb) {
    const cookie = await getCookie();
    if (!canRequestIt(url, cookie, cb)) {
        return;
    }
    fetch(url, {
        headers: {
            'Cookie': `user=${cookie}`
        }
    }).then((response) => response.text())
        .then((data) => cb({ success: true, data }))
        .catch(() => cb({ success: false, err: "Error while fetching url" }));
}


chrome.runtime.onMessage.addListener((message, sender, sendMessage) => {
    if (message.type === 'EPIAUTH_GETDATA') {
        getUrl(message.data.url, sendMessage);
        return true
    }
});