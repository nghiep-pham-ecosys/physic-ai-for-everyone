// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import starlightLinksValidator from 'starlight-links-validator';

export default defineConfig({
  integrations: [
    starlight({
      title: 'Physical AI for Everyone',
      // English is the default locale and is served at the root (ADR-2).
      defaultLocale: 'root',
      locales: {
        root: { label: 'English', lang: 'en' },
        vi: { label: 'Tiếng Việt', lang: 'vi' },
      },
      // Fails the build on broken internal links.
      plugins: [starlightLinksValidator()],
      // Architecture §5. Lessons and Project groups are added when they have pages.
      sidebar: [
        {
          label: 'Start here',
          translations: { vi: 'Bắt đầu' },
          items: ['start-here/about', 'start-here/setup', 'start-here/how-to-use'],
        },
        {
          label: 'Reference',
          translations: { vi: 'Tham khảo' },
          items: ['reference/glossary'],
        },
      ],
    }),
  ],
});
