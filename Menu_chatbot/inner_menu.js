const express = require('express');
const fs = require('fs')
const app = express();
app.use(express.json())

app.get('/get/:day/:time',(req,res)=>{
    day = req.params.day.split('_')
    time = req.params.time.split('_')

    var jsondata = fs.readFileSync('menu.json')
    var data = JSON.parse(jsondata);

        for(j=0;j<day.length;j++)
        for(i=0;i<data.length;i++){

            if (day[j] in data[i]){
            day=day[j]
            let todayMeal=data[i][day]

                for(k=0;k<todayMeal.length;k++)
                for(l=0;l<time.length;l++){

                    if (time[l] in todayMeal[k]){
                        time=time[l]
                        return res.json(todayMeal[k][time])  
                }
            }
        }

        }
    
});

app.put('/menu_update/:day/:time', (req, res) => {
    day = req.params.day.split('_')
    time = req.params.time.split('_')

   var jsonData = fs.readFileSync('menu.json');
   var data = JSON.parse(jsonData);
   for(j=0;j<day.length;j++)
   for(i=0;i<data.length;i++){

       if (day[j] in data[i]){
           day=day[j]
           let todayMeal=data[i][day]

            for(k=0;k<todayMeal.length;k++)
            for(l=0;l<time.length;l++){

                if (time[l] in todayMeal[k]){
                    time=time[l]
                    console.log(time)
                todayMeal[k][time] = req.body.time;
                }
                
       }
   }
   fs.writeFileSync(__dirname +"/menu.json", (JSON.stringify(data, null, 2)));
   res.json(data)
}
});


app.listen(4040,()=>{
    console.log("done")
})