// Scroll to specific section
function scrollToSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (section) {
        section.scrollIntoView({ behavior: 'smooth' });
    }
}

document.getElementById("register-form").addEventListener("submit", function(event) {
    event.preventDefault();  // Prevent form from submitting normally

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;

    if (name && email) {
        alert("Thank you for registering, " + name + "!");
        // You can add code here to actually send the form data to your server.
    } else {
        alert("Please fill in all fields.");
    }
});
