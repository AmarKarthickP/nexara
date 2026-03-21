<template>
    <div class="text-[#1b2133]">
        <p class="font-semibold text-3xl text-center">
            Good evening,
            <span class="font-medium bg-gradient-to-r from-cyan-400 via-blue-500 to-fuchsia-500 bg-clip-text text-transparent">
                Amar
            </span>
            <br>
            What can I help you with today?
        </p>
        
        <!-- Chatbox section -->
        <chat-box />

        <!-- Get into section -->
        <div class="flex relative gap-5 mt-8">
            <button class="bg-gray-200 text-sm rounded-full py-1.5 px-3 opacity-50 hover:bg-white hover:opacity-100 font-medium transition-all duration-300 ease-in-out">
                Check attendance
            </button>
            <button class="bg-gray-200 text-sm rounded-full py-1.5 px-3 opacity-50 hover:bg-white hover:opacity-100 font-medium transition-all duration-300 ease-in-out">
                Approve leaves
            </button>
            <button class="bg-gray-200 text-sm rounded-full py-1.5 px-3 opacity-50 hover:bg-white hover:opacity-100 font-medium transition-all duration-300 ease-in-out">
                Create a report
            </button>
            <button class="bg-gray-200 text-sm rounded-full py-1.5 px-3 opacity-50 hover:bg-white hover:opacity-100 font-medium transition-all duration-300 ease-in-out">
                Make a plan
            </button>
            <button class="bg-gray-200 text-sm rounded-full py-1.5 px-3 opacity-50 hover:bg-white hover:opacity-100 font-medium transition-all duration-300 ease-in-out">
                Get help
            </button>
        </div>
    </div>

</template>

<script setup lang="ts">
import ChatBox from '@/components/ChatBox.vue';

</script>
