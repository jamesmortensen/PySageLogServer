
## SageLog Logs Notifier

This will eventually be a server that acts as a companion to the [SageLog JavaScript Logging library](https://github.com/jamesmortensen/SageLog).
The idea is the server listens for log collections from remote client applications, stores it in the
Google App Engine Datastore, and then emails a link to the developers.

The idea is also to expand it to have a nice UI for viewing logs in the browser.


## Development

For local development, it helps to use a livereload plugin like https://github.com/lepture/python-livereload.
To install it only for this application, use virtualenv.

From the root of the project, run the following command:

```bash
$ virtualenv gcd
```

Then activate it:

```bash
$  source gcd/bin/activate
```

Now you're clear to install extra Python modules. To install livereload, run the following command:

```bash
$ pip install livereload
```

This installs livereload in gcd/build/livereload/

Lastly, embed the following code inside a load listener on your web page, which listens for livereload events
from the livereload server and subsequently reloads the page:

```javascript
// LiveReloadHelper.js

(function() {
	var script = document.createElement("script");
	script.setAttribute("type", "text/javascript");
	script.setAttribute("src","//localhost:35729/livereload.js");
	document.body.appendChild(script);
})();
```

Then to watch your code for changes, run the following command:

```bash
$ livereload .
```



## Client-side initialization

Get the SageLog client and install SageLog.min.js in the browser.

```
 var logHandler = new SageLog();
      var requestUrl = "http://localhost:8080/logs";   // change this to the URL of your appspot.com server
      window.addEventListener('load', function() {
        logHandler.init({
            "captureLogs": true,
            "logLevel": SageLog.DEBUG,
            "logStorerClassName": "JsonLogStorer",
            "server": requestUrl
        });

        console.debug('test test test');
        console.log('test test test');
        console.info('test test test');
        console.warn('test test test');
        console.error('test test test');

        var observer = logHandler.sendLogsToServer();
        observer.done(function(result) {
          console.debug('done sending to server');
          console.debug(result);
        });
      });
```

## Example payload

```json
{
    "handshake": 1403478503263,
    "message": {
        "logBundles": [
            {
                "bundleName": "default",
                "logEntries": [
                    {
                        "type": "info",
                        "color": "#006400",
                        "encodedData": "hello world",
                        "pathname": "/tests/_SpecRunner.html",
                        "timestamp": 1403478503259
                    },
                    {
                        "type": "error",
                        "color": "red",
                        "encodedData": "hello test",
                        "pathname": "/tests/_SpecRunner.html",
                        "timestamp": 1403478503259
                    },
                    {
                        "type": "warn",
                        "color": "#DAA520",
                        "encodedData": "hello careful",
                        "pathname": "/tests/_SpecRunner.html",
                        "timestamp": 1403478503260
                    },
                    {
                        "type": "error",
                        "color": "red",
                        "encodedData": "~`!@#$%^&*()_+-=;\":/?.&gt;,&lt;[]{}|'\\\n &lt;div&gt;Test & test&lt;/div&gt;",
                        "pathname": "/tests/_SpecRunner.html",
                        "timestamp": 1403478503260
                    }
                ]
            }
        ]
    }
}
```

## License

Copyright 2014, James Mortensen ([@jmort253](https://twitter.com/jmort253)), MIT License.
