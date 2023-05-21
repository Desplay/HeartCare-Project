const socket = new WebSocket("ws://" + window.location.host + "/ws/lobby/");

var DataTemp;

const refresh = (data) => {
  const table = document.getElementById("dataTable").getElementsByTagName("tbody")[0];
  if (data.length === 0) document.getElementById("TablePatients").style.display = "none";
  else document.getElementById("TablePatients").style.display = "block";
  table.innerHTML = "";
  data.map((element, index) => {
    if (index < 3) {
      let Row = document.createElement("tr");

      let Number = document.createElement("td");
      Number.textContent = index + 1;

      let Name = document.createElement("td");
      let link = document.createElement("a");
      link.classList.add("_parent");
      let linkTitle = document.createTextNode(element.name);
      link.appendChild(linkTitle);
      link.title = element.name;
      link.href = "/edit-patient?ID=" + element.IDCode;
      Name.appendChild(link);

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

      Row.appendChild(Number);
      Row.appendChild(Name);
      Row.appendChild(Age);
      Row.appendChild(Gender);
      Row.appendChild(Date);
      Row.appendChild(Disease);
      Row.appendChild(Message);
      table.appendChild(Row);
    }
  });
};

function sendEvent() {
  const event = {
    'method': 'SyncLobby',
    'data': DataTemp
  };
  socket.send(event);
}

socket.onmessage = function (event) {
  var data = JSON.parse(event.data);
  if(DataTemp !== data)
    DataTemp = data;
    refresh(data);
  sendEvent();
};

