window.postMessage({ type: 'EPIAUTH_INIT' }, '*');

window.addEventListener('message', message => {
    if (message.data.type === 'EPIAUTH_GET') {
        chrome.runtime.sendMessage({ type: 'EPIAUTH_GETDATA', data: message.data.data }, (response) => {
            window.postMessage({ type: 'EPIAUTH_RESULT', data: {...message.data.data, response} }, '*');
        });
    }
});
