const btnDelete = document.querySelectorAll('.btn-delete')
console.log(btnDelete);

if (btnDelete) {
  const arrayButtonsDelete = Array.from(btnDelete)
  arrayButtonsDelete.forEach(btn=>{
    btn.addEventListener('click', (e) => {
      if(!confirm('Are you secure you want to delete it?')){
        e.preventDefault()
      }
    })
  });
}
