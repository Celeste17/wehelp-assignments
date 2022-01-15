// wehelp week-3
const dataUrl = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
// console.log(dataUrl)
var xhr = new XMLHttpRequest()
xhr.open('GET', dataUrl, true)
xhr.send()
xhr.onload = function () {
    var data = JSON.parse(this.responseText);
    console.log(data);

    const allDetail = data.result.results;

    /*
    //景點名稱
    console.log(allDetail[0].stitle)
    //景點圖片
    let file = allDetail[0].file
    let firstFilePosition = file.toLowerCase().indexOf('.jpg') + 4
    console.log(file.substring(0, firstFilePosition))
    */

    allDetail.forEach(function (item, index) {
        // console.log(item, index)
        //景點名稱
        console.log(item.stitle)
        //景點圖片
        let file = item.file
        let firstFilePosition = file.toLowerCase().indexOf('.jpg') + 4
        console.log(file.substring(0, firstFilePosition))
        showAttraction(item.stitle, file.substring(0, firstFilePosition))
    })

}
// xhr.onreadystatechange = function () {
//     if (this.readyState === 4 && this.status === 200) {
//         var data = JSON.parse(this.responseText);
//         console.log(data);
//     }
// }


function showAttraction(title, firstPicture) {
    const div = document.createElement("div");
    const str = document.createElement('h2');
    const li = document.createElement('li')
    const ul = document.querySelector('.attractions')

    // img.setAttribute("src", firstPicture)
    div.setAttribute("class", "adjustPic")
    div.setAttribute("style", "background-image: url(" + firstPicture + ");")

    str.textContent = title

    {/* <div class="adjustPic" style="background-image: url(./src/Boracay1.JPG);"></div> */ }
    li.appendChild(div) && li.appendChild(str);
    ul.appendChild(li);
}



/* 
//理解 createElement & appendChild

const img = document.createElement("img");
img.setAttribute("src", "https://www.travel.taipei/d_upload_ttn/sceneadmin/image/A0/B0/C0/D7/E150/F719/71eb4b56-f771-43bc-856c-2fb265a5cc6e.jpg")
const str = document.createElement('h2');
str.textContent = "景點名稱"

const li = document.createElement('li')
li.appendChild(img) && li.appendChild(str);
const ul = document.querySelector('.attractions').appendChild(li);
*/



