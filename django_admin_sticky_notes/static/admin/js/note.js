const stickyNote = document.querySelector(".sticky-note");

function getCookie(name) {
    if (!document.cookie) {
        return null;
    }

    const xsrfCookies = document.cookie.split(';')
        .map(c => c.trim())
        .filter(c => c.startsWith(name + '='));

    if (xsrfCookies.length === 0) {
        return null;
    }
    return decodeURIComponent(xsrfCookies[0].split('=')[1]);
}

function delay(fn, ms) {
    let timer = 0
    return function (...args) {
        clearTimeout(timer)
        timer = setTimeout(fn.bind(this, ...args), ms || 0)
    }
}

function getStickyNoteData() {
    fetch("/sticky-note")
        .then(response => response.json())
        .then(data => stickyNote.innerHTML = data.note)
}

getStickyNoteData();

stickyNote.addEventListener("keyup", delay(function (event) {
    const notes = event.target.innerHTML;
    console.log('notes', notes)

    fetch('/sticky-note', {
        headers: {
            "Content-Type": "application/json; charset=utf-8",
            "X-CSRFToken": getCookie('csrftoken')
        },
        method: "POST",
        body: JSON.stringify({"note": notes})
    })
}, 500))