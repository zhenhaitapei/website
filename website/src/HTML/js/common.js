$(document).ready(function() {
    $('#feedback-form').on('submit', function(e) {
        var target = $(e.target);
        var serialized = target.serializeArray();
        var len = serialized.length;
        var data = {};
        var item;

        e.preventDefault();

        for (var i = 0; i < len; i++) {
            item = serialized[i];
            data[item.name] = item.value;
        }

        target.find('input, textarea').each(function() {
            $(this).val('');
        });

        $.post('/feedback', data);
        return
    });
});
