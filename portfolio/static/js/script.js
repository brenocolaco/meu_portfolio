/* menu responsivo */

const menuHamburger = document.querySelector('.menu-hamburger')
menuHamburger.addEventListener('click', () => {
    toggleMenu()
});

function toggleMenu() {
    const nav = document.querySelector('.nav-responsive');
    menuHamburger.classList.toggle('change');

    if (menuHamburger.classList.contains('change')){
        nav.style.display = 'block';
    } else {
        nav.style.display = 'none';
    }
}

/* Criar um elemento HTML. Neste caso; uma div que é passado como argumento para a propriedade innerHTML. */
/* Retorna o primeiro elemento filho da div, que será o elemento criado a partir da string HTML. */
const createElement = str => {
    const el = document.createElement('div'); 
    el.innerHTML = str;
    return el.firstElementChild;
};

/* Onde os elementos do portifolio serão criados */
let portifolioContainer = document.querySelector('.portifolio-container');

/* Com o uso da extensão do LiveServer */
/* Faz-se uma requisição para o arquivos .json para obter as informações sobre os projetos */
fetch('/static/projetos.json')
.then((response) => response.json())
.then((data) => {
    
    data.forEach(dados_projeto => {

        let el = createElement(`<div class="portifolio-box">
            <div style="background-image: url(${dados_projeto.imagem})"></div>
            <img src="${dados_projeto.imagem}" alt="${dados_projeto.titulo}">
            <div class="portifolio-layer">
                <h4>${dados_projeto.titulo}</h4>
                <p>${dados_projeto.descricao}</p>
                <a href="#portifolio" id="portifolio-button" data-projeto="${dados_projeto.id}"><i class='bx bx-link-external'></i></a>
            </div>   
        </div>`)
    
        let button = el.querySelector('#portifolio-button');
    
        button.addEventListener('click' , () => {
    
            let modal = document.querySelector('#modal-projetos');
            
            modal.classList.add('active');
            /* Os elementos dentro da modal são criados para a imagem é feita uma verificação 
            para garantir que o campo imagem exista no seu objeto dados_projeto. Isso evita 
            erros caso algum projeto não tenha uma imagem definida. */
            modal.querySelector('#conteudo-projeto').innerHTML = `
                <a id="portifolio-modal-close" class='x'><i>❌</i></a>
                <h1>${dados_projeto.titulo}</h1>
                <div>${dados_projeto.descricao}</div>
                <br />
            
                ${dados_projeto._html ? '' : (dados_projeto.imagem ? `<img src="${dados_projeto.imagem}" alt="${dados_projeto.titulo}" style="max-width: 100%; height: auto;">` : '')}
                ${dados_projeto._html ? '' : '<br />'}
                ${dados_projeto._html || ''}
                ${dados_projeto.anexos?.map(anexo => `<a href="${anexo.url}" target="_blank">${anexo.nome}</a>`).join('<br />')}
            `;
            /*Primeiro, verificamos se dados_projeto._html existe (é true). Se existir, renderizamos uma string vazia (''), ou seja, nada da imagem será exibido.
            Se dados_projeto._html não existir (é false), então passamos para a segunda condição: verificar se dados_projeto.imagem existe. Se existir, a tag <img>
            é renderizada normalmente. Caso contrário, uma string vazia é renderizada.*/

            const closeButton = modal.querySelector('#portifolio-modal-close'); /* Seleciona a ancora que tem o botão */

            closeButton.addEventListener('click', () => {
                modal.classList.remove('active'); /* Remove a classe active escondendo a modal novamente */
        });
    
        })
    
        portifolioContainer.appendChild(el);

        
    })

})
.catch(console.error);

fetch('/static/images/circuit.svg')
    .then(response => response.text())
    .then(data => document.getElementById('circuit').innerHTML = data); 

let modal = document.querySelector('#modal-sobre-mim');

document.querySelector('#btn-sobre-mim').addEventListener('click' , () => {
    
    modal.classList.add('active');
});

const closeButton = document.querySelector('#about-modal-close'); /* Seleciona a ancora que tem o botão */

closeButton.addEventListener('click', () => {
    modal.classList.remove('active'); /* Remove a classe active escondendo a modal novamente */
});