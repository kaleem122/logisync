import {useState} from "react"


function TaskCard(props) {
    const[currentStatus, setCurrentStatus] = useState(props.status);

    function markAsDone(){
        setCurrentStatus("completed");
    }
    return (
        <div className = "bg-slate-800 p-6 rounded-xl shadow-lg border border-slate-700 hover:scale-105 transition duration-300">
            <h2 className = "text-xl font-bold text-white mb-2">{props.action}</h2>
            <p className = "text-slate-400 mb-4">Status: {currentStatus}</p>
            <button onClick={markAsDone} className = "bg-indigo-600 hover:bg-indigo-500 text-white font-medium py-2 px-4 rounded-lg transition">Mark as Done</button>

        </div>
    )
}
export default TaskCard;