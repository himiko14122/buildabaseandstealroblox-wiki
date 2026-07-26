import {
  Gift, BookOpen, Dice6, Shield, Swords, DollarSign, PawPrint,
  Wrench, Brain, HelpCircle, Megaphone, Users, Home, Info,
  Map, ScrollText, Flame, Zap, Target, Lock, TrendingUp, Gamepad2,
  type LucideIcon,
} from 'lucide-react';

export const NAVIGATION_CONFIG = [
  { key: 'home', labelKey: 'nav_home', path: '/', icon: Home, showInHeader: false, showInSidebar: true, showInFooter: false, sitemap: true, priority: 1, changeFrequency: 'daily' },
  { key: 'codes', labelKey: 'nav_codes', path: '/codes', icon: Gift, isContentType: true, showInHeader: true, showInSidebar: true, showInFooter: true, sitemap: true, priority: 0.9, changeFrequency: 'daily' },
  { key: 'beginner-guide', labelKey: 'nav_beginnerGuide', path: '/beginner-guide', icon: BookOpen, isContentType: true, showInHeader: true, showInSidebar: true, showInFooter: true, sitemap: true, priority: 0.9, changeFrequency: 'weekly' },
  { key: 'pet-rolling', labelKey: 'nav_petRolling', path: '/pet-rolling', icon: Dice6, isContentType: true, showInHeader: true, showInSidebar: true, showInFooter: true, sitemap: true, priority: 0.9, changeFrequency: 'weekly' },
  { key: 'base-defense', labelKey: 'nav_baseDefense', path: '/base-defense', icon: Shield, isContentType: true, showInHeader: true, showInSidebar: true, showInFooter: true, sitemap: true, priority: 0.9, changeFrequency: 'weekly' },
  { key: 'raiding', labelKey: 'nav_raiding', path: '/raiding', icon: Swords, isContentType: true, showInHeader: true, showInSidebar: true, showInFooter: true, sitemap: true, priority: 0.9, changeFrequency: 'weekly' },
  { key: 'offline-money', labelKey: 'nav_offlineMoney', path: '/offline-money', icon: DollarSign, isContentType: true, showInHeader: true, showInSidebar: true, showInFooter: true, sitemap: true, priority: 0.8, changeFrequency: 'weekly' },
  { key: 'pets-list', labelKey: 'nav_petsList', path: '/pets-list', icon: PawPrint, isContentType: true, showInHeader: true, showInSidebar: true, showInFooter: true, sitemap: true, priority: 0.8, changeFrequency: 'weekly' },
  { key: 'gear', labelKey: 'nav_gear', path: '/gear', icon: Wrench, isContentType: true, showInHeader: true, showInSidebar: true, showInFooter: true, sitemap: true, priority: 0.8, changeFrequency: 'weekly' },
  { key: 'strategies', labelKey: 'nav_strategies', path: '/strategies', icon: Brain, isContentType: true, showInHeader: false, showInSidebar: true, showInFooter: true, sitemap: true, priority: 0.8, changeFrequency: 'weekly' },
  { key: 'faq', labelKey: 'nav_faq', path: '/faq', icon: HelpCircle, isContentType: true, showInHeader: false, showInSidebar: true, showInFooter: true, sitemap: true, priority: 0.7, changeFrequency: 'weekly' },
  { key: 'updates', labelKey: 'nav_updates', path: '/updates', icon: Megaphone, isContentType: true, showInHeader: false, showInSidebar: true, showInFooter: true, sitemap: true, priority: 0.7, changeFrequency: 'weekly' },
  { key: 'community', labelKey: 'nav_community', path: '/community', icon: Users, isContentType: true, showInHeader: false, showInSidebar: true, showInFooter: true, sitemap: true, priority: 0.7, changeFrequency: 'weekly' },
  { key: 'guides', labelKey: 'nav_guides', path: '/guides', icon: BookOpen, isContentType: true, showInHeader: true, showInSidebar: true, showInFooter: true, sitemap: true, priority: 0.9, changeFrequency: 'weekly' },
  { key: 'about', labelKey: 'nav_about', path: '/about', icon: Info, showInHeader: false, showInSidebar: false, showInFooter: true, sitemap: true, priority: 0.7, changeFrequency: 'monthly' },
  { key: 'sitemap', labelKey: 'nav_sitemap', path: '/sitemap', icon: Map, showInHeader: false, showInSidebar: false, showInFooter: true, sitemap: false, priority: 0.5, changeFrequency: 'monthly' },
  { key: 'privacy-policy', labelKey: 'nav_privacyPolicy', path: '/privacy-policy', icon: ScrollText, showInHeader: false, showInSidebar: false, showInFooter: true, sitemap: true, priority: 0.4, changeFrequency: 'yearly' },
  { key: 'terms-of-service', labelKey: 'nav_termsOfService', path: '/terms-of-service', icon: ScrollText, showInHeader: false, showInSidebar: false, showInFooter: true, sitemap: true, priority: 0.4, changeFrequency: 'yearly' },
] as const;

