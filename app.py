html1="""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@400..800&family=Baloo+Bhai+2:wght@400..800&display=swap" rel="stylesheet">
    <style>
        /* utilities start */
        body {
            overflow-x: hidden;
	    font-family: "Baloo Bhai 2", sans-serif;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            /* Ensures padding and borders are included in the width and height */
        }

        .icon {
            width: 35px;
            height: 35px;
            object-fit: cover;
            margin: 0;
        }

        .icon.dot {
            width: 20px;
            margin-top: 2px;
        }

        /* utilities end */
        .chtscont {}

        .allheads {
            color: teal;
            position: fixed;
            top: 0;
            z-index: 10;
            font-weight: 700;
            width: 100vw;
            padding: 10px;
            border-bottom: 1px solid #e5e5e5;
            font-size: 2rem;
            background-color: #ffffff;
        }

        .chtsicons {
            display: flex;
            width: 70vw;
            justify-content: flex-end;
        }

        main {
            position: relative;
            top: 55px;
            overflow-y: auto;
            /* Allow vertical scrolling */
            height: calc(100vh - 80px);
            /* Ensure it fills the viewport */
        }

        .activenav {
            border-top: 3px solid #D8FD99;
        }

        .friend {
            display: flex;
            flex-direction: row;
            width: 100vw;
            position: relative;
            /* Added position relative for proper alignment of time */
        }

        .frname {
            font-weight: 500;
            font-size: 17px;
            margin-top: 10px;
            display: flex;
        }

        .lastmsg {
            margin-top: 4px;
            margin-left: 3px;
        }

        .time {
            position: absolute;
            right: 10px;
            /* Position the time on the right side */
            top: 10px;
            /* Adjust the vertical position */
            font-weight: 500;
            font-size: 13px;
            color: #6A7074;
        }

        img.frprofile {
            padding: 10px;
            width: 70px;
            /* Keep the profile image size unchanged */
            height: 70px;
            object-fit: cover;
            border-radius: 50%;
        }

        .friends {
            display: flex;
            flex-direction: column;
            border-bottom: 1px solid #e5e5e5;
            margin-bottom: 40vh;
            gap: 5px;
            margin-top: 20px;
        }

        .add-user-btn {
            background-color: #25D366;
            color: #fff;
            padding: 10px;
            border: none;
            border-radius: 50%;
            cursor: pointer;
            margin-bottom: 20px;
            transition: background-color 0.3s ease;
            font-size: 24px;
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 50px;
            height: 50px;
        }

        .add-user-btn:hover {
            background-color: #128C7E;
        }

        .user-form {
            display: none;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            padding: 20px;
            width: calc(100% - 60px);
            position: absolute;
            top: 50%;
            animation: expandForm 0.5s ease;
            transition: opacity 0.5s ease;
            opacity: 0;
            margin: 10px;
        }

        .user-form input {
            width: calc(100% - 10px);
            margin-bottom: 10px;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            transition: all 0.3s ease;
            animation: placeholderAnim 1.5s infinite;
        }

        .user-form input:focus {
            border-color: #25D366;
            box-shadow: 0 0 5px #25D366;
        }

        .user-form input::placeholder {
            color: #888;
            transition: color 0.5s ease;
        }

        .user-form input:focus::placeholder {
            color: transparent;
        }

        .user-form button {
            background-color: #075e54;
            color: #fff;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        .user-form button:hover {
            background-color: #128C7E;
        }

        @keyframes expandForm {
            from {
                opacity: 0;
                transform: scale(0);
            }

            to {
                opacity: 1;
                transform: scale(1);
            }
        }

        @keyframes placeholderAnim {
            0% {
                transform: translateY(0);
            }

            50% {
                transform: translateY(-8px);
            }

            100% {
                transform: translateY(0);
            }
        }

        input {
            outline: none;
        }

        #close {
            color: black;
            font-size: 16px;
            position: relative;
            left: 90%;
            background-color: transparent;
        }

        .user-form button:hover {
            background-color: #128C7E;
        }

        span {
            letter-spacing: 6px;
        }

        .error {
            margin-bottom: 15px;
        }

        .name {
            position: fixed;
            /* Fixed position to keep it at the bottom right */
            bottom: 10px;
            /* Space from the bottom */
            right: 10px;
            /* Space from the right */
            font-size: 16px;
            /* Adjust the font size */
            color: #333;
            /* Set the text color */
            background-color: #ffffff;
            /* Background color */
            padding: 5px;
            /* Padding around the text */
            border-radius: 5px;
            /* Rounded corners */
            box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
            /* Optional shadow for better visibility */
            cursor: move;
            /* Cursor indicates draggable */
            width: 100px;
            /* Fixed width */
            height: 40px;
            /* Fixed height */
            display: flex;
            /* Flexbox for centering text */
            align-items: center;
            /* Vertically center the text */
            justify-content: center;
            /* Horizontally center the text */
            text-align: center;
            /* Center the text */
            z-index: 20;
        }
	.link{
       color:blue;
       }
    </style>
    
    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.7.5/socket.io.js"></script>
</head>

<body>
    <header class="allheads">
        <div class="whtsname">
            Talkup...
        </div>
    </header>

    <main id="friendsList">
        <div class="friends">
            {% for d in data %}
     <div class="friend" onclick="go_Tochat('{{ d[0] }}')">
        <img class="frprofile" src="https://drive.google.com/uc?export=view&id=12NR8OO1L9vFY7ucwi2ZP4Z67MmWZrUm_" >
        <div class="frinfo">
            <div class="frname">
                {{ d[0] }}
                <div class="time">
                    {{ d[2] }}
                </div>
            </div>  
            <div class="lastmsg">
	       {% if d[1]|length >= 20 %}
                 {{ d[1][:20]+"....." }}
	       {% else  %}
                 {{ d[1] }}
	       {% endif %}
             </div> 
        </div>
    </div>
 {% endfor %}

        </div>


        <button class="add-user-btn" onclick="showForm()">+</button>
        <div class="user-form" id="userForm">
            <button id="close" class="close-btn" onclick="closeForm()">&times;</button>
            <div>
                <input type="text" placeholder="Enter number" id="f_number" required>
                <span id="error" class="error"></span><br><br>
                <button onclick="add_friend()">Add</button>
            </div>
        </div>
    </main>

    <div class="name" id="movableName">
        {{ u_number }} 
    </div>

    <script>
        var u = "{{ u_number }}";
        var socket = io();

        function go_Tochat(d) {
            window.location.href = `/chat/${d}`;
        }

        function add_friend() {
            var data = {
                u_number: u,
                f_number: document.getElementById("f_number").value
            };
            socket.emit("add", data);
            document.getElementById("f_number").value = "";
            document.getElementById("error").textContent = "";
        }

        function showForm() {
            var form = document.getElementById("userForm");
            form.style.display = "block";
            setTimeout(function() {
                form.style.opacity = 1;
            }, 100);
        }

        function closeForm() {
            var form = document.getElementById("userForm");
            form.style.opacity = 0; // Fade out the form
            setTimeout(function() {
                form.style.display = "none"; // Hide the form after fading out
            }, 500);
            document.getElementById("f_number").value = "";
            document.getElementById("error").textContent = "";
        }

        socket.on("not_found", function(data) {
            document.getElementById("error").textContent = data;
        });

        socket.on("redirect", function() {
            window.location.reload();
            window.location.href = "/";
        });
    </script>




    <script>
        const movableName = document.getElementById('movableName');
        const friendsList = document.getElementById('friendsList');

        let offsetX, offsetY;
        let isDragging = false;

        movableName.addEventListener('mousedown', (e) => {
            isDragging = true;
            offsetX = e.clientX - movableName.getBoundingClientRect().left;
            offsetY = e.clientY - movableName.getBoundingClientRect().top;

            // Prevent scrolling of the friends list while dragging
            friendsList.style.overflow = 'hidden';

            document.addEventListener('mousemove', moveName);
        });

        document.addEventListener('mouseup', () => {
            isDragging = false;
            friendsList.style.overflow = 'auto'; // Allow scrolling again
            document.removeEventListener('mousemove', moveName);
        });

        function moveName(e) {
            if (isDragging) {
                let newX = e.clientX - offsetX;
                let newY = e.clientY - offsetY;

                // Constrain the position within the viewport
                const viewportWidth = window.innerWidth;
                const viewportHeight = window.innerHeight;

                const nameWidth = movableName.offsetWidth;
                const nameHeight = movableName.offsetHeight;

                // Ensure the name div stays within the viewport
                if (newX < 0) newX = 0;
                if (newX + nameWidth > viewportWidth) newX = viewportWidth - nameWidth;
                if (newY < 0) newY = 0;
                if (newY + nameHeight > viewportHeight) newY = viewportHeight - nameHeight;

                movableName.style.left = `${newX}px`;
                movableName.style.top = `${newY}px`;
                movableName.style.position = 'fixed'; // Keep the position fixed while dragging
            }
        }

        // Touch support for mobile devices
        movableName.addEventListener('touchstart', (e) => {
            isDragging = true;
            const touch = e.touches[0];
            offsetX = touch.clientX - movableName.getBoundingClientRect().left;
            offsetY = touch.clientY - movableName.getBoundingClientRect().top;

            // Prevent scrolling of the friends list while dragging
            friendsList.style.overflow = 'hidden';

            document.addEventListener('touchmove', moveNameTouch);
        });

        document.addEventListener('touchend', () => {
            isDragging = false;
            friendsList.style.overflow = 'auto'; // Allow scrolling again
            document.removeEventListener('touchmove', moveNameTouch);
        });

        function moveNameTouch(e) {
            if (isDragging) {
                const touch = e.touches[0];
                let newX = touch.clientX - offsetX;
                let newY = touch.clientY - offsetY;

                // Constrain the position within the viewport
                const viewportWidth = window.innerWidth;
                const viewportHeight = window.innerHeight;

                const nameWidth = movableName.offsetWidth;
                const nameHeight = movableName.offsetHeight;

                // Ensure the name div stays within the viewport
                if (newX < 0) newX = 0;
                if (newX + nameWidth > viewportWidth) newX = viewportWidth - nameWidth;
                if (newY < 0) newY = 0;
                if (newY + nameHeight > viewportHeight) newY = viewportHeight - nameHeight;

                movableName.style.left = `${newX}px`;
                movableName.style.top = `${newY}px`;
                movableName.style.position = 'fixed'; // Keep the position fixed while dragging
            }
        }
    </script>
</body>

</html>
"""

