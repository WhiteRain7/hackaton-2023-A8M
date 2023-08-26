<template>
    <button
        type="button"
        :id="'nav-' + nav_id"
        @click="scroll_to(`slide-${nav_id}`)"
        class="nav-button"
        :class="{
            'nav-not-empty': any(checks),
            'nav-fulfilled': all(checks)
        }"
    >
        {{ nav_id }}
    </button>
</template>

<script>
export default {
    name: 'navButton',
    props: ['nav_id', 'checks'],

    methods: {
        any: function (iterable) {
            for (let i = 0; i < iterable.length; i++) {
                if (iterable[i]) return true
            }
            return false
        },

        all: function (iterable) {
            for (let i = 0; i < iterable.length; i++) {
                if (!iterable[i]) return false
            }
            return true
        },

        scroll_to: function (id) {
            try { document.getElementById(id).scrollIntoView({
                behavior: 'smooth',
                block: 'center',
                inline: 'nearest'
            }) } catch {}
        },
    }
}
</script>

<style scoped>
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
button.nav-button:hover {
    background-color: #b3ced6 !important;
}
button.nav-button:hover {
    background-color: #a0b9c0 !important;
}

button.nav-button.nav-not-empty {
    background-color: #c9bd88 !important;
}
button.nav-button.nav-not-empty:hover {
    background-color: #b1a573 !important;
}

button.nav-button.nav-fulfilled {
    background-color: #88c99b !important;
}
button.nav-button.nav-fulfilled:hover {
    background-color: #6cad80 !important;
}
</style>
