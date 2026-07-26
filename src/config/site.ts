import { routing, type Locale } from '@/i18n/routing';

export const SITE_URL = process.env.NEXT_PUBLIC_SITE_URL || 'https://buildabaseandstealroblox.wiki';
export const SITE_NAME = 'Build a Base and Steal Wiki';
export const HERO_IMAGE = '/images/hero.webp';
export const LOGO_IMAGE = '/favicon.svg';
export const TWITTER_HANDLE = 'BuildBaseSteal';
export const GA_TRACKING_ID = 'G-LC9021XYBB';
export const SLUG_PREFIX = 'buildabaseandstealroblox-';

export const EXTERNAL_LINKS = {
  roblox: 'https://www.roblox.com/games/132016691802922/Build-a-Base-and-Steal',
  discord: 'https://discord.gg/buildabaseandsteal',
  youtube: 'https://youtube.com/@replayablefungames',
  wiki: 'https://buildabaseandsteal.wiki/',
  twitter: 'https://x.com/buildabasesteal',
  website: 'https://www.roblox.com/games/132016691802922/Build-a-Base-and-Steal',
} as const;

export function absoluteUrl(path = '/') {
  const normalized = path.startsWith('/') ? path : `/${path}`;
  return `${SITE_URL}${normalized}`;
}

export function localizedPath(locale: Locale | string, path = '/') {
  const normalized = path === '' ? '/' : path.startsWith('/') ? path : `/${path}`;
  if (locale === routing.defaultLocale) {
    return normalized === '/' ? '/' : normalized;
  }
  return normalized === '/' ? `/${locale}` : `/${locale}${normalized}`;
}
