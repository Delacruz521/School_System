
const API_URL = "http://127.0.0.1:8000/api/students/";

// LOAD STUDENTS
function loadStudents() {
    fetch(API_URL)
    .then(res => res.json())
    .then(data => {
        let table = document.getElementById("studentTable");
        table.innerHTML = "";

        data.forEach(s => {
            table.innerHTML += `
                <tr>
                    <td>${s.student_id}</td>
                    <td>${s.name}</td>
                    <td>
                        <button class="delete-btn" onclick="deleteStudent(${s.student_id})">
                            Delete
                        </button>
                    </td>
                </tr>
            `;
        });
    });
}

// ADD STUDENT
function addStudent() {
    let name = document.getElementById("name").value;

    fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ name: name })
    })
    .then(() => {
        document.getElementById("name").value = "";
        loadStudents();
    });
}

// DELETE STUDENT
function deleteStudent(id) {
    fetch(API_URL + id + "/", {
        method: "DELETE"
    })
    .then(() => loadStudents());
}

// INIT
loadStudents();
