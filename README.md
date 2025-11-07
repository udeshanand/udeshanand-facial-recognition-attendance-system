
  <h1> Facial Recognition Attendance System (Flask)</h1>

  <p>
    A smart attendance management system built using <strong>Flask</strong> and <strong>Facial Recognition</strong>.  
    It allows users to register new faces, extract features, and mark attendance automatically based on live camera input.
  </p>

  <hr />

  <h2> Features</h2>
  <ul>
    <li>Register new users using a camera interface</li>
    <li>Extract facial features and store them in a CSV</li>
    <li>Automatically mark attendance using facial recognition</li>
    <li>View attendance records filtered by date</li>
    <li>SQLite database for attendance storage</li>
  </ul>

  <h2> Technologies Used</h2>
  <ul>
    <li><strong>Python 3</strong></li>
    <li><strong>Flask</strong> — web framework</li>
    <li><strong>SQLite</strong> — database for attendance logs</li>
    <li><strong>OpenCV</strong> and <strong>dlib</strong> — for face detection and recognition</li>
    <li><strong>HTML </strong> — for rendering templates</li>
  </ul>

  <h2>How It Works</h2>
  <ol>
    <li>User registers their face via webcam (using <code>get_faces_from_camera_tkinter.py</code>).</li>
    <li>Facial features are extracted and stored in a CSV file (<code>features_extraction_to_csv.py</code>).</li>
    <li>During attendance marking, the system captures live frames and matches faces (<code>attendance_taker.py</code>).</li>
    <li>The recognized faces are stored with timestamps in the SQLite database (<code>attendance.db</code>).</li>
    <li>The web interface allows viewing attendance data by date.</li>
  </ol>

 

  <h2> Application Routes</h2>

  <div class="endpoint">
    <h3>GET /</h3>
    <p>Renders the main dashboard (<code>index.html</code>), allowing date selection and displaying attendance data.</p>
  </div>

  <div class="endpoint">
    <h3>POST /attendance</h3>
    <p>Fetches attendance records from the database for a specific date.</p>
    <p><strong>Form field:</strong> <code>selected_date</code></p>
  </div>

  <div class="endpoint">
    <h3>POST /handle_action</h3>
    <p>Handles button actions from the UI.</p>
    <ul>
      <li><code>register</code> → Triggers face registration + feature extraction</li>
      <li><code>mark_attendance</code> → Runs attendance marking process</li>
    </ul>
  </div>

  <hr />


  <h2>Example Workflow</h2>
  <ol>
    <li>Start the Flask app.</li>
    <li>Click “Register” → System opens camera → Captures face → Saves data.</li>
    <li>Click “Mark Attendance” → Recognizes faces in real-time → Logs them in the database.</li>
    <li>Select a date → View attendance records.</li>
  </ol>

  <h2>Database Schema (attendance.db)</h2>
  <pre><code>CREATE TABLE attendance (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  date TEXT NOT NULL,
  time TEXT NOT NULL
);</code></pre>

  <h2>Limitations</h2>
  <ul>
    <li>Database is stored locally (no cloud integration yet).</li>
    <li>Facial recognition accuracy depends on lighting and camera quality.</li>
    <li>No user authentication implemented.</li>
  </ul>

  <h2> Future Enhancements</h2>
  <ul>
    <li>Integrate user authentication and roles</li>
    <li>Store data in cloud (e.g., Firebase or PostgreSQL)</li>
    <li>Add dashboard analytics and CSV export</li>
    <li>Improve accuracy using deep learning (DeepFace / FaceNet)</li>
  </ul>

 
