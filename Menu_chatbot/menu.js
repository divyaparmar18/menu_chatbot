const express = require('express');
const fs = require('fs')
const app = express();
app.use(express.json())

app.get('/get/:day',(req,res)=>{
    day = req.params.day.split('_')
    console.log(day)
    //console.log(day)
    var jsondata = fs.readFileSync('menu.json')
        var data = JSON.parse(jsondata);
    for(j=0;j<day.length;j++)
    for(i=0;i<data.length;i++){
        if (day[j] in data[i]){
            //console.log(data[i])
            return res.json(data[i][day])
        }
    }
});



app.post('/post_newCourse', (req, res) => {
    var NewCourse = {
        holi_day: req.body.holi_day,
    }
    let data = fs.readFileSync('menu.json')
    data = data.toString();
    let Data = JSON.parse(data)
    //NewCourse.id = Data.length + 1;
    Data.push(NewCourse)
    fs.writeFileSync(__dirname + '/menu.json', JSON.stringify(Data, null, 2));
    return res.json(Data)
});



app.put('/menu_update/:day', (req, res) => {
     day = req.params.day.split('_')
     console.log(day)

    var jsonData = fs.readFileSync('menu.json');
    var data = JSON.parse(jsonData);
    for(j=0;j<day.length;j++)
    for(i=0;i<data.length;i++){
        if (day[j] in data[i]){
        data[i][day] = req.body.day;
        }
    }
    fs.writeFileSync(__dirname +"/menu.json", (JSON.stringify(data, null, 2)));
    res.json(data)
});



app.listen(4000,()=>{
    console.log("done")
})