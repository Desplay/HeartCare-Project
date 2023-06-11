const socket = new WebSocket("ws://" + window.location.host + "/ws/doctor-room/");

var DataTempOnDoctorRoom = [];

const refresh = (dataPatients) => {
    const table = document.getElementById("dataTable").getElementsByTagName("tbody")[0];
    if (dataPatients.length === 0) {
      document.getElementById("TablePatients").style.display = "none";
      return
    }
    else document.getElementById("TablePatients").style.display = "block";
    table.innerHTML = "";
    dataPatients.map((element, index) => {
      let Row = document.createElement("tr");
  
      let Number = document.createElement("td");
      Number.textContent = index + 1;
  
      let PhyID = document.createElement("td");
      PhyID.textContent = element.PhyID;

      let Name = document.createElement("td");
      Name.textContent = element.name;
  
      let Age = document.createElement("td");
      Age.textContent = element.age;
  
      let Gender = document.createElement("td");
      Gender.textContent = element.gender.value;
  
      let Date = document.createElement("td");
      Date.textContent = element.date;
  
      let Disease = document.createElement("td");
      Disease.textContent = element.disease.name;
  
      let Message = document.createElement("td");
      Message.textContent = element.message;
  
      let Treat = document.createElement("td");
  
      Row.appendChild(Number);
      Row.appendChild(PhyID);
      Row.appendChild(Name);
      Row.appendChild(Age);
      Row.appendChild(Gender);
      Row.appendChild(Date);
      Row.appendChild(Disease);
      Row.appendChild(Message);
      Row.appendChild(Treat)
      table.appendChild(Row);
    });
  
    let firstRows = table.rows.item(0).getElementsByTagName("td");
    firstRows.item(firstRows.length-1).textContent = "Now treating";
    for(let i = 0; i < firstRows.length; i++) {
      firstRows.item(i).style.fontWeight = "bold";
      firstRows.item(i).style.color = "red";
    }
  };

function sendEvent() {
  const params = new URLSearchParams(window.location.search);
  
  const event = {
    'method': 'SyncDoctorRoom',
    'data': params.get("ID"),
  };
  socket.send(JSON.stringify(event));
}

socket.onopen = function (event) {
  sendEvent();
};

socket.onmessage = function (event) {
  var data = JSON.parse(event.data).Queue;
  if(DataTempOnDoctorRoom.length === 0)
    refresh(data);
    
  if(DataTempOnDoctorRoom.length === 0 && data.length !== 0) {
    DataTempOnLobby = data;
    refresh(data);
  }
  data.forEach(element => {
    if(DataTempOnDoctorRoom.findIndex(x => x.IDCode === element.IDCode) === -1) {
      DataTempOnDoctorRoom = data;
      refresh(data);
    }
  });
  sendEvent();
};

