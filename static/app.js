document.getElementById("moodForm").addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent form submission

    const mood = document.getElementById("mood").value;
    const stressLevel = document.getElementById("stressLevel").value;

    // Display response
    const responseMessage = document.getElementById("responseMessage");
    responseMessage.textContent = `Thank you for your input. You are feeling ${mood} with a stress level of ${stressLevel}/10.`;

    // Send data to server
    fetch('/submitMood', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            mood: mood,
            stressLevel: stressLevel
        })
    })
    .then(response => response.json())
    .then(data => console.log('Mood data submitted:', data))
    .catch(error => console.error('Error submitting mood data:', error));
});
