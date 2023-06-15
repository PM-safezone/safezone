$("#image-upload").change(function(e) {
    var reader = new FileReader();
    reader.onload = function(e) {
        $('#image-preview').attr('src', e.target.result);
        $('.pre-container').show(); // 이미지가 선택되면 컨테이너를 보이도록 설정
        $('.form-container').css('height', '75rem');
    }
    if (e.target.files[0]) {
        reader.readAsDataURL(e.target.files[0]);
    } else {
        $('#image-preview').attr('src', '#');
        $('.pre-container').hide(); // 이미지가 선택되지 않으면 컨테이너를 숨김
    }
});


