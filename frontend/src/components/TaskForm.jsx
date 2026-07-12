import {useState} from 'react';

function TaskForm({onTaskAdded}) { 
    const [action, setAction] = useState("");

    function handleSubmit(event) { 
        event.preventDefault();

        fetch("http://localhost:8000/tasks", {
            method: "POST", 
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({action: action, status:"pending"})
        })
        .then(response => response.json())
        .then(data => {
            console.log("Success:", data);
            setAction("");

            onTaskAdded(data);
        
        })

    }
    

    return (
        <form onSubmit = {handleSubmit} style = {{margin: "10px"}}>
            <input
            type = "text"
            value = {action}
            onChange = {(e) => setAction(e.target.value)}
            placeholder = "New Task"
            /> 
            <button type = "submit">Add Task</button>
        
        </form>
    );
}
export default TaskForm
