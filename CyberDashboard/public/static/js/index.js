
// function updateMap() {
//     fetch("/json-data")
//         .then(response => response.json())
//         .then(rsp => { 
//             // console.log(rsp)
//             rsp.forEach(element => {
//                 // console.log(element.src_ip)
//                 $.ajax({
//                     type: 'GET',
//                     url: "{% url 'get_geo_cordinates' %}",
//                     data : {ip : element.src_ip },
//                     success: function(response) {
//                         console.log(response.status)
//                     },
//                     error: function(error) {
//                         console.error('An error occurred', error);
//                     }
//                     });
                        
//             })
//     })
// }

function updateMap() {
    fetch("/json-data")
        .then(response => response.json())
        .then(data => {
            data.forEach(element => {
                $.ajax({
                    type: 'GET',
                    url: "{% url 'get_geo_cordinates_ajax' %}",  // Update to the correct URL name
                    data: {ip: element.src_ip},
                    success: function (response) {
                        console.log(response.status);
                    },
                    error: function (error) {
                        console.error('An error occurred', error);
                    }
                });
            });
        })
        .catch(error => {
            console.error('An error occurred while fetching JSON data', error);
        });
}

updateMap();
