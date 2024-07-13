$(document).ready(function() {
    $('form').on('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission
        var formData = $(this).serialize(); // Serialize the form data

        $.ajax({
            type: 'POST',
            url: '{% url "index" %}', // Ensure this matches your Django URL pattern
            data: formData,
            success: function(response) {
                // Show the success message above the form
                $('#success-message').text('Form submitted successfully...!').show();

                // Clear the form fields
                $('form')[0].reset();

                // Hide the success message after 5 seconds and refresh the page
                setTimeout(function() {
                    $('#success-message').fadeOut('slow', function() {
                        location.reload();
                    });
                }, 5000);
            },
            error: function(response) {
                // Handle error
                alert('An error occurred: ' + response.responseText);
            }
        });
    });
});
    