html = """
<!DOCTYPE
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Class 10 Facebook</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="google-site-verification" content="sKP4alsXsHG6lsdaSyAEvSi1PgLGpTITHkd6UvzOyJU" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@400..800&family=Baloo+Bhai+2:wght@400..800&display=swap" rel="stylesheet">

  <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.7.5/socket.io.js"></script>
  <style>
:root {
    --body-color: #f0f4f9;
    --header-bg: linear-gradient(45deg, white, gray);
    --you-bg: #C6E7FF;
    /* Light green background for user's messages */
    --friend-bg: #FFF6E9;
    /* White background for friend's messages */
  }

    body {
      background-color: var(--body-color);
      margin: 0;
      font-family: Arial, sans-serif;
      display: flex;
      flex-direction: column;
      height: 100vh;
      font-family: "Baloo Bhai 2", sans-serif;
    }

    .header {
      box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.4);
      padding: 10px;
      background-image: var(--header-bg);
      position: sticky;
      top: 0;
      display: flex;
      align-items: center;
      z-index: 1;
    }

    .friend-profile {
      width: 40px;
      height: 40px;
      border-radius: 50%;
      margin-right: 10px;
    }

    .friend-name {
      font-size: 20px;
      font-weight: bold;
    }

    .chat {
      flex: 1;
      overflow-y: auto;
      padding: 10px;
      margin-bottom: 60px;
      /* Footer height + some padding */
    }

    .message {
      display: flex;
      flex-direction: column;
      margin-bottom: 20px;
      overflow-wrap: break-word;
    }

    .you {
      align-self: flex-end;
    }

    .friend {
      align-self: flex-start;
    }

    .message-content {
      display: flex;
      flex-direction: column;
      box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
      border-radius: 15px;
      padding: 10px;
      max-width: 70%;
      word-break: break-word;
      margin-bottom: 3px;
      margin: 0,2px,0,2px;
      background-color: var(--friend-bg);
    }

    .message-content.you {
      color: white;
      color: #a07855ff;
      background-color: var(--you-bg);
    }
    .message-content.friend {
      color: #a07855ff;
      background-color: var(--friend-bg);
      align-items: flex-end;
    }

    footer {
      display: flex;
      align-items: center;
      background-color: white;
      padding: 10px;
      position: fixed;
      bottom: 0;
      width: 100%;
      box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }

    .input-box {
      flex: 1;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 20px;
      outline: none;
      margin-right: 10px;
      font-size: 16px;
    }

    .send {
      background-color: #ce4a7eff;
      border: none;
      border-radius: 10%;
      padding: 10px;
      box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
      cursor: pointer;
    }

    .send i {
      font-size: 18px;
      color: gray;
      margin-right: 10px;
    }

    .send:hover {
      animation: an1 0.3s;
    }

    @keyframes an1 {
      0% {
        transform: rotate(0deg);
      }
      50% {
        transform: rotate(180deg);
      }
      100% {
        transform: rotate(0deg);
      }
    }

    .scroll-button {
      display: none;
      position: fixed;
      bottom: 80px;
      /* Adjusted for better positioning */
      right: 20px;
      background-color: #f7ced7ff;
      border: none;
      border-radius: 50%;
      padding: 15px;
      box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
      cursor: pointer;
      z-index: 1;

    }

    .scroll-button i {
      font-size: 18px;
      color: #6e4c1eff;

    }
    .date {
      font-size: 10px;
      color: gray;
    }
    .date span {
      font-size: 15px;
      margin: 2px;
    }
  </style>
</head>
<body>
  <div class="header">
    <img class="friend-profile" src="">
    <label class="friend-name">{{ f_number }}</label>
  </div>
  <div id="chat" class="chat">
    {% for j in chats %}
    <div class='message'>
      <div class="message-content {{j[0]}}">
            {% if j[1].startswith('http://') or j[1].startswith('https://') %}
               <a href="{{ j[1] }}" target="_blank"> {{ j[1] }} </a>
            {% else %}
               {{ j[1] }}
            {% endif %}
	
        <div class="date">
          {{j[2][0]}} <br>{{j[2][1]}}
        </div>
      </div>
    </div>
    
    {% endfor %}
  </div>
  <footer>
    <input class="input-box" placeholder="Message" id="message_input" type="text">
    <button class="send" id="sendbtn">
      <i class="fas fa-paper-plane"></i>
    </button>
  </footer>
  <button id="scrollButton" class="scroll-button" onclick="scrollToBottom()">
    <i class="fas fa-arrow-down"></i>
  </button>
  <script>
    var f = "{{ f_number }}";
    var u = "{{ u_number }}";
    var socket = io();
    var chat = document.getElementById('chat');
    var scrollButton = document.getElementById('scrollButton');
    var messageInput = document.getElementById('message_input');

   function isValidURL(string) {
    try {
      new URL(string);
     return true;
      } catch (_) {
      return false;
     }
    }
    
    function sendMessage() {
      event.preventDefault();
      var message = messageInput.value.trim();
      if (message === "") {
        return;
      }
      var data = {
        message: message,
        f_number: f,
        u_number: u
      };
      socket.emit('send_message', data);
    }

    function addMessage(message) {
      var messageDiv = document.createElement("div");
      let mes;
      if ( isValidURL(message.message)){
        mes = `<a href="${message.message}" target ="_blank"> ${message.message} </a>   `
      } else {
        mes = `${message.message}`
      }
      
      messageDiv.classList.add("message");
      messageDiv.innerHTML = `
      <div class="message-content friend">
      ${mes}
      <div class="date">
      ${message.date} <br>${message.time}
      </div>
      </div>
      `;
      chat.appendChild(messageDiv);
      showScrollButtonIfNeeded();
    }

    function scrollToBottom() {
      chat.scrollTop = chat.scrollHeight;
    }

    function showScrollButtonIfNeeded() {
      if (chat.scrollTop + chat.clientHeight < chat.scrollHeight - 1) {
        scrollButton.style.display = 'block';
      } else {
        scrollButton.style.display = 'none';
      }
    }

    messageInput.addEventListener('keyup', function(event) {
      if (event.key === 'Enter') {
        sendMessage();
      }
    });

    document.getElementById("sendbtn").addEventListener("click", sendMessage);

    document.getElementById("scrollButton").addEventListener("click", scrollToBottom);

    socket.emit('join_room', {
      u_number: u,
      f_number: f
    });

    socket.on("date_time", function(date_time) {
      var messageDiv = document.createElement("div");
      let message= date_time.message;
      let tag ;
      if (isValidURL(message)){
          tag = `<a href="${message} target="_blank"> ${message}</a>`
      }else{
          tag = `${message}`
      }
      messageDiv.classList.add("message");
      messageDiv.innerHTML = `
      <div class="message-content you">
      ${tag}
      <div class="date">
      ${date_time.date} <br>${date_time.time}
      </div>
      </div>
      `;
      chat.appendChild(messageDiv);
      messageInput.value = '';
      scrollToBottom();
    });

    socket.on('receive_message', function(message) {
      addMessage(message);
    });

    chat.addEventListener('scroll', function() {
      showScrollButtonIfNeeded();
    });

    messageInput.addEventListener('focus', function() {
      if (scrollButton.style.display !== 'none') {
        scrollButton.click();
      }
    });

    scrollToBottom();
  </script>
</body>

</html>
"""
from flask import Flask, render_template_string, request, session, redirect 
from flask_socketio import SocketIO, emit, join_room
from flask_cors import CORS
import random 
import nepali_datetime

