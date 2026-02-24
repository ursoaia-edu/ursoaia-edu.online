import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap';
import node from '@astrojs/node';

export default defineConfig({
    output: 'server',
    adapter: node({
        mode: 'standalone'
    }),
    site: 'https://ursoaia-edu.online',
    integrations: [tailwind(), sitemap()],
    build: {
        format: 'directory'
    },
    server: {
        port: 4321,
        host: true
    }
});
