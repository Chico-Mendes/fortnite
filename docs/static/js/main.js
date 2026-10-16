const API_URL = "";
const frogChicoId = 3925413;
let   frogChicoDoc;
let seasons = [];
let currentSeason = 0;
init();

async function init() {
    // frogChicoDoc = await getDocument(`${API_URL}?id=${frogChicoId}`);
    // console.log(frogChicoDoc);
    const template = document.querySelector("template");
    frogChicoDoc = template.content;
    

    console.log(getSeasons());
    console.log(getCurrentSeason());
}

async function getDocument(url) {
    const response = await fetch(url);
    const html = await response.text();

    return new DOMParser()
        .parseFromString(html, "text/html");
}

function getSeasons() {
    const div = frogChicoDoc.getElementById("sprites-season-filters");
    const season_divs = div.querySelectorAll("[data-sprite-season]");
    seasons = [...season_divs]
        .map(sd => Number(sd.dataset.spriteSeason))
        .filter(Number.isFinite);

    return seasons;
}

function getCurrentSeason() {
    currentSeason = Math.max(...seasons);
    return currentSeason;
}