app = Flask(__name__)
app.secret_key = "hbcguf FF for diff FjdjsjsjsjF ft f"
app.config['SESSION_TYPE'] = 'filesystem'
CORS(app)
sio = SocketIO(app)

rooms = [] 
used_numbers = set()
database = {}

def get_room_name(n1, n2):
    return str(int(n1) + int(n2))
	
def generate_number():
    global used_numbers
    while True:
        number = random.randint(10000000, 99999999)
        if number not in used_numbers:
            used_numbers.add(number)
            return "98" + str(number)

def get_date():
    nepali_dt = nepali_datetime.datetime.now()
    date = str(nepali_dt.date())
    time = str(nepali_dt.strftime('%I:%M %p'))
    return (date, time)
	
@app.route('/')
def index():
    session.permanent = True    		
    if session.get("number") is not None:
        number = session['number']
        if not (number in database):
            number = generate_number()
            session["number"] = number 
            database[number] = { "number": number, "friends": {} }
    else: 
        number = generate_number()
        session['number'] = number
        database[number] = { "number": number, "friends": {} }
    data = list(database[number]['friends'].keys())
    data = []
    for key in database[number]["friends"].keys():
        data.append( [ key , database[number]["friends"][key][-1][1] ,database[number]["friends"][key][-1][2][0] ] )
    return render_template_string(html1, data=data, u_number=number)

