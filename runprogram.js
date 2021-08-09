const shell = require('shelljs');
console.log("HEREBEFORE")
shell.exec('./runcommentbot.sh');
console.log("here1");
setInterval(function() {
    shell.exec('runcommentbot.sh');
}, 1000 * 60 * 60 * 2);