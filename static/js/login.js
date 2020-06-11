function submitForm() {
    $.post(
        '/api/v1/auth/token/login/',
        $('#login-form').serialize(),
        (data) => {
            localStorage.setItem("authToken", data.authToken);
            document.location = "/";
        }

    ).fail((event) => {
        alert(event.responseJSON.nonFieldErrors[0]);
    });
    return false;
}