@app.route("/chat/<f_number>")
def chat(f_number):
    if not(session.get('number')):
        return redirect('/')
    u = session["number"]
    f = f_number
    if not (u in database and f in database):
        return redirect("/")
    chats = database[u]['friends'][f]
    return render_template_string(html, chats=chats, f_number=f, u_number=u)

@app.route("/alive")
def Alive():
    return f" Website Stopped from shutting down"
# For chatting 
@sio.on("join_room")
def handle_join(data):
    u = data["u_number"]
    f = data["f_number"]
    room = get_room_name(u, f)
    join_room(room)
    #("room joined", room)

@sio.on("send_message")
def handle_message(data):
    u = data["u_number"]
    f = data["f_number"]
    message = data["message"]
    #("m",message)
    dt = get_date()
    database[u]['friends'][f].append(("you", message, dt))
    database[f]["friends"][u].append(("friend", message, dt))
    date = {  "message": message , "date": dt[0], "time": dt[1] }
    #("\nreached\n")
    emit("date_time", date, sid=request.sid)
    message = { "message": message, "date": dt[0], "time": dt[1] }
    room_name = get_room_name(u, f)
    emit("receive_message", message, skip_sid=request.sid, room=room_name)

# For adding new friends 
@sio.on("add")
def add(data):
    u = data['u_number'].strip()
    f = data['f_number'].strip()
    u = str(u)
    f = str(f)
    if u == f:
        data = "This is your own number"
        emit("not_found", data, sid=request.sid)
        return 
    elif not f in database:
        data = "user not found"
        emit("not_found", data, sid=request.sid)
        return 
    if f in database:
        room_name = get_room_name(u, f)
        if not room_name in rooms:
            dt = get_date()
            database[u]['friends'][f] = [("you", "hi", dt)]
            database[f]['friends'][u] = [("friend", "hi", dt)]
            rooms.append(room_name)
            join_room(room_name)
            emit("redirect", sid=request.sid)

if __name__ == '__main__':

    sio.run(app, debug=True)
    
    
    
