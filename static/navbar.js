function about() {
    document.getElementById('about').style.backgroundPosition = '100% 100%'
    document.getElementById('projects').style.backgroundPosition = '0% 0%'
    document.getElementById('contacts').style.backgroundPosition = '0% 0%'
    window.scrollTo(0, 0)
}

function projects() {
    document.getElementById('projects').style.backgroundPosition = '100% 100%'
    document.getElementById('about').style.backgroundPosition = '0% 0%'
    document.getElementById('contacts').style.backgroundPosition = '0% 0%'
    window.scrollTo(0, 0)
}

function contacts() {
    document.getElementById('contacts').style.backgroundPosition = '100% 100%'
    document.getElementById('about').style.backgroundPosition = '0% 0%'
    document.getElementById('projects').style.backgroundPosition = '0% 0%'
    window.scrollTo(0, 0)
}
