// alert("Hello")

const inputUsername = document.querySelector(".inputUsername");
const btnSearch = document.querySelector(".btnSearch");
const searchResult = document.querySelector(".searchResult");
// const changeName = document.querySelector(".changeName");
// const btnChange = document.querySelector(".btnChange");
// const changeResult = document.querySelector(".changeResult");


// 監聽「查詢」按鈕
btnSearch.addEventListener("click", function () {
    username = inputUsername.value;
    // searchResult.textContent =
    url = "/api/members?username=" + username
    fetch(url)
        .then(function (response) {
            return response.json();
        }).then(function (result) {
            // console.log(result)
            showResult(result)
        })
})

// 顯示「查詢」結果
function showResult(result) {
    // memberName = result.data.name
    // username = result.data.username
    // console.log(memberName, username)
    // searchResult.textContent = `${memberName}(${username})`
    if (result.data == null) {
        searchResult.textContent = "查無此筆帳號"
        console.log("查無此筆帳號")

    } else {
        memberName = result.data.name
        username = result.data.username
        console.log(memberName, username)
        searchResult.textContent = `${memberName}(${username})`
    }

}