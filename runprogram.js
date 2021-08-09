const shell = require('shelljs');
shell.exec('./runcommentbot.sh')
setInterval(function() {
    shell.exec('./runcommentbot.sh');
}, 1000 * 60 * 60 * 10);