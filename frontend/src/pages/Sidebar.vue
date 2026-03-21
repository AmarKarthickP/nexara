<template>
    <!-- New Dropdown -->
    <transition name="bounce">
        <div v-if="showDropdown" v-click-outside="closeDropdown" ref="dropdownRef" class="bg-white rounded-lg  ml-7 mt-5 px-3 py-3">
            <button class="flex gap-3 hover:bg-[#f5f4f2] w-full transition-all duration-300 ease-in-out px-2 py-1 rounded-lg cursor-pointer">
                <img src="../assets/icons/pen.png" alt="new-conversation" class="h-5" />
                New Conversation
            </button>
            <button class="flex gap-3 w-full mt-1 hover:bg-[#f5f4f2] transition-all duration-300 ease-in-out px-2 py-1 rounded-lg cursor-pointer">
                <img src="../assets/icons/copy-writing.png" alt="new-conversation" class="h-5" />
                New Page
            </button>
        </div>
    </transition>

    <!-- History -->
    <transition name="nested">
        <div v-if="showSidebar">
            <div class="bg-white rounded-lg  ml-7 mt-5 px-3 py-3 outer text-[#1b2133]">
                <div>
                    <p class="font-medium mt-2">Pages</p>
                    <div class="inner mt-1">
                        <p class="hover:bg-[#f5f4f2] transition-all duration-300 ease-in-out py-1 px-2 cursor-pointer rounded-lg">page 1</p>
                        <p class="hover:bg-[#f5f4f2] transition-all duration-300 ease-in-out py-1 px-2 cursor-pointer rounded-lg">page 2</p>
                        <p class="hover:bg-[#f5f4f2] transition-all duration-300 ease-in-out py-1 px-2 cursor-pointer rounded-lg">page 3</p>
                        <p class="hover:bg-[#f5f4f2] transition-all duration-300 ease-in-out py-1 px-2 cursor-pointer rounded-lg">page 4</p>
                    </div>
                </div>

                <div>
                    <p class="font-medium mt-3">Conversions</p>
                    <div class="inner mt-1">
                        <!-- Today -->
                        <p class="text-sm text-gray-600 transition-all duration-300 ease-in-out py-1 px-2 rounded-lg">Today</p>
                        <p class="hover:bg-[#f5f4f2] transition-all duration-300 ease-in-out py-1 px-2 cursor-pointer rounded-lg">conversation 1</p>
                        <p class="hover:bg-[#f5f4f2] transition-all duration-300 ease-in-out py-1 px-2 cursor-pointer rounded-lg">conversation 2</p>

                        <!-- Yesterday -->
                        <p class="text-sm text-gray-600 transition-all duration-300 ease-in-out py-1 px-2 rounded-lg">Yesterday</p>
                        <p class="hover:bg-[#f5f4f2] transition-all duration-300 ease-in-out py-1 px-2 cursor-pointer rounded-lg">conversation 3</p>
                        <p class="hover:bg-[#f5f4f2] transition-all duration-300 ease-in-out py-1 px-2 cursor-pointer rounded-lg">conversation 4</p>

                        <!-- Older -->
                        <p class="text-sm text-gray-600 transition-all duration-300 ease-in-out py-1 px-2 rounded-lg">Older</p>
                        <p class="hover:bg-[#f5f4f2] transition-all duration-300 ease-in-out py-1 px-2 cursor-pointer rounded-lg">conversation 5</p>
                        <p class="hover:bg-[#f5f4f2] transition-all duration-300 ease-in-out py-1 px-2 cursor-pointer rounded-lg">conversation 6</p>
                        <p class="hover:bg-[#f5f4f2] transition-all duration-300 ease-in-out py-1 px-2 cursor-pointer rounded-lg">conversation 7</p>
                        <p class="hover:bg-[#f5f4f2] transition-all duration-300 ease-in-out py-1 px-2 cursor-pointer rounded-lg">conversation 8</p>
                    </div>
                </div>
            </div>
            <div class="bg-white rounded-lg  ml-7 mt-5 px-3 py-3 outer text-[#1b2133]">
                <div class="flex gap-3 cursor-pointer rounded-lg inner">
                    <img class="w-10 h-10 rounded-full" src="../assets/icons/empty-male-avatar.jpg" alt="profile" />
                    <div>
                        <p>Amar Karthick P</p>
                        <p class="text-sm">Free Plan</p>
                    </div>
                </div>
            </div>
        </div>
    </transition>
</template>

<script setup>
import { ref } from 'vue';

const showDropdown = ref(false);
const showSidebar = ref(false);

const closeDropdown = ()=> {
    showDropdown.value = false;
};
</script>

<style scoped>
/* Nested Fade */

.nested-enter-active,
.nested-leave-active {
    transition: all 0.3s ease-in-out;
}

/* delay leave of parent element */
.nested-leave-active {
    transition-delay: 0.25s;
}

.nested-enter-from,
.nested-leave-to {
    transform: translateY(30px);
    opacity: 0;
}

/* we can also transition nested elements using nested selectors */
.nested-enter-active .inner,
.nested-leave-active .inner {
    transition: all 0.3s ease-in-out;
}

/* delay enter of nested element */
.nested-enter-active .inner {
    transition-delay: 0.25s;
}

.nested-enter-from .inner,
.nested-leave-to .inner {
    transform: translateX(30px);
    /*
Hack around a Chrome 96 bug in handling nested opacity transitions.
This is not needed in other browsers or Chrome 99+ where the bug
has been fixed.
*/
    opacity: 0.001;
}
</style>