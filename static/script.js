document.addEventListener("DOMContentLoaded", () => {
  const input = document.getElementById("user-input");
  input.addEventListener("keypress", function(e) {
    if (e.key === "Enter") {
      sendMessage();
    }
  });
});

async function sendMessage() {
  const input = document.getElementById("user-input");
  const chat = document.getElementById("chat");
  const message = input.value.trim();

  if (message === "") return;

  // Display user message
  chat.innerHTML += `<div class="message user">${message}</div>`;
  input.value = "";

  try {
    const res = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message })
    });

    const data = await res.json();
    chat.innerHTML += `<div class="message bot">${data.reply}</div>`;
    chat.scrollTop = chat.scrollHeight;

  } catch (err) {
    chat.innerHTML += `<div class="message bot">⚠️ Error: ${err.message}</div>`;
  }
}
