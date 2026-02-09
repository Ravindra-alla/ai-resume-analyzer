document.addEventListener('DOMContentLoaded', () => {
    // File Upload Interaction
    const fileInput = document.getElementById('resume');
    const fileLabel = document.querySelector('.file-upload-text span');
    const uploadWrapper = document.querySelector('.file-upload-wrapper');

    if (fileInput) {
        fileInput.addEventListener('change', (e) => {
            if (e.target.files.length > 0) {
                const fileName = e.target.files[0].name;
                fileLabel.textContent = `Selected: ${fileName}`;
                uploadWrapper.style.borderColor = 'var(--success-color)';
                uploadWrapper.style.background = 'rgba(29, 209, 161, 0.1)';
            }
        });

        // Drag and Drop Visuals
        ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
            uploadWrapper.addEventListener(eventName, preventDefaults, false);
        });

        function preventDefaults(e) {
            e.preventDefault();
            e.stopPropagation();
        }

        ['dragenter', 'dragover'].forEach(eventName => {
            uploadWrapper.addEventListener(eventName, highlight, false);
        });

        ['dragleave', 'drop'].forEach(eventName => {
            uploadWrapper.addEventListener(eventName, unhighlight, false);
        });

        function highlight(e) {
            uploadWrapper.style.borderColor = 'var(--accent-color)';
            uploadWrapper.style.background = 'rgba(255, 255, 255, 0.1)';
        }

        function unhighlight(e) {
            uploadWrapper.style.borderColor = 'var(--card-border)';
            uploadWrapper.style.background = 'transparent';
        }

        uploadWrapper.addEventListener('drop', handleDrop, false);

        function handleDrop(e) {
            const dt = e.dataTransfer;
            const files = dt.files;
            fileInput.files = files;

            if (files.length > 0) {
                const fileName = files[0].name;
                fileLabel.textContent = `Selected: ${fileName}`;
                uploadWrapper.style.borderColor = 'var(--success-color)';
                uploadWrapper.style.background = 'rgba(29, 209, 161, 0.1)';
            }
        }
    }
});
