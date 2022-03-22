# Terminal Timeline
Epitech Timeline in your favourite shell

![Timeline Example](https://raw.githubusercontent.com/MathiDEV/epitech_productivity_tools/main/terminal_timeline/timeline.png)

## Usage
```
python3 my_timeline.py
```

To get precisions about a project

```
python3 my_timeline.py <MODULE> <PROJECT>
```

Example: 
```
python3 my_timeline.py PSU 3
```

## Update timeline
To use your own time line just change the timeline.json

To get your Epitech timeline, the easiest way is to go on

-> Intranet
-> Administration
-> Annual Planning
-> [Enter year and semester(s)]

When everything is displayed, run the code above in your browser console, available when you use "Inspect element" :
```js
var all_projects = [];
$("div.column.item.proj").each(function () {

    let infos = $(this).find(".infobulle").text().split("Du ").join('|').split(" au ").join('|').split("Date de rendu : ").join('|').split('|');
    let module = $(this).parents(".module").find(".row .column.head.title").text()
    all_projects.push({ project: infos[0], module: module, start: infos[1], end: infos[2]})
})
console.log(JSON.stringify(all_projects));
```

And you'll have your timeline in JSON !
