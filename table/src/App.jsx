import React, { useEffect, useState } from "react";

function App() {
  const [users, setUsers] = useState([]);
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");

  const fetchUsers = async () => {
    const res = await fetch("http://127.0.0.1:5000/users");
    const data = await res.json();
    setUsers(data);
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  const addUser = async () => {
    await fetch("http://127.0.0.1:5000/users", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, email }),
    });
    fetchUsers();
  };

  const deleteUser = async (id) => {
    await fetch(`http://127.0.0.1:5000/users/${id}`, {
      method: "DELETE",
    });
    fetchUsers();
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>User Management</h2>
      <input placeholder="Name" onChange={(e) => setName(e.target.value)} />
      <input placeholder="Email" onChange={(e) => setEmail(e.target.value)} />
      <button onClick={addUser}>Add</button>

      <table border="1">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Delete</th>
          </tr>
        </thead>
        <tbody>
          {users.map((u) => (
            <tr key={u[0]}>
              <td>{u[0]}</td>
              <td>{u[1]}</td>
              <td>{u[2]}</td>
              <td>
                <button onClick={() => deleteUser(u[0])}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;