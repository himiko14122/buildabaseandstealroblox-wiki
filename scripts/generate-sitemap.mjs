import fs from 'fs';
import path from 'path';

const SITE_URL = 'https://buildabaseandstealroblox.wiki';
const LOCALES = ['en', 'ko', 'ja', 'de'];
const routing_defaultLocale = 'en';
const CONTENT_TYPES = [
  'codes', 'beginner-guide', 'pet-rolling', 'base-defense', 'raiding',
  'offline-money', 'pets-list', 'gear', 'strategies', 'faq', 'updates',
  'community', 'guides', 'categories'
];
const NAV_PAGES = [
  { path: '/', priority: 1, changefreq: 'daily' },
  { path: '/codes', priority: 0.9, changefreq: 'daily' },
  { path: '/beginner-guide', priority: 0.9, changefreq: 'weekly' },
  { path: '/pet-rolling', priority: 0.9, changefreq: 'weekly' },
  { path: '/base-defense', priority: 0.9, changefreq: 'weekly' },
  { path: '/raiding', priority: 0.9, changefreq: 'weekly' },
  { path: '/offline-money', priority: 0.8, changefreq: 'weekly' },
  { path: '/pets-list', priority: 0.8, changefreq: 'weekly' },
  { path: '/gear', priority: 0.8, changefreq: 'weekly' },
  { path: '/strategies', priority: 0.8, changefreq: 'weekly' },
  { path: '/faq', priority: 0.7, changefreq: 'weekly' },
  { path: '/updates', priority: 0.7, changefreq: 'weekly' },
  { path: '/community', priority: 0.7, changefreq: 'weekly' },
  { path: '/guides', priority: 0.9, changefreq: 'weekly' },
  { path: '/about', priority: 0.7, changefreq: 'monthly' },
  { path: '/sitemap', priority: 0.5, changefreq: 'monthly' },
  { path: '/privacy-policy', priority: 0.4, changefreq: 'yearly' },
  { path: '/terms-of-service', priority: 0.4, changefreq: 'yearly' },
];

function localizedPath(locale, p) {
  if (locale === 'en') {
    if (p === '/') return '/';
    return `/en${p}/`;
  }
  return p === '/' ? `/${locale}/` : `/${locale}${p}/`;
}

const manifestPath = path.join(process.cwd(), 'src', 'lib', 'content-manifest.json');
let contentPaths = [];
if (fs.existsSync(manifestPath)) {
  const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf-8'));
  contentPaths = manifest.contentPaths || [];
}

const now = new Date().toISOString().split('T')[0];
const urls = [];

for (const page of NAV_PAGES) {
  for (const locale of LOCALES) {
    const lp = localizedPath(locale, page.path);
    const allAlternates = LOCALES.map((l) => {
      const alp = localizedPath(l, page.path);
      return `    <xhtml:link rel="alternate" hreflang="${l}" href="${SITE_URL}${alp}" />`;
    }).join('\n');
    const defaultLp = localizedPath(routing_defaultLocale, page.path);
    const xDefault = `    <xhtml:link rel="alternate" hreflang="x-default" href="${SITE_URL}${defaultLp}" />`;
    urls.push(`  <url>
    <loc>${SITE_URL}${lp}</loc>
    <lastmod>${now}</lastmod>
    <changefreq>${page.changefreq}</changefreq>
    <priority>${page.priority}</priority>
${allAlternates}
${xDefault}
  </url>`);
  }
}

for (const item of contentPaths) {
  if (item.locale !== routing_defaultLocale) continue;
  const contentPath = `/${item.contentType}/${item.slug}`;
  const lp = localizedPath(routing_defaultLocale, contentPath);
  const allAlternates = LOCALES.map((l) => {
    const alp = localizedPath(l, contentPath);
    return `    <xhtml:link rel="alternate" hreflang="${l}" href="${SITE_URL}${alp}" />`;
  }).join('\n');
  const defaultLp = localizedPath(routing_defaultLocale, contentPath);
  const xDefault = `    <xhtml:link rel="alternate" hreflang="x-default" href="${SITE_URL}${defaultLp}" />`;
  urls.push(`  <url>
    <loc>${SITE_URL}${lp}</loc>
    <lastmod>${now}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
${allAlternates}
${xDefault}
  </url>`);
}

const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
${urls.join('\n')}
</urlset>`;

const outputPath = path.join(process.cwd(), 'public', 'sitemap.xml');
fs.writeFileSync(outputPath, xml);
console.log(`Sitemap generated: ${urls.length} URLs`);
