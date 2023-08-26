<template>
    <div id="container">
        <header id="header">
            <menu id="header-controls">
                <button type="reset" @click="reset()" form="main-form" class="click-button button-gradient">начать новый</button>
            </menu>

            <nav id="header-nav">
                <button type="button" @click="scroll_to('main-slide')">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -960 960 960" width="32" height="32"><path d="M453-280h60v-240h-60v240Zm26.982-314q14.018 0 23.518-9.2T513-626q0-14.45-9.482-24.225-9.483-9.775-23.5-9.775-14.018 0-23.518 9.775T447-626q0 13.6 9.482 22.8 9.483 9.2 23.5 9.2Zm.284 514q-82.734 0-155.5-31.5t-127.266-86q-54.5-54.5-86-127.341Q80-397.681 80-480.5q0-82.819 31.5-155.659Q143-709 197.5-763t127.341-85.5Q397.681-880 480.5-880q82.819 0 155.659 31.5Q709-817 763-763t85.5 127Q880-563 880-480.266q0 82.734-31.5 155.5T763-197.684q-54 54.316-127 86Q563-80 480.266-80Zm.234-60Q622-140 721-239.5t99-241Q820-622 721.188-721 622.375-820 480-820q-141 0-240.5 98.812Q140-622.375 140-480q0 141 99.5 240.5t241 99.5Zm-.5-340Z"/></svg>
                </button>
                <navButton
                    :nav_id="1"
                    :checks="[project_name != '', short_description != '']"
                />
                <navButton
                    :nav_id="2"
                    :checks="[problem.length > 0]"
                />
                <navButton
                    :nav_id="3"
                    :checks="[description != '']"
                />
                <navButton
                    :nav_id="4"
                    :checks="[...clients.values()]"
                />
                <navButton
                    :nav_id="5"
                    :checks="[revenue != 0, clients_count != 0, churn_rate != 0]"
                />
            </nav>

            <menu id="header-submit">
                <button type="submit" form="main-form" class="click-button button-gradient">сгенерировать</button>
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
                                <div>
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -960 960 960" width="38" height="38"><path d="M385-120q-51 0-86.5-38T258-244q-59-5-98.5-49.5T120-402q0-22 5.5-42.5T142-484q-11-18-16.5-38t-5.5-43q0-60 41.5-103t98.5-50q2-51 38.5-86.5T386-840q29 0 51.5 10.5T480-799q20-20 42-30.5t51-10.5q50 0 86 35.5t39 86.5q58 5 100 48.5T840-565q0 23-6 43.5T817-483q11 20 17 42t6 43q0 64-39.5 106.5T702-244q-5 48-41 86t-86 38q-30 0-52-10t-43-30q-21 20-43 30t-52 10Zm125-600v480q0 25 19.5 42.5T576-180q26 0 45-23t21-47q-23-8-43-21.5T565-305q-8-11-6-22.5t13-19.5q11-8 22.5-6t19.5 13q13 18 32 27.5t42 9.5q38 0 65-26t27-69q0-9-2-18.5t-4-19.5q-18 13-39.5 19.5T690-410q-13 0-21.5-8.5T660-440q0-13 8.5-21.5T690-470q38 0 64-28t26-67q0-38-28-65t-64-29q-10 24-28.5 42.5T617-589q-12 5-23-.5T579-607q-4-12 1-23.5t17-15.5q18-6 29.5-24t11.5-41q0-29-19-49t-45-20q-26 0-45 17.5T510-720Zm-60 480v-480q0-25-18.5-42.5T386-780q-26 0-45.5 20T321-711q0 23 11 40.5t29 23.5q12 4 17.5 15.5T380-609q-5 12-16.5 18t-23.5 1q-24-8-42-26.5T270-659q-35 3-62.5 29.5T180-565q0 39 26 67t64 28q13 0 21.5 8.5T300-440q0 13-8.5 21.5T270-410q-23 0-44.5-7T186-436q-3 8-4.5 17t-1.5 18q0 43 26.5 70.5T271-303q22 0 41.5-10t32.5-27q8-10 20-12.5t22 5.5q10 8 12.5 20t-5.5 22q-14 20-33.5 33.5T318-250q2 24 21 47t46 23q27 0 46-17.5t19-42.5Zm30-240Z"/></svg>
                                </div>
                            </button>
                        </div>
                    </div>
                </fieldset>

                <fieldset class="slide" id="slide-1">
                    <h1>Слайд 1 - Название</h1>

                    <div>
                        <label for="project_name-2">Название</label>
                        <input type="text" id="project_name-2" placeholder="Название" v-model="project_name" />
                    </div>

                    <div>
                        <label for="short_description">Короткое описание</label>
                        <input type="text" id="short_description" placeholder="Короткое описание" v-model="short_description" />
                    </div>
                </fieldset>

                <fieldset class="slide" id="slide-2">
                    <h1>Слайд 2/4 - Целевая аудитория</h1>

                    <div v-for="i in problem.length">
                        <div class="input-with-controls">
                            <input type="text" name="target_audience" placeholder="Целевая аудитория" v-model="problem[i-1].target_audience"/>
                            <button type="button" class="controls-red-button" @click="remove_audience(i-1)">
                                <p>Удалить аудиторию</p>
                                <div>
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -960 960 960" width="38" height="38"><path d="M360-200q-22 0-40-11.5T289-241L120-480l169-239q13-18 31-29.5t40-11.5h420q24.75 0 42.375 17.625T840-700v440q0 24.75-17.625 42.375T780-200H360Zm420-60v-440 440Zm-431 0h431v-440H349L195-480l154 220Zm99-66 112-112 112 112 43-43-113-111 111-111-43-43-110 112-112-112-43 43 113 111-113 111 43 43Z"/></svg>
                                </div>
                            </button>
                            <button type="button" class="controls-green-button" @click="add_problem(i-1)">
                                <p>Добавить проблему</p>
                                <div>
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -960 960 960" width="32" height="32"><path d="M261-322q12 0 21-9t9-21q0-12-9-21t-21-9q-12 0-21 9t-9 21q0 12 9 21t21 9Zm-30-130h60v-191h-60v191Zm179 80h319v-60H410v60Zm0-171h319v-60H410v60ZM132-160q-24 0-42-18t-18-42v-520q0-24 18-42t42-18h696q24 0 42 18t18 42v520q0 24-18 42t-42 18H132Zm0-60h696v-520H132v520Zm0 0v-520 520Z"/></svg>
                                </div>
                            </button>
                        </div>
                        <br />
                        <template v-for="i2 in problem[i-1].issue.length">
                            <textarea name="issue" placeholder="Описание проблемы" v-model="problem[i-1].issue[i2-1]"></textarea>
                            <textarea name="solution" class="with-margin" placeholder="Решение проблемы" v-model="problem[i-1].solution[i2-1]"></textarea>
                            <button type="button" class="click-button with-margin" @click="remove_problem(i-1, i2-1)">Удалить проблему</button>
                        </template>
                        <hr />
                    </div>

                    <menu>
                        <button type="button" class="click-button button-gradient" @click="add_auditory()">добавить целевую аудиторию</button>
                    </menu>
                </fieldset>

                <fieldset class="slide" id="slide-3">
                    <h1>Слайд 3 - Описание</h1>

                    <div>
                        <label for="description">Описание</label>
                        <textarea name="description" placeholder="Подробное описание" v-model="description"></textarea>
                    </div>
                </fieldset>

                <fieldset class="slide" id="slide-4">
                    <h1>Слайд 4 - Клиенты</h1>

                    <div v-for="i in clients.length">
                        <div class="input-with-controls">
                            <input type="text" name="clients" placeholder="Клиенты" v-model="clients[i-1]" />
                            <button type="button" class="controls-red-button" @click="remove_client(i-1)">
                                <p>Удалить клиента</p>
                                <div>
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -960 960 960" width="38" height="38"><path d="M360-200q-22 0-40-11.5T289-241L120-480l169-239q13-18 31-29.5t40-11.5h420q24.75 0 42.375 17.625T840-700v440q0 24.75-17.625 42.375T780-200H360Zm420-60v-440 440Zm-431 0h431v-440H349L195-480l154 220Zm99-66 112-112 112 112 43-43-113-111 111-111-43-43-110 112-112-112-43 43 113 111-113 111 43 43Z"/></svg>
                                </div>
                            </button>
                        </div>
                    </div>

                    <menu>
                        <button type="button" class="click-button button-gradient" @click="add_client()">добавить клиента</button>
                    </menu>
                </fieldset>

                <fieldset class="slide" id="slide-5">
                    <h1>Слайд 5 - Прибыль</h1>

                    <div>
                        <label for="revenue">Прибыль</label>
                        <div class="input-number-with-controls">
                            <input type="number" id="revenue" placeholder="Прибыль" v-model="revenue"/>
                            <input type="text" id="revenue_suffix" list="amount_list" class="small-input" placeholder="ед." v-model="revenue_suffix"/>
                            <div>
                                <button type="button" class="controls-red-button" @click="revenue -= 1">
                                    <svg
                                        xmlns="http://www.w3.org/2000/svg"
                                        viewBox="0 -960 960 960"
                                        width="32"
                                        height="32"
                                    >
                                        <path d="M200-450v-60h560v60H200Z"/>
                                    </svg>
                                </button>
                                <button type="button" class="controls-green-button" @click="revenue = Number(revenue) + 1">
                                    <svg
                                        xmlns="http://www.w3.org/2000/svg"
                                        viewBox="0 -960 960 960"
                                        width="32"
                                        height="32"
                                    >
                                        <path d="M450-450H200v-60h250v-250h60v250h250v60H510v250h-60v-250Z"/>
                                    </svg>
                                </button>
                            </div>
                        </div>
                    </div>

                    <div>
                        <label for="clients_count">Количество клиентов</label>
                        <div class="input-number-with-controls">
                            <input
                                type="number"
                                id="clients_count"
                                placeholder="Количество клиентов"
                                min="0"
                                v-model="clients_count"
                                @input="clients_count = Math.max(0, $event.target.value)"
                            />
                            <div>
                                <button type="button" class="controls-red-button" @click="clients_count = Math.max(0, clients_count - 1)">
                                    <svg
                                        xmlns="http://www.w3.org/2000/svg"
                                        viewBox="0 -960 960 960"
                                        width="32"
                                        height="32"
                                    >
                                        <path d="M200-450v-60h560v60H200Z"/>
                                    </svg>
                                </button>
                                <button type="button" class="controls-green-button" @click="clients_count = Number(clients_count) + 1">
                                    <svg
                                        xmlns="http://www.w3.org/2000/svg"
                                        viewBox="0 -960 960 960"
                                        width="32"
                                        height="32"
                                    >
                                        <path d="M450-450H200v-60h250v-250h60v250h250v60H510v250h-60v-250Z"/>
                                    </svg>
                                </button>
                            </div>
                        </div>
                    </div>

                    <div>
                        <label for="churn_rate">Процент оттока</label>
                        <div class="input-range">
                            <input type="range" id="churn_rate" min="0" max="100" step="1" v-model="churn_rate" />
                            <input
                                type="number"
                                min="0" max="100" step="1"
                                v-model="churn_rate"
                                @input="churn_rate = Math.max(0, Math.min(100, $event.target.value))"
                            />
                        </div>
                    </div>

                    <div>
                        <label for="is_exist">Компания существует</label>
                        <button type="button" class="input-options" @click="is_exist = !is_exist">
                            <span class="selector" :data-position="is_exist ? 0 : 1"></span>
                            <p>существует</p>
                            <p>не существует</p>
                        </button>
                    </div>

                    <div>
                        <label for="inn">ИНН</label>
                        <input type="text" id="inn" placeholder="ИНН" v-model="inn" :disabled="is_exist ? null : 'disabled'" />
                    </div>
                </fieldset>

                <fieldset class="slide" id="slide-6">
                    <h1>Слайд 6 - Команда</h1>

                    <div v-for="i in members.length">
                        <div class="input-with-controls">
                            <input type="text" name="members" placeholder="ФИО участника" v-model="members[i-1].full_name" />
                            <button type="button" class="controls-red-button" @click="remove_member(i-1)">
                                <p>Удалить участника</p>
                                <div>
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -960 960 960" width="38" height="38"><path d="M360-200q-22 0-40-11.5T289-241L120-480l169-239q13-18 31-29.5t40-11.5h420q24.75 0 42.375 17.625T840-700v440q0 24.75-17.625 42.375T780-200H360Zm420-60v-440 440Zm-431 0h431v-440H349L195-480l154 220Zm99-66 112-112 112 112 43-43-113-111 111-111-43-43-110 112-112-112-43 43 113 111-113 111 43 43Z"/></svg>
                                </div>
                            </button>
                        </div>

                        <div class="with-margin">
                            <input type="text" name="proffesion" placeholder="Должность" v-model="members[i-1].proffesion" />
                        </div>

                        <div>
                            <div class="file-input">
                                <input type="file" name="photo" accept="image/*" multiple="false" :data-member="i-1" @change="process_image($event, 'members')" />
                                <div v-if="members[i-1].photo == null">загрузить фото</div>
                                <div v-else class="file-input-loaded">загружено&nbsp;<span disabled>({{ members[i-1].photo.length }} байт)</span></div>
                            </div>
                        </div>

                        <hr />
                    </div>

                    <menu>
                        <button type="button" class="click-button button-gradient" @click="add_member()">добавить участника</button>
                    </menu>
                </fieldset>

                <fieldset class="slide" id="slide-7">
                    <h1>Слайд 7 - Спонсоры</h1>

                    <div v-for="i in investors.length">
                        <div class="input-with-controls">
                            <input type="text" placeholder="Спонсор" v-model="investors[i-1].name" />
                            <button type="button" class="controls-red-button" @click="remove_investor(i-1, 'members')">
                                <p>Удалить спонсора</p>
                                <div>
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -960 960 960" width="38" height="38"><path d="M360-200q-22 0-40-11.5T289-241L120-480l169-239q13-18 31-29.5t40-11.5h420q24.75 0 42.375 17.625T840-700v440q0 24.75-17.625 42.375T780-200H360Zm420-60v-440 440Zm-431 0h431v-440H349L195-480l154 220Zm99-66 112-112 112 112 43-43-113-111 111-111-43-43-110 112-112-112-43 43 113 111-113 111 43 43Z"/></svg>
                                </div>
                            </button>
                        </div>

                        <div class="with-margin">
                            <div class="file-input">
                                <input type="file" accept="image/*" multiple="false" :data-investor="i-1" @change="process_image($event, 'investors')" />
                                <div v-if="investors[i-1].image == null">загрузить фото</div>
                                <div v-else class="file-input-loaded">загружено&nbsp;<span disabled>({{ investors[i-1].image.length }} байт)</span></div>
                            </div>
                        </div>

                        <hr />
                    </div>

                    <menu>
                        <button type="button" class="click-button button-gradient" @click="add_investor()">добавить спонсора</button>
                    </menu>

                    <hr />

                    <div v-for="i in investing_rounds.length">
                        <div>
                            <label>Объём инвестиций</label>
                            <div class="input-number-with-controls">
                                <input
                                    type="number"
                                    placeholder="Объём инвестиций"
                                    min="0"
                                    v-model="investing_rounds[i-1].amount"
                                    @input="clients_count = Math.max(0, $event.target.value)"
                                />
                                <select v-model="investing_rounds[i-1].amount_modifier" required class="small-input">
                                    <option value="1">руб.</option>
                                    <option value="1000">тыс. руб.</option>
                                    <option value="1000000">млн. руб.</option>
                                </select>

                                <div>
                                    <button type="button" class="controls-red-button" @click="investing_rounds[i-1].amount = Math.max(0, investing_rounds[i-1].amount - 1)">
                                        <svg
                                            xmlns="http://www.w3.org/2000/svg"
                                            viewBox="0 -960 960 960"
                                            width="32"
                                            height="32"
                                        >
                                            <path d="M200-450v-60h560v60H200Z"/>
                                        </svg>
                                    </button>
                                    <button type="button" class="controls-green-button" @click="investing_rounds[i-1].amount = Number(investing_rounds[i-1].amount) + 1">
                                        <svg
                                            xmlns="http://www.w3.org/2000/svg"
                                            viewBox="0 -960 960 960"
                                            width="32"
                                            height="32"
                                        >
                                            <path d="M450-450H200v-60h250v-250h60v250h250v60H510v250h-60v-250Z"/>
                                        </svg>
                                    </button>
                                </div>
                            </div>
                        </div>

                        <div class="with-margin">
                            <select v-model="investing_rounds[i-1].stage" required>
                                <option value="" selected="selected">Стадия</option>
                                <option value="pre-seed">pre-seed</option>
                                <option value="seed">seed</option>
                                <option value="раунд A">раунд A</option>
                                <option value="раунд B">раунд B</option>
                                <option value="раунд C">раунд C</option>
                                <option value="IPO">IPO</option>
                            </select>
                        </div>

                        <div>
                            <!--div v-for="i in "></div-->
                        </div>

                        <hr />
                    </div>

                    <menu>
                        <button type="button" class="click-button button-gradient" @click="add_investor()">добавить спонсора</button>
                    </menu>
                </fieldset>
            </form>
        </main>

        <datalist id="amount_list">
            <option>руб.</option>
            <option>тыс. руб.</option>
            <option>млн руб.</option>
        </datalist>

        <footer id="footer">

        </footer>
    </div>
