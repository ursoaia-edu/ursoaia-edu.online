import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
    output: 'static',
    site: 'https://ursoaia-edu.online',
    integrations: [tailwind()],
    build: {
        format: 'directory'
    },
    server: {
        port: 4321,
        host: true
    }
});