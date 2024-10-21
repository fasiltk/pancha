window.addEventListener('DOMContentLoaded', function() {
    if (document.getElementById('alert-flag').value === 'true') {
        alert('Check your mail');
    }
});



document.addEventListener("DOMContentLoaded", function () {
    const passwordInput = document.getElementById("password");
    const confirmPasswordInput = document.getElementById("confirmPassword");
    const submitButton = document.getElementById("submit");

    // Function to validate password
    function validatePassword(password) {
        // Password must contain at least one numeric digit
        const hasNumber = /\d/.test(password);
        // Password must contain at least one uppercase letter
        const hasUppercase = /[A-Z]/.test(password);
        // Password must contain at least one lowercase letter
        const hasLowercase = /[a-z]/.test(password);
        // Password must contain at least one special character
        const hasSpecialChar = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+/.test(password);

        return hasNumber && hasUppercase && hasLowercase && hasSpecialChar;
    }

    // Function to check if passwords match
    function passwordsMatch() {
        return passwordInput.value === confirmPasswordInput.value;
    }

    // Function to handle form submission
    function handleSubmit(event) {
        if (!validatePassword(passwordInput.value)) {
            alert("Password must contain at least one numeric digit, one uppercase letter, one lowercase letter, and one special character.");
            event.preventDefault();
        } else if (!passwordsMatch()) {
            alert("Passwords do not match. Please re-enter.");
            event.preventDefault();
        }
    }

    // Add event listener for form submission
    submitButton.addEventListener("click", handleSubmit);
});