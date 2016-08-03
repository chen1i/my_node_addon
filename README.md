my_node_addon
=========
this is a code sample by following this blog: [How to Create C/C++ Addons in Node](http://stackabuse.com/how-to-create-c-cpp-addons-in-node/)

### Pre-requirements:

 * node.js and npm (I ran this on node.js v6.3.1 and npm 3.10.3)
 * [node-gyp](https://github.com/nodejs/node-gyp)
 * [nan](https://www.npmjs.com/package/nan)


### How to play
===========

* clone code, cd to that root of source
* install dependencies
  * node-gyp, the build tool
  ``` bash
  $ npm install -g node-gyp
  ```
  * nan, the lib to easily writing native cpp code
  ``` bash
  $ npm install --save nan
  ```
* prepare build env
``` bash
$ node-gyp configure
```
* build
``` bash
$ node-gyp build
```
* test
run in node REPL or put these lines in a .js file
``` javascript
var addon = require('./build/Release/pow');
console.log(addon.pow(24, 2));
```
you should see 576 output.
