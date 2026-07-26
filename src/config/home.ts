import {
  Gift, BookOpen, Dice6, Shield, Swords, DollarSign, PawPrint,
  Wrench, Brain, HelpCircle, Megaphone, Users,
  type LucideIcon,
} from 'lucide-react';

export interface StatConfig {
  val: string;
  labelKey: string;
}

export interface ModuleCardConfig {
  key: string;
  labelKey: string;
  titleKey: string;
  descKey: string;
  href: string;
  stats: StatConfig[];
  icon: LucideIcon;
  ctaKey?: string;
}

export interface GameFeatureConfig {
  titleKey: string;
  descKey: string;
  icon: LucideIcon;
}

export interface StartHereStepConfig {
  titleKey: string;
  descKey: string;
  href: string;
}

export interface HeroCtaConfig {
  labelKey: string;
  href: string;
  style: 'primary' | 'secondary';
}

export const HOME_CONFIG = {
  hero: {
    videoId: '',
    badgeKeys: [
      'home_hero_badge_release',
      'home_hero_badge_updated',
      'home_hero_badge_visits',
      'home_hero_badge_favorites',
      'home_hero_badge_server',
    ],
    ctas: [
      { labelKey: 'home_hero_cta_primary', href: '/beginner-guide', style: 'primary' as const },
      { labelKey: 'home_hero_cta_secondary', href: '/base-defense', style: 'secondary' as const },
      { labelKey: 'home_hero_cta_tertiary', href: '/codes', style: 'secondary' as const },
    ],
  },
  startHere: {
    titleKey: 'home_start_title',
    steps: [
      {
        number: 1,
        titleKey: 'home_start_step1_title',
        descKey: 'home_start_step1_desc',
        href: '/beginner-guide',
      },
      {
        number: 2,
        titleKey: 'home_start_step2_title',
        descKey: 'home_start_step2_desc',
        href: '/pet-rolling',
      },
      {
        number: 3,
        titleKey: 'home_start_step3_title',
        descKey: 'home_start_step3_desc',
        href: '/base-defense',
      },
      {
        number: 4,
        titleKey: 'home_start_step4_title',
        descKey: 'home_start_step4_desc',
        href: '/raiding',
      },
      {
        number: 5,
        titleKey: 'home_start_step5_title',
        descKey: 'home_start_step5_desc',
        href: '/offline-money',
      },
    ],
  },
  featuredGuides: {
    titleKey: 'home_featured_guides_title',
    guides: [
      {
        slug: 'beginner-guide',
        titleKey: 'featured_guide_beginner_title',
        descKey: 'featured_guide_beginner_desc',
        readTime: '8 min read',
      },
      {
        slug: 'pet-rolling',
        titleKey: 'featured_guide_rolling_title',
        descKey: 'featured_guide_rolling_desc',
        readTime: '12 min read',
      },
      {
        slug: 'base-defense',
        titleKey: 'featured_guide_base_title',
        descKey: 'featured_guide_base_desc',
        readTime: '10 min read',
      },
    ],
  },
  modules: [
    {
      key: 'codes',
      labelKey: 'nav_codes',
      titleKey: 'module_codes_title',
      descKey: 'module_codes_desc',
      href: '/codes',
      stats: [
        { val: '__activeCodesCount', labelKey: 'module_codes_stat_active' },
        { val: '__totalCodesCount', labelKey: 'module_codes_stat_total' },
      ],
      icon: Gift,
      ctaKey: 'module_codes_cta',
    },
    {
      key: 'beginner-guide',
      labelKey: 'nav_beginnerGuide',
      titleKey: 'module_beginner_title',
      descKey: 'module_beginner_desc',
      href: '/beginner-guide',
      stats: [
        { val: '5', labelKey: 'module_beginner_stat_sections' },
        { val: '10 min', labelKey: 'module_beginner_stat_time' },
      ],
      icon: BookOpen,
      ctaKey: 'module_beginner_cta',
    },
    {
      key: 'pet-rolling',
      labelKey: 'nav_petRolling',
      titleKey: 'module_rolling_title',
      descKey: 'module_rolling_desc',
      href: '/pet-rolling',
      stats: [
        { val: '__petCount', labelKey: 'module_rolling_stat_pets' },
        { val: '__rarityCount', labelKey: 'module_rolling_stat_rarities' },
      ],
      icon: Dice6,
      ctaKey: 'module_rolling_cta',
    },
    {
      key: 'base-defense',
      labelKey: 'nav_baseDefense',
      titleKey: 'module_base_title',
      descKey: 'module_base_desc',
      href: '/base-defense',
      stats: [
        { val: '__defenseStrategyCount', labelKey: 'module_base_stat_strategies' },
        { val: '__baseDesignCount', labelKey: 'module_base_stat_designs' },
      ],
      icon: Shield,
      ctaKey: 'module_base_cta',
    },
    {
      key: 'raiding',
      labelKey: 'nav_raiding',
      titleKey: 'module_raiding_title',
      descKey: 'module_raiding_desc',
      href: '/raiding',
      stats: [
        { val: '__gearCount', labelKey: 'module_raiding_stat_gear' },
        { val: '__strategyCount', labelKey: 'module_raiding_stat_strategies' },
      ],
      icon: Swords,
      ctaKey: 'module_raiding_cta',
    },
    {
      key: 'offline-money',
      labelKey: 'nav_offlineMoney',
      titleKey: 'module_offline_title',
      descKey: 'module_offline_desc',
      href: '/offline-money',
      stats: [
        { val: '__offlineStrategyCount', labelKey: 'module_offline_stat_strategies' },
        { val: '__maxOfflineHours', labelKey: 'module_offline_stat_maxHours' },
      ],
      icon: DollarSign,
      ctaKey: 'module_offline_cta',
    },
    {
      key: 'pets-list',
      labelKey: 'nav_petsList',
      titleKey: 'module_pets_title',
      descKey: 'module_pets_desc',
      href: '/pets-list',
      stats: [
        { val: '__petCount', labelKey: 'module_pets_stat_total' },
        { val: '__legendaryCount', labelKey: 'module_pets_stat_legendary' },
      ],
      icon: PawPrint,
      ctaKey: 'module_pets_cta',
    },
    {
      key: 'gear',
      labelKey: 'nav_gear',
      titleKey: 'module_gear_title',
      descKey: 'module_gear_desc',
      href: '/gear',
      stats: [
        { val: '__gearCount', labelKey: 'module_gear_stat_total' },
        { val: '__gearCategoryCount', labelKey: 'module_gear_stat_categories' },
      ],
      icon: Wrench,
      ctaKey: 'module_gear_cta',
    },
    {
      key: 'strategies',
      labelKey: 'nav_strategies',
      titleKey: 'module_strategies_title',
      descKey: 'module_strategies_desc',
      href: '/strategies',
      stats: [
        { val: '__strategyCount', labelKey: 'module_strategies_stat_total' },
        { val: '__proTipCount', labelKey: 'module_strategies_stat_proTips' },
      ],
      icon: Brain,
      ctaKey: 'module_strategies_cta',
    },
    {
      key: 'faq',
      labelKey: 'nav_faq',
      titleKey: 'module_faq_title',
      descKey: 'module_faq_desc',
      href: '/faq',
      stats: [
        { val: '__faqCount', labelKey: 'module_faq_stat_total' },
        { val: '__commonIssueCount', labelKey: 'module_faq_stat_common' },
      ],
      icon: HelpCircle,
      ctaKey: 'module_faq_cta',
    },
    {
      key: 'updates',
      labelKey: 'nav_updates',
      titleKey: 'module_updates_title',
      descKey: 'module_updates_desc',
      href: '/updates',
      stats: [
        { val: '__updateCount', labelKey: 'module_updates_stat_recent' },
        { val: 'Jul 2026', labelKey: 'module_updates_stat_lastUpdated' },
      ],
      icon: Megaphone,
      ctaKey: 'module_updates_cta',
    },
    {
      key: 'community',
      labelKey: 'nav_community',
      titleKey: 'module_community_title',
      descKey: 'module_community_desc',
      href: '/community',
      stats: [
        { val: '174K+', labelKey: 'module_community_stat_favorites' },
        { val: '25.9M+', labelKey: 'module_community_stat_visits' },
      ],
      icon: Users,
      ctaKey: 'module_community_cta',
    },
  ],
  keywordHub: {
    titleKey: 'home_keyword_hub_title',
    keywords: [
      'build a base and steal codes',
      'pet rolling guide',
      'base defense tips',
      'offline income calculator',
      'raiding strategies',
      'best pets build a base and steal',
      'how to steal pets',
      'base design ideas',
      'gamepasses list',
      'rebirth guide',
    ],
  },
  aboutGame: {
    titleKey: 'home_about_title',
    paragraphs: [
      'home_about_para1',
      'home_about_para2',
    ],
    stats: [
      { label: 'home_about_stat_developer', value: 'replayable fun games' },
      { label: 'home_about_stat_platform', value: 'Roblox' },
      { label: 'home_about_stat_genre', value: 'Simulation / Tycoon' },
      { label: 'home_about_stat_visits', value: '25.9M+' },
      { label: 'home_about_stat_favorites', value: '174K+' },
      { label: 'home_about_stat_server', value: '6 Players' },
      { label: 'home_about_stat_updated', value: 'July 2026' },
    ],
    ctaKeys: [
      'home_about_cta_primary',
      'home_about_cta_secondary',
    ],
  },
  finalCta: {
    titleKey: 'home_final_cta_title',
    descKey: 'home_final_cta_desc',
    guideHref: '/beginner-guide',
    guideLabelKey: 'home_final_cta_primary',
    externalLinkKey: 'roblox',
    externalLabelKey: 'home_final_cta_secondary',
  },
  gameOverview: {
    titleKey: 'home_about_title',
    cta: {
      guideHref: '/beginner-guide',
      guideLabelKey: 'home_about_cta_primary',
      externalLinkKey: 'roblox',
      externalLabelKey: 'home_about_cta_secondary',
    },
  },
};

export const CATEGORY_ORDER = [
  'codes',
  'beginner-guide',
  'pet-rolling',
  'base-defense',
  'raiding',
  'offline-money',
  'pets-list',
  'gear',
  'strategies',
  'faq',
  'updates',
  'community',
];