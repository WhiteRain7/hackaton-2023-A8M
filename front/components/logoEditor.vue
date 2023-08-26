<template>
    <dialog id="logo-panel">
        <section>
            <div>
            <div>
                <div>
                <div>
                    <span>Global</span>
                    <button type="button" data-toggle="collapse" data-target="#global-fieldset"
                    aria-expanded="true" aria-controls="global-fieldset"><i aria-hidden="true"></i></button>
                </div>
                <div id="global-fieldset">
                    <div>
                    <div>
                        <span id="basic-addon1">Layout</span>
                    </div>
                    <input type="checkbox" checked data-toggle="toggle" data-on="Horizontal"
                        data-off="Vertical" data-onstyle="outline-dark" data-offstyle="outline-secondary" data-size="sm"
                        data-param="layout" data-component="global" id="layout-toggle">
                    </div>
                    <div>
                    <div>
                        <span id="basic-addon1">Shapes</span>
                    </div>
                    <input type="checkbox" checked data-toggle="toggle" data-on="On" data-off="Off"
                        data-onstyle="outline-dark" data-offstyle="outline-secondary" data-size="sm" data-param="shapes"
                        data-component="global" id="shapes-toggle">
                    </div>
                    <div>
                    <div>
                        <span id="basic-addon1">Offset</span>
                    </div>
                    <input type="color" id="offset-clr" value="#f2f2f2" aria-label="color"
                        aria-describedby="basic-addon1" data-param="offsetColor" data-component="global"/>
                    <input type="range" data-param="offsetSize"
                        data-component="global" value="0" min="0" max="10" step=".5" id="offset_size-rng" />
                    <div data-display="value">
                        <span id="offset_size-value">0</span>
                    </div>
                    </div>
                </div>
                </div>
            </div>

            <div>
                <div>
                <div>
                    <span>Icon</span>
                    <button type="button" data-toggle="collapse" data-target="#icon-fieldset"
                    aria-expanded="true" aria-controls="icon-fieldset"><i aria-hidden="true"></i></button>
                </div>
                <div id="icon-fieldset">
                    <div>
                    <div>
                        <span id="basic-addon1">Icon</span>
                    </div>
                    <div>
                        <div>
                        <button id="icp-component" type="button"
>
                            <i aria-hidden="true"></i>
                        </button>
                        <button id="icp" type="button" data-selected="fa-car"
                            data-toggle="dropdown">
                            <span></span>
                            <span>Toggle Dropdown</span>
                        </button>
                        <div></div>
                        </div>
                    </div>
                    </div>
                    <div>
                    <div>
                        <span id="basic-addon1">Size</span>
                    </div>
                    <input type="range" value="48" min="25" max="100" step="1"
                        id="icon-sz" data-param="fontSize" data-component="icon" />
                    <div data-display="value">
                        <span id="icon_size-value">48</span>
                    </div>
                    </div>
                    <div>
                    <div>
                        <span id="basic-addon1">Color</span>
                    </div>
                    <input type="color" id="icon-clr" aria-label="color"
                        aria-describedby="basic-addon1" data-param="color" data-component="icon" />
                    </div>
                </div>
                </div>
            </div>
            </div>

            <div>
            <div>
                <span>Main</span>
                <button type="button" data-toggle="collapse" data-target="#main-fieldset"
                aria-expanded="true" aria-controls="main-fieldset"><i aria-hidden="true"></i></button>
            </div>
            <div id="main-fieldset">
                <div>
                <div>
                    <span id="basic-addon1">Text</span>
                </div>
                <input type="text" id="main-input" aria-label="outblock"
                    aria-describedby="basic-addon1" data-param="text" data-component="main" />
                </div>
                <div>
                <div>
                    <span id="basic-addon1">Font</span>
                </div>
                <input type="color" id="main-clr" aria-label="color" aria-describedby="basic-addon1"
                    data-param="color" data-component="main" />
                <select id="main_font-select" aria-label="font" aria-describedby="basic-addon1"
                    data-param="fontFamily" data-component="main"></select>
                <input type="checkbox" checked data-toggle="toggle" data-on="Bold" data-off="Normal"
                    data-onstyle="outline-dark" data-offstyle="outline-secondary" data-size="sm" data-param="font_weight"
                    data-component="main" id="main_weight-toggle">
                </div>
                <div>
                <div>
                    <div>
                    <span id="basic-addon1">Size</span>
                    </div>
                    <input type="range" value="48" min="10" max="100" step="1"
                    id="main-sz" data-param="fontSize" data-component="main" />
                    <div data-display="value">
                    <span id="main_size-value">48</span>
                    </div>
                </div>
                <div>
                    <div>
                    <span id="basic-addon1">Letter spacing</span>
                    </div>
                    <input type="range" data-param="letter_space" data-component="main"
                    value="0" min="0" max="20" step="1" id="main_letter_space-rng" />
                    <div data-display="value">
                    <span id="main_letter_space-value">0</span>
                    </div>
                </div>
                </div>
            </div>
            </div>

            <div>
            <div>
                <span>Accent</span>
                <button type="button" data-toggle="collapse" data-target="#accent-fieldset"
                aria-expanded="true" aria-controls="accent-fieldset"><i aria-hidden="true"></i></button>
            </div>
            <div id="accent-fieldset">
                <div>
                <div>
                    <span id="basic-addon1">Text</span>
                </div>
                <input type="text" id="accent-input" aria-label="inblock"
                    aria-describedby="basic-addon1" data-param="text" data-component="accent" />
                </div>
                <div>
                <div>
                    <span id="basic-addon1">Font</span>
                </div>
                <input type="color" value="#cccccc" id="accent-clr" aria-label="color2"
                    aria-describedby="basic-addon1" data-param="color" data-component="accent" />
                <select id="accent_font-select" aria-label="font"
                    aria-describedby="basic-addon1" data-param="fontFamily" data-component="accent"></select>
                <input type="checkbox" checked data-toggle="toggle" data-on="Bold" data-off="Normal"
                    data-onstyle="outline-dark" data-offstyle="outline-secondary" data-size="sm" data-param="font_weight"
                    data-component="accent" id="accent_weight-toggle">
                </div>
                <div>
                <div>
                    <div>
                    <span id="basic-addon1">Size</span>
                    </div>
                    <input type="range" value="48" min="10" max="100" step="1"
                    id="accent-sz" data-param="fontSize" data-component="accent" />
                    <div data-display="value">
                    <span id="accent_size-value">48</span>
                    </div>
                </div>
                <div>
                    <div>
                    <span id="basic-addon1">Letter spacing</span>
                    </div>
                    <input type="range" data-param="letter_space" data-component="accent"
                    value="0" min="0" max="20" step="1" id="accent_letter_space-rng" />
                    <div data-display="value">
                    <span id="accent_letter_space-value">0</span>
                    </div>
                </div>
                </div>
                <div>
                <div>
                    <span id="basic-addon1">Effects</span>
                </div>
                <div role="group" aria-label="Basic example">
                    <a id="compliment_color-btn">Compliment Color</a>
                </div>
                </div>
            </div>
            </div>

            <section>
            <div id="fav-container">
                <p>Favicon</p>
                <canvas id="fav-canvas" style="border: none solid #d3d3d3"></canvas>
            </div>
            <div id="logo-container">
                <p>Logo</p>
                <canvas id="logo-canvas" style="border: none solid #d3d3d3"></canvas>
            </div>
            </section>

            <div role="toolbar" aria-label="Toolbar with button groups">
            <div>
                <div>
                <div>Format</div>
                </div>
                <select id="export_format-select" aria-label="format"
                aria-describedby="basic-addon1">
                <option value="image/png">png</option>
                <option value="image/jpeg">jpg</option>
                <option value="image/webp">webp</option>
                <option value="image/svg+xml">svg</option>
                </select>
            </div>
            <div role="group" aria-label="First group">
                <a href="#" id="fav_download-btn" download="favicon.png">Download
                favicon</a>
                <a href="#" id="logo_download-btn" download="logo.png">Download
                logo</a>
            </div>
            </div>

            <div>
            <div>
                <div>
                <span>Export Configuration</span>
                <button type="button" data-toggle="collapse" data-target=".imp_exp_conf"
                    aria-expanded="false" aria-controls="exp_conf-fieldset imp_conf-fieldset"><i
 aria-hidden="true"></i></button>
                </div>
                <div id="exp_conf-fieldset">
                <div>
                    <div>
                    <div>Export</div>
                    </div>
                    <div>
                    <a href="#" id="conf_download-btn"
                        download="simplegen.json">Download
                        Configuration</a>
                    </div>
                </div>
                </div>
            </div>

            <div>
                <div>
                <span>Import Configuration</span>
                <button type="button" data-toggle="collapse" data-target=".imp_exp_conf"
                    aria-expanded="false" aria-controls="exp_conf-fieldset imp_conf-fieldset"><i
 aria-hidden="true"></i></button>
                </div>
                <div id="imp_conf-fieldset">
                <div>
                    <input type="file" id="conf_upload-fs" accept=".json">
                    <label for="conf_upload-fs">Choose file</label>
                </div>
                </div>
            </div>
            </div>

            <div role="alert">
            If things aren't working, sorry, use Chrome or Firefox...
            </div>
        </section>

        <script
            src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
            integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
            crossorigin="anonymous"
        ></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
            integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1"
            crossorigin="anonymous"
        ></script>
        <script
            src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
            integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM"
            crossorigin="anonymous"
        ></script>
        <script
            src="https://cdn.jsdelivr.net/gh/Scalesoft/fontawesome-iconpicker@393acfd/dist/js/fontawesome-iconpicker.min.js"
            crossorigin="anonymous"
            referrerpolicy="no-referrer"
        ></script>
        <script
            src="https://cdn.jsdelivr.net/npm/bs-darkmode@1.2.0/js/bs-darkmodejquery.min.js"
            integrity="sha256-F2n4uDLTOf7uGUhhaW0zzfed4SPHEToImxLu3FHaga8="
            crossorigin="anonymous"
        ></script>
        <script
            src="https://cdn.jsdelivr.net/npm/bootstrap5-toggle@3.7.3/js/bootstrap5-toggle.min.js"
            integrity="sha256-ctgYdt/F2ief8nbGZXReoYssWvM5rSwz6sS0CFcyy2c="
            crossorigin="anonymous"
        ></script>
        <script
            src="https://cdn.jsdelivr.net/npm/bs-custom-file-input@1.3.4/dist/bs-custom-file-input.min.js"
        ></script>
        <script
            src="https://cdn.jsdelivr.net/npm/canvas2svg-visjs@1.0.21/canvas2svg.min.js"
        ></script>
        <script
            src="https://cdnjs.cloudflare.com/ajax/libs/showdown/2.1.0/showdown.min.js"
            integrity="sha512-LhccdVNGe2QMEfI3x4DVV3ckMRe36TfydKss6mJpdHjNFiV07dFpS2xzeZedptKZrwxfICJpez09iNioiSZ3hA=="
            crossorigin="anonymous" referrerpolicy="no-referrer"
        ></script>
    </dialog>
</template>


<script>
import 'https://cdnjs.cloudflare.com/ajax/libs/showdown/2.1.0/showdown.min.js'
import * as simplegen from '~/static/simplegen'

export default {
    name: 'logoEditor',

    methods: {
        show_logo_editor: function () {
            document.getElementById('logo-panel').showModal();
        }
    }
}
</script>

<style scoped>
#logo-panel:not([open]) {
    display: none !important;
}

#logo-panel {
    display: flex;
    flex-direction: column;
    flex-wrap: nowrap;
    margin: auto;
    box-sizing: border-box;
    width: 90%;
    max-width: 900px;
    height: 90%;
    border: 3px solid var(--colour-decoration-alt);
    border-radius: 20px;
    background-color: var(--colour-back);
    background-clip: border-box;
    z-index: 100;
}
#logo-panel::backdrop {
    background-color: #272a2c;
    opacity: .8;
}
</style>
