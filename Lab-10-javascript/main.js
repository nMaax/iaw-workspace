"use strict"

/* ESERCIZIO 1 */

/*

const voti = [20, 20, 30, 25, 29, 27, 26, 24, 30];

let voti_copia1 = Array.from(voti);
let voti_copia2 = Array.from(voti);

voti_copia1.sort(integerComparator);

print("Array iniziale " + voti_copia1)

print("Voto massimo: " + voti_copia1.pop());
print("Voto minimo: " + voti_copia1.shift());

print("Array finale: " + voti_copia1);

print("***********")

voti_copia2 = Array.from(voti);
print("Array iniziale " + voti_copia1);

let sum = 0;
for (let a of voti_copia2) {
    sum = sum +  a
};


let mean = sum / voti_copia2.length
let rounded_mean = Math.round(mean)

print("Media voti: "+mean)
print("Media voti (arrotondata): "+rounded_mean)

voti_copia2.push(rounded_mean)
voti_copia2.push(rounded_mean)

print("Array finale: " + voti_copia2)

print("***********")

print("Array originale: "+voti)
print("Array copia 1: "+voti_copia1)
print("Array copia 2: "+voti_copia2)

*/

/* ESERCIZIO 2 */

const ISO_DATE = "YYYY-MM-DD";


// Some books to test stuff
let GGA = new Libro(1, "Guida galattica per autostoppisti", "Douglas Adams", dayjs("2012-01-01"), 5);

let TPS = new Libro(2, "Il Toyota Production System", "Taichiro Ono", dayjs("1950-01-01"), 4);

let LDS = new Libro(3, "Il lupo della steppa", "Herman Hesse", dayjs("1946-01-01"), 3);

/*
    ... stuff you want to test ...
*/

/* Class Libreria */
function Libreria() {
    
    /* ATTRIBUTES */

    this.libri = [];

    /* METHODS */

    this.aggiungiLibro = function(libro) {
        if (libro instanceof Libro) {
            this.libri.push(libro) 
        };
    }
    
    this.cancellaLibro = function(libro) {
        if (libro instanceof Libro) {
            for (let libroInLibreria of this.libri) {
                if (libro.equals(libroInLibreria)) {
                    let indexOfLibroInLib = this.libri.indexOf(libroInLibreria)
                    this.libri.splice( indexOfLibroInLib, 1 )
                };
            };
        };
    }

    this.calcolaMedia = function() {

        let sum = 0;
        for (let libro of this.libri) {
            sum += libro.rating;
        };
        let mean = sum / this.libri.length;
        return mean;

    }

    this.ritardaPubblicazione = function(n) {
        for (let libro of this.libri) {
            libro.date = libro.date.add(n, "day")
        };
    }

    this.toString = function() {
        let s = "";

        for (let libro of this.libri) {
            s = s + libro.toString() + ", ";
        };

        if (s.length >= 2) {
            s = s.substring(0, s.length-1)
            s = s.substring(0, s.length-1)
        };

        return s;
    }

}

/* Class Libro */
function Libro(id=-1, title="NO_TITLE", author="NO_AUTH", date="NO_DATE", rating=0) {

    /* CONSTANTS */

    const RATING_SCALE = [1, 2, 3, 4, 5];

    /* ATTRIBUTES */

    this.id = id;
    this.title = title;
    this.author = author;
    this.date = date;

    if (RATING_SCALE.includes(rating)) {
        this.rating = rating;
    } else {
        this.rating = 0;
    };

    /* METHODS */

    this.sayHello = function() {
        print("Hello! I'm a book, my name is \"" + this.title + "\" and I was wrote by " + this.author);
    }

    this.equals = function(other) {
        let output = true;
        if (other instanceof Libro) {
            for (let attr in other) {
                if (typeof this[attr] != 'function' && typeof other[attr] != 'function') {
                    output &= (other[attr] === this[attr])
                };
            };
        } else {
            output = false
        };
        return output
    }

    this.toString = function() {
        print("\"" + this.title + "\" by " + this.author);
    }
}

/* Funzioni utilizzate */

function integerComparator(a, b) {
    return a-b;
}

// Shortcut per console.log()
function print(object) {
    console.log(object);
}