export const CONTENT_TYPES = NAVIGATION_CONFIG.filter((item) => 'isContentType' in item && item.isContentType).map((item) => item.key);

export const CONTENT_TYPES_WITH_DEDICATED_PAGES = new Set(CONTENT_TYPES);

export type NavigationItem = (typeof NAVIGATION_CONFIG)[number];
export type ContentType = (typeof CONTENT_TYPES)[number];

export function isContentType(value: string): value is ContentType {
  return CONTENT_TYPES.includes(value as ContentType);
}

export function getNavigationItem(path: string) {
  const normalized = path === '' ? '/' : path.startsWith('/') ? path : `/${path}`;
  return NAVIGATION_CONFIG.find((item) => item.path === normalized || item.key === path);
}

export const CONTENT_DIR_NAMES: Record<ContentType | string, string> = {
  codes: 'codes',
  'beginner-guide': 'beginner-guide',
  'pet-rolling': 'pet-rolling',
  'base-defense': 'base-defense',
  raiding: 'raiding',
  'offline-money': 'offline-money',
  'pets-list': 'pets-list',
  gear: 'gear',
  strategies: 'strategies',
  faq: 'faq',
  updates: 'updates',
  community: 'community',
  guides: 'guides',
} as Record<ContentType, string>;

export function getContentDir(contentType: ContentType): string {
  return CONTENT_DIR_NAMES[contentType] || contentType;
}

export const GUIDE_CATEGORIES: Record<string, { emoji: string; order: number }> = {
  general:           { emoji: '🚀', order: 1 },
  codes:             { emoji: '🎁', order: 2 },
  'beginner-guide':  { emoji: '📚', order: 3 },
  'pet-rolling':     { emoji: '🎲', order: 4 },
  'base-defense':    { emoji: '🛡️', order: 5 },
  raiding:           { emoji: '⚔️', order: 6 },
  'offline-money':   { emoji: '💰', order: 7 },
  'pets-list':       { emoji: '🐾', order: 8 },
  gear:              { emoji: '🔧', order: 9 },
  strategies:        { emoji: '🧠', order: 10 },
  faq:               { emoji: '❓', order: 11 },
  updates:           { emoji: '📢', order: 12 },
  community:         { emoji: '👥', order: 13 },
};

export const CATEGORY_ORDER = Object.entries(GUIDE_CATEGORIES)
  .sort(([, a], [, b]) => a.order - b.order)
  .map(([key]) => key);

export const CATEGORY_AFFINITY: Record<string, string[]> = {
  general:           ['beginner-guide', 'guides'],
  codes:             ['beginner-guide', 'strategies'],
  'beginner-guide':  ['pet-rolling', 'base-defense', 'raiding'],
  'pet-rolling':     ['pets-list', 'offline-money', 'strategies'],
  'base-defense':    ['raiding', 'gear', 'strategies'],
  raiding:           ['gear', 'strategies', 'base-defense'],
  'offline-money':   ['pet-rolling', 'pets-list', 'strategies'],
  'pets-list':       ['pet-rolling', 'offline-money', 'gear'],
  gear:              ['raiding', 'base-defense', 'strategies'],
  strategies:        ['pet-rolling', 'base-defense', 'raiding'],
  faq:               ['beginner-guide', 'guides'],
  updates:           ['guides', 'community'],
  community:         ['updates', 'guides'],
  guides:             ['beginner-guide', 'strategies'],
};
