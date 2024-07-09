const loginForm = document.getElementById('login-form');
        const registerForm = document.getElementById('register-form');
        
        const loginLink = document.getElementById('login-link');
        const registerLink = document.getElementById('register-link');
        
        registerForm.style.display = 'none';
        
        loginLink.addEventListener('click', () => {
            loginForm.style.display = 'block';
            registerForm.style.display = 'none';
        });
        
        registerLink.addEventListener('click', () => {
            loginForm.style.display = 'none';
            registerForm.style.display = 'block';
        });