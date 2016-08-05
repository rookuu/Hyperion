var socket = io.connect('http://' + document.domain + ':' + location.port);

socket.on('connect', function () {
    socket.emit('connection', {data: 'Client Connected'});
});