window.onload = function () {
    const parts = [];
    let mediaRecorder;
    navigator.mediaDevices.getUserMedia({ audio: true, video: true }).then(stream => {
        document.getElementById("video").srcObject = stream;
        document.getElementById("start").onclick = function () {
            mediaRecorder = new MediaRecorder(stream);
            mediaRecorder.start(1000);
            mediaRecorder.ondataavailable = function (e) {
                parts.push(e.data);
            }
        }
    });

    document.getElementById("stop").onclick = function() {
        mediaRecorder.stop();
        const blob = new Blob(parts, {
            type: "video/webm"
        });    
        const url = URL.createObjectURL(blob);
        const a = document.createElement("a");
        document.body.appendChild(a)
        a.style = "dispaly: none";
        a.href = url;
        a.download = "test.webm";
        a.click();
    }
}

