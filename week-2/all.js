//wehelp week-2

//要求一
console.log("JS 要求一");
function calculate(min, max) {
    // console.log(min + max); //驗證函式有執行
    let sum = 0;
    for (i = min; i <= max; i++) {
        // console.log(i)      //驗證迴圈
        sum = sum + i;
    }
    console.log(sum)           //結果
}
calculate(1, 3); // 計算 1+2+3，最後印出 6
calculate(4, 8); // 計算 4+5+6+7+8，最後印出 30
console.log("--------------------");

//要求二
console.log("JS 要求二");

function avg(data) {
    // console.log(data.count);               //數量
    // console.log(data.employees.length);    //員工陣列長度
    let sumSalary = 0;
    let avgSalary = 0;
    data.employees.forEach(function (item, index) {
        // console.log(item, index)           //驗證迴圈
        // console.log(item.salary)           //驗證資料
        sumSalary += item.salary
    })
    // console.log(data.employees[0].salary); //驗證資料
    avgSalary = sumSalary / data.count;
    console.log(avgSalary)                 //結果
    console.log(Math.round(avgSalary * 100) / 100); //結果 四捨五入至小數點第二位

}
avg({
    "count": 3,
    "employees": [
        {
            "name": "John",
            "salary": 30000
        },
        {
            "name": "Bob",
            "salary": 60000
        },
        {
            "name": "Jenny",
            "salary": 50000
        }
    ]
}); // 呼叫 avg 函式


console.log("--------------------");


//要求三
console.log("JS 要求三");

// let newArrayMult = []; //篩選陣列獨立，因此不需要使用
function maxProduct(nums) {
    // console.log(nums[0])
    let mult;
    let arrayMult = [];

    nums.forEach(function (item, index) {
        // console.log("第一層" + item);          //確認第一層資料
        nums.forEach(function (item2, index2) {
            if (index === index2) {
                // console.log("不計算");
            } else {
                // console.log("第二層" + item2); //確認第二層資料
                mult = item * item2;
                // console.log(mult);
                // arrayMult.push(mult);          //不管 -0 狀態
                if (mult === -0) {                //檢查 -0 狀態
                    // console.log(-mult);
                    arrayMult.push(-mult);
                } else {
                    arrayMult.push(mult);
                }
                // console.log(arrayMult);        //所有相乘資料
            }
        })
    })
    // filter(arrayMult);

    //---- 篩選陣列 程式碼獨立------------------------------------------------------
    // console.log("資料：" + newArrayMult);         //顯示篩選不重複後資料
    // console.log(Math.max.apply(null, newArrayMult)); //結果
    //----------------------------------------------------------

    // console.log("資料：" + filter(arrayMult));         //顯示篩選不重複後資料
    console.log(Math.max.apply(null, filter(arrayMult))); //結果
}

//篩選陣列裡重複資料 
function filter(array) {
    let newArray = array.filter(function (element, index, arr) {
        // console.log("element：" + element + " ,index：" + index + ",arr：" + arr); //理解變數
        return arr.indexOf(element) === index;
    })
    return newArray;
}


maxProduct([5, 20, 2, 6]) // 得到 120
maxProduct([10, -20, 0, 3]) // 得到 30
maxProduct([-1, 2]) // 得到 -2
maxProduct([-1, 0, 2]) // 得到 0
maxProduct([-1, -2, 0]) // 得到 2

console.log("--------------------");


//要求四
console.log("JS 要求四");

function twoSum(nums, target) {
    let final = [];
    let add = 0;
    // console.log(nums);
    // console.log(target);
    nums.forEach(function (item, index) {
        // console.log("第一層" + item);          //確認第一層資料
        nums.forEach(function (item2, index2) {
            if (index === index2) {
                // console.log("不計算");
            } else {
                // console.log("第二層" + item2); //確認第二層資料
                add = item + item2;
                // console.log(add);              //相加結果
                if (add === target) {
                    final.push(index, index2);
                }
            }
        })
    })
    return filter(final);
}
let result = twoSum([2, 11, 7, 15], 9);
console.log(result); // show [0, 2] because nums[0]+nums[2] is 9
// console.log(twoSum([11, 11, 7, 15], 22))

console.log("--------------------");

