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
        <form onSubmit = {handleSubmit} className = "bg-slate-800 p-6 rounded-xl shadow-lg border border-slate-700 flex gap-4">
            <input
            type = "text"
            value = {action}
            onChange = {(e) => setAction(e.target.value)}
            placeholder = "New Task"
            className = "flex-1 bg-slate-900 text-white px-4 py-2 rounded-lg border border-slate-600 focus:outline-none focus:border-indigo-500 transition"
            /> 
            <button type = "submit"
                    className = "bg-indigo-600 hover:bg-indigo-500 text-white font-bold py-2 px-6 rounded-lg transition shadow-md" 
            >Add Task</button>
        
        </form>
    );
}
export default TaskForm
