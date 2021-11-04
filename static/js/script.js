const forms = document.querySelectorAll('.vote');

const save_vote = function (target) {
    const formData = new FormData();
    formData.append('entry_id', target.entry_id.value);
    formData.append('csrfmiddlewaretoken', target.csrfmiddlewaretoken.value);

    fetch('uzytkownik/save_vote', {
        body: formData,
        method: 'post'
    }).then(data => data.json()).then(function(data){
       document.querySelector('.entry-' +data.entry_id).innerHTML = data.vote_score
    });

}

for (let i = 0; i < forms.length; i++) {
    forms[i].addEventListener('submit', function (event) {
        save_vote(event.target);
        event.preventDefault();
    });
}
