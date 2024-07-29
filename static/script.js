document.addEventListener('DOMContentLoaded', () => {
    const modeToggle = document.getElementById('mode-toggle');
    const body = document.body;
    const container = document.querySelector('.container');
    const h1 = document.querySelector('h1');
    const input = document.querySelector('input[type="text"]');
    const button = document.querySelector('button');
    const results = document.querySelectorAll('.result');

    // Check localStorage for dark mode preference
    if (localStorage.getItem('dark-mode') === 'enabled') {
        body.classList.add('dark-mode');
        container.classList.add('dark-mode');
        h1.classList.add('dark-mode');
        input.classList.add('dark-mode');
        button.classList.add('dark-mode');
        results.forEach(result => result.classList.add('dark-mode'));
        modeToggle.checked = true;
    }

    // Toggle dark mode
    modeToggle.addEventListener('change', () => {
        if (modeToggle.checked) {
            body.classList.add('dark-mode');
            container.classList.add('dark-mode');
            h1.classList.add('dark-mode');
            input.classList.add('dark-mode');
            button.classList.add('dark-mode');
            results.forEach(result => result.classList.add('dark-mode'));
            localStorage.setItem('dark-mode', 'enabled');
        } else {
            body.classList.remove('dark-mode');
            container.classList.remove('dark-mode');
            h1.classList.remove('dark-mode');
            input.classList.remove('dark-mode');
            button.classList.remove('dark-mode');
            results.forEach(result => result.classList.remove('dark-mode'));
            localStorage.setItem('dark-mode', 'disabled');
        }
    });
});
