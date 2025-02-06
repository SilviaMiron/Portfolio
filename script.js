document.querySelectorAll('.icon').forEach(icon => {
  icon.addEventListener('click', function () {
      window.open(this.href, '_blank');
      });
  });


  document.getElementById("contactForm").addEventListener("submit", async function(event) {
    event.preventDefault(); // Prevent default form submission
 
    let formData = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        message: document.getElementById("message").value
    };
 
    let responseMessage = document.getElementById("responseMessage");
 
    try {
        let response = await fetch("http://127.0.0.1:5000/send_email", {
            method: "POST",
            headers: { 
              "Content-Type": "application/json"
          },
            body: JSON.stringify(formData)
        });
 
        let result = await response.json();
        responseMessage.textContent = result.message;
 
        if (response.ok) {
            responseMessage.style.color = "green";
            document.getElementById("contactForm").reset();
            alert("Thank you for reaching out! I'll get back to you soon.");  // Show alert after successful submission
        } else {
            responseMessage.style.color = "red";
        }
    } catch (error) {
        responseMessage.textContent = "Error sending message. Try again later.";
        responseMessage.style.color = "red";
    }
 
  });