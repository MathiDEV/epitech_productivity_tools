# Epiauth

This project wants to provide a simple way to manage authentication and authorization for your applications that interacts with EPITECH intranet.

## Installation

Epiauth authentication is based on a Chrome Extension. You can include the script on your website and, if the user has the extension, the authentication will be done automatically.

### Webapp side

```html
<script src="path/to/client.js"></script>
<script>
    window.epiAuth.onLoad(() => {
        // EpiAuth is loaded
        window.epiAuth.getUser().then(user => {
            // Get user data, will fail if not authenticated on the intranet.
            console.log(user);
        });
    });
</script>
```

### Chrome Extension side

Go to `chrome://extensions` and drag-and-drop the zip file.

You're done !

## Mozilla users...

I'll make a manifest for you soon :)

## API

#### `epiAuth.onLoad`

Set a callback triggered on extension loading

```javascript
window.epiAuth.onLoad(...)
```

#### `epiAuth.getUser()`

Get the user data

```javascript
window.epiAuth.getUser().then(user => {
    console.log(user);
});
```

#### `epiAuth.get(<url>)`

Get data of any endpoint on the intranet

```javascript
window.epiAuth.get(url).then(data => {
    console.log(data);
});
```

## Contibuting

This project is nothing without contribution, feel free to [contact me](mailto:mathias.andre@epitech.eu) to work together on the improvement of this project.
