function getKeywords() {
  var buttonKeyword = document.getElementById("button-keyword");
  return JSON.parse(buttonKeyword.getAttribute("data-keywords"));
}

var keywords = getKeywords();

function renderKeywordButtons() {
  var buttonKeyword = document.getElementById("button-keyword");
  buttonKeyword.innerHTML = "";

  for (var i = 0; i < keywords.length; i++) {
    var button = document.createElement("button");
    button.setAttribute("type", "button");
    button.setAttribute("class", "button-keyword"); // 클래스 추가
    button.textContent = keywords[i];
    button.onclick = (function (index) {
      return function () {
        removeKeyword(index);
      };
    })(i);

    buttonKeyword.appendChild(button);
  }
}

function removeKeyword(index) {
  keywords.splice(index, 1);
  renderKeywordButtons();
}

function submitRequest() {
  var url = "/image?keywords=" + encodeURIComponent(JSON.stringify(keywords));
  window.location.href = url;
}

renderKeywordButtons();
