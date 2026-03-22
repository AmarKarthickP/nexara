<template>
    <div class="text-[#1b2133]">
        <p class="font-semibold text-3xl text-center">
            {{ greeting }},
            <span class="font-medium bg-gradient-to-r from-cyan-400 via-blue-500 to-fuchsia-500 bg-clip-text text-transparent">
                {{ first_name }}
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
import { ref, computed, onMounted } from 'vue';
import ChatBox from '@/components/ChatBox.vue';
import { getUserInfo, getUserSettings } from '@/services/user';

const now = ref(new Date());
const first_name = ref("");
let sidebar = ref("");

const greeting = computed(() => {
  const hours = now.value.getHours();
  if (hours < 12) return 'Good morning';
  if (hours < 17) return 'Good afternoon';
  return 'Good evening';
});

onMounted(async () => {
  try {
    const user_info = await getUserInfo();
    first_name.value = user_info.first_name || "User";
  } catch (e) {
    first_name.value = "User";
  }

  try {
    const user_settings = await getUserSettings();
    console.log(user_settings);
    first_name.value = user_settings.first_name || "User";
    sidebar.value = user_settings.first_name;
  } catch (e) {
    // first_name.value = "User";
  }
});
</script>