window.onload = alert("Hurray! Enjoy my game\nClick on 'START' then you should put the numbers in order from 1 to 9...\nSo click on a cell number the empty cell...\nENJOY!!!");

var steps = 0;
var sec = "00";
var min = 0;
var seconds;
var minutes;
var div_sec = document.getElementById('sec');
var div_min = document.getElementById('min');

function startTimer() {
    seconds = setInterval(secTimer, 1000);
    minutes = setInterval(minTimer, 60000);
}

function secTimer() {
    sec++;

    if(sec < 10){
        sec = "0" + sec;
    }
    else if(sec > 59){
        sec = "0" + 0;
    }

    div_sec.innerHTML = sec;
}

function minTimer(){
    min++;
    div_min.innerHTML = min;
    }

function clearTimer(){
    clearInterval(seconds);
    clearInterval(minutes);
}

function resetTimer() {
    sec = "00";
    min = 0;
    div_sec.innerHTML = sec;
    div_min.innerHTML = min;
}

var numbers = document.getElementsByClassName('numbers');

function change(x, left, up, right, down, left2, up2, right2, down2){
    var id = x;

    if(left == true && verIfEmpty(id-1) == true){
        steps++;
        changeContent(id, id-1);
    }
    else if(left2 == true && verIfEmpty(id-2) == true){
        steps++;
        changeContent(id-1, id-2);
        changeContent(id, id-1);
    }
    else if(up == true && verIfEmpty(id-3) == true){
        steps++;
        changeContent(id, id-3);
    }
    else if(up2 == true && verIfEmpty(id-6) == true){
        steps++;
        changeContent(id-3, id-6);
        changeContent(id, id-3);
    }
    else if(right == true && verIfEmpty(id+1) == true){
        steps++;
        changeContent(id, id+1);
    }
    else if(right2 == true && verIfEmpty(id+2) == true){
        steps++;
        changeContent(id+1, id+2);
        changeContent(id, id+1);
    }
    else if(down == true && verIfEmpty(id+3) == true){
        steps++;
        changeContent(id, id+3);
    }
    else if(down2 == true && verIfEmpty(id+6) == true){
        steps++;
        changeContent(id+3, id+6);
        changeContent(id, id+3);
    }
}

function verIfEmpty(x){
    var a = document.getElementById(x);
    var c = a.innerHTML;
    if(c == ""){
        y = true;
    }
    else{
        y = false;
    }
    return y;
}

function changeContent(x, y){
    var m = document.getElementById(x);
    var n = document.getElementById(y);
    n.innerHTML = m.innerHTML
    m.innerHTML = "";
    win();
    showScore();
    ok();
}

// RANDOM GENERATOR FUNCTION
function randomGenerator(low, high){
    if(arguments.length < 2){
        high = low;
        low = 0;
    }
    this.low = low;
    this.high = high;
    this.reset();
}

randomGenerator.prototype = {
    reset: function(){
        this.remaining = [];
        for(var i = this.low; i <= this.high; i++){
            this.remaining.push(i);
        }
    },
    get: function() {
        if(!this.remaining.length){
            this.reset();
        }
        var index = Math.floor(Math.random() * this.remaining.length);
        var val = this.remaining[index];
        this.remaining.splice(index, 1);
        return val;
    }
}
// WRITE THE RAMDOM NUMBERS IN THE PUZZLE
function getNum(){
    var randomNoRepeatNumbers = new randomGenerator(0,8);
    for(var i=1; i<=9; i++){
        var newNumbers = document.getElementById(i);
        newNumbers.innerHTML = randomNoRepeatNumbers.get();
    }
    for(var i in numbers){
        if(numbers[i].innerHTML == 0){
            numbers[i].innerHTML = "";
        }
    }
    steps = 0;
    showScore();
    verifArray();
    clearTimer();
    resetTimer();
    startTimer();
    ok();
}

function win(){
    var time = min + ":" + sec;
    var win = true;
    for (var i in numbers){
        if(numbers[i].innerHTML != numbers[i].id){
            if(numbers[i].id != numbers.length){
                win = false;
                break;
            }
        }
    }
    if(win){
        clearTimer();
        navigator.vibrate(500);
        function showAlert(){
            alert("YOU WIN!\nYOU MADE "+ steps+" MOVES\n YOUR TIME IS "+min+" min. AND "+sec+" sec.");
        }
        setTimeout(showAlert, 1000);
        document.getElementById('9').innerHTML = "9";
    }
}

function showScore(){
    document.getElementById("score").innerHTML = ("MOVES = "+steps);
}

function verifArray(){
    var count = 0;
    var arrayNum = [];
    for(var i = 1; i <= 9; i++){
        var w = document.getElementById(i).innerHTML;
        arrayNum[i-1] = w;
    }
    for(var i = 0; i <= arrayNum.length - 1; i++){
        for(var n = i+1; n <= arrayNum.length - 1; n++){
            if(arrayNum[i]>arrayNum[n] && arrayNum[n]!=0){
                count++;
            }
        }
    }
    if(count % 2 != 0){
        getNum();
    }
}

function ok() {
    for(var i=1; i<10; i++){
        var x = document.getElementById(i);
        if(x.innerHTML == i){
            x.style.color = "#74a57a";
        }
        else{
            x.style.color = "#ffffff";
        }
    }
}