</template>

<script>
import NavButton from '~/components/navButton.vue';
import navButton from '~/components/navButton.vue';

export default {
    name: 'indexPage',
    data: function () {
        return {
            project_name: '',
            short_description: '',

            problem: [
                {
                    target_audience: '',
                    issue: [''],
                    solution: [''],
                }
            ],

            description: '',

            clients: [''],

            revenue: 0,
            revenue_suffix: '',
            clients_count: 0,
            churn_rate: 0,
            inn: "",
            is_exist: false,

            members: [
                {
                    full_name: "",
                    proffesion: "",
                    photo: null
                }
            ],

            investors: [
                {
                    name: "",
                    image: null
                }
            ],
            investing_rounds: [
                {
                    amount: 0,
                    amount_modifier: "1",
                    stage: "",
                    spending: [
                        {
                            name: "",
                            percent: ""
                        }
                    ]
                }
            ]
        };
    },
    methods: {
        scroll_to: function (id) {
            try {
                document.getElementById(id).scrollIntoView({
                    behavior: 'smooth',
                    block: 'center',
                    inline: 'nearest'
                });
            }
            catch { }
        },
        process_image: function (event, type) {
            const input = event.target;

            if (input.files && input.files[0]) {
                const reader = new FileReader();

                if (type == 'members') {
                    reader.onload = (e) => {
                        const member_id = input.dataset.member;
                        this.members[member_id].photo = e.target.result;
                    }
                }

                else if (type == 'investors') {
                    reader.onload = (e) => {
                        const investor_id = input.dataset.investor;
                        this.investors[investor_id].image = e.target.result;
                    }
                }

                reader.readAsDataURL(input.files[0]);
            }
            else {
                this.members[member_id].photo = null;
            }
        },

        remove_audience: function (i) {
            this.problem.splice(i, 1);
        },
        add_auditory: function () {
            this.problem.push({
                target_audience: '',
                issue: [''],
                solution: [''],
            })
        },

        remove_problem: function (audience_id, i) {
            this.problem[audience_id].issue.splice(i, 1);
            this.problem[audience_id].solution.splice(i, 1);
        },
        add_problem: function (audience_id) {
            this.problem[audience_id].issue.push('');
            this.problem[audience_id].solution.push('');
        },

        remove_client: function (i) {
            this.clients.splice(i, 1);
        },
        add_client: function () {
            this.clients.push('');
        },

        remove_member: function (i) {
            this.members.splice(i, 1);
        },
        add_member: function () {
            this.members.push({
                full_name: "",
                proffesion: "",
                photo: null
            });
        },

        remove_investor: function (i) {
            this.investors.splice(i, 1);
        },
        add_investor: function () {
            this.investors.push({
                name: "",
                image: null
            });
        },

        send: function (event) {
            event.preventDefault();

            const body = JSON.stringify({
                project_name: this.project_name,
                short_description: this.short_description,
                problem: this.problem,
                description: this.description,
                clients: this.clients,
                revenue: this.revenue.toString() + ' ' + this.revenue_suffix ?? '',
                clients_count: this.clients_count.toString(),
                churn_rate: this.churn_rate.toString(),
                inn: this.inn,
                is_exist: this.is_exist,
                members: this.members,
                investors: this.investors,
                investing_rounds: this.investing_rounds,

                "roadmap": [
                    {
                    "name": "string",
                    "start_date": "2023-08-26",
                    "end_date": "2023-08-26"
                    }
                ],
                "contacts": [
                    {
                    "type": "phone",
                    "value": "string"
                    }
                ],
                "sphere": "string"
            })

            console.log({
                project_name: this.project_name,
                short_description: this.short_description,
                problem: this.problem,
                description: this.description,
                clients: this.clients,
                revenue: this.revenue.toString() + ' ' + this.revenue_suffix ?? '',
                clients_count: this.clients_count.toString(),
                churn_rate: this.churn_rate.toString(),
                inn: this.inn,
                is_exist: this.is_exist,
                members: this.members,
                investors: this.investors,
                investing_rounds: this.investing_rounds,

                "roadmap": [
                    {
                    "name": "string",
                    "start_date": "2023-08-26",
                    "end_date": "2023-08-26"
                    }
                ],
                "contacts": [
                    {
                    "type": "phone",
                    "value": "string"
                    }
                ],
                "sphere": "string"
            })

            var requestOptions = {
                method: 'POST',
                body: body,
                headers: {'content-type': 'application/json'},
                redirect: 'follow'
            };

            fetch("http://127.0.0.1:8000/presentation/", requestOptions)
            .then(response => response.blob())
  .then(blob => {
    const downloadLink = document.createElement('a');
    downloadLink.href = URL.createObjectURL(blob);
    downloadLink.download = 'your-filename.pptx'; // Change the filename as needed

    document.body.appendChild(downloadLink);
    downloadLink.click();
    document.body.removeChild(downloadLink);
  })
  .catch(error => {
    console.error('Error fetching or downloading the PPTX file:', error);
  })
                // .then(response => response.blob())
                // .then( blob => {
                //     var file = window.URL.createObjectURL(blob)
                //     window.location.assign(file)
                // })
                // .then(result => console.log(result))
                // .catch(error => console.log('error', error));

            // this.$axios.post('http://localhost:8000/presentation/', body).then(
            //     response => {
            //         console.log(response)
            //     }
            // )
        },
        reset: function () {
            this.project_name = '';
            this.short_description = '';
            this.problem = [
                {
                    target_audience: '',
                    issue: [''],
                    solution: [''],
                }
            ];
            this.description = '';
            this.clients = [''];
            this.revenue = 0;
            this.revenue_suffix = '';
            this.clients_count = 0;
            this.churn_rate = 0;
            this.inn = "";
        }
    },
    components: { NavButton }
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

.button-gradient {
    min-height: 40px;
    background: linear-gradient(to bottom right, var(--colour-decoration), var(--colour-decoration-alt));
    background-size: 200% 200%;
    color: #FFFFFF;
    animation: button-hover-exit-anim ease-out;
    animation-duration: .5s;
    animation-direction: normal;
    animation-fill-mode: forwards;
    transition: .5s;
}
.button-gradient:hover {
    animation: button-hover-anim ease-out;
    animation-duration: .5s;
    animation-direction: normal;
    animation-fill-mode: forwards;
}
.button-gradient:active {
    filter: brightness(80%);
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

@media screen and (max-width: 600px) {
    #header-nav { display: none; }
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
    width: 60%;
    padding-left: 10px;
    margin-bottom: 6px;
    border-bottom: 2px solid var(--colour-decoration);
    font-size: 110%;
    font-style: italic;
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

.slide input[type="number"] {
    flex-shrink: 1;
    appearance: none;
}
.slide input[type="number"]::-webkit-outer-spin-button,
.slide input[type="number"]::-webkit-inner-spin-button {
    appearance: none;
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
.input-with-controls button > div {
    display: flex;
    justify-content: center;
    align-items: center;
    position: absolute;
    top: 0;
    right: 0;
    width: 38px;
    height: 38px;
}

.input-with-controls button:hover {
    width: 400px;
    border: 1px solid var(--colour-decoration);
    background-color: var(--colour-decoration-light);
}


.controls-red-button:hover {
    background-color: #e290af !important;
    color: #000000 !important;
}
.controls-green-button:hover {
    background-color: #90e2bc !important;
    color: #000000 !important;
}


.input-number-with-controls {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
}

.input-number-with-controls input {
    flex-shrink: 1;
}

.input-number-with-controls div {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    gap: 0;
    box-sizing: border-box;
    width: 80px;
    min-width: 80px;
    height: 40px;
    min-height: 40px;
    border: 1px dashed var(--colour-decoration-alt);
    border-radius: 666px;
    background-color: var(--colour-back);
    overflow: hidden;
    background-clip: border-box;
    color: var(--colour-front);
    transition: .25s;
}
.input-number-with-controls div button {
    display: flex;
    justify-content: center;
    align-items: center;
    box-sizing: border-box;
    width: 40px;
    min-width: 40px;
    height: 40px;
    min-height: 40px;
    background-color: var(--colour-back);
    color: var(--colour-front);
    cursor: pointer;
    transition: .25s;
}

.input-number-with-controls div button:first-child {
    border-radius: 666px 0 0 666px;
}

.input-number-with-controls div button:last-child {
    border-radius: 0 666px 666px 0;
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


.with-margin {
    margin-block: 6px;
}


.slide .input-range {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
}

.slide .input-range input[type='range'] {
    display: flex;
    box-sizing: border-box;
    width: 80%;
    accent-color: var(--colour-decoration);
}

.slide .input-range input[type='number'] {
    display: flex;
    flex-grow: 1;
    box-sizing: border-box;
    width: 50px;
    flex-basis: 50px;
}

.slide .input-options {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
    box-sizing: border-box;
    width: 100%;
    height: 40px;
    border: 1px dashed var(--colour-decoration-alt);
    border-radius: 666px;
    background-color: var(--colour-back);
    background-clip: border-box;
    overflow: hidden;
    position: relative;
    transition: .25s;
}
.slide .input-options:hover {
    border: 1px solid var(--colour-decoration);
    background-color: var(--colour-decoration-light);
}

.slide .input-options > p {
    display: flex;
    flex-grow: 1;
    justify-content: center;
    align-items: center;
    width: 20px;
}
.slide .input-options > span {
    position: absolute;
    top: 0;
    box-sizing: border-box;
    width: calc(50% - 5px);
    height: 38px;
    border-radius: 666px;
    opacity: .45;
    transition: .25s;
}

.slide .input-options > span[data-position="0"] {
    left: 0;
    background-color: #009973;
}
.slide .input-options > span[data-position="1"] {
    left: calc(50% + 5px);
    background-color: #a50066;
}

[disabled] {
    opacity: .5;
}


.small-input {
    width: 120px !important;
    min-width: 120px !important;
}



.slide hr {
    width: 60%;
    height: 4px;
    margin: 20px auto;
    border: none;
    border-radius: 666px;
    background-color: var(--colour-decoration-alt);
}

.slide menu {
    padding: 0 20px;
}


@keyframes button-hover-anim {
    0% { background-position: 10% 0% }
    100% { background-position: 91% 100% }
}
@keyframes button-hover-exit-anim {
    0% { background-position: 91% 100% }
    100% { background-position: 10% 0% }
}

@keyframes button-active-anim {
    0% { background-position: 91% 100% }
    100% { background-position: 10% 100% }
}
</style>
