import type { Metadata } from 'next';
import { routing, type Locale } from '@/i18n/routing';
import {
  absoluteUrl,
  EXTERNAL_LINKS,
  HERO_IMAGE,
  localizedPath,
  LOGO_IMAGE,
  SITE_NAME,
  SITE_URL,
} from '@/config/site';

export type PageType = 'website' | 'article';

export function getAlternates(path = '/', locale: Locale | string) {
  const languages = Object.fromEntries(
    routing.locales.map((item) => [item, absoluteUrl(localizedPath(item, path))])
  );

  return {
    canonical: absoluteUrl(localizedPath(locale, path)),
    languages: {
      ...languages,
      'x-default': absoluteUrl(localizedPath(routing.defaultLocale, path)),
    },
  };
}

export function getOgLocale(locale: string) {
  if (locale === 'de') return 'de_DE';
  if (locale === 'ru') return 'ru_RU';
  if (locale === 'fr') return 'fr_FR';
  return 'en_US';
}

export function getBaseMetadata(
  path: string,
  locale: Locale | string,
  title: string,
  description: string,
  pageType: PageType = 'website',
  image?: string,
  keywords?: string[],
  extra?: { category?: string; datePublished?: string; dateModified?: string },
): Metadata {
  const ogImage = image ? absoluteUrl(image) : absoluteUrl(HERO_IMAGE);
  const cleanDescription = description?.slice(0, 200);

  return {
    title,
    description: cleanDescription,
    keywords: keywords && keywords.length > 0 ? keywords : undefined,
    authors: [{ name: SITE_NAME, url: SITE_URL }],
    creator: SITE_NAME,
    publisher: SITE_NAME,
    category: extra?.category,
    alternates: getAlternates(path, locale),
    openGraph: {
      title,
      description: cleanDescription,
      url: absoluteUrl(localizedPath(locale, path)),
      siteName: SITE_NAME,
      locale: getOgLocale(locale),
      alternateLocale: routing.locales.map(getOgLocale),
      type: pageType,
      images: [{ url: ogImage, width: 1200, height: 630, alt: title }],
      ...(pageType === 'article' && {
        publishedTime: extra?.datePublished,
        modifiedTime: extra?.dateModified || extra?.datePublished,
      }),
    },
    twitter: {
      card: 'summary_large_image',
      title,
      description: cleanDescription,
      images: [ogImage],
    },
    robots: {
      index: true,
      follow: true,
      googleBot: {
        index: true,
        follow: true,
        'max-video-preview': -1,
        'max-image-preview': 'large',
        'max-snippet': -1,
      },
    },
  };
}

export function organizationJsonLd() {
  return {
    '@context': 'https://schema.org',
    '@type': 'Organization',
    name: SITE_NAME,
    url: SITE_URL,
    logo: absoluteUrl(LOGO_IMAGE),
    image: absoluteUrl(HERO_IMAGE),
    sameAs: [EXTERNAL_LINKS.discord, EXTERNAL_LINKS.youtube, EXTERNAL_LINKS.roblox],
  };
}

export function websiteJsonLd() {
  return {
    '@context': 'https://schema.org',
    '@type': 'WebSite',
    name: SITE_NAME,
    url: SITE_URL,
  };
}

export function breadcrumbJsonLd(
  items: { name: string; path: string }[],
  locale: Locale | string,
) {
  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: items.map((item, index) => ({
      '@type': 'ListItem',
      position: index + 1,
      name: item.name,
      item: absoluteUrl(localizedPath(locale, item.path)),
    })),
  };
}

export function articleJsonLd(input: {
  title: string;
  description: string;
  path: string;
  locale: Locale | string;
  datePublished?: string;
  dateModified?: string;
  image?: string;
}) {
  return {
    '@context': 'https://schema.org',
    '@type': 'Article',
    headline: input.title,
    description: input.description,
    url: absoluteUrl(localizedPath(input.locale, input.path)),
    image: absoluteUrl(input.image || HERO_IMAGE),
    datePublished: input.datePublished,
    dateModified: input.dateModified || input.datePublished,
    author: { '@type': 'Organization', name: SITE_NAME },
    publisher: organizationJsonLd(),
  };
}

export function itemListJsonLd(
  items: { name: string; path: string }[],
  locale: Locale | string,
) {
  return {
    '@context': 'https://schema.org',
    '@type': 'ItemList',
    itemListElement: items.map((item, index) => ({
      '@type': 'ListItem',
      position: index + 1,
      name: item.name,
      url: absoluteUrl(localizedPath(locale, item.path)),
    })),
  };
}

export function videoGameJsonLd() {
  return {
    '@context': 'https://schema.org',
    '@type': 'VideoGame',
    name: 'Build a Base and Steal',
    description:
      'A Roblox tycoon-style base building and raiding game where you collect pets, build defenses, and raid other players for rare rewards.',
    image: absoluteUrl(HERO_IMAGE),
    url: EXTERNAL_LINKS.roblox,
    gamePlatform: 'Roblox',
    genre: ['Simulation', 'Tycoon', 'Strategy', 'Pet Collecting'],
    playMode: 'MultiPlayer',
    applicationCategory: 'Game',
    operatingSystem: 'Windows, macOS, iOS, Android, Xbox',
    publisher: organizationJsonLd(),
    offers: {
      '@type': 'Offer',
      price: '0',
      priceCurrency: 'USD',
      availability: 'https://schema.org/InStock',
    },
  };
}

export function faqJsonLd(
  items: { question: string; answer: string }[],
) {
  return {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: items.map((item) => ({
      '@type': 'Question',
      name: item.question,
      acceptedAnswer: {
        '@type': 'Answer',
        text: item.answer,
      },
    })),
  };
}
