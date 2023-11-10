function captureAndDownloadImage() {
    var letterContainer = document.getElementById("letter-container");

    html2canvas(letterContainer, {
        onrendered: function(canvas) {
            var imgDataUrl = canvas.toDataURL("image/png");
            var link = document.createElement("a");
            link.href = imgDataUrl;
            link.download = "letter_image.png";
            link.click();
        },
    });
}
