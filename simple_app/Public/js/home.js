let elementTotalData = $('#total-data')
let elementRowData = $('#row-data')

$(document).ready(function(){
    let socket = io.connect('http://localhost:5000/todo-data')

    socket.on('connect', function(){
        // socket.emit('join',{})
    })

    socket.on('message', function(payload){
        console.log(payload.data);
        
        elementTotalData.html(payload.data.length)
        elementRowData.html(rowPopulate(payload.data))
    })

})

function rowPopulate(data){
    let elementArray = []
    for (let item of data) {
        elementArray.push(`<tr><td>${item.title}</td><td>${item.description}</td></tr>`)
    }

    return elementArray
}