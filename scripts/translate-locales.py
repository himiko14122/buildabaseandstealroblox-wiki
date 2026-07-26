#!/usr/bin/env python3
"""Translate locale JSON files from English to Korean, Japanese, and German.
Comprehensive translation covering all 877 keys.
"""
import json
import os

LOCALES_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'locales')

# Master translation map: i18n key -> {'ko': ..., 'ja': ..., 'de': ...}
T = {
    # ===== Site / Page metadata =====
    'site_title': {'ko': 'Build a Base and Steal 위키', 'ja': 'Build a Base and Steal Wiki', 'de': 'Build a Base and Steal Wiki'},
    'site_description': {
        'ko': '활성 코드, 펫 롤링 가이드, 기지 방어 팁, 오프라인 돈 계산기, 2026년 레이딩 전략을 갖춘 완전한 Build a Base and Steal 위키입니다.',
        'ja': 'アクティブなコード、ペットローリングガイド、ベース防衛のヒント、オフラインマネーカルキュレーター、2026年のレイド戦略を備えた完全なBuild a Base and Stealウィキです。',
        'de': 'Vollständiges Build a Base and Steal Wiki mit aktiven Codes, Pet-Rolling-Anleitungen, Base-Defense-Tipps, Offline-Geld-Rechner und Raid-Strategien für 2026.',
    },
    'page_home': {
        'ko': 'Build a Base and Steal 위키 — 코드, 가이드, 펫 롤링',
        'ja': 'Build a Base and Steal Wiki — コード、ガイド、ペットローリング',
        'de': 'Build a Base and Steal Wiki — Codes, Anleitungen, Pet-Rolling',
    },
    'page_home_description': {
        'ko': '활성 코드, 펫 롤링 가이드, 기지 방어 팁, 오프라인 돈 계산기, 2026년 레이딩 전략을 갖춘 완전한 Build a Base and Steal 위키입니다.',
        'ja': 'アクティブなコード、ペットローリングガイド、ベース防衛のヒント、オフラインマネーカルキュレーター、2026年のレイド戦略を備えた完全なBuild a Base and Stealウィキです。',
        'de': 'Vollständiges Build a Base and Steal Wiki mit aktiven Codes, Pet-Rolling-Anleitungen, Base-Defense-Tipps, Offline-Geld-Rechner und Raid-Strategien für 2026.',
    },
    'home_hero_tagline': {'ko': '팬 제작 커뮤니티 위키', 'ja': 'コミュニティ制作のウィキ', 'de': 'Von der Community erstelltes Wiki'},
    'home_hero_description': {
        'ko': '희귀 펫을 롤링하고, 난공불락의 기지를 건설하고, 패시브 소득을 올리고, 다른 플레이어를 레이드하여 보물을 훔치세요. 이 궁극의 Roblox 타이쿤 전략 게임에서 건설, 보호, 훔치기의 순환을 마스터하세요.',
        'ja': 'レアペットをロールし、侵入不可能なベースを構築し、パッシブ収入を稼ぎ、他のプレイヤーをレイドして彼らの宝を盗み出しましょう。この究極のRobloxタイコンストラテジーゲームで、構築、保護、盗みのループをマスターしてください。',
        'de': 'Rolle für seltene Pets, baue uneinnehmbare Basen, verdiene passives Einkommen und überfalle andere Spieler, um ihre Schätze zu stehlen. Meistere den Kreislauf aus Bauen, Schützen und Stehlen in diesem ultimativen Roblox-Tycoon-Strategiespiel.',
    },
    'home_hero_trailer': {'ko': '공식 미디어', 'ja': '公式メディア', 'de': 'Offizielle Medien'},
    'home_hero_badge_release': {'ko': '2026년 출시', 'ja': '2026年リリース', 'de': 'Erschienen 2026'},
    'home_hero_badge_updated': {'ko': '2026년 7월 업데이트', 'ja': '2026年7月更新', 'de': 'Aktualisiert Jul 2026'},
    'home_hero_badge_visits': {'ko': '2590만 회 이상 방문', 'ja': '2590万回以上の訪問', 'de': '25.9M+ Besuche'},
    'home_hero_badge_favorites': {'ko': '17.4만 이상 즐겨찾기', 'ja': '17.4万人以上のお気に入り', 'de': '174K+ Favoriten'},
    'home_hero_badge_server': {'ko': '서버당 6명', 'ja': 'サーバーあたり6人', 'de': '6 Spieler pro Server'},
    'home_hero_cta_primary': {'ko': '초보자 가이드 시작', 'ja': '初心者ガイドを開始', 'de': 'Einsteiger-Anleitung starten'},
    'home_hero_cta_secondary': {'ko': '기지 방어 팁 확인', 'ja': 'ベース防衛のヒントを確認', 'de': 'Base-Defense-Tipps prüfen'},
    'home_hero_cta_tertiary': {'ko': '활성 코드 보기', 'ja': 'アクティブなコードを表示', 'de': 'Aktive Codes anzeigen'},
    'home_start_label': {'ko': '여기서 시작', 'ja': 'ここから始める', 'de': 'Start hier'},
    'home_start_title': {'ko': '당신의 Build and Steal 여정', 'ja': 'あなたのBuild and Stealの旅', 'de': 'Deine Build-und-Steal-Reise'},
    'home_start_subtitle': {
        'ko': 'Build a Base and Steal에서 펫 롤링, 기지 건설, 레이딩을 마스터하려면 다음 단계를 따르세요.',
        'ja': 'Build a Base and Stealでペットローリング、ベース構築、レイドをマスターするために、これらの手順に従ってください。',
        'de': 'Folge diesen Schritten, um Pet-Rolling, Basenbau und Raids in Build a Base and Steal zu meistern.',
    },
    'home_start_step1_title': {'ko': '초보자 가이드', 'ja': '初心者ガイド', 'de': 'Einsteiger-Anleitung'},
    'home_start_step1_desc': {
        'ko': '첫 세션 전체 안내, 롤링 메커니즘 학습, 패시브 소득 시작.',
        'ja': '初回セッションの完全なウォークスルー、ローリングメカニクスの学習、パッシブ収入の開始。',
        'de': 'Vollständiger Walkthrough für die erste Sitzung, lerne Rolling-Mechaniken und beginne, passives Einkommen zu verdienen.',
    },
    'home_start_step2_title': {'ko': '펫 롤링', 'ja': 'ペットローリング', 'de': 'Pet-Rolling'},
    'home_start_step2_desc': {
        'ko': '롤링 시스템을 마스터하고, 드롭 확률을 이해하며, 희귀 펫을 위한 예산을 계획하세요.',
        'ja': 'ローリングシステムをマスターし、ドロップ率を理解し、レアペットのための予算を計画する。',
        'de': 'Meistere das Rolling-System, verstehe Drop-Raten und plane dein Budget für seltene Pets.',
    },
    'home_start_step3_title': {'ko': '기지 방어', 'ja': 'ベース防衛', 'de': 'Base-Defense'},
    'home_start_step3_desc': {
        'ko': '난공불락의 기지를 설계하고, 펫을 보호하며, 레이드 취약점을 최소화하세요.',
        'ja': '侵入不可能なベースを設計し、ペットを保護し、レイドの脆弱性を最小限に抑える。',
        'de': 'Entwirf uneinnehmbare Basen, schütze deine Pets und minimiere Raid-Schwachstellen.',
    },
    'home_start_step4_title': {'ko': '레이딩', 'ja': 'レイド', 'de': 'Raids'},
    'home_start_step4_desc': {
        'ko': '레이딩 전략을 배우고, 장비를 효과적으로 사용하며, 다른 플레이어의 귀중한 펫을 훔치세요.',
        'ja': 'レイド戦略を学び、ギアを効果的に使用し、他のプレイヤーから価値あるペットを盗む。',
        'de': 'Lerne Raid-Strategien, verwende Ausrüstung effektiv und stehle wertvolle Pets von anderen.',
    },
    'home_start_step5_title': {'ko': '오프라인 돈', 'ja': 'オフラインマネー', 'de': 'Offline-Geld'},
    'home_start_step5_desc': {
        'ko': '고급 전략과 계산으로 오프라인 중 패시브 소득을 극대화하세요.',
        'ja': '高度な戦略と計算でオフライン中のパッシブ収入を最大化する。',
        'de': 'Maximiere passives Einkommen im Offline-Modus mit fortgeschrittenen Strategien und Berechnungen.',
    },
    'home_modules_label': {'ko': '탐색', 'ja': '探索', 'de': 'Erkunden'},
    'home_modules_title': {'ko': '게임 모듈 및 가이드', 'ja': 'ゲームモジュールとガイド', 'de': 'Spielmodule & Anleitungen'},
    'home_modules_subtitle': {
        'ko': 'Build a Base and Steal을 마스터하는 데 필요한 모든 것 — 펫 롤링과 기지 방어부터 레이딩 전략과 오프라인 소득 최적화까지.',
        'ja': 'Build a Base and Stealをマスターするために必要なすべて — ペットローリングとベース防衛からレイド戦略とオフライン収入最適化まで。',
        'de': 'Alles, was du zum Meistern von Build a Base and Steal brauchst — von Pet-Rolling und Base-Defense bis zu Raid-Strategien und Offline-Einkommens-Optimierung.',
    },
    # ===== Nav =====
    'nav_codes': {'ko': '코드', 'ja': 'コード', 'de': 'Codes'},
    'nav_beginnerGuide': {'ko': '초보자 가이드', 'ja': '初心者ガイド', 'de': 'Einsteiger-Anleitung'},
    'nav_petRolling': {'ko': '펫 롤링', 'ja': 'ペットローリング', 'de': 'Pet-Rolling'},
    'nav_baseDefense': {'ko': '기지 방어', 'ja': 'ベース防衛', 'de': 'Base-Defense'},
    'nav_raiding': {'ko': '레이딩', 'ja': 'レイド', 'de': 'Raids'},
    'nav_offlineMoney': {'ko': '오프라인 돈', 'ja': 'オフラインマネー', 'de': 'Offline-Geld'},
    'nav_petsList': {'ko': '모든 펫', 'ja': 'すべてのペット', 'de': 'Alle Pets'},
    'nav_gear': {'ko': '장비 아이템', 'ja': 'ギアアイテム', 'de': 'Ausrüstung'},
    'nav_strategies': {'ko': '전략', 'ja': '戦略', 'de': 'Strategien'},
    'nav_faq': {'ko': 'FAQ', 'ja': 'よくある質問', 'de': 'FAQ'},
    'nav_updates': {'ko': '업데이트', 'ja': 'アップデート', 'de': 'Updates'},
    'nav_community': {'ko': '커뮤니티', 'ja': 'コミュニティ', 'de': 'Community'},
    'nav_guides': {'ko': '가이드', 'ja': 'ガイド', 'de': 'Anleitungen'},
    'nav_home': {'ko': '홈', 'ja': 'ホーム', 'de': 'Startseite'},
    'nav_about': {'ko': '소개', 'ja': '詳細', 'de': 'Über'},
    'nav_sitemap': {'ko': '사이트맵', 'ja': 'サイトマップ', 'de': 'Sitemap'},
    'nav_privacyPolicy': {'ko': '개인정보 처리방침', 'ja': 'プライバシーポリシー', 'de': 'Datenschutzrichtlinie'},
    'nav_termsOfService': {'ko': '서비스 이용약관', 'ja': '利用規約', 'de': 'Nutzungsbedingungen'},
    # ===== Module cards =====
    'module_codes_title': {'ko': '활성 코드', 'ja': 'アクティブなコード', 'de': 'Aktive Codes'},
    'module_codes_desc': {'ko': '무료 펫, 현금, 부스트를 주는 현재 작동하는 교환 코드', 'ja': '無料ペット、現金、ブーストを提供する現在機能する引き換えコード', 'de': 'Aktuell funktionierende Einlösecodes für kostenlose Pets, Geld und Boosts'},
    'module_codes_stat_active': {'ko': '활성 코드', 'ja': 'アクティブなコード', 'de': 'aktive Codes'},
    'module_codes_stat_total': {'ko': '전체 코드', 'ja': '合計コード', 'de': 'Gesamt-Codes'},
    'module_codes_cta': {'ko': '코드 교환 →', 'ja': 'コードを引き換える →', 'de': 'Codes einlösen →'},
    'module_beginner_title': {'ko': '초보자 가이드', 'ja': '初心者ガイド', 'de': 'Einsteiger-Anleitung'},
    'module_beginner_desc': {'ko': '새 플레이어를 위한 완전한 안내 - 첫 세션 팁과 기본', 'ja': '新しいプレイヤーのための完全なウォークスルー - 最初のセッションのヒントと基本', 'de': 'Vollständiger Walkthrough für neue Spieler - Tipps und Grundlagen für die erste Sitzung'},
    'module_beginner_stat_sections': {'ko': '섹션', 'ja': 'セクション', 'de': 'Abschnitte'},
    'module_beginner_stat_time': {'ko': '10분 분량', 'ja': '10分読み', 'de': '10 Min. Lesezeit'},
    'module_beginner_cta': {'ko': '학습 시작 →', 'ja': '学習を開始 →', 'de': 'Lernen starten →'},
    'module_rolling_title': {'ko': '펫 롤링 가이드', 'ja': 'ペットローリングガイド', 'de': 'Pet-Rolling-Anleitung'},
    'module_rolling_desc': {'ko': '희귀 펫 롤링 방법, 예산 계획, 드롭 확률', 'ja': 'レアペットのロール方法、予算計画、ドロップ率', 'de': 'Wie man für seltene Pets rollt, Budgetplanung und Drop-Raten'},
    'module_rolling_stat_pets': {'ko': '펫', 'ja': 'ペット', 'de': 'Pets'},
    'module_rolling_stat_rarities': {'ko': '희귀도', 'ja': 'レアリティ', 'de': 'Seltenheiten'},
    'module_rolling_cta': {'ko': '롤링 시작 →', 'ja': 'ローリング開始 →', 'de': 'Rolling starten →'},
    'module_base_title': {'ko': '기지 방어', 'ja': 'ベース防衛', 'de': 'Base-Defense'},
    'module_base_desc': {'ko': '최고의 기지 설계, 방어 전략, 보호 팁', 'ja': '最高のベースデザイン、防御戦略、保護のヒント', 'de': 'Beste Base-Designs, Verteidigungsstrategien und Schutztipps'},
    'module_base_stat_strategies': {'ko': '전략', 'ja': '戦略', 'de': 'Strategien'},
    'module_base_stat_designs': {'ko': '설계', 'ja': 'デザイン', 'de': 'Designs'},
    'module_base_cta': {'ko': '기지 건설 →', 'ja': 'ベースを構築 →', 'de': 'Basen bauen →'},
    'module_raiding_title': {'ko': '레이딩 가이드', 'ja': 'レイドガイド', 'de': 'Raid-Anleitung'},
    'module_raiding_desc': {'ko': '다른 플레이어 레이드 방법, 장비 사용, 훔치기 전략', 'ja': '他のプレイヤーをレイドする方法、ギアの使用、盗みの戦略', 'de': 'Wie man andere Spieler überfällt, Ausrüstungsverwendung und Diebstahlsstrategien'},
    'module_raiding_stat_gear': {'ko': '장비 아이템', 'ja': 'ギアアイテム', 'de': 'Ausrüstungsgegenstände'},
    'module_raiding_stat_strategies': {'ko': '전략', 'ja': '戦略', 'de': 'Strategien'},
    'module_raiding_cta': {'ko': '레이딩 시작 →', 'ja': 'レイド開始 →', 'de': 'Raids starten →'},
    'module_offline_title': {'ko': '오프라인 돈', 'ja': 'オフラインマネー', 'de': 'Offline-Geld'},
    'module_offline_desc': {'ko': '이 전략들로 오프라인 중 패시브 소득 극대화', 'ja': 'これらの戦略でオフライン中のパッシブ収入を最大化', 'de': 'Maximiere passives Einkommen im Offline-Modus mit diesen Strategien'},
    'module_offline_stat_strategies': {'ko': '전략', 'ja': '戦略', 'de': 'Strategien'},
    'module_offline_stat_maxHours': {'ko': '최대 시간', 'ja': '最大時間', 'de': 'max. Stunden'},
    'module_offline_cta': {'ko': '소득 계산 →', 'ja': '収入を計算 →', 'de': 'Einkommen berechnen →'},
    'module_pets_title': {'ko': '모든 펫', 'ja': 'すべてのペット', 'de': 'Alle Pets'},
    'module_pets_desc': {'ko': '희귀도, 능력치, 가치를 갖춘 완전한 펫 데이터베이스', 'ja': 'レアリティ、ステータス、価値を備えた完全なペットデータベース', 'de': 'Vollständige Pet-Datenbank mit Seltenheiten, Statistiken und Werten'},
    'module_pets_stat_total': {'ko': '전체 펫', 'ja': '合計ペット', 'de': 'Gesamt-Pets'},
    'module_pets_stat_legendary': {'ko': '전설 펫', 'ja': 'レジェンダリーペット', 'de': 'legendäre Pets'},
    'module_pets_cta': {'ko': '모든 펫 보기 →', 'ja': 'すべてのペットを表示 →', 'de': 'Alle Pets anzeigen →'},
    'module_gear_title': {'ko': '장비 아이템', 'ja': 'ギアアイテム', 'de': 'Ausrüstungsgegenstände'},
    'module_gear_desc': {'ko': '모든 레이딩 장비, 무기, 효과', 'ja': 'すべてのレイドギア、武器、その効果', 'de': 'Alle Raid-Ausrüstungen, Waffen und ihre Effekte'},
    'module_gear_stat_total': {'ko': '전체 장비', 'ja': '合計ギア', 'de': 'Gesamtausrüstung'},
    'module_gear_stat_categories': {'ko': '카테고리', 'ja': 'カテゴリー', 'de': 'Kategorien'},
    'module_gear_cta': {'ko': '모든 장비 보기 →', 'ja': 'すべてのギアを表示 →', 'de': 'Alle Ausrüstungen anzeigen →'},
    'module_strategies_title': {'ko': '고급 전략', 'ja': '高度な戦略', 'de': 'Fortgeschrittene Strategien'},
    'module_strategies_desc': {'ko': '프로 팁, 팀 전술, 고수준 게임플레이', 'ja': 'プロのヒント、チーム戦術、ハイレベルなゲームプレイ', 'de': 'Pro-Tipps, Teamtaktiken und High-Level-Gameplay'},
    'module_strategies_stat_total': {'ko': '전략', 'ja': '戦略', 'de': 'Strategien'},
    'module_strategies_stat_proTips': {'ko': '프로 팁', 'ja': 'プロのヒント', 'de': 'Pro-Tipps'},
    'module_strategies_cta': {'ko': '전략 마스터 →', 'ja': '戦略をマスター →', 'de': 'Strategien meistern →'},
    'module_faq_title': {'ko': 'FAQ', 'ja': 'よくある質問', 'de': 'FAQ'},
    'module_faq_desc': {'ko': '자주 묻는 질문과 해결된 일반적인 문제', 'ja': 'よくある質問と解決済みの一般的な問題', 'de': 'Häufig gestellte Fragen und Lösungen für häufige Probleme'},
    'module_faq_stat_total': {'ko': '질문', 'ja': '質問', 'de': 'Fragen'},
    'module_faq_stat_common': {'ko': '일반적인 문제', 'ja': '一般的な問題', 'de': 'häufige Probleme'},
    'module_faq_cta': {'ko': '답변 얻기 →', 'ja': '回答を得る →', 'de': 'Antworten erhalten →'},
    'module_updates_title': {'ko': '최신 업데이트', 'ja': '最新アップデート', 'de': 'Neueste Updates'},
    'module_updates_desc': {'ko': '최근 게임 변경사항, 패치 노트, 새로운 기능', 'ja': '最近のゲーム変更、パッチノート、新機能', 'de': 'Neueste Spieländerungen, Patch-Notizen und neue Funktionen'},
    'module_updates_stat_recent': {'ko': '최신 업데이트', 'ja': '最新アップデート', 'de': 'neueste Updates'},
    'module_updates_stat_lastUpdated': {'ko': '마지막 업데이트', 'ja': '最終更新', 'de': 'zuletzt aktualisiert'},
    'module_updates_cta': {'ko': '업데이트 보기 →', 'ja': 'アップデートを表示 →', 'de': 'Updates anzeigen →'},
    'module_community_title': {'ko': '커뮤니티', 'ja': 'コミュニティ', 'de': 'Community'},
    'module_community_desc': {'ko': 'Discord, YouTube, 기타 커뮤니티 리소스', 'ja': 'Discord、YouTube、その他のコミュニティリソース', 'de': 'Discord, YouTube und andere Community-Ressourcen'},
    'module_community_stat_favorites': {'ko': '즐겨찾기', 'ja': 'お気に入り', 'de': 'Favoriten'},
    'module_community_stat_visits': {'ko': '방문', 'ja': '訪問', 'de': 'Besuche'},
    'module_community_cta': {'ko': '커뮤니티 참여 →', 'ja': 'コミュニティに参加 →', 'de': 'Community beitreten →'},
    # ===== Home modules =====
    'home_module_default_cta': {'ko': '더 알아보기 →', 'ja': '詳細を見る →', 'de': 'Mehr erfahren →'},
    'home_module_petsList': {'ko': '펫', 'ja': 'ペット', 'de': 'Pets'},
    'home_module_pets_title': {'ko': '펫 컬렉션', 'ja': 'ペットコレクション', 'de': 'Pet-Sammlung'},
    'home_module_pets_desc': {
        'ko': 'Build a Base and Steal의 모든 펫을 발견하세요 — 전설적인 Brainrot부터 희귀 소득 생성기까지. 각 펫은 고유한 희귀도, 가치, 소득 잠재력을 가집니다.',
        'ja': 'Build a Base and Stealのすべてのペットを発見 — 伝説のBrainrotから希少な収入生成まで。各ペットには独自のレアリティ、価値、収入ポテンシャルがあります。',
        'de': 'Entdecke alle Pets in Build a Base and Steal — von legendären Brainrots bis zu seltenen Einkommensgeneratoren. Jedes Pet hat einzigartige Seltenheit, Wert und Einkommenspotenzial.',
    },
    'home_module_gear': {'ko': '장비', 'ja': 'ギア', 'de': 'Ausrüstung'},
    'home_module_gear_title': {'ko': '레이딩 장비', 'ja': 'レイドギア', 'de': 'Raid-Ausrüstung'},
    'home_module_gear_desc': {
        'ko': '다른 플레이어의 기지를 레이드하기 위한 무기, 방패, 도구, 부스트. 각 장비는 기지 침투 시 고유한 효과와 전략적 용도가 있습니다.',
        'ja': '他のプレイヤーのベースをレイドするための武器、盾、ツール、ブースト。各ギアにはベース浸透時の独自の効果と戦略的な用途があります。',
        'de': 'Waffen, Schilde, Werkzeuge und Boosts für Überfälle auf die Basen anderer Spieler. Jedes Ausrüstungsgegenstand hat einzigartige Effekte und strategische Verwendungen bei der Base-Infiltration.',
    },
    'home_module_rarities': {'ko': '희귀도', 'ja': 'レアリティ', 'de': 'Seltenheiten'},
    'home_module_rarities_title': {'ko': '펫 희귀도', 'ja': 'ペットレアリティ', 'de': 'Pet-Seltenheiten'},
    'home_module_rarities_desc': {
        'ko': '펫 희귀도 등급 이해 — 일반부터 전설까지. 희귀도가 높은 펫은 더 나은 소득 배수를 제공하며 레이드의 더 가치 있는 대상이 됩니다.',
        'ja': 'ペットのレアリティティアを理解 — コモンからレジェンダリーまで。レアリティの高いペットはより良い収入乗数を提供し、レイドのより価値ある対象となります。',
        'de': 'Verstehen der Pet-Seltenheitsstufen — von häufig bis legendär. Pets mit höherer Seltenheit bieten bessere Einkommensmultiplikatoren und sind wertvollere Ziele für Raids.',
    },
    'home_module_baseDefense': {'ko': '기지 방어', 'ja': 'ベース防衛', 'de': 'Base-Defense'},
    'home_module_baseDefense_title': {'ko': '기지 설계', 'ja': 'ベースデザイン', 'de': 'Base-Designs'},
    'home_module_baseDefense_desc': {
        'ko': '레이드로부터 펫을 보호하기 위해 검증된 기지 레이아웃과 방어 전략. 미로 래버린스부터 콤팩트 요새까지, 당신의 플레이 스타일에 맞는 설계를 찾으세요.',
        'ja': 'レイドからペットを保護するために実証されたベースレイアウトと防御戦略。迷路ラビリンスからコンパクトな要塞まで、あなたのプレイスタイルに合ったデザインを見つけてください。',
        'de': 'Bewährte Base-Layouts und Verteidigungsstrategien zum Schutz deiner Pets vor Raids. Von Maze-Labyrinthen bis zu kompakten Festungen findest du das Design, das zu deinem Spielstil passt.',
    },
    'home_about_label': {'ko': '게임 소개', 'ja': 'ゲームについて', 'de': 'Über das Spiel'},
    'home_about_title': {'ko': 'Build a Base and Steal이란?', 'ja': 'Build a Base and Stealとは？', 'de': 'Was ist Build a Base and Steal?'},
    'home_about_p1': {
        'ko': 'Build a Base and Steal은 오프라인에서도 패시브 소득을 생성하는 펫을 수집하는 Roblox 시뮬레이션 타이쿤 게임입니다. 희귀 Brainrot을 롤링하고, 보물을 보호할 맞춤형 기지를 설계하며, 장비를 사용해 다른 플레이어의 요새를 레이드하세요.',
        'ja': 'Build a Base and Stealは、オフライン時にもパッシブ収入を生成するペットを集めるRobloxシミュレーションタイクーンゲームです。レアなBrainrotをロールし、宝物を保護するカスタムベースを設計し、ギアを使って他のプレイヤーの要塞をレイドしましょう。',
        'de': 'Build a Base and Steal ist ein Roblox-Simulationstycoon-Spiel, in dem du Pets sammelst, die auch im Offline-Modus passives Einkommen generieren. Rolle für seltene Brainrots, entwirfe benutzerdefinierte Basen zum Schutz deiner Schätze, und verwende Ausrüstung, um die Festungen anderer Spieler zu überfallen.',
    },
    'home_about_p2': {
        'ko': '핵심 게임 루프는 전략적 펫 롤링, 방어를 위한 기지 건설, 다른 플레이어의 귀중한 펫을 훔치기 위한 전술적 레이딩으로 구성됩니다. 새 펫 롤링과 레이드에 대한 기지 강화 사이에서 예산을 균형 있게 조절하세요.',
        'ja': 'コアなゲームプレイループは、戦略的なペットローリング、防御のためのベース構築、他のプレイヤーの価値あるペットを盗むための戦術的なレイドで構成されています。新しいペットのローリングとレイドに対するベース強化の間で予算のバランスを取ってください。',
        'de': 'Der Kern-Spielkreis beinhaltet strategisches Pet-Rolling, Basenbau zur Verteidigung und taktische Raids, um wertvolle Pets von anderen Spielern zu stehlen. Balance dein Budget zwischen Rolling für neue Pets und der Befestigung deiner Base gegen Raids.',
    },
    'home_feature_pet_collecting': {'ko': '펫 수집', 'ja': 'ペット収集', 'de': 'Pet-Sammeln'},
    'home_feature_pet_collecting_desc': {
        'ko': '다양한 희귀도와 가치의 펫을 롤링하세요. 희귀 펫은 더 많은 소득을 생성하며 고가치 대상이 됩니다.',
        'ja': '異なるレアリティと価値のペットをロールする。レアペットはより多くの収入を生成し、高価値の対象となります。',
        'de': 'Rolle für Pets mit verschiedenen Seltenheiten und Werten. Seltene Pets generieren mehr Einkommen und werden zu hochwertigen Zielen.',
    },
    'home_feature_base_building': {'ko': '기지 건설', 'ja': 'ベース構築', 'de': 'Basenbau'},
    'home_feature_base_building_desc': {
        'ko': '레이드로부터 펫을 보호하기 위해 벽, 함정, 방어 구조물을 갖춘 맞춤형 기지를 설계하세요.',
        'ja': 'レイドからペットを保護するために壁、トラップ、防御構造物を備えたカスタムベースを設計する。',
        'de': 'Entwirf benutzerdefinierte Basen mit Wänden, Fallen und Verteidigungsstrukturen zum Schutz deiner Pets vor Raids.',
    },
    'home_feature_raiding_system': {'ko': '레이딩 시스템', 'ja': 'レイドシステム', 'de': 'Raid-System'},
    'home_feature_raiding_system_desc': {
        'ko': '장비와 전략을 사용해 다른 플레이어의 기지를 침투하고 귀중한 펫을 훔치세요.',
        'ja': 'ギアと戦略を使用して他のプレイヤーのベースに浸透し、価値あるペットを盗む。',
        'de': 'Verwende Ausrüstung und Strategie, um in die Basen anderer Spieler einzudringen und ihre wertvollen Pets zu stehlen.',
    },
    'home_feature_passive_income': {'ko': '패시브 소득', 'ja': 'パッシブ収入', 'de': 'Passives Einkommen'},
    'home_feature_passive_income_desc': {
        'ko': '오프라인에서도 펫이 소득을 생성합니다. 축적된 부와 진행 상황으로 돌아오세요.',
        'ja': 'オフラインでもペットが収入を生成します。蓄積された富と進行に戻ってください。',
        'de': 'Pets generieren Einkommen, auch wenn du offline bist. Komm zurück zu angesammeltem Reichtum und Fortschritt.',
    },
    'home_info_developer': {'ko': '개발자', 'ja': '開発者', 'de': 'Entwickler'},
    'home_info_developer_value': {'ko': 'replayable fun games', 'ja': 'replayable fun games', 'de': 'replayable fun games'},
    'home_info_platform': {'ko': '플랫폼', 'ja': 'プラットフォーム', 'de': 'Plattform'},
    'home_info_platform_value': {'ko': 'Roblox', 'ja': 'Roblox', 'de': 'Roblox'},
    'home_info_genre': {'ko': '장르', 'ja': 'ジャンル', 'de': 'Genre'},
    'home_info_genre_value': {'ko': '시뮬레이션 / 타이쿤', 'ja': 'シミュレーション / タイクーン', 'de': 'Simulation / Tycoon'},
    'home_info_visits': {'ko': '방문', 'ja': '訪問', 'de': 'Besuche'},
    'home_info_visits_value': {'ko': '25.9M+', 'ja': '25.9M+', 'de': '25.9M+'},
    'home_info_favorites': {'ko': '즐겨찾기', 'ja': 'お気に入り', 'de': 'Favoriten'},
    'home_info_favorites_value': {'ko': '174K+', 'ja': '174K+', 'de': '174K+'},
    'home_info_server': {'ko': '서버 규모', 'ja': 'サーバーサイズ', 'de': 'Servergröße'},
    'home_info_server_value': {'ko': '6명', 'ja': '6人', 'de': '6 Spieler'},
    'home_info_updated': {'ko': '마지막 업데이트', 'ja': '最終更新', 'de': 'Zuletzt aktualisiert'},
    'home_info_updated_value': {'ko': '2026년 7월', 'ja': '2026年7月', 'de': 'Juli 2026'},
    'home_about_cta_primary': {'ko': '모든 가이드 탐색', 'ja': 'すべてのガイドを探索', 'de': 'Alle Anleitungen erkunden'},
    'home_about_cta_secondary': {'ko': 'Roblox에서 플레이', 'ja': 'Robloxでプレイ', 'de': 'Auf Roblox spielen'},
    'home_final_cta_title': {
        'ko': 'Build a Base and Steal을 마스터할 준비가 되셨나요?',
        'ja': 'Build a Base and Stealをマスターする準備はできましたか？',
        'de': 'Bereit, Build a Base and Steal zu meistern?',
    },
    'home_final_cta_desc': {
        'ko': '오늘 제국 건설을 시작하고, 펫을 보호하고, 전설적인 보물을 레이드하세요.',
        'ja': '今日から帝国の構築を始め、ペットを保護し、伝説の宝をレイドしましょう。',
        'de': 'Starte heute mit dem Aufbau deines Imperiums, dem Schutz deiner Pets und Raids für legendäre Schätze.',
    },
    'home_final_cta_primary': {'ko': '초보자 가이드 읽기', 'ja': '初心者ガイドを読む', 'de': 'Einsteiger-Anleitung lesen'},
    'home_final_cta_secondary': {'ko': 'Roblox에서 플레이', 'ja': 'Robloxでプレイ', 'de': 'Auf Roblox spielen'},
    'section_faq': {'ko': 'FAQ', 'ja': 'よくある質問', 'de': 'FAQ'},
    'home_faq_title': {'ko': '자주 묻는 질문', 'ja': 'よくある質問', 'de': 'Häufig gestellte Fragen'},
    'home_cta_title': {'ko': '오늘 건설 제국을 시작하세요', 'ja': '今日、建設帝国を始めましょう', 'de': 'Starte heute dein Baureich'},
    'home_cta_description': {
        'ko': '궁극의 기지 건설과 펫 훔치기 모험에서 수백만 플레이어와 함께하세요. 희귀 펫을 롤링하고, 난공불락의 요새를 건설하며, Build a Base and Steal에서 가장 부유한 레이더가 되세요.',
        'ja': '究極のベース構築とペット盗みの冒険で数百万人のプレイヤーに加わりましょう。レアペットをロールし、侵入不可能な要塞を構築し、Build a Base and Stealで最も裕福なレイダーになりましょう。',
        'de': 'Schließe dich Millionen von Spielern im ultimativen Basenbau- und Pet-Diebstahl-Abenteuer an. Rolle seltene Pets, baue uneinnehmbare Festungen und werde der wohlhabendste Räuber in Build a Base and Steal.',
    },
    'home_featured_guides_title': {'ko': '추천 가이드', 'ja': '注目ガイド', 'de': 'Empfohlene Anleitungen'},
    'home_keyword_hub_title': {'ko': '인기 검색 주제', 'ja': '人気の検索トピック', 'de': 'Beliebte Suchthemen'},
    'view_all': {'ko': '모두 보기', 'ja': 'すべて表示', 'de': 'Alle anzeigen'},
    'read_more': {'ko': '더 읽기', 'ja': '続きを読む', 'de': 'Mehr lesen'},
    'featured_guides': {'ko': '추천 가이드', 'ja': '注目ガイド', 'de': 'Empfohlene Anleitungen'},
    'explore_all_guides': {'ko': '모든 가이드 탐색 →', 'ja': 'すべてのガイドを探索 →', 'de': 'Alle Anleitungen erkunden →'},
    'latest_updates': {'ko': '최신 업데이트', 'ja': '最新アップデート', 'de': 'Neueste Updates'},
    # ===== Rarity =====
    'rarity_legendary': {'ko': '전설', 'ja': 'レジェンダリー', 'de': 'Legendär'},
    'rarity_legendary_desc': {'ko': '가장 희귀하고 가치 있는 펫. 최대 소득 배수.', 'ja': '最も希少で価値あるペット。最大収入乗数。', 'de': 'Die seltensten und wertvollsten Pets. Maximale Einkommensmultiplikatoren.'},
    'rarity_mythic': {'ko': '신화', 'ja': 'ミシック', 'de': 'Mythisch'},
    'rarity_mythic_desc': {'ko': '매우 희귀한 펫으로 뛰어난 소득 잠재력을 가집니다.', 'ja': '非常に希少なペットで、優れた収入ポテンシャルを持ちます。', 'de': 'Extrem seltene Pets mit ausgezeichnetem Einkommenspotenzial.'},
    'rarity_epic': {'ko': '에픽', 'ja': 'エピック', 'de': 'Episch'},
    'rarity_epic_desc': {'ko': '좋은 소득 생성을 가진 희귀 펫.', 'ja': '良い収入生成を持つレアペット。', 'de': 'Seltene Pets mit gutem Einkommensgenerierung.'},
    'rarity_rare': {'ko': '희귀', 'ja': 'レア', 'de': 'Selten'},
    'rarity_rare_desc': {'ko': '괜찮은 소득 속도를 가진 일반적이지 않은 펫.', 'ja': 'まともな収入率を持つあまり一般的でないペット。', 'de': 'Ungewöhnliche Pets mit anständigen Einkommensraten.'},
    'rarity_color_legendary': {'ko': '금색', 'ja': '金', 'de': 'Gold'},
    'rarity_color_mythic': {'ko': '보라색', 'ja': '紫', 'de': 'Lila'},
    'rarity_color_epic': {'ko': '분홍색', 'ja': 'ピンク', 'de': 'Rosa'},
    'rarity_color_rare': {'ko': '파란색', 'ja': '青', 'de': 'Blau'},
    'difficulty_hard': {'ko': '어려움', 'ja': '難しい', 'de': 'Schwer'},
    'difficulty_medium': {'ko': '보통', 'ja': '普通', 'de': 'Mittel'},
    'difficulty_easy': {'ko': '쉬움', 'ja': '簡単', 'de': 'Einfach'},
    'effectiveness_very_high': {'ko': '매우 높음', 'ja': '非常に高い', 'de': 'Sehr hoch'},
    'effectiveness_high': {'ko': '높음', 'ja': '高い', 'de': 'Hoch'},
    'effectiveness_medium': {'ko': '보통', 'ja': '普通', 'de': 'Mittel'},
    # ===== Base designs =====
    'base_design_maze': {'ko': '미로 래버린스', 'ja': '迷路ラビリンス', 'de': 'Maze-Labyrinth'},
    'base_design_maze_desc': {'ko': '레이더를 혼란시키고 지연시키는 복잡한 굽은 길.', 'ja': 'レイダーを混乱させ遅延させる複雑な曲がり道。', 'de': 'Komplexe gewundene Wege, die Räuber verwirren und verzögern.'},
    'base_design_multi_layer': {'ko': '다층 방어', 'ja': '多層防御', 'de': 'Mehrschichtige Verteidigung'},
    'base_design_multi_layer_desc': {'ko': '체크포인트와 함정을 갖춘 여러 방어 층.', 'ja': 'チェックポイントとトラップを備えた複数の防御層。', 'de': 'Mehrere Verteidigungsschichten mit Kontrollpunkten und Fallen.'},
    'base_design_trap': {'ko': '함정 중심 레이아웃', 'ja': 'トラップ中心レイアウト', 'de': 'Fallen-fokussiertes Layout'},
    'base_design_trap_desc': {'ko': '최대 레이딩 피해를 위한 높은 함정 집중.', 'ja': '最大レイドダメージのための高いトラップ集中。', 'de': 'Schwere Fallenkonzentration für maximalen Raidschaden.'},
    'base_design_compact': {'ko': '콤팩트 요새', 'ja': 'コンパクト要塞', 'de': 'Kompakte Festung'},
    'base_design_compact_desc': {'ko': '집중된 방어를 갖춘 공간 효율적 설계.', 'ja': '集中防御を備えたスペース効率的なデザイン。', 'de': 'Platzeffizientes Design mit konzentrierten Verteidigungen.'},
    # ===== Pet types =====
    'pet_brainrot_legendary': {'ko': '전설 Brainrot', 'ja': 'レジェンダリーBrainrot', 'de': 'Legendärer Brainrot'},
    'pet_brainrot_mythic': {'ko': '신화 Brainrot', 'ja': 'ミシックBrainrot', 'de': 'Mythischer Brainrot'},
    'pet_brainrot_epic': {'ko': '에픽 Brainrot', 'ja': 'エピックBrainrot', 'de': 'Epischer Brainrot'},
    'pet_guard_legendary': {'ko': '전설 수호자', 'ja': 'レジェンダリーガード', 'de': 'Legendärer Wächter'},
    'pet_guard_mythic': {'ko': '신화 수호자', 'ja': 'ミシックガード', 'de': 'Mythischer Wächter'},
    'pet_attacker_legendary': {'ko': '전설 공격자', 'ja': 'レジェンダリーアタッカー', 'de': 'Legendärer Angreifer'},
    'pet_attacker_mythic': {'ko': '신화 공격자', 'ja': 'ミシックアタッカー', 'de': 'Mythischer Angreifer'},
    'pet_income_legendary': {'ko': '전설 소득', 'ja': 'レジェンダリー収入', 'de': 'Legendäres Einkommen'},
    'pet_income_mythic': {'ko': '신화 소득', 'ja': 'ミシック収入', 'de': 'Mythisches Einkommen'},
    'pet_income_epic': {'ko': '에픽 소득', 'ja': 'エピック収入', 'de': 'Episches Einkommen'},
    'pet_rarity_legendary': {'ko': '전설', 'ja': 'レジェンダリー', 'de': 'Legendär'},
    'pet_rarity_mythic': {'ko': '신화', 'ja': 'ミシック', 'de': 'Mythisch'},
    'pet_rarity_epic': {'ko': '에픽', 'ja': 'エピック', 'de': 'Episch'},
    'pet_rarity_rare': {'ko': '희귀', 'ja': 'レア', 'de': 'Selten'},
    'pet_rarity_common': {'ko': '일반', 'ja': 'コモン', 'de': 'Häufig'},
    'pet_type_brainrot': {'ko': 'Brainrot', 'ja': 'Brainrot', 'de': 'Brainrot'},
    'pet_type_guard': {'ko': '수호자', 'ja': 'ガード', 'de': 'Wächter'},
    'pet_type_attacker': {'ko': '공격자', 'ja': 'アタッカー', 'de': 'Angreifer'},
    'pet_type_income': {'ko': '소득', 'ja': '収入', 'de': 'Einkommen'},
    # ===== Gear =====
    'gear_weapon_basic': {'ko': '기본 무기', 'ja': '基本武器', 'de': 'Basiswaffe'},
    'gear_weapon_advanced': {'ko': '고급 무기', 'ja': '高度な武器', 'de': 'Fortgeschrittene Waffe'},
    'gear_weapon_legendary': {'ko': '전설 무기', 'ja': 'レジェンダリー武器', 'de': 'Legendäre Waffe'},
    'gear_shield_basic': {'ko': '기본 방패', 'ja': '基本盾', 'de': 'Basisschild'},
    'gear_shield_advanced': {'ko': '고급 방패', 'ja': '高度な盾', 'de': 'Fortgeschrittener Schild'},
    'gear_tool_infiltration': {'ko': '침투 도구', 'ja': '浸透ツール', 'de': 'Infiltrationswerkzeug'},
    'gear_tool_extraction': {'ko': '추출 도구', 'ja': '抽出ツール', 'de': 'Extraktionswerkzeug'},
    'gear_boost_luck': {'ko': '행운 부스트', 'ja': 'ラックブースト', 'de': 'Glücks-Boost'},
    'gear_boost_income': {'ko': '소득 부스트', 'ja': '収入ブースト', 'de': 'Einkommens-Boost'},
    'gear_type_weapon': {'ko': '무기', 'ja': '武器', 'de': 'Waffe'},
    'gear_type_shield': {'ko': '방패', 'ja': '盾', 'de': 'Schild'},
    'gear_type_tool': {'ko': '도구', 'ja': 'ツール', 'de': 'Werkzeug'},
    'gear_type_boost': {'ko': '부스트', 'ja': 'ブースト', 'de': 'Boost'},
    'gear_weapon_basic_effect': {'ko': '기본 벽 피해', 'ja': '基本壁ダメージ', 'de': 'Basiswandschaden'},
    'gear_weapon_advanced_effect': {'ko': '향상된 벽 피해', 'ja': '強化壁ダメージ', 'de': 'Verbesserter Wandschaden'},
    'gear_weapon_legendary_effect': {'ko': '최대 벽 파괴', 'ja': '最大壁破壊', 'de': 'Maximale Wandzerstörung'},
    'gear_shield_basic_effect': {'ko': '기본 피해 감소', 'ja': '基本ダメージ減少', 'de': 'Basis-Schadensreduktion'},
    'gear_shield_advanced_effect': {'ko': '향상된 피해 감소', 'ja': '強化ダメージ減少', 'de': 'Verbesserte Schadensreduktion'},
    'gear_tool_infiltration_effect': {'ko': '특정 방어 우회', 'ja': '特定の防御を回避', 'de': 'Bestimmte Verteidigungen umgehen'},
    'gear_tool_extraction_effect': {'ko': '더 빠른 펫 추출', 'ja': 'より速いペット抽出', 'de': 'Schnellerer Pet-Diebstahl'},
    'gear_boost_luck_effect': {'ko': '향상된 롤 확률', 'ja': '向上したロール率', 'de': 'Erhöhte Drop-Chancen'},
    'gear_boost_income_effect': {'ko': '소득 생성 증가', 'ja': '収入生成の増加', 'de': 'Einkommensmultiplikator'},
    # ===== Guide categories =====
    'guide_category_Base Defense': {'ko': '기지 방어', 'ja': 'ベース防衛', 'de': 'Basisverteidigung'},
    'guide_category_Beginner Guide': {'ko': '초보자 가이드', 'ja': '初心者ガイド', 'de': 'Anfängerleitfaden'},
    'guide_category_Codes': {'ko': '코드', 'ja': 'コード', 'de': 'Codes'},
    'guide_category_Community': {'ko': '커뮤니티', 'ja': 'コミュニティ', 'de': 'Community'},
    'guide_category_FAQ': {'ko': 'FAQ', 'ja': 'よくある質問', 'de': 'FAQ'},
    'guide_category_Gear': {'ko': '장비', 'ja': 'ギア', 'de': 'Ausrüstung'},
    'guide_category_Guides': {'ko': '가이드', 'ja': 'ガイド', 'de': 'Anleitungen'},
    'guide_category_Offline Money': {'ko': '오프라인 돈', 'ja': 'オフラインマネー', 'de': 'Offline-Geld'},
    'guide_category_Pet Rolling': {'ko': '펫 롤링', 'ja': 'ペットローリング', 'de': 'Pet-Würfeln'},
    'guide_category_Pets List': {'ko': '펫 목록', 'ja': 'ペットリスト', 'de': 'Haustierliste'},
    'guide_category_Raiding': {'ko': '레이딩', 'ja': 'レイド', 'de': 'Raiding'},
    'guide_category_Strategies': {'ko': '전략', 'ja': '戦略', 'de': 'Strategien'},
    'guide_category_Updates': {'ko': '업데이트', 'ja': 'アップデート', 'de': 'Updates'},
    # ===== About page =====
    'about_gameTitle': {'ko': 'Build a Base and Steal 소개', 'ja': 'Build a Base and Stealについて', 'de': 'Über Build a Base and Steal'},
    'about_gameP1': {
        'ko': 'Build a Base and Steal은 오프라인에서도 패시브 소득을 생성하는 펫을 수집하는 Roblox 시뮬레이션 타이쿤 게임입니다. 희귀 Brainrot을 롤링하고, 보물을 보호할 맞춤형 기지를 설계하며, 장비를 사용해 다른 플레이어의 요새를 레이드하세요.',
        'ja': 'Build a Base and Stealは、オフライン時にもパッシブ収入を生成するペットを集めるRobloxシミュレーションタイクーンゲームです。レアなBrainrotをロールし、宝物を保護するカスタムベースを設計し、ギアを使って他のプレイヤーの要塞をレイドしましょう。',
        'de': 'Build a Base and Steal ist ein Roblox-Simulationstycoon-Spiel, in dem du Pets sammelst, die auch im Offline-Modus passives Einkommen generieren. Rolle für seltene Brainrots, entwirfe benutzerdefinierte Basen zum Schutz deiner Schätze, und verwende Ausrüstung, um die Festungen anderer Spieler zu überfallen.',
    },
    'about_gameP2': {
        'ko': '핵심 게임 루프는 전략적 펫 롤링, 방어를 위한 기지 건설, 다른 플레이어의 귀중한 펫을 훔치기 위한 전술적 레이딩으로 구성됩니다. 새 펫 롤링과 레이드에 대한 기지 강화 사이에서 예산을 균형 있게 조절하세요.',
        'ja': 'コアなゲームプレイループは、戦略的なペットローリング、防御のためのベース構築、他のプレイヤーの価値あるペットを盗むための戦術的なレイドで構成されています。新しいペットのローリングとレイドに対するベース強化の間で予算のバランスを取ってください。',
        'de': 'Der Kern-Spielkreis beinhaltet strategisches Pet-Rolling, Basenbau zur Verteidigung und taktische Raids, um wertvolle Pets von anderen Spielern zu stehlen. Balance dein Budget zwischen Rolling für neue Pets und der Befestigung deiner Base gegen Raids.',
    },
    'about_wikiTitle': {'ko': 'Build a Base and Steal 위키란?', 'ja': 'Build a Base and Steal Wikiとは？', 'de': 'Was ist Build a Base and Steal Wiki?'},
    'about_wikiP1': {
        'ko': 'Build a Base and Steal 위키는 플레이어가 펫 롤링, 기지 건설, 레이딩 전략을 마스터하도록 돕는 커뮤니티 기반 리소스입니다. 이 위키는 replayable fun games와 제휴하지 않습니다.',
        'ja': 'Build a Base and Steal Wikiは、プレイヤーがペットローリング、ベース構築、レイド戦略をマスターするのを助けるコミュニティ駆動のリソースです。このウィキはreplayable fun gamesと提携していません。',
        'de': 'Build a Base and Steal Wiki ist eine community-getragene Ressource, die Spielern hilft, Pet-Rolling, Basenbau und Raiding-Strategien zu meistern. Dieses Wiki ist nicht mit replayable fun games verbunden.',
    },
    'about_wikiP2': {'ko': '모든 게임 자산, 이름, 상표는 각 소유자의 재산입니다.', 'ja': 'すべてのゲームアセット、名称、商標はそれぞれの所有者の財産です。', 'de': 'Alle Spiel-Assets, Namen und Marken sind Eigentum ihrer jeweiligen Eigentümer.'},
    'about_disclaimerTitle': {'ko': '면책 조항', 'ja': '免責事項', 'de': 'Haftungsausschluss'},
    'about_disclaimerP': {
        'ko': '이것은 비공식 팬 제작 위키입니다. Build a Base and Steal은 replayable fun games가 개발했습니다. 모든 게임 콘텐츠, 이름, 이미지는 각 소유자의 상표 또는 저작권입니다. 이 위키는 정보 제공 목적으로만 작성되었으며 게임 자산의 소유권을 주장하지 않습니다.',
        'ja': 'これは非公式のファン制作ウィキです。Build a Base and Stealはreplayable fun gamesによって開発されています。すべてのゲームコンテンツ、名称、画像はそれぞれの所有者の商標または著作権です。このウィキは情報提供のみを目的としており、ゲームアセットの所有権を主張しません。',
        'de': 'Dies ist ein inoffizielles Fan-Wiki. Build a Base and Steal wird von replayable fun games entwickelt. Alle Spielinhalte, Namen und Bilder sind Marken oder Urheberrechte ihrer jeweiligen Eigentümer. Dieses Wiki dient nur zu Informationszwecken und beansprucht kein Eigentum an Spiel-Assets.',
    },
    'about_coverTitle': {'ko': '다루는 내용', 'ja': 'カバーする内容', 'de': 'Was wir abdecken'},
    'about_cover_1': {'ko': '활성 코드', 'ja': 'アクティブなコード', 'de': 'Aktive Codes'},
    'about_cover_1_desc': {'ko': '무료 펫, 현금, 부스트를 주는 현재 작동하는 교환 코드', 'ja': '無料ペット、現金、ブーストを提供する現在機能する引き換えコード', 'de': 'Aktuell funktionierende Einlösecodes für kostenlose Pets, Geld und Boosts'},
    'about_cover_2': {'ko': '초보자 가이드', 'ja': '初心者ガイド', 'de': 'Einsteiger-Anleitung'},
    'about_cover_2_desc': {'ko': '새 플레이어를 위한 완전한 안내 - 첫 세션 팁과 기본', 'ja': '新しいプレイヤーのための完全なウォークスルー - 最初のセッションのヒントと基本', 'de': 'Vollständiger Walkthrough für neue Spieler - Tipps und Grundlagen für die erste Sitzung'},
    'about_cover_3': {'ko': '펫 롤링', 'ja': 'ペットローリング', 'de': 'Pet-Rolling'},
    'about_cover_3_desc': {'ko': '희귀 펫 롤링 방법, 예산 계획, 드롭 확률', 'ja': 'レアペットのロール方法、予算計画、ドロップ率', 'de': 'Wie man für seltene Pets rollt, Budgetplanung und Drop-Raten'},
    'about_cover_4': {'ko': '기지 방어', 'ja': 'ベース防衛', 'de': 'Base-Defense'},
    'about_cover_4_desc': {'ko': '최고의 기지 설계, 방어 전략, 보호 팁', 'ja': '最高のベースデザイン、防御戦略、保護のヒント', 'de': 'Beste Base-Designs, Verteidigungsstrategien und Schutztipps'},
    'about_cover_5': {'ko': '레이딩', 'ja': 'レイド', 'de': 'Raids'},
    'about_cover_5_desc': {'ko': '다른 플레이어 레이드 방법, 장비 사용, 훔치기 전략', 'ja': '他のプレイヤーのレイド方法、ギアの使用、盗みの戦略', 'de': 'Wie man andere Spieler überfällt, Ausrüstungsverwendung und Diebstahlsstrategien'},
    'about_cover_6': {'ko': '오프라인 돈', 'ja': 'オフラインマネー', 'de': 'Offline-Geld'},
    'about_cover_6_desc': {'ko': '고급 전략으로 오프라인 중 패시브 소득 극대화', 'ja': '高度な戦略でオフライン中のパッシブ収入を最大化', 'de': 'Maximiere passives Einkommen im Offline-Modus mit fortgeschrittenen Strategien'},
    'about_sourcesTitle': {'ko': '출처', 'ja': '情報源', 'de': 'Unsere Quellen'},
    'about_source_1': {'ko': '게임 내 테스트 및 데이터 수집', 'ja': 'ゲーム内テストとデータ収集', 'de': 'Im Spiel getestet und Daten gesammelt'},
    'about_source_2': {'ko': '공식 Build a Base and Steal Discord 및 개발자 공지', 'ja': '公式Build a Base and Steal Discordと開発者発表', 'de': 'Offizieller Build a Base and Steal Discord und Entwicklerankündigungen'},
    'about_source_3': {'ko': 'Roblox 게임 페이지 업데이트와 커뮤니티 토론', 'ja': 'Robloxゲームページの更新とコミュニティディスカッション', 'de': 'Roblox-Spielseiten-Updates und Community-Diskussionen'},
    'about_source_4': {'ko': '커뮤니티 제출 전략과 기지 설계', 'ja': 'コミュニティ投稿の戦略とベースデザイン', 'de': 'Von der Community eingereichte Strategien und Base-Designs'},
    'about_playRoblox': {'ko': 'Roblox에서 플레이', 'ja': 'Robloxでプレイ', 'de': 'Auf Roblox spielen'},
    'about_officialPage': {'ko': '공식 게임 사이트', 'ja': '公式ゲームサイト', 'de': 'Offizielle Spiel-Website'},
    'about_joinDiscord': {'ko': 'Discord 참여', 'ja': 'Discordに参加', 'de': 'Discord beitreten'},
    'about_watchYouTube': {'ko': 'YouTube에서 보기', 'ja': 'YouTubeで見る', 'de': 'Auf YouTube ansehen'},
    'about_communityServer': {'ko': '커뮤니티 서버', 'ja': 'コミュニティサーバー', 'de': 'Community-Server'},
    'about_devChannel': {'ko': '개발자 채널', 'ja': '開発者チャンネル', 'de': 'Entwicklerkanal'},
    'privacy_policy_title': {'ko': '개인정보 처리방침', 'ja': 'プライバシーポリシー', 'de': 'Datenschutzrichtlinie'},
    'terms_of_service_title': {'ko': '서비스 이용약관', 'ja': '利用規約', 'de': 'Nutzungsbedingungen'},
    'tierList_tierLabel': {'ko': '티어', 'ja': 'ティア', 'de': 'Tier'},
    # ===== Page descriptions =====
    'page_codes_description': {
        'ko': 'Build a Base and Steal의 활성 작동 코드 전체 목록. 이 코드를 교환하여 무료 펫, 현금, 부스트 등 가치 있는 아이템을 얻고 더 빨리 진행하세요.',
        'ja': 'Build a Base and Stealのアクティブな機能コードの完全なリスト。これらのコードを引き換えて、無料のペット、現金、ブースト、その他の価値あるアイテムを入手し、より速く進行しましょう。',
        'de': 'Vollständige Liste der aktiven funktionierenden Codes für Build a Base and Steal. Löse diese Codes ein, um kostenlose Pets, Geld, Boosts und andere wertvolle Items zu erhalten und schneller voranzukommen.',
    },
    'page_beginnerGuide_description': {
        'ko': 'Build a Base and Steal의 완전한 초보자 안내. 첫 세션에서 펫 롤링, 기지 건설, 레이딩의 기본을 배우세요.',
        'ja': 'Build a Base and Stealの完全な初心者ウォークスルー。最初のセッションでペットローリング、ベース構築、レイドの基本を学びましょう。',
        'de': 'Vollständiger Einsteiger-Walkthrough für Build a Base and Steal. Lerne in deiner ersten Sitzung die Grundlagen von Pet-Rolling, Basenbau und Raiding.',
    },
    'page_petRolling_description': {
        'ko': '펫 롤링 메커니즘을 마스터하고, 드롭 확률을 이해하며, 희귀 Brainrot과 고가치 펫을 얻기 위한 전략을 익히세요.',
        'ja': 'ペットローリングのメカニクスをマスターし、ドロップ率を理解し、レアなBrainrotと高価値ペットを得るための戦略を学びましょう。',
        'de': 'Meistere Pet-Rolling-Mechaniken, verstehe Drop-Raten, Budgetplanung und Strategien, um seltene Brainrots und hochwertige Pets zu erhalten.',
    },
    'page_baseDefense_description': {
        'ko': '레이드로부터 펫을 보호하기 위한 최고의 기지 설계, 방어 전략, 보호 팁. 난공불락의 요새를 건설하세요.',
        'ja': 'レイドからペットを保護するための最高のベースデザイン、防御戦略、保護のヒント。侵入不可能な要塞を構築しましょう。',
        'de': 'Beste Base-Designs, Verteidigungsstrategien und Schutztipps, um deine Pets vor Raids zu schützen. Baue uneinnehmbare Festungen.',
    },
    'page_raiding_description': {
        'ko': '장비 사용, 침투 전략, 다른 플레이어의 귀중한 펫을 훔치는 팁을 포함한 종합 레이딩 가이드.',
        'ja': 'ギアの使用、浸透戦略、他のプレイヤーの価値あるペットを盗むヒントを含む包括的なレイドガイド。',
        'de': 'Umfassende Raid-Anleitung inklusive Ausrüstungsverwendung, Infiltrationsstrategien und Tipps zum Stehlen wertvoller Pets von anderen Spielern.',
    },
    'page_offlineMoney_description': {
        'ko': '고급 계산 전략과 최적화 기법으로 Build a Base and Steal에서 오프라인 패시브 소득을 극대화하세요.',
        'ja': '高度な計算戦略と最適化テクニックでBuild a Base and Stealのオフラインパッシブ収入を最大化しましょう。',
        'de': 'Maximiere dein passives Einkommen im Offline-Modus mit fortgeschrittenen Berechnungsstrategien und Optimierungstechniken für Build a Base and Steal.',
    },
    'page_petsList_description': {
        'ko': '모든 희귀도, 능력치, 가치, 소득 배수를 갖춘 완전한 펫 데이터베이스. 당신의 전략에 가장 좋은 펫을 찾으세요.',
        'ja': 'すべてのレアリティ、ステータス、価値、収入乗数を備えた完全なペットデータベース。あなたの戦略に最適なペットを見つけてください。',
        'de': 'Vollständige Pet-Datenbank mit allen Seltenheiten, Stats, Werten und Einkommensmultiplikatoren. Finde die besten Pets für deine Strategie.',
    },
    'page_gear_description': {
        'ko': '모든 레이딩 장비, 무기, 방패, 도구, 부스트. 각 아이템의 기능과 효과적인 사용 시기를 배우세요.',
        'ja': 'すべてのレイドギア、武器、盾、ツール、ブースト。各アイテムの機能と効果的な使用时机を学びましょう。',
        'de': 'Alle Raid-Ausrüstung, Waffen, Schilde, Werkzeuge und Boosts. Lerne, was jeder Gegenstand tut und wann du ihn effektiv einsetzt.',
    },
    'page_strategies_description': {
        'ko': 'Build a Base and Steal을 지배할 고급 프로 팁, 팀 전술, 고수준 게임플레이 전략.',
        'ja': 'Build a Base and Stealを支配するための高度なプロのヒント、チーム戦術、ハイレベルなゲームプレイ戦略。',
        'de': 'Erweiterte Pro-Tipps, Teamtaktiken und High-Level-Gameplay-Strategien, um Build a Base and Steal zu dominieren.',
    },
    'page_faq_description': {
        'ko': '자주 묻는 질문과 해결된 일반적인 문제. Build a Base and Steal에 관한 모든 질문에 대한 답을 얻으세요.',
        'ja': 'よくある質問と解決済みの一般的な問題。Build a Base and Stealに関するすべての質問に対する回答を得てください。',
        'de': 'Häufig gestellte Fragen und gelöste Probleme. Erhalte Antworten auf alle deine Build a Base and Steal Fragen.',
    },
    'page_updates_description': {
        'ko': 'Build a Base and Steal의 최신 게임 업데이트, 패치 노트, 새로운 기능, 변경 사항.',
        'ja': 'Build a Base and Stealの最新ゲームアップデート、パッチノート、新機能、変更点。',
        'de': 'Neueste Spiel-Updates, Patch-Notizen, neue Funktionen und Änderungen in Build a Base and Steal.',
    },
    'page_community_description': {
        'ko': 'Discord, YouTube, 기타 플랫폼에서 Build a Base and Steal 커뮤니티에 참여하세요. 다른 플레이어와 연결되고 최신 뉴스를 받으세요.',
        'ja': 'Discord、YouTube、その他のプラットフォームでBuild a Base and Stealコミュニティに参加してください。他のプレイヤーと繋がり、最新ニュースを入手しましょう。',
        'de': 'Tritt der Build a Base and Steal Community auf Discord, YouTube und anderen Plattformen bei. Verbinde dich mit anderen Spielern und erhalte die neuesten Nachrichten.',
    },
    'page_guides_description': {
        'ko': 'Build a Base and Steal 전체 가이드 라이브러리 탐색 - 롤링, 방어, 레이딩, 거래, 파밍, 모든 플레이어 레벨의 진행을 다룹니다.',
        'ja': 'Build a Base and Stealの完全なガイドライブラリを見る - ローリング、防御、レイド、取引、ファーミング、すべてのプレイヤーレベルの進行をカバー。',
        'de': 'Durchsuche die vollständige Build a Base and Steal Guide-Bibliothek - Rollen, Verteidigung, Raids, Handel, Farmen und Fortschritt für jede Spielerstufe.',
    },
    'page_about_description': {
        'ko': 'Build a Base and Steal 게임과 이 커뮤니티 위키 프로젝트에 대해 알아보세요.',
        'ja': 'Build a Base and Stealゲームとこのコミュニティウィキプロジェクトについて学ぶ。',
        'de': 'Erfahre mehr über das Build a Base and Steal Spiel und dieses Community-Wiki-Projekt.',
    },
    'page_privacyPolicy_description': {
        'ko': 'Build a Base and Steal 위키의 개인정보 처리방침.',
        'ja': 'Build a Base and Steal Wikiのプライバシーポリシー。',
        'de': 'Datenschutzrichtlinie für Build a Base and Steal Wiki.',
    },
    'page_sitemap_description': {
        'ko': 'Build a Base and Steal 위키의 모든 페이지에 대한 완전한 사이트맵.',
        'ja': 'Build a Base and Steal Wikiのすべてのページの完全なサイトマップ。',
        'de': 'Vollständige Sitemap aller Seiten auf Build a Base and Steal Wiki.',
    },
    'page_termsOfService_description': {
        'ko': 'Build a Base and Steal 위키의 서비스 이용약관.',
        'ja': 'Build a Base and Steal Wikiの利用規約。',
        'de': 'Nutzungsbedingungen für Build a Base and Steal Wiki.',
    },
    # ===== Common =====
    'common_readMore': {'ko': '더 읽기', 'ja': '続きを読む', 'de': 'Mehr lesen'},
    'common_updated': {'ko': '업데이트됨', 'ja': '更新済み', 'de': 'Aktualisiert'},
    'content_fallbackNotice': {'ko': '콘텐츠를 사용할 수 없습니다', 'ja': 'コンテンツは利用できません', 'de': 'Inhalt nicht verfügbar'},
    'content_noContent': {'ko': '사용 가능한 콘텐츠 없음', 'ja': '利用可能なコンテンツはありません', 'de': 'Kein Inhalt verfügbar'},
    'explore_more': {'ko': '더 탐색하기', 'ja': 'さらに探索', 'de': 'Mehr erkunden'},
    'footer_community': {'ko': '커뮤니티', 'ja': 'コミュニティ', 'de': 'Community'},
    'footer_gameCategories': {'ko': '게임 카테고리', 'ja': 'ゲームカテゴリー', 'de': 'Spielkategorien'},
    'footer_joinDiscord': {'ko': 'Discord 참여', 'ja': 'Discordに参加', 'de': 'Discord beitreten'},
    'footer_officialYouTube': {'ko': '공식 YouTube', 'ja': '公式YouTube', 'de': 'Offizielles YouTube'},
    'footer_playOnSteam': {'ko': 'Roblox에서 플레이', 'ja': 'Robloxでプレイ', 'de': 'Auf Roblox spielen'},
    'footer_resources': {'ko': '리소스', 'ja': 'リソース', 'de': 'Ressourcen'},
    'footer_rights': {'ko': '모든 권리 보유', 'ja': 'すべての権利予約', 'de': 'Alle Rechte vorbehalten'},
    'guide_beginner': {'ko': '초보자', 'ja': '初心者', 'de': 'Einsteiger'},
    'guide_nav_all': {'ko': '모든 가이드', 'ja': 'すべてのガイド', 'de': 'Alle Anleitungen'},
    'guide_nav_next': {'ko': '다음', 'ja': '次へ', 'de': 'Weiter'},
    'guide_nav_prev': {'ko': '이전', 'ja': '前へ', 'de': 'Zurück'},
    'guide_sidebar_all': {'ko': '모든 가이드 보기', 'ja': 'すべてのガイドを表示', 'de': 'Alle Anleitungen anzeigen'},
    'guide_sidebar_more': {'ko': '더 많은 가이드', 'ja': 'もっとガイド', 'de': 'Weitere Anleitungen'},
    'guide_sidebar_toc': {'ko': '목차', 'ja': '目次', 'de': 'Inhaltsverzeichnis'},
    'guides_featured': {'ko': '추천 가이드', 'ja': '注目ガイド', 'de': 'Empfohlene Anleitungen'},
    'no_articles_yet': {'ko': '아직 기사가 없습니다', 'ja': 'まだ記事がありません', 'de': 'Noch keine Artikel'},
    'section_codes_desc': {'ko': 'Build a Base and Steal의 활성 작동 코드', 'ja': 'Build a Base and Stealのアクティブな機能コード', 'de': 'Aktive funktionierende Codes für Build a Base and Steal'},
    'section_guides_desc': {'ko': '모든 게임플레이 측면을 위한 종합 가이드', 'ja': 'すべてのゲームプレイ側面の包括的なガイド', 'de': 'Umfassende Anleitungen für alle Aspekte des Gameplays'},
    'sidebar_wikiNav': {'ko': '위키 탐색', 'ja': 'ウィキナビゲーション', 'de': 'Wiki-Navigation'},
    'sitemap_legalPages': {'ko': '법적 페이지', 'ja': '法的ページ', 'de': 'Rechtliche Seiten'},
    'sitemap_mainPages': {'ko': '주요 페이지', 'ja': 'メインページ', 'de': 'Hauptseiten'},
    # ===== Featured guides =====
    'featured_guide_beginner_title': {
        'ko': 'Build a Base and Steal 초보자 가이드 - 여정 시작',
        'ja': 'Build a Base and Steal初心者ガイド - 旅の始まり',
        'de': 'Build a Base and Steal Einsteigerleitfaden - Starte deine Reise',
    },
    'featured_guide_beginner_desc': {
        'ko': '게임이 처음이신가요? 첫 30분, 일상 루틴, 핵심 경제 메커니즘을 다루는 종합 초보자 가이드로 시작하세요.',
        'ja': 'ゲームが初めてですか？最初の30分、日常ルーチン、コア経済メカニクスをカバーする包括的な初心者ガイドから始めましょう。',
        'de': 'Neu beim Spiel? Starte mit unserem umfassenden Einsteigerleitfaden, der die ersten 30 Minuten, tägliche Routinen und Kernwirtschaftsmechaniken abdeckt.',
    },
    'featured_guide_rolling_title': {
        'ko': '펫 롤링 드롭 확률 및 전략 가이드',
        'ja': 'ペットローリングのドロップ率と戦略ガイド',
        'de': 'Pet-Rolling Drop-Raten und Strategieleitfaden',
    },
    'featured_guide_rolling_desc': {
        'ko': '상세한 드롭 확률 분석, 가차 시스템 분석, 효율적 진행을 위한 예산 관리 전략으로 펫 롤링을 마스터하세요.',
        'ja': '詳細なドロップ率分析、天井システムの分解、効率的な進行のための予算管理戦略でペットローリングをマスターしましょう。',
        'de': 'Meistere Pet-Rolling mit detaillierter Drop-Raten-Analyse, Pity-System-Aufschlüsselung und Budgetverwaltungs-Strategien für effizienten Fortschritt.',
    },
    'featured_guide_base_title': {
        'ko': '최고의 기지 방어 레이아웃 및 보호',
        'ja': '最高のベース防御レイアウトと保護',
        'de': 'Bestes Base-Defense-Layout und Schutz',
    },
    'featured_guide_base_desc': {
        'ko': '벽 전략, 함정 시스템, 다층 방어, 카운터 레이더 전술을 다루는 완전한 기지 방어 가이드로 귀중한 펫을 보호하세요.',
        'ja': '壁戦略、トラップシステム、多層防御、対レイダー戦術をカバーする完全なベース防御ガイドで価値あるペットを保護しましょう。',
        'de': 'Schütze deine wertvollen Pets mit unserem vollständigen Base-Defense-Leitfaden zu Wandstrategien, Fallensystemen, mehrschichtiger Verteidigung und Anti-Raider-Taktiken.',
    },
    # ===== FAQ (home page) =====
    'faq_how_to_start': {'ko': 'Build a Base and Steal 플레이는 어떻게 시작하나요?', 'ja': 'Build a Base and Stealのプレイはどうやって始めますか？', 'de': 'Wie fange ich an, Build a Base and Steal zu spielen?'},
    'faq_how_to_start_answer': {
        'ko': '무료 화폐로 첫 펫을 롤링하면서 시작하세요. 펫을 보호할 간단한 기지를 짜고 패시브 소득을 올리기 시작하세요. 부가 축적되면 더 나은 펫과 더 강한 기지 방어에 투자하세요.',
        'ja': '無料通貨で最初のペットをロールすることから始めます。彼らを保護するためにシンプルなベースを構築し、パッシブ収入を稼ぎ始めます。富が蓄積されたら、より良いペットとより強力なベース防御に投資します。',
        'de': 'Starte, indem du mit der freien Währung für deine ersten Pets rollst. Baue eine einfache Base zum Schutz und beginne dann, passives Einkommen zu verdienen. Investiere mit zunehmendem Reichtum in bessere Pets und stärkere Base-Verteidigungen.',
    },
    'faq_best_pets': {'ko': '롤링하기 가장 좋은 펫은 무엇인가요?', 'ja': 'ロールするのに最適なペットは何ですか？', 'de': 'Welche sind die besten Pets zum Rollen?'},
    'faq_best_pets_answer': {
        'ko': '전설 Brainrot이 가장 높은 소득 배수를 제공하지만 롤링 비용이 비쌉니다. 더 나은 가성비를 위해 에픽과 신화 펫으로 시작하고, 안정적인 소득이 생기면 전설 펫을 위해 저축하세요.',
        'ja': 'レジェンダリーBrainrotは最高の収入乗数を提供しますが、ロールするのが高価です。より良い価値のためにエピックとミシックペットから始め、安定した収入ができたらレジェンダリーペットのために貯金します。',
        'de': 'Legendäre Brainrots bieten die höchsten Einkommensmultiplikatoren, sind aber teuer zu rollen. Beginne mit epischen und mythischen Pets für besseren Wert, spare dann für legendäre Pets, sobald du ein stabiles Einkommen hast.',
    },
    'faq_base_protection': {'ko': '레이드로부터 기지를 어떻게 보호하나요?', 'ja': 'レイドからベースをどうやって保護しますか？', 'de': 'Wie schütze ich meine Base vor Raids?'},
    'faq_base_protection_answer': {
        'ko': '미로형 레이아웃, 여러 벽 층, 전략적 함정 배치를 사용하세요. 콤팩트 기지는 탐색하기 어렵고 미로 기지는 레이더를 혼란시킵니다. 방어 비용과 보호하는 펫의 가치를 균형 있게 조절하세요.',
        'ja': '迷路のようなレイアウト、複数の壁の層、戦略的なトラップ配置を使用してください。コンパクトなベースはナビゲートが難しく、迷路ベースはレイダーを混乱させます。防御コストと保護するペットの価値のバランスを取ってください。',
        'de': 'Verwende maze-artige Layouts, mehrere Wandschichten und strategische Fallenplatzierung. Kompakte Basen sind schwerer zu navigieren, während Maze-Basen Räuber verwirren. Balance die Verteidigungskosten mit dem Wert der Pets, die du schützt.',
    },
    'faq_offline_income': {'ko': '오프라인 소득은 어떻게 작동하나요?', 'ja': 'オフライン収入はどう機能しますか？', 'de': 'Wie funktioniert Offline-Einkommen?'},
    'faq_offline_income_answer': {
        'ko': '오프라인에서도 펫이 계속 소득을 생성합니다. 금액은 펫 희귀도, 수량, 부스트 아이템에 따라 달라집니다. 소득은 오프라인 12시간에서 제한되므로 최대 수익을 모으려면 정기적으로 로그인하세요.',
        'ja': 'オフラインでもペットは収入を生成し続けます。金額はペットのレアリティ、数量、ブーストアイテムによって異なります。収入はオフライン12時間で上限に達するので、最大の収益を集めるには定期的にログインしてください。',
        'de': 'Deine Pets generieren weiterhin Einkommen, auch wenn du offline bist. Der Betrag hängt von Pet-Seltenheit, -menge und allen Boost-Items ab. Das Einkommen ist auf 12 Stunden Offline begrenzt, also melde dich regelmäßig an, um maximale Einnahmen zu sammeln.',
    },
    'faq_raiding_tips': {'ko': '가장 좋은 레이딩 전략은 무엇인가요?', 'ja': '最も良いレイド戦略は何ですか？', 'de': 'Was sind die besten Raid-Strategien?'},
    'faq_raiding_tips_answer': {
        'ko': '먼저 대상을 정찰해 방어를 평가하세요. 미로에는 침투 도구, 직접 공격에는 무기 등 기지 유형에 맞는 장비를 사용하세요. 대상이 부를 축적했을 가능성이 높을 때 레이드를 계획하세요.',
        'ja': 'まずターゲットを偵察して防御を評価してください。迷路には浸透ツール、直接攻撃には武器など、ベースタイプに適したギアを使用してください。ターゲットが富を蓄積している可能性が高い時にレイドを計画してください。',
        'de': 'Kundschafter zuerst, um ihre Verteidigungen zu bewerten. Verwende entsprechende Ausrüstung für verschiedene Base-Typen — Infiltrationswerkzeuge für Mazes, Waffen für direkte Angriffe. Plane deine Raids, wenn Ziele wahrscheinlich angesammelten Reichtum haben.',
    },
    'faq_codes_working': {'ko': '작동하는 코드가 있나요?', 'ja': '機能するコードはありますか？', 'de': 'Gibt es funktionierende Codes?'},
    'faq_codes_working_answer': {
        'ko': '현재 활성 작동 코드가 없습니다. 코드는 개발자가 주기적으로 발표하므로 정기적으로 확인하거나 새 코드 발표 업데이트를 받으려면 커뮤니티 Discord에 참여하세요.',
        'ja': '現在、アクティブな機能コードはありません。コードは開発者によって定期的にリリースされるので、定期的に確認するか、新しいコードリリースの更新を受け取るためにコミュニティDiscordに参加してください。',
        'de': 'Derzeit gibt es keine aktiven funktionierenden Codes. Codes werden regelmäßig vom Entwickler veröffentlicht, also prüfe regelmäßig oder trete der Community-Discord bei, um Updates zu neuen Code-Veröffentlichungen zu erhalten.',
    },
    'faq_private_server': {'ko': '개인 서버를 사용해야 하나요?', 'ja': 'プライベートサーバーを使うべきですか？', 'de': 'Sollte ich einen privaten Server verwenden?'},
    'faq_private_server_answer': {
        'ko': '개인 서버는 위험 없이 기지 설계를 연습하고 전략을 테스트하는 데 좋습니다. 친구와 플레이하고 협업 기지 레이아웃을 테스트할 수도 있습니다. 하지만 공개 서버에 비해 진행 속도가 느립니다.',
        'ja': 'プライベートサーバーは、リスクなくベースデザインを練習し戦略をテストするのに最適です。友人とプレイし、協力ベースレイアウトをテストすることもできます。ただし、パブリックサーバーに比べて進行が遅くなります。',
        'de': 'Private Server sind großartig zum Üben von Base-Designs und Testen von Strategien ohne Risiko. Sie ermöglichen es dir auch, mit Freunden zu spielen und kollaborative Base-Layouts zu testen. Du verdienst jedoch weniger Fortschritt als auf öffentlichen Servern.',
    },
    'faq_rebirth_system': {'ko': '환생이나 프레스티지 시스템이 있나요?', 'ja': '転生やプレステージシステムはありますか？', 'de': 'Gibt es ein Wiedergeburts- oder Prestige-System?'},
    'faq_rebirth_system_answer': {
        'ko': '이 게임은 펫 컬렉션과 기지 업그레이드를 통해 진행됩니다. 진행을 리셋하기보다 강한 펫 컬렉션과 난공불락의 기지를 구축하는 데 집중하세요. 고급 플레이어는 전문화된 목표로 자신을 도전할 수 있습니다.',
        'ja': 'このゲームはペットコレクションとベースアップグレードを通じて進行します。進行をリセットするのではなく、強力なペットコレクションと侵入不可能なベースの構築に集中してください。上級プレイヤーは専門化された目標で自分自身を挑戦できます。',
        'de': 'Das Spiel bietet Fortschritt durch Pet-Sammlung und Base-Upgrades. Konzentriere dich auf den Aufbau einer starken Pet-Sammlung und einer uneinnehmbaren Base statt des Zurücksetzens von Fortschritten. Fortgeschrittene Spieler können sich mit spezialisierten Zielen herausfordern.',
    },
}

