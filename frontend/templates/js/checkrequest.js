        function approveRequest(rownum, request_id){

            var statuscol = document.getElementById("requests").rows[rownum].cells[6]
            var approvebutton = document.getElementById("approve"+request_id+"")
            var rejectbutton = document.getElementById("reject"+request_id+"")
                fetch("api/"+request_id+"/",{
                    method: 'PATCH',
                    headers:{
                        'Content-Type': 'application/json',
                        'Authorization' : 'Bearer '+localStorage.getItem("token"),
                    },
                    body: JSON.stringify({
                        status: "Approved"
                    })
                })
                // Converting received data to JSON
                .then(response => {
                    if (response.ok){
                        console.log(response)
                        statuscol.innerHTML = "Approved";
                        approvebutton.disabled = true;
                        rejectbutton.disabled = true;
                    }
                    return response.json();
                })
                .then(json => {
                })
                .catch(error => console.log(error));

        }

        function rejectRequest(rownum, request_id){
            var statuscol = document.getElementById("requests").rows[rownum].cells[6]
            var approvebutton = document.getElementById("approve"+request_id+"")
            var rejectbutton = document.getElementById("reject"+request_id+"")
                fetch("api/"+request_id+"/",{
                    method: 'PATCH',
                    headers:{
                        'Content-Type': 'application/json',
                        'Authorization' : 'Bearer '+localStorage.getItem("token"),
                    },
                    body: JSON.stringify({
                        status: "Rejected"
                    })
                })
                // Converting received data to JSON
                .then(response => {
                    if (response.ok){
                        console.log(response)
                        statuscol.innerHTML = "Rejected";
                        approvebutton.disabled = true;
                        rejectbutton.disabled = true;
                    }
                    return response.json();
                })
                .then(json => {
                })
                .catch(error => console.log(error));

        }

        function getUserInfo(worker_id){
                    var ui = document.getElementById("userinfo")

                fetch("api/workerid/"+worker_id+"/",{
                    method: 'GET',
                    headers:{
                        'Content-Type': 'application/json',
                        'Authorization' : 'Bearer '+localStorage.getItem("token"),
                    }
                })
                // Converting received data to JSON
                .then(response => {
                    return response.json();
                })
                .then(json => {
                    content = `<h3>User Info</h3><br>
                            <h5>workerid : ${json.id}</h5>
                            <h5>username : ${json.username}</h5>
                           <h5>team : ${json.team}</h5>`
                    ui.classList.add("d-block");
                    ui.innerHTML = content
                    console.log(json);
                })
                .catch(error => console.log(error));
        }

        function logout(){
                fetch("/"+"logout/api/",{
                    method: 'POST',
                    headers:{
                        'Content-Type': 'application/json',
                        'Authorization' : 'Bearer '+localStorage.getItem("token"),
                    },
                    body: JSON.stringify({
                        refresh_token : localStorage.getItem("tokenrefresh")
                    })
                })
                // Converting received data to JSON
                .then(response => {
                    if (response.ok){
                        localStorage.removeItem("token");
                        localStorage.removeItem("tokenrefresh");
                        // console.log(response)
                        window.location.href = "";
                    }
                    return response.json();
                })
                .then(json => {

                    console.log(json)
                })
                .catch(error => console.log(error));

        }
