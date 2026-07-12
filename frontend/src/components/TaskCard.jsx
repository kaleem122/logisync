import {useState} from "react"


function TaskCard(props) {
    const[currentStatus, setCurrentStatus] = useState(props.status);

    function markAsDone(){
        setCurrentStatus("completed");
    }
    return (
        <div style = {{border: "1px solid gray", margin: "10px", padding: "10px", borderRadius: "8px"}}>
            <h2>{props.action}</h2>
            <p>Status: {currentStatus}</p>
            <button onClick = {markAsDone}>Mark as Done</button>
        </div>
    )
}
export default TaskCard;