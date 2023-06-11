const socket = new WebSocket("ws://" + window.location.host + "/ws/lobby/");

var DataTempOnLobby = [];

const refresh = (data) => {
  const table = document.getElementById("dataTable").getElementsByTagName("tbody")[0];
  if (data.length === 0) document.getElementById("TablePatients").style.display = "none";
  else document.getElementById("TablePatients").style.display = "block";
  table.innerHTML = "";
  data.map((element, index) => {
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
};

function sendEvent() {
  const event = {
    'method': 'SyncLobby',
    'data': DataTempOnLobby
  };
  socket.send(JSON.stringify(event));
}

socket.onmessage = function (event) {
  var data = JSON.parse(event.data);
  console.log(data);
  if(DataTempOnLobby.length === 0 || data.length === 0)
    refresh(data);
    
  if(DataTempOnLobby.length === 0 && data.length !== 0) {
    DataTempOnLobby = data;
    refresh(data);
  }
  data.forEach(element => {
    if(DataTempOnLobby.findIndex(x => x.IDCode === element.IDCode) === -1) {
      DataTempOnLobby = data;
      refresh(data);
    }
  });
  sendEvent();
};

