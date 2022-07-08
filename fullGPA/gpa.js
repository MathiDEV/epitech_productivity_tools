const grades = {
    A: 4,
    B: 3,
    C: 2,
    D: 1,
    E: 0,
    Echec: 0,
}


const login = document.querySelector("#profil > div.bloc.main > div > div.infos > div.item.login > span").innerText
fetch(`https://${window.location.hostname}/user/${login}/notes?format=json`, {
    method: 'GET',
    credentials: 'include',
}).then(response => response.json()).then(data => {
    let total = 0,
        divisor = 0;

    for (module of data["modules"]) {
        if (grades[module.grade] !== undefined) {
            total += grades[module.grade] * module.credits;
            divisor += module.credits;
        }
    }
    document.querySelector("#profil > div.bloc.top > div.rzone > span > span:nth-child(4)").innerText = divisor == 0 ? 0 : (total / divisor).toFixed(10);
})