<template>
  <div class="relative mt-10 w-[140%] -ml-[20%]">
    
    <svg class="absolute inset-0 w-full h-full pointer-events-none overflow-visible">
      <defs>
        <linearGradient id="borderGradient" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#22d3ee" />
          <stop offset="50%" stop-color="#3b82f6" />
          <stop offset="100%" stop-color="#d946ef" />
        </linearGradient>
      </defs>
      
      <rect x="0" y="0" width="100%" height="100%" rx="12" ry="12" 
            class="fill-transparent stroke-gray-100 stroke-[2px]" />

      <rect x="0" y="0" width="100%" height="100%" rx="12" ry="12" 
            pathLength="100"
            class="animating-rect fill-transparent stroke-[url(#borderGradient)] stroke-[3px]" />
    </svg>

    <div class="relative bg-white rounded-xl min-h-20 p-2 border border-gray-100 shadow-sm">
      <textarea
        ref="textarea"
        v-model="message"
        rows="1"
        placeholder="Ask anything..."
        class="w-full bg-transparent px-5 mt-1 outline-none resize-none overflow-y-auto max-h-60 break-words"
      ></textarea>
      
      <div class="flex mt-3 px-5 text-lg">
        <h4 class="font-medium">Nexara</h4>
        <h1 class="font-medium bg-gradient-to-r from-cyan-400 via-blue-500 to-fuchsia-500 bg-clip-text text-transparent">.ai</h1>
        </div>
    </div>
  </div>
</template>

<style scoped>
.animating-rect {
  /* pathLength="100" means the whole perimeter is 100 units. */
  /* 100 / 7 = ~14.28. So dash is 14.28, gap is 85.72 */
  stroke-dasharray: 14.28 85.72;
  animation: border-chase 10s linear infinite;
  stroke-linecap: round; /* Makes the ends of the segment rounded */
}

@keyframes border-chase {
  from {
    stroke-dashoffset: 100;
  }
  to {
    stroke-dashoffset: 0;
  }
}
</style>