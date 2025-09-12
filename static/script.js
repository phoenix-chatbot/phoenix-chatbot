document.addEventListener("DOMContentLoaded", () => {
  const input = document.getElementById("user-input");
  const sendBtn = document.getElementById("send-btn");
  const chatBox = document.getElementById("chat-box");

  function appendMessage(sender, message) {
    const msgDiv = document.createElement("div");
    msgDiv.className = sender === "You" ? "user-msg" : "bot-msg";
    msgDiv.textContent = message;
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
  }

  async function sendMessage() {
    const message = input.value.trim();
    if (!message) return;

    appendMessage("You", message);
    input.value = "";

    const res = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message })
    });

    const data = await res.json();
    appendMessage("Bot", data.reply);
  }

  sendBtn.addEventListener("click", sendMessage);
  input.addEventListener("keypress", (e) => {
    if (e.key === "Enter") sendMessage();
  });
});
