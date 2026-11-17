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
      // Architecture §5: one Lessons group per phase.
      sidebar: [
        {
          label: 'Start here',
          translations: { vi: 'Bắt đầu' },
          items: ['start-here/about', 'start-here/setup', 'start-here/how-to-use'],
        },
        {
          label: 'P1: Robot Body',
          translations: { vi: 'P1: Thân robot' },
          items: ['lessons/01-ros2-essentials', 'lessons/02-tf2'],
        },
        {
          label: 'Reference',
          translations: { vi: 'Tham khảo' },
          items: ['reference/glossary'],
        },
        {
          label: 'Project',
          translations: { vi: 'Dự án' },
          items: ['project/roadmap', 'project/lesson-03-plan'],
        },
      ],
    }),
  ],
});
