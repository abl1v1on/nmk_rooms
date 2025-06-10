import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'


export default defineConfig({
  plugins: [react()],
  server: {
    allowedHosts: [
      '50f8-77-238-239-82.ngrok-free.app'
    ]
  }
})