# Apply translations
def main():
    en = json.load(open(os.path.join(LOCALES_DIR, 'en.json')))
    # Load existing translations to preserve any that are already correct
    existing = {}
    for locale in ['ko', 'ja', 'de']:
        path = os.path.join(LOCALES_DIR, f'{locale}.json')
        if os.path.exists(path):
            existing[locale] = json.load(open(path))
        else:
            existing[locale] = {}

    for locale in ['ko', 'ja', 'de']:
        out = {}
        for k, v in en.items():
            if not isinstance(v, str):
                out[k] = v
                continue
            # If we have a translation in T, use it
            if k in T and locale in T[k]:
                out[k] = T[k][locale]
            # Otherwise, check if existing translation is valid (different from EN or is a brand/number)
            elif k in existing[locale] and existing[locale][k] != v:
                out[k] = existing[locale][k]
            # Otherwise check if existing is same as EN but should be kept (brand/number)
            elif k in existing[locale] and _should_keep_en(v):
                out[k] = existing[locale][k]
            else:
                out[k] = v
        # Write sorted
        sorted_out = {k: out[k] for k in sorted(out.keys())}
        path = os.path.join(LOCALES_DIR, f'{locale}.json')
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(sorted_out, f, ensure_ascii=False, indent=2)
            f.write('\n')
        print(f'Wrote {locale}.json: {len(sorted_out)} keys')

def _should_keep_en(v):
    BRAND = {'Build a Base and Steal', 'Roblox', 'replayable fun games', 'Brainrots', 'Brainrot', 'Discord', 'YouTube', 'FAQ', 'Robux', 'Twitter', 'X'}
    if v in BRAND:
        return True
    if not isinstance(v, str):
        return True
    if v.replace(',','').replace('.','').replace('+','').replace('K','').replace('M','').replace('%','').replace('-','').replace(' ','').replace(':','').isdigit():
        return True
    if v.startswith('<table') or v.startswith('<'):
        return True
    return False

if __name__ == '__main__':
    main()
