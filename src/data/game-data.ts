import { PawPrint, Shield, Swords, Zap, DollarSign, Wrench, Sparkles, Home, Crown, Flame, type LucideIcon } from 'lucide-react';

/* ──────────────── Pet Interface ──────────────── */
export interface Pet {
  id: string;
  nameKey: string;
  tier: string;
  rarityKey: string;
  typeKey: string;
  valueKey: string;
  icon: LucideIcon;
}

export const pets: Pet[] = [
  { id: 'brainrot-legendary', nameKey: 'pet_brainrot_legendary', tier: 'S', rarityKey: 'pet_rarity_legendary', typeKey: 'pet_type_brainrot', valueKey: 'pet_value_1M', icon: Sparkles },
  { id: 'brainrot-mythic', nameKey: 'pet_brainrot_mythic', tier: 'A', rarityKey: 'pet_rarity_mythic', typeKey: 'pet_type_brainrot', valueKey: 'pet_value_500K', icon: Sparkles },
  { id: 'brainrot-epic', nameKey: 'pet_brainrot_epic', tier: 'B', rarityKey: 'pet_rarity_epic', typeKey: 'pet_type_brainrot', valueKey: 'pet_value_100K', icon: Sparkles },
  { id: 'guard-legendary', nameKey: 'pet_guard_legendary', tier: 'S', rarityKey: 'pet_rarity_legendary', typeKey: 'pet_type_guard', valueKey: 'pet_value_800K', icon: Shield },
  { id: 'guard-mythic', nameKey: 'pet_guard_mythic', tier: 'A', rarityKey: 'pet_rarity_mythic', typeKey: 'pet_type_guard', valueKey: 'pet_value_400K', icon: Shield },
  { id: 'attacker-legendary', nameKey: 'pet_attacker_legendary', tier: 'S', rarityKey: 'pet_rarity_legendary', typeKey: 'pet_type_attacker', valueKey: 'pet_value_750K', icon: Swords },
  { id: 'attacker-mythic', nameKey: 'pet_attacker_mythic', tier: 'A', rarityKey: 'pet_rarity_mythic', typeKey: 'pet_type_attacker', valueKey: 'pet_value_350K', icon: Swords },
  { id: 'income-legendary', nameKey: 'pet_income_legendary', tier: 'S', rarityKey: 'pet_rarity_legendary', typeKey: 'pet_type_income', valueKey: 'pet_value_600K', icon: DollarSign },
  { id: 'income-mythic', nameKey: 'pet_income_mythic', tier: 'A', rarityKey: 'pet_rarity_mythic', typeKey: 'pet_type_income', valueKey: 'pet_value_300K', icon: DollarSign },
  { id: 'income-epic', nameKey: 'pet_income_epic', tier: 'B', rarityKey: 'pet_rarity_epic', typeKey: 'pet_type_income', valueKey: 'pet_value_75K', icon: DollarSign },
];

/* ──────────────── Gear Interface ──────────────── */
export interface Gear {
  id: string;
  nameKey: string;
  typeKey: string;
  effectKey: string;
  costKey: string;
  icon: LucideIcon;
}

export const gear: Gear[] = [
  { id: 'weapon-basic', nameKey: 'gear_weapon_basic', typeKey: 'gear_type_weapon', effectKey: 'gear_weapon_basic_effect', costKey: 'gear_weapon_basic_cost', icon: Swords },
  { id: 'weapon-advanced', nameKey: 'gear_weapon_advanced', typeKey: 'gear_type_weapon', effectKey: 'gear_weapon_advanced_effect', costKey: 'gear_weapon_advanced_cost', icon: Swords },
  { id: 'weapon-legendary', nameKey: 'gear_weapon_legendary', typeKey: 'gear_type_weapon', effectKey: 'gear_weapon_legendary_effect', costKey: 'gear_weapon_legendary_cost', icon: Zap },
  { id: 'shield-basic', nameKey: 'gear_shield_basic', typeKey: 'gear_type_shield', effectKey: 'gear_shield_basic_effect', costKey: 'gear_shield_basic_cost', icon: Shield },
  { id: 'shield-advanced', nameKey: 'gear_shield_advanced', typeKey: 'gear_type_shield', effectKey: 'gear_shield_advanced_effect', costKey: 'gear_shield_advanced_cost', icon: Shield },
  { id: 'tool-infiltration', nameKey: 'gear_tool_infiltration', typeKey: 'gear_type_tool', effectKey: 'gear_tool_infiltration_effect', costKey: 'gear_tool_infiltration_cost', icon: Wrench },
  { id: 'tool-extraction', nameKey: 'gear_tool_extraction', typeKey: 'gear_type_tool', effectKey: 'gear_tool_extraction_effect', costKey: 'gear_tool_extraction_cost', icon: Wrench },
  { id: 'boost-luck', nameKey: 'gear_boost_luck', typeKey: 'gear_type_boost', effectKey: 'gear_boost_luck_effect', costKey: 'gear_boost_luck_cost', icon: Sparkles },
  { id: 'boost-income', nameKey: 'gear_boost_income', typeKey: 'gear_type_boost', effectKey: 'gear_boost_income_effect', costKey: 'gear_boost_income_cost', icon: DollarSign },
];

/* ──────────────── Rarity Cards Interface ──────────────── */
export interface RarityCard {
  id: string;
  nameKey: string;
  descriptionKey: string;
  colorKey: string;
  icon: LucideIcon;
  petCount: number;
}

