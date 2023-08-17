document.addEventListener('DOMContentLoaded', function() {
    var currentTime = new Date().toLocaleTimeString('en-US', { hour12: false, hour: '2-digit', minute: '2-digit' });
    document.getElementById('logTime').value = currentTime;
});