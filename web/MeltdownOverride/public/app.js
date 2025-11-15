let temperature = 75;

function updateTemperature(newTemp) {
    temperature = newTemp;
    const tempValue = document.getElementById('tempValue');
    const flameIcon = document.getElementById('flameIcon');
    const body = document.body;

    tempValue.textContent = temperature + '°C';
    tempValue.className = 'temp-value';

    if (temperature > 1000) {
        tempValue.classList.add('temp-critical');
        flameIcon.classList.add('critical');
        body.classList.add('meltdown');
    }
}

function displayUserData(users) {
    let html = '';
    let flagFound = false;

    users.forEach((user) => {
        html += `<div class="user-data">
            <div class="user-data-title">USER RECORD #${user.id}</div>
            <div class="user-field"><span>Username:</span> ${user.username}</div>
            <div class="user-field"><span>Role:</span> ${user.role}</div>
            <div class="user-field"><span>Clearance:</span> ${user.clearance}</div>
            <div class="user-field"><span>Notes:</span> ${user.notes}</div>`;
    });

    return { html, flagFound };
}

function showResult(message, users = []) {
    const resultBox = document.getElementById('resultBox');
    const resultText = document.getElementById('resultText');
    const userData = document.getElementById('userData');

    resultText.textContent = message;

    if (users.length > 0) {
        const { html, flagFound } = displayUserData(users);
        userData.innerHTML = html;

        if (flagFound) {
            resultBox.classList.add('critical');
        }
    } else {
        userData.innerHTML = '';
    }

    resultBox.className = 'result-box show';
}

document.getElementById('loginForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const submitBtn = document.getElementById('submitBtn');

    submitBtn.disabled = true;
    submitBtn.textContent = 'Processing...';

    try {
        const response = await fetch('/api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });

        const data = await response.json();

        updateTemperature(data.temperature);

        showResult(data.message, data.users);

    } catch (error) {
        showResult('❌ Error: Could not connect to reactor control system');
    } finally {
        submitBtn.disabled = false;
        submitBtn.textContent = '🚨 Emergency Access';
    }
});