export const rarityCards: RarityCard[] = [
  { id: 'legendary', nameKey: 'rarity_legendary', descriptionKey: 'rarity_legendary_desc', colorKey: 'rarity_color_legendary', icon: Crown, petCount: 3 },
  { id: 'mythic', nameKey: 'rarity_mythic', descriptionKey: 'rarity_mythic_desc', colorKey: 'rarity_color_mythic', icon: Sparkles, petCount: 3 },
  { id: 'epic', nameKey: 'rarity_epic', descriptionKey: 'rarity_epic_desc', colorKey: 'rarity_color_epic', icon: Flame, petCount: 2 },
  { id: 'rare', nameKey: 'rarity_rare', descriptionKey: 'rarity_rare_desc', colorKey: 'rarity_color_rare', icon: PawPrint, petCount: 2 },
];

/* ──────────────── Base Design Cards Interface ──────────────── */
export interface BaseDesignCard {
  id: string;
  nameKey: string;
  descriptionKey: string;
  difficultyKey: string;
  icon: LucideIcon;
  effectivenessKey: string;
}

export const baseDesignCards: BaseDesignCard[] = [
  { id: 'maze-labyrinth', nameKey: 'base_design_maze', descriptionKey: 'base_design_maze_desc', difficultyKey: 'difficulty_hard', icon: Zap, effectivenessKey: 'effectiveness_very_high' },
  { id: 'multi-layer', nameKey: 'base_design_multi_layer', descriptionKey: 'base_design_multi_layer_desc', difficultyKey: 'difficulty_medium', icon: Shield, effectivenessKey: 'effectiveness_high' },
  { id: 'trap-focused', nameKey: 'base_design_trap', descriptionKey: 'base_design_trap_desc', difficultyKey: 'difficulty_easy', icon: Flame, effectivenessKey: 'effectiveness_medium' },
  { id: 'compact-fortress', nameKey: 'base_design_compact', descriptionKey: 'base_design_compact_desc', difficultyKey: 'difficulty_medium', icon: Home, effectivenessKey: 'effectiveness_high' },
];

/* ──────────────── Color Mapping ──────────────── */
export function tierColor(tier: string): string {
  const colorMap: Record<string, string> = {
    'S': '#EF4444',
    'A': '#F97316',
    'B': '#EAB308',
    'C': '#22C55E',
    'D': '#3B82F6',
  };
  return colorMap[tier] || '#6B7280';
}

export function rarityColor(rarity: string): string {
  const colorMap: Record<string, string> = {
    'legendary': '#EAB308',
    'mythic': '#A855F7',
    'epic': '#EC4899',
    'rare': '#3B82F6',
    'common': '#6B7280',
  };
  return colorMap[rarity] || '#6B7280';
}

export function gearTypeColor(type: string): string {
  const colorMap: Record<string, string> = {
    'weapon': 'text-red-500 bg-red-50 dark:bg-red-950',
    'shield': 'text-blue-500 bg-blue-50 dark:bg-blue-950',
    'tool': 'text-green-500 bg-green-50 dark:bg-green-950',
    'boost': 'text-purple-500 bg-purple-50 dark:bg-purple-950',
  };
  return colorMap[type] || 'text-gray-500 bg-gray-50 dark:bg-gray-950';
}

/* ──────────────── Icon Mapping ──────────────── */
export const PET_ICONS: Record<string, LucideIcon> = {
  brainrot: Sparkles,
  guard: Shield,
  attacker: Swords,
  income: DollarSign,
};

export const GEAR_ICONS: Record<string, LucideIcon> = {
  weapon: Swords,
  shield: Shield,
  tool: Wrench,
  boost: Sparkles,
};

export const RARITY_ICONS: Record<string, LucideIcon> = {
  legendary: Crown,
  mythic: Sparkles,
  epic: Flame,
  rare: PawPrint,
};

export const BASE_DESIGN_ICONS: Record<string, LucideIcon> = {
  'maze-labyrinth': Zap,
  'multi-layer': Shield,
  'trap-focused': Flame,
  'compact-fortress': Home,
};

/* ──────────────── Stats ──────────────── */
export const PET_STATS = {
  totalCount: pets.length,
  legendaryCount: pets.filter(p => p.rarityKey === 'pet_rarity_legendary').length,
  mythicCount: pets.filter(p => p.rarityKey === 'pet_rarity_mythic').length,
  epicCount: pets.filter(p => p.rarityKey === 'pet_rarity_epic').length,
};

export const GEAR_STATS = {
  totalCount: gear.length,
  weaponCount: gear.filter(g => g.typeKey === 'gear_type_weapon').length,
  shieldCount: gear.filter(g => g.typeKey === 'gear_type_shield').length,
  toolCount: gear.filter(g => g.typeKey === 'gear_type_tool').length,
  boostCount: gear.filter(g => g.typeKey === 'gear_type_boost').length,
};

export const RARITY_STATS = {
  totalCount: rarityCards.length,
  legendaryCount: rarityCards.filter(r => r.id === 'legendary').length,
  mythicCount: rarityCards.filter(r => r.id === 'mythic').length,
  epicCount: rarityCards.filter(r => r.id === 'epic').length,
  rareCount: rarityCards.filter(r => r.id === 'rare').length,
};

export const BASE_DESIGN_STATS = {
  totalCount: baseDesignCards.length,
  highDifficultyCount: baseDesignCards.filter(b => b.difficultyKey === 'difficulty_hard').length,
  highEffectivenessCount: baseDesignCards.filter(b => b.effectivenessKey === 'effectiveness_very_high' || b.effectivenessKey === 'effectiveness_high').length,
};