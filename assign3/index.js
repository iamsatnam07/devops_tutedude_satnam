const button = document.getElementById("button");

button.addEventListener('click',(e)=>{
    e.preventDefault();
    console.log(e);

    const inputs = document.querySelectorAll('input');

    inputs.forEach((input) => {
        input.addEventListener('blur', () => { 
            validateInput(input);
        });
    });

    function validateInput(input) {
        const value = input.value.trim();
        
        // 1. Ensure required fields are not empty
        if (input.required && !value) {
            showError(input, "This field is required");
            return;
        }

        // 2. Validate based on input type
        switch(input.type) {
            case 'email':
            validateEmail(input, value);
            break;
            case 'number': // Changed from 'number' for phone inputs
            validatePhone(input, value);
            break;
            case 'password':
            validatePassword(input, value);
            break;
            default:
            // Other input types
            clearError(input);
        }
    }

    // Email validation
    function validateEmail(input, email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        
        if (!emailRegex.test(email)) {
            showError(input, "Please enter a valid email (e.g., user@example.com)");
        } else {
            clearError(input);
        }
    }

    // Phone validation (exactly 10 digits)
    function validatePhone(input, phone) {
        const phoneRegex = /^\d{10}$/;
        
        if (!phoneRegex.test(phone)) {
            showError(input, "Phone number must be exactly 10 digits");
        } else {
            clearError(input);
        }
        }

        // Password validation
        function validatePassword(input, password) {
        const errors = [];
        
        if (password.length < 8) {
            errors.push("at least 8 characters");
        }
        if (!/[A-Z]/.test(password)) {
            errors.push("one uppercase letter");
        }
        if (!/[a-z]/.test(password)) {
            errors.push("one lowercase letter");
        }
        if (!/\d/.test(password)) {
            errors.push("one number");
        }

        if (errors.length > 0) {
            showError(input, `Password must contain: ${errors.join(", ")}`);
        } else {
            clearError(input);
        }
    }

    // Helper functions
    function showError(input, message) {
        clearError(input); // Clear previous errors
        input.classList.add('invalid');
        
        let errorElement = input.nextElementSibling;
        if (!errorElement || !errorElement.classList.contains('error-message')) {
            errorElement = document.createElement('div');
            errorElement.className = 'error-message';
            input.parentNode.insertBefore(errorElement, input.nextSibling);
        }
        
        errorElement.textContent = message;
    }

    function clearError(input) {
        input.classList.remove('invalid');
        const errorElement = input.nextElementSibling;
        if (errorElement && errorElement.classList.contains('error-message')) {
            errorElement.remove();
        }
    }
})