"use strict"

/* ******************************** */

/* OGGETTI E FUNZIONI */

/* Oggetto Post*/
function Post(id, daysago) { //(node) --> node.id, node.daysago
    this.id = id;
    this.daysago = daysago;

    this.toString = function(){
        let output = "" + `Post [id: ${this.id}, daysago: ${this.daysago}]`;
        return output;
    }

    this.compareTo = function(other) {
        return this.daysago - other.daysago;
    };

    this.equals = function(other) {
        if (!(other instanceof Post)) {
            return false;
        };
        let output = true;
        for (let att in this) {
            output = output && this['att']==+other['att']
        };
        return output
    };
}

/* Comparatore per ordinare strutture contenenti oggetti Post: Se a viene prima di b restituisce true, false altrimenti */
function descPostComparator(a, b) {
    return !postComparator(a,b);
}

/* Comparatore per ordinare strutture contenenti oggetti Post: Se a viene dopo b restituisce true, false altrimenti */
function postComparator(a, b) {
    return a.compareTo(b) > 0;
}

/* Resetta l'attributo di stile "display" per ogni post passato come parametro */
function resetDisplayOfAllPosts(posts) {
    console.log("Resetting display style attribute of all posts")
    for (let post of posts) {
        let htmlPost = document.querySelector(`#${post.id}`);
        htmlPost.style.display = '';
    };
}

function pushPostById(postsAsNodes, id) {
    for (let i=0; i < postsAsNodes.length; i++) {
        //console.log(postsAsNodes[i]);
        if (postsAsNodes[i].id == id) {
            let main = document.querySelector('main');
            main.appendChild(postsAsNodes[i]);
        };
    };
}

/* ******************************** */

/* MAIN */

/* Setup */

// Imposto un id ad ogni post

let postsAsNodes = document.querySelectorAll('a > article');

let id = 1;
for (let post of postsAsNodes) {
    post.id = "post-"+id;
    id++;
};

// Estraggo i valori di daysago per ogni post

let multiDaysago = document.querySelectorAll('.daysago');
let daysagoList = [];
for (let singleDaysago of multiDaysago) {
    let daysago = singleDaysago.innerText.split(" ")[0];
    daysagoList.push(daysago);
};

/* 

    In questo momento abbiamo due array: 
    
    I nodi di post          I daysago ad essi relativi
    index 0: [post@id1] --> [daysago@post@id1] 
    index 1: [post@id2] --> [daysago@post@id2]
    index 2: [post@id3] --> [daysago@post@id3]

    ...

    Dove
    * idPost = indexArray + 1
    * indexArray = idPost - 1

*/

// Predo i dati appena estratti e li condenso tutti in un array di oggetti Post chiamato "posts" (riutilizzo il vecchio riferimento)
let posts = [];
for (let i=0; i < postsAsNodes.length; i++) {
    //console.log(posts[i].id);
    //console.log(daysagoList[i])
    posts.push(new Post(postsAsNodes[i].id, daysagoList[i]));
};  
console.log("Post in questa pagina: " + posts);

/* Gestione degli eventi sui bottoni */

// Estraggo i vari nodi dei "bottoni"

let todayBtn = document.querySelector('#todayBtn');
let thisWeekBtn = document.querySelector('#thisWeekBtn');
let thisMonthBtn = document.querySelector('#thisMonthBtn');

let mostRecentSortBtn = document.querySelector('#mostRecent') 
let lessRecentSortBtn = document.querySelector('#lessRecent')

//Imposto dei listener sui vari bottoni

/* Listener di click sul bottone "Dal piú recente" */
mostRecentSortBtn.addEventListener('click', e => {
    console.log('Click on most recent button');

    let ascPosts = posts.sort(postComparator);
    //console.log(ascPosts);

    let main = document.querySelector('main');
    while (main.firstChild) {
        main.removeChild(main.lastChild);
    };

    for (let post of ascPosts) {
        pushPostById(postsAsNodes, post.id);
    };
    
});


/* Listener di click sul bottone "Dal meno recente" */
lessRecentSortBtn.addEventListener('click', e => {
    console.log('Click on less recent button');

    let descPosts = posts.sort(descPostComparator);
    //console.log(ascPosts);

    let main = document.querySelector('main');
    while (main.firstChild) {
        main.removeChild(main.lastChild);
    };

    for (let post of descPosts) {
        //console.log(post.id);
        pushPostById(postsAsNodes, post.id);
    };
    
});

/* Listener di click sul bottone "Oggi" */
let resetTodayButton = false;
todayBtn.addEventListener('click', e => {
    // Rimuove ogni post che non sia di oggi
    console.log('Click on today button');
    resetDisplayOfAllPosts(posts); 

    if (!resetTodayButton) {
        for (let post of posts) {
            if (post.daysago > 0) {
                let htmlPost = document.querySelector(`#${post.id}`);
                htmlPost.style.display = 'none';
            };
        };
        resetTodayButton = true;
    } else {
        resetTodayButton = false;
    };
});


/* Listener di click sul bottone "Questa settimana" */
let resetWeekButton = false;
thisWeekBtn.addEventListener('click', e => {
    // Rimuove ogni post che non sia di questa settimana
    console.log('Click on this week button');
    resetDisplayOfAllPosts(posts); 

    if (!resetWeekButton) {
        for (let post of posts) {
            if (Number(post.daysago) > 7) {
                let htmlPost = document.querySelector(`#${post.id}`);
                htmlPost.style.display = 'none';
            };
        };
        resetWeekButton = true;
    } else {
        resetWeekButton = false;
    };
});


/* Listener di click sul bottone "Questo mese" */
let resetMonthButton = false;
thisMonthBtn.addEventListener('click', e => {
    // Rimuove ogni post che non sia di questo mese
    console.log('Click on this month button');
    resetDisplayOfAllPosts(posts); 

    if (!resetMonthButton) {
        for (let post of posts) {
            if (Number(post.daysago) > 30) {
                let htmlPost = document.querySelector(`#${post.id}`);
                htmlPost.style.display = 'none';
            };
        };
        resetMonthButton = true;
    } else {
        resetMonthButton = false;
    };
});