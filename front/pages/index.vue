<template>
    <div id="container">
        <header id="header">
            <menu id="header-controls">
                <button type="reset" form="main-form" class="click-button button-new">начать новый</button>
            </menu>

            <nav id="header-nav">
                <button type="button" @click="scroll_to('main-slide')">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -960 960 960" width="32" height="32"><path d="M453-280h60v-240h-60v240Zm26.982-314q14.018 0 23.518-9.2T513-626q0-14.45-9.482-24.225-9.483-9.775-23.5-9.775-14.018 0-23.518 9.775T447-626q0 13.6 9.482 22.8 9.483 9.2 23.5 9.2Zm.284 514q-82.734 0-155.5-31.5t-127.266-86q-54.5-54.5-86-127.341Q80-397.681 80-480.5q0-82.819 31.5-155.659Q143-709 197.5-763t127.341-85.5Q397.681-880 480.5-880q82.819 0 155.659 31.5Q709-817 763-763t85.5 127Q880-563 880-480.266q0 82.734-31.5 155.5T763-197.684q-54 54.316-127 86Q563-80 480.266-80Zm.234-60Q622-140 721-239.5t99-241Q820-622 721.188-721 622.375-820 480-820q-141 0-240.5 98.812Q140-622.375 140-480q0 141 99.5 240.5t241 99.5Zm-.5-340Z"/></svg>
                </button>
                <button type="button" v-for="i in 12" :id="`nav-${i}`"  @click="scroll_to(`slide-${i}`)">
                    {{ i }}
                </button>
            </nav>

            <menu id="header-submit">
                <button type="submit" form="main-form" class="click-button button-generate">сгенерировать</button>
            </menu>
        </header>

        <main id="main">
            <form id="main-form" method="POST" action="http://localhost:8000/presentation/" target="_self" @submit="send($event)">
                <fieldset class="slide main-slide" id="main-slide">
                    <h1>Основные данные</h1>

                    <div>
                        <label for="project_name">Название</label>
                        <div class="input-with-controls">
                            <input type="text" name="project_name" id="project_name" placeholder="Название" v-model="project_name" />
                            <button type="button">
                                <p>вариант от ИИ</p>
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -960 960 960" width="38" height="38"><path d="M385-120q-51 0-86.5-38T258-244q-59-5-98.5-49.5T120-402q0-22 5.5-42.5T142-484q-11-18-16.5-38t-5.5-43q0-60 41.5-103t98.5-50q2-51 38.5-86.5T386-840q29 0 51.5 10.5T480-799q20-20 42-30.5t51-10.5q50 0 86 35.5t39 86.5q58 5 100 48.5T840-565q0 23-6 43.5T817-483q11 20 17 42t6 43q0 64-39.5 106.5T702-244q-5 48-41 86t-86 38q-30 0-52-10t-43-30q-21 20-43 30t-52 10Zm125-600v480q0 25 19.5 42.5T576-180q26 0 45-23t21-47q-23-8-43-21.5T565-305q-8-11-6-22.5t13-19.5q11-8 22.5-6t19.5 13q13 18 32 27.5t42 9.5q38 0 65-26t27-69q0-9-2-18.5t-4-19.5q-18 13-39.5 19.5T690-410q-13 0-21.5-8.5T660-440q0-13 8.5-21.5T690-470q38 0 64-28t26-67q0-38-28-65t-64-29q-10 24-28.5 42.5T617-589q-12 5-23-.5T579-607q-4-12 1-23.5t17-15.5q18-6 29.5-24t11.5-41q0-29-19-49t-45-20q-26 0-45 17.5T510-720Zm-60 480v-480q0-25-18.5-42.5T386-780q-26 0-45.5 20T321-711q0 23 11 40.5t29 23.5q12 4 17.5 15.5T380-609q-5 12-16.5 18t-23.5 1q-24-8-42-26.5T270-659q-35 3-62.5 29.5T180-565q0 39 26 67t64 28q13 0 21.5 8.5T300-440q0 13-8.5 21.5T270-410q-23 0-44.5-7T186-436q-3 8-4.5 17t-1.5 18q0 43 26.5 70.5T271-303q22 0 41.5-10t32.5-27q8-10 20-12.5t22 5.5q10 8 12.5 20t-5.5 22q-14 20-33.5 33.5T318-250q2 24 21 47t46 23q27 0 46-17.5t19-42.5Zm30-240Z"/></svg>
                            </button>
                        </div>
                    </div>
                </fieldset>

                <fieldset class="slide" id="slide-1">
                    <h1>Слайд 1 - Название</h1>

                    <div>
                        <input type="text" id="name" placeholder="Название" v-model="project_name" />
                    </div>

                    <div>
                        <textarea id="short_description" placeholder="Короткое описание" v-model="short_description">
                        </textarea>
                    </div>
                </fieldset>

                <fieldset class="slide" id="slide-2">
                    <h1>Слайд 2 - Описание проблем</h1>

                    <div v-for="i in problem.length">
                        <div class="input-with-controls">
                            <input type="text" name="issue" placeholder="Название проблемы" v-model="problem[i-1].issue"/>
                            <button type="button" class="controls-red-button" @click="remove_problem(i-1)">
                                <p>Удалить проблему</p>
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -960 960 960" width="38" height="38"><path d="M360-200q-22 0-40-11.5T289-241L120-480l169-239q13-18 31-29.5t40-11.5h420q24.75 0 42.375 17.625T840-700v440q0 24.75-17.625 42.375T780-200H360Zm420-60v-440 440Zm-431 0h431v-440H349L195-480l154 220Zm99-66 112-112 112 112 43-43-113-111 111-111-43-43-110 112-112-112-43 43 113 111-113 111 43 43Z"/></svg>
                            </button>
                        </div>
                        <br />
                        <textarea name="target_audience" placeholder="Описание проблемы" v-model="problem[i-1].target_audience"></textarea>
                        <br />
                        <textarea type="text" name="solution" placeholder="Решение проблемы" v-model="problem[i-1].solution"></textarea>
                        <hr />
                    </div>

                    <menu>
                        <button type="button" class="click-button button-new" @click="add_problem()">добавить проблему</button>
                    </menu>
                </fieldset>

                <fieldset class="slide" id="slide-3">
                    <h1>Слайд 3 - Описание</h1>

                    <div>
                        <textarea name="description" placeholder="Подробное описание" v-model="description"></textarea>
                    </div>
                </fieldset>

                <fieldset class="slide" id="slide-4">
                    <h1>Слайд 4 - Клиенты</h1>

                    <div>
                        <input type="text" name="clients" placeholder="Клиенты" v-model="clients" />
                    </div>
                </fieldset>
            </form>
        </main>

        <footer id="footer">

        </footer>
    </div>
</template>

<script>
export default {
    name: 'indexPage',

    data: function () {
        return {
            project_name: '',
            short_description: '',
            problem: [
                {
                    issue: '',
                    target_audience: '',
                    solution: '',
                }
            ],
            description: '',
            clients: ''
        }
    },

    methods: {
        scroll_to: function (id) {
            try { document.getElementById(id).scrollIntoView({
                behavior: 'smooth',
                block: 'center',
                inline: 'nearest'
            }) } catch {}
        },

        process_image: function (event) {
            const input = event.target
            const div = input.parentElement.querySelector('div')

            if (input.files && input.files[0]) {
                div.innerHTML = 'загружено'
                div.classList.add('file-input-loaded')
            }
            else {
                div.innerHTML = 'загрузить фото'
                div.classList.remove('file-input-loaded')
            }
        },

        remove_problem: function (i) {
            this.problem.splice(i, 1)
        },

        add_problem: function () {
            this.problem.push({
                issue: '',
                target_audience: '',
                solution: '',
            })
        },

        send: function (event) {
            event.preventDefault()

            let form = new FormData(event.target)

            form.forEach(function (value, key) {
                console.log(key, value)
            })
        }
    }
}
</script>

<style>
:root {
    --colour-back: #FFFFFF;
    --colour-preback: #e9f2f7;
    --colour-semiback: #CCCCCC;
    --colour-semifront: #777777;
    --colour-prefront: #222222;
    --colour-front: #000000;

    --colour-btn-back: #555555;
    --colour-btn-front: #ffffff;
    --colour-btn-back-hover: #303030;
    --colour-btn-front-hover: #ffffff;
    --colour-btn-back-active: #2b2b2b;
    --colour-btn-front-active: #ffffff;

    --colour-decoration: #2d4c7c;
    --colour-decoration-alt: #107a7a;

    --colour-decoration-light: #c3cfe0;
}

* {
    font-family: Arial, Helvetica, sans-serif;
    font-size: inherit;

    padding: 0;
    margin: 0;

    border: none;

    background-color: inherit;
    color: inherit;
}

html {
    background-color: var(--colour-back);
    color: var(--colour-front);
    fill: var(--colour-front);
    font-size: 16px;
}

.click-button {
    display: inline-block;
    padding: 6px 20px;
    border: none;
    border-radius: 10px;
    background-color: var(--colour-btn-back);
    color: var(--colour-btn-front);
    cursor: pointer;
    transition: .25s;
}
.click-button:hover {
    background-color: var(--colour-btn-back-hover);
    color: var(--colour-btn-front-hover);
}
.click-button:active {
    background-color: var(--colour-btn-back-active);
    color: var(--colour-btn-front-active);
}

.button-new {
    background: linear-gradient(to bottom right, var(--colour-decoration), var(--colour-decoration-alt));
    background-size: 200% 200%;
    color: #FFFFFF;
}
.button-new:hover {
    animation: button-hover-anim ease-out;
    animation-duration: .5s;
    animation-direction: normal;
    animation-fill-mode: forwards;
}
.button-new:active {
    animation: button-active-anim .5s ease;
    animation-duration: .5s;
    animation-direction: normal;
    animation-fill-mode: forwards;
}

.button-generate {
    background: linear-gradient(to bottom right, var(--colour-decoration), var(--colour-decoration-alt));
    /* background: linear-gradient(to bottom right, #ee733a, #851a3a); */
    background-size: 200% 200%;
    color: #FFFFFF;
}
.button-generate:hover {
    animation: button-hover-anim ease-out;
    animation-duration: .5s;
    animation-direction: normal;
    animation-fill-mode: forwards;
}
.button-generate:active {
    animation: button-active-anim .5s ease;
    animation-duration: .5s;
    animation-direction: normal;
    animation-fill-mode: forwards;
}


body {
    background-color: #f0f0f0;
}


#header {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: space-between;
    align-items: center;
    gap: 20px;
    position: sticky;
    top: 0;
    left: 0;
    box-sizing: border-box;
    width: 100%;
    height: min-content;
    min-height: 60px;
    padding: 6px 20px;
    border-bottom: 3px solid var(--colour-semifront);
    background-color: #FFFFFF;
    z-index: 1000;
}

:is(#header-controls, #header-submit) {
    height: 100%;
}

:is(#header-controls, #header-submit) button {
    min-height: 40px;
    font-size: 120%;
}

#header-nav {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    gap: 10px;
}

#header-nav button {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 40px;
    height: 40px;
    border-radius: 10px;
    background-color: #cbdee4;
    color: #000000;
    font-size: 24px;
    cursor: pointer;
    transition: .25s;

}
#header-nav button:hover {
    background-color: #b3ced6;
}
#header-nav button:hover {
    background-color: #a0b9c0;
}


#main {
    width: 90%;
    max-width: 800px;
    margin: 30px auto;
}

#main-form {
    display: flex;
    flex-direction: column;
    flex-wrap: nowrap;
    gap: 30px;
    width: 100%;
}

.slide {
    padding: 0 0 20px 0;
    border-radius: 20px;
    background-color: var(--colour-preback);
    background-clip: border-box;
    box-shadow: 0 1px 4px 2px #000000;
    position: relative;
}

.slide h1 {
    display: block;
    box-sizing: border-box;
    width: 100%;
    padding: 6px 20px;
    margin-bottom: 10px;
    border-radius: 20px 20px 0 0;
    background: linear-gradient(to bottom right, var(--colour-decoration) 30%, var(--colour-decoration-alt));
    color: #ffffff;
    text-align: center;
    font-size: 120%;
}

.slide > div {
    box-sizing: border-box;
    width: 100%;
    padding: 10px 20px;
    margin: 10px 0;
}

.slide label {
    display: block;
    box-sizing: border-box;
    width: 100%;
    padding-left: 10px;
    margin-bottom: 6px;
    font-size: 110%;
}

.slide :is(input[type="text"], input[type="number"]) {
    display: block;
    box-sizing: border-box;
    width: 100%;
    height: 40px;
    padding: 6px 10px;
    border: 1px dashed var(--colour-decoration-alt);
    border-radius: 666px;
    background-color: var(--colour-back);
    color: #002d9e;
    font-weight: bold;
    transition: .25s;
}
.slide :is(input[type="text"], input[type="number"]):hover {
    border: 1px solid var(--colour-decoration);
    background-color: var(--colour-decoration-light);
}
.slide :is(input[type="text"], input[type="number"]):not(:placeholder-shown) {
    border: 1px solid var(--colour-decoration);
}


.input-with-controls {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    gap: 10px;
}
.input-with-controls :is(input[type="text"], input[type="number"]) {
    display: flex;
    flex-shrink: 1;
    flex-basis: 100%;
}

.input-with-controls button {
    box-sizing: border-box;
    width: 40px;
    min-width: 40px;
    height: 40px;
    min-height: 40px;
    border: 1px dashed var(--colour-decoration-alt);
    border-radius: 666px;
    background-color: var(--colour-back);
    color: var(--colour-front);
    overflow: hidden;
    cursor: pointer;
    position: relative;
    transition: .25s;
}
.input-with-controls button > p {
    position: absolute;
    top: 50%;
    right: 44px;
    transform: translateY(-50%);
    width: max-content;
    font-size: 110%;
}
.input-with-controls button > svg {
    position: absolute;
    top: 0;
    right: 0;
}

.input-with-controls button:hover {
    width: 300px;
    border: 1px solid var(--colour-decoration);
    background-color: var(--colour-decoration-light);
}

.input-with-controls button.controls-red-button:hover {
    background-color: #e29090;
    color: #000000;
}


.slide textarea {
    display: block;
    box-sizing: border-box;
    width: 100%;
    height: 100px;
    min-height: 60px;
    padding: 6px 10px;
    border: 1px dashed var(--colour-decoration-alt);
    border-radius: 8px;
    background-color: var(--colour-back);
    color: #002d9e;
    font-weight: bold;
    resize: vertical;
    transition: .25s;
}
.slide textarea:hover {
    border: 1px solid var(--colour-decoration);
    background-color: var(--colour-decoration-light);
}
.slide textarea:not(:placeholder-shown) {
    border: 1px solid var(--colour-decoration);
}


.slide select {
    display: block;
    box-sizing: border-box;
    width: 100%;
    height: 40px;
    padding: 6px 10px;
    border: 1px dashed var(--colour-decoration-alt);
    border-radius: 666px;
    appearance: none;
    background-image: url("data:image/svg+xml;utf8,<svg fill='black' height='24' viewBox='0 0 24 24' width='24' xmlns='http://www.w3.org/2000/svg'><path d='M7 10l5 5 5-5z'/><path d='M0 0h24v24H0z' fill='none'/></svg>");
    background-repeat: no-repeat;
    background-position-x: calc(100% - 5px);
    background-position-y: 7px;
    background-color: var(--colour-back);
    color: #002d9e;
    font-weight: bold;
    cursor: pointer;
    transition: .25s;
}
.slide select:hover {
    border: 1px solid var(--colour-decoration);
    background-color: var(--colour-decoration-light);
}
.slide select:valid {
    border: 1px solid var(--colour-decoration);
}


.file-input {
    display: block;
    box-sizing: border-box;
    width: 100%;
    height: 40px;
    position: relative;
}

.file-input input[type="file"] {
    position: absolute;
    top: 0;
    left: 0;
    display: block;
    width: 100%;
    height: 100%;
    opacity: 0;
    cursor: pointer;
    z-index: 10;
}

.file-input div {
    display: flex;
    align-items: center;
    box-sizing: border-box;
    width: 100%;
    height: 100%;
    padding: 6px 10px;
    border: 1px dashed var(--colour-decoration-alt);
    border-radius: 666px;
    background-color: var(--colour-back);
    color: #002d9e;
    font-weight: bold;
    cursor: pointer;
    transition: .25s;
    z-index: 8;
}
.file-input input[type="file"]:hover + div {
    border: 1px solid var(--colour-decoration);
    background-color: var(--colour-decoration-light);
}
.file-input div:hover {
    border: 1px solid var(--colour-decoration);
    background-color: var(--colour-decoration-light);
}
.file-input div.file-input-loaded {
    border: 1px solid var(--colour-decoration);
}


.checkbox-wrapper {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: flex-start;
    align-items: center;
    gap: 4px;
    margin: 10px;
}
.checkbox-wrapper input[type='checkbox'] {
    width: 20px;
    min-width: 20px;
    height: 20px;
    min-height: 20px;
}
.checkbox-wrapper label {
    display: inline;
    padding: 0;
    margin: 0;
}


.date-wrapper {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
}

.date-wrapper input[type='date'] {
    display: flex;
    align-items: center;
    flex-grow: 1;
    box-sizing: border-box;
    width: 40%;
    height: 100%;
    padding: 6px 10px;
    border: 1px dashed var(--colour-decoration-alt);
    border-radius: 666px;
    background-color: var(--colour-back);
    color: #002d9e;
    font-weight: bold;
    cursor: pointer;
    transition: .25s;
}
.slide input[type='date']:hover {
    border: 1px solid var(--colour-decoration);
    background-color: var(--colour-decoration-light);
}
.slide input[type='date']:valid {
    border: 1px solid var(--colour-decoration);
}


.slide menu {
    padding: 0 20px;
}


@keyframes button-hover-anim {
    0% { background-position: 10% 0% }
    100% { background-position: 91% 100% }
}

@keyframes button-active-anim {
    0% { background-position: 90% 0% }
    100% { background-position: 10% 100% }
}
</style>
