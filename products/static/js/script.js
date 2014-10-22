// Redirect user to a product page on klikking the product.
// This is used over simply using the a tag to prevent
// accidental style overrides.

$(document).ready(function() {
    $('.product-cell').click( function() {
        window.location = $(this).data('url');
    });
});
