
const items = document.querySelectorAll("ul li");


if (performance.navigation.type == performance.navigation.TYPE_RELOAD || window.performance){
    let lastDirectory = pathURL()
    check(lastDirectory)
}

function pathURL(){
    let path = window.location.pathname;
    let directories = path.split("/");
    let lastDirectory = directories[(directories.length - 2)];
    return lastDirectory
}

function check(lastDirectory){
    let chosen = lastDirectory
     for (let s = 0; s<items.length; s++){
        items[s].classList.remove('active');
    }
    document.querySelector(`[name=${chosen}]`).classList.add('active')
}
