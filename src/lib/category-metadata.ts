import type { Metadata } from 'next';
import { getTranslations, setRequestLocale } from 'next-intl/server';
import { routing, type Locale } from '@/i18n/routing';
import { getBaseMetadata } from '@/lib/seo';

export async function generateCategoryMetadata(
  localeInput: string,
  camel: string,
  slug: string,
  ogImage?: string,
): Promise<Metadata> {
  const locale: Locale = routing.locales.includes(localeInput as Locale)
    ? (localeInput as Locale)
    : routing.defaultLocale;
  setRequestLocale(locale);
  const t = await getTranslations();
  const navKey = t.has(`nav_${camel}`) ? `nav_${camel}` : 'nav_home';
  const descKey = `page_${camel}_description`;
  const kwKey = `page_${camel}_keywords`;
  const description = t.has(descKey) ? t(descKey) : t('site_description');
  const kwRaw = t.has(kwKey) ? t(kwKey) : '';
  const keywords = kwRaw
    ? (kwRaw as string)
        .split(',')
        .map((s) => s.trim())
        .filter(Boolean)
    : undefined;
  return getBaseMetadata(
    slug.startsWith('/') ? slug : `/${slug}`,
    locale,
    t(navKey),
    description,
    'website',
    ogImage,
    keywords,
    { category: camel },
  );
}
