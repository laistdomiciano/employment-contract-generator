document.addEventListener('DOMContentLoaded', function() {
    // Handle Signup Form Validation
    const signupForm = document.querySelector('form[action="/signup"]');
    if (signupForm) {
        signupForm.addEventListener('submit', function(event) {
            const password1 = document.getElementById('password1').value;
            const password2 = document.getElementById('password2').value;
            const errorElement = document.getElementById('signup-message');

            if (password1 !== password2) {
                event.preventDefault();
                errorElement.textContent = "Passwords do not match.";
                return false;
            }
            errorElement.textContent = "";
        });
    }

    // Handle Login Form Validation
    const loginForm = document.querySelector('form[action="/login"]');
    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            const errorElement = document.getElementById('login-message');

            if (!username || !password) {
                event.preventDefault();
                errorElement.textContent = "Both fields are required.";
                return false;
            }
            errorElement.textContent = "";
        });
    }

    // Handle Dynamic Content for Contract Creation
    const contractLinks = document.querySelectorAll('.dashboard-container a');
    if (contractLinks.length) {
        contractLinks.forEach(link => {
            link.addEventListener('click', function(event) {
                event.preventDefault();
                const contractType = this.getAttribute('href').split('=')[1];
                showContractForm(contractType);
            });
        });
    }

    function showContractForm(contractType) {
        // Fetch the appropriate form or show a modal for contract creation
        fetch(`/contract_form?type=${contractType}`)
            .then(response => response.text())
            .then(html => {
                const formContainer = document.createElement('div');
                formContainer.innerHTML = html;
                document.body.appendChild(formContainer);

                // Optionally, you can handle form submission here
                const contractForm = document.querySelector('form#contract-form');
                if (contractForm) {
                    contractForm.addEventListener('submit', function(event) {
                        event.preventDefault();
                        const formData = new FormData(contractForm);
                        fetch('/create_contract', {
                            method: 'POST',
                            body: formData
                        })
                        .then(response => response.json())
                        .then(data => {
                            if (data.pdf_path) {
                                alert(`Contract created successfully! Download it <a href="${data.pdf_path}" target="_blank">here</a>.`);
                            } else {
                                alert('An error occurred while creating the contract.');
                            }
                        });
                    });
                }
            })
            .catch(error => console.error('Error fetching contract form:', error));
    }
});




