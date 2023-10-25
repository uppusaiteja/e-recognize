const imageInput = document.getElementById('image');
const imagePreview = document.getElementById('image-preview');

imageInput.addEventListener('change', ImageChangeFunc);
function ImageChangeFunc() {
    const file = imageInput.files[0] || null;

    if (file) {
        const reader = new FileReader();
        if (file.type.indexOf("image") === -1) {
            alert("Unsupported File Format");
            document.getElementById('image').value = ''
        }

        reader.onload = function(e) {
            imagePreview.src = e.target.result;
        };

        reader.readAsDataURL(file);
    } else {
        imagePreview.src = '';
    }
}