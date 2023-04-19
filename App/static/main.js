
async function getUserData(){
    const response = await fetch('/api/users');
    return response.json();
}

function loadTable(users){
    const table = document.querySelector('#result');
    for(let user of users){
        table.innerHTML += `<tr>
            <td>${user.id}</td>
            <td>${user.username}</td>
        </tr>`;
    }
}

async function main(){
    const users = await getUserData();
    loadTable(users);
}

//for Parallax effect
document.addEventListener('DOMContentLoaded', () =>{
    const eff = document.querySelectorAll('.parallax');
    M.Parallax.init(eff, {});
});

main();