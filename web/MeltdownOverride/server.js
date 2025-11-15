const express = require('express');
const cors = require('cors');
const sqlite3 = require('sqlite3').verbose();
const app = express();

app.use(cors());
app.use(express.json());
app.use(express.static('public'));

const db = new sqlite3.Database(':memory:');

db.serialize(() => {
    db.run(`CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT,
        role TEXT,
        clearance TEXT,
        notes TEXT
    )`);

    const stmt = db.prepare('INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)');
    stmt.run(1, 'engineer', 'jO*#$&T%Opilfujsdbpifsdujbf320984023984-032198', 'Lead Engineer', 'Level 3', 'CTF{C0R3_0V3RH34T_D3T3CT3D}');
    stmt.finalize();
});

app.post('/api/login', (req, res) => {
    const { username, password } = req.body;

    console.log(`Login attempt: username="${username}", password="${password}"`);

    const query = `SELECT * FROM users WHERE username = '${username}' AND password = '${password}'`;

    console.log(`Executing query: ${query}`);

    db.all(query, [], (err, rows) => {
        if (err) {
            console.error('Query error:', err.message);
            return res.json({
                success: false,
                temperature: 75,
                message: 'Access denied - Cooling systems stable\n\nQuery error occurred.',
                users: []
            });
        }

        if (rows.length === 0) {
            return res.json({
                success: false,
                temperature: 75,
                message: 'Access denied - Cooling systems stable\n\nAuthentication failed. No matching records found.',
                users: []
            });
        }

        console.log(`SQL Injection successful! Returned ${rows.length} users`);

        return res.json({
            success: true,
            temperature: 9999,
            message: '🔥 LOGIN SUCCESSFUL!\n\nYOU WERE TOO LATE - MELTDOWN HAS STARTED!',
            users: rows
        });
    });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, '0.0.0.0', (error) => {
    if (error) {
        throw error;
    }

    console.log(`🔥 Meltdown Override running on port ${PORT}`);
});
