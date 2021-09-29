// POST
const requestForm = document.getElementById('requestForm');
if(requestForm){
    requestForm.addEventListener('submit', function(e){
        e.preventDefault()

        fetch("api/",{
            method: 'POST',
            headers:{
                'Content-Type': 'application/json',
                'Authorization' : 'Bearer '+localStorage.getItem("token"),
            },
            body: JSON.stringify({
                start_date: document.getElementById("start_date").value,
                end_date: document.getElementById("end_date").value,
            })
        })
        .then(response =>{
            if(response.ok){
                location.reload()
            }
            return response.json()
        })
        .then(data => {
            console.log(data)
            if(data.error){
                document.getElementById("error-date").classList.remove("d-none")
                document.getElementById("error-date").innerHTML = data.error + " !"
            }
        })
        .catch(error => {
            console.log(error)
        })
    });
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
                window.location.href = "/";

            }
            return response.json();
        })
        .then(data => {

            console.log(data)
        })
        .catch(error => console.log(error));
}
