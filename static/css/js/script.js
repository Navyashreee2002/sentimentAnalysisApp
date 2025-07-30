function validateForm() {
    const text = document.getElementById('text').value.trim();
    if (text === '') {
        alert('Please enter some text!');
        return false;
    }
    if (text.length < 5) {
        alert('Text must be at least 5 characters long!');
        return false;
    }
    return true;
}