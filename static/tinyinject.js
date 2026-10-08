var script = document.createElement("script");

script.src = "https://cdn.tiny.cloud/1/x9r3u4y9dhtcw0sivnf8pzq85vbybpx995fjfe07mfcr6p59/tinymce/7/tinymce.min.js";

document.head.appendChild(script);

script.onload = function () {
    tinymce.init({
        selector: '#id_content',
        height: 400,
        menubar: true,
        plugins: 'lists link table code',
        toolbar: 'undo redo | blocks | bold italic underline | bullist numlist | link table | code',
        readonly: false,
        setup: function (editor) {
            editor.on('init', function () {
                editor.getBody().contentEditable = true;
                editor.getDoc().designMode = 'on';
            });
        }
    });
};

//     var script = document.createElement("script");

// script.type = "text/javascript";

// script.src = "https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js";

// document.head.appendChild(script);

// script.onload = function () {

//     tinymce.init({
//         selector: "#id_content",
//         height: 400,
//         menubar: true,
//         plugins: "advlist autolink lists link image charmap print preview anchor",
//         toolbar: "undo redo | formatselect | bold italic backcolor | \
// alignleft aligncenter alignright alignjustify | \
// bullist numlist outdent indent | removeformat | help"
//     });

// };