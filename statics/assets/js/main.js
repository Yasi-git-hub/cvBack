// document.addEventListener('DOMContentLoaded', function(){
//     document.querySelectorAll('a[href^="#"]').forEach(function(link){
//         link.addEventListener('click', function(event){
//             const targetID=link.getAttribute('href');
//             if(!targetID || targetID === '#'){
//                 return;
//             }
//             const target= document.querySelector(targetID);
//             if(target){
//                 event.preventDefault();
//                 target.scrollIntoView({
//                     behavior:'smooth',
//                     block:'start'
//                 });
//                 history.replaceState(null,'',targetID)
//             }
//         });
//     });
    
// });