<template>
    <div class="relative bg-white mt-10 rounded-xl min-h-20">
        <svg class="absolute inset-0 w-full h-full pointer-events-none overflow-visible">
            <defs>
                <linearGradient id="borderGradient" x1="0%" y1="0%" x2="100%" y2="0%">
                    <stop offset="0%" stop-color="#22d3ee" />
                    <stop offset="50%" stop-color="#3b82f6" />
                    <stop offset="100%" stop-color="#d946ef" />
                </linearGradient>

                <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
                    <feGaussianBlur stdDeviation="3" result="blur" />
                    <feComposite in="SourceGraphic" in2="blur" operator="over" />
                </filter>
            </defs>

            <rect x="1" y="1" width="calc(100% - 2px)" height="calc(100% - 2px)" rx="12" ry="12" class="fill-transparent stroke-gray-100 stroke-[1px]" />

            <rect x="1" y="1" width="calc(100% - 2px)" height="calc(100% - 2px)" rx="12" ry="12" pathLength="100" filter="url(#glow)" class="animating-rect fill-transparent stroke-[url(#borderGradient)] stroke-[4px]" />
        </svg>
        <div class="relative bg-white rounded-xl min-h-20 p-2 border border-gray-100 shadow-sm">
            <textarea ref="textarea" v-model="message" rows="1" placeholder="Ask anything..." class="w-full bg-transparent px-5 mt-1 outline-none resize-none overflow-y-auto max-h-60 break-words" @input="autoResize"></textarea>

            <!-- Chatbox Menu -->
            <div class="flex mt-3 px-5 text-lg">
                <h4 class="font-medium">
                    Nexara
                </h4>
                <h1 class="font-medium bg-gradient-to-r from-cyan-400 via-blue-500 to-fuchsia-500 bg-clip-text text-transparent">
                    .ai
                </h1>

                <div class="flex ml-auto gap-3">
                    <!-- Add New... -->
                    <button @click.stop="showAddMenuOptions=!showAddMenuOptions; showDictateOptions=false" 
                        class="cursor-pointer hover:bg-[#f5f4f2] hover:rounded-md px-1.5 py-1.5 transition-all duration-300 ease-in-out"
                        :class="{'bg-gray-200 rounded-md': showAddMenuOptions}"
                    >
                        <img src="../assets/icons/plus(1).png" alt="dictate" class="h-4" />
                    </button>
                    <!-- Dictate -->
                    <button 
                        v-show="!message" 
                        @click.stop="showDictateOptions=!showDictateOptions; showAddMenuOptions=false" 
                        class="cursor-pointer hover:bg-[#f5f4f2] hover:rounded-md px-1.5 py-1.5 transition-all duration-300 ease-in-out"
                        :class="{'bg-gray-200 rounded-md': showDictateOptions}"
                    >
                        <img src="../assets/icons/mic.png" alt="dictate" class="h-4 w-5" />
                    </button>
                    <!-- Send -->
                    <button v-show="message" @click="showDictateOptions=false" class="cursor-pointer hover:bg-gray-200 bg-[#f5f4f2] rounded-md px-1.5 py-1.5 transition-all duration-300 ease-in-out">
                        <img src="../assets/icons/top.png" alt="dictate" class="h-4 w-5" />
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!-- Add New Section -->
    <transition name="bounce">
        <div v-if="showAddMenuOptions" v-click-outside="closePopups" class="absolute left-[58%] z-30 bg-white rounded-lg w-[15%] ml-7 mt-1 px-3 py-3">
            <button class="flex gap-3 hover:bg-[#f5f4f2] w-full transition-all duration-300 ease-in-out px-2 py-1 rounded-lg cursor-pointer">
                <img src="../assets/icons/attach-file.png" alt="new-conversation" class="h-5" />
                Upload
            </button>
            <button class="flex gap-3 hover:bg-[#f5f4f2] w-full transition-all duration-300 ease-in-out px-2 py-1 rounded-lg cursor-pointer">
                <img src="../assets/icons/pen.png" alt="new-conversation" class="h-5" />
                New Conversation
            </button>
        </div>
    </transition>

    <!-- Dictate Section -->
    <transition name="bounce">
        <div v-if="showDictateOptions" v-click-outside="closePopups" class="absolute left-[64%] z-30 bg-white rounded-lg w-[15%] ml-7 mt-1 px-3 py-3">
            <p class="flex gap-3 text-[Red] transition-all duration-300 ease-in-out px-2 py-1 rounded-lg cursor-not-allowed">
                <img src="../assets/icons/exclamation-mark.png" alt="warning" class="h-5" />
                Comming Soon
            </p>
        </div>
    </transition>
</template>

<script setup>
import {
    onMounted,
    ref,
    nextTick
} from 'vue';

const message = ref('')
const textarea = ref(null)
const showAddMenuOptions = ref(false)
const showDictateOptions = ref(false)

const closePopups = ()=> {
    showAddMenuOptions.value = false;
    showDictateOptions.value = false;
}

const autoResize = () => {
    textarea.value.style.height = 'auto'
    textarea.value.style.height = textarea.value.scrollHeight + 'px'
}

onMounted(() => {
    nextTick(() => autoResize())
})
</script>

<style scoped>
    .animating-rect {
        /* summ of stroke-dasharray should be 100 */
        stroke-dasharray: 10 90;
        animation: border-chase 6s linear infinite;
        stroke-linecap: round;
    }
    @keyframes border-chase {
        from {
            stroke-dashoffset: 100;
        }

        to {
            stroke-dashoffset: 0;
        }
    }
    /* Dropdown bounce in animation */
    .bounce-enter-active {
        animation: bounce-in 0.5s;
    }
    @keyframes bounce-in {
        0% {
            transform: scale(0);
        }
        50% {
            transform: scale(1);
        }
        100% {
            transform: scale(1);
        }
    }
</style>