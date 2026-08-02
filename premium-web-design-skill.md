---
name: premium-web-design-system
description: Niche-agnostic premium website design and implementation guidance. Use when building or redesigning modern websites, landing pages, portfolios, SaaS pages, product sites, agency sites, startup sites, dashboards with marketing surfaces, or any web UI where the user wants refined typography, immersive hero sections, glassmorphism, smooth motion, professional spacing, responsive polish, and non-generic visual taste.
---

# Premium Web Design System

> **Goal**: Design and build high-end, editorial-product website experiences based on layout taste, refined typography, subtle animation, and commercial-grade polish. Adapt the visual system dynamically to any business, audience, or brand.

---

## Quick Navigation

- [1. Intake Rules](#1-intake-rules)
- [2. Design DNA](#2-design-dna)
- [3. Typography System](#3-typography-system)
- [4. Layout System](#4-layout-system)
- [5. Hero Direction & Overlay](#5-hero-direction--overlay)
- [6. Glass UI Specifications](#6-glass-ui-specifications)
- [7. Motion Taste & Timing](#7-motion-taste--timing)
- [8. Component Guidelines](#8-component-guidelines)
  - [Collaboration Logo Rail](#collaboration-logo-rail)
  - [Testimonials Section](#testimonials-section)
- [9. Color Direction](#9-color-direction)
- [10. Responsive & Mobile Rules](#10-responsive--mobile-rules)
- [11. Implementation Standards](#11-implementation-standards)
- [12. Copywriting Taste](#12-copywriting-taste)
- [13. Verification Checklist](#13-verification-checklist)
- [14. Anti-Patterns](#14-anti-patterns)
- [15. Default Build Plan](#15-default-build-plan)

---

## 1. Intake Rules

If the user does not provide sufficient context, ask **4-5 concise questions** before designing. Ask only what materially changes the result:

1. **Niche & Objective**: What is the niche or business type, and what should the website help visitors do?
2. **Structure**: How many pages or sections do you need?
3. **Color Direction**: What color direction should the brand use (*light, dark, bold, minimal, luxury, playful, corporate, or custom colors*)?
4. **Brand Identity**: What is the company or product name, and do you have a logo or brand assets?
5. **Audience & Goal**: Who is the target audience, and what is the primary call to action (CTA)?

> [!TIP]
> **Handling Partial Context**  
> - **Partial Answers**: Make tasteful, high-grade assumptions and continue without delaying.  
> - **"Just Make It" Request**: Default to a premium, clean, conversion-focused single-page architecture featuring a strong hero, partner/logo rail, feature section, visual proof section, testimonials, final CTA, and footer.

---

## 2. Design DNA

Build with a **premium editorial-product aesthetic**:

- **First Viewport Impact**: Full-screen or near-full-screen first viewport anchored by one dominant visual asset.
- **Confident Typography**: Large display headings with tight, refined tracking.
- **Typographic Contrast**: Incorporate one elegant contrast typeface moment (e.g., an italic serif word inside a bold sans-serif headline).
- **Floating Navigation**: Clean navigation housed inside a soft glass or floating pill container.
- **Visual Hierarchy**: Headline first $\rightarrow$ Social Proof second $\rightarrow$ Actionable CTA third $\rightarrow$ Decorative accents last.
- **Restrained Glassmorphism**: Use glass cards strictly where they present information layer, not as background filler.
- **Rich Media**: Use real photos, video, or high-fidelity generated bitmap visuals instead of generic CSS color gradients.
- **Calm & Spacious**: Keep layouts uncluttered, well-padded, and deliberately spaced. Avoid template-like rigid card grids.
- **Commercial Polish**: Ensure the site looks like an approved enterprise or high-end startup product.

---

## 3. Typography System

### Font Pairing Strategy

| Role | Font Family Options | Style & Usage Notes |
| :--- | :--- | :--- |
| **Primary Sans** | `Plus Jakarta Sans`, `Inter`, `Geist`, `Satoshi`, `Manrope` | Modern geometric/humanist sans for main structural UI, subheadings, and body. |
| **Accent Serif** | `Cormorant Garamond`, `Playfair Display`, `Fraunces` | Use sparingly for high-impact contrast (1 word in hero, pull quotes, section titles). |

> [!NOTE]
> **Typography Best Practices**
> - **Weight Distribution**: Reserve `bold` or `extrabold` for major headings—do not apply bold weights everywhere.
> - **Tracking & Letter Spacing**: Tighten letter spacing slightly on large display headings only. **Never** apply negative letter spacing to small body or UI text.
> - **Body Copy Readability**: Keep copy concise, readable, and informative. Avoid marketing filler.

### Hero Headline Pattern

```text
Next-Generation [Category] [Offer] Solutions
```

**Styling Treatment**:
- **Main Words**: Modern Sans-Serif, `font-bold` or `font-extrabold`, tight display tracking.
- **Accent Word**: Italic Serif, slightly lighter weight (`font-normal` or `font-medium`).
- **Supporting Paragraph**: Medium weight, 1–2 lines max, high visual contrast against background.

---

## 4. Layout System

Use this 8-stage section sequence when no explicit layout structure is specified:

```
┌─────────────────────────────────────────────────────────┐
│ 1. HERO (Immersive Media, Pill Nav, Proof, Headline, CTA)│
├─────────────────────────────────────────────────────────┤
│ 2. COLLABORATION STRIP (Continuous Infinite Logo Rail) │
├─────────────────────────────────────────────────────────┤
│ 3. CORE OFFER (3–6 Content Panels / Value Props)        │
├─────────────────────────────────────────────────────────┤
│ 4. VISUAL PROOF (Product Shots, Gallery, Case Studies)  │
├─────────────────────────────────────────────────────────┤
│ 5. PROCESS / TECH (Sticky or Scroll-Reveal Feature)     │
├─────────────────────────────────────────────────────────┤
│ 6. TESTIMONIALS (Refined Avatar Quote Cards)           │
├─────────────────────────────────────────────────────────┤
│ 7. FINAL CTA (Bold, Single-Focus Call to Action)        │
├─────────────────────────────────────────────────────────┤
│ 8. FOOTER (Navigation Links, Brand Mark, Legal)        │
└─────────────────────────────────────────────────────────┘
```

> [!IMPORTANT]
> Keep sections visually distinct yet harmoniously connected. Prefer full-width structural bands over stacked nested card wrappers.

---

## 5. Hero Direction & Overlay

The hero section must feel cinematic, immersive, and fully functional.

### Required Hero Qualities
- **Background Media**: Use a high-quality visual asset. Video is preferred when available.
- **Video Standards**: `<video>` must include `autoplay`, `muted`, `loop`, `playsInline`, and a static `poster` fallback image.
- **Background Overlay**: Use smooth CSS gradient masks rather than flat black overlays unless strictly required for contrast.
- **Content Positioning**: Place the primary headline and main CTA near the lower-left or lower-center (avoid default dead-center positioning).
- **Proof Elements**: Integrate avatar rating pills, key metric badges, or subtle glass cards.
- **Mobile Simplification**: On small viewports, simplify the hero by hiding secondary metric clusters that clutter the screen.

### Hero Overlay Checklist

- [ ] Headline remains high-contrast and readable over background media.
- [ ] Primary CTA is visible above the fold on standard mobile screens.
- [ ] Zero text collision or overlapping with the top navigation bar.
- [ ] No horizontal scrollbars or viewport overflow.
- [ ] Scroll-driven motion effects are subtle, smooth, and non-distracting.

---

## 6. Glass UI Specifications

Apply glassmorphism intentionally as an informational overlay layer:

| Property | Value Range / Spec |
| :--- | :--- |
| **Background Fill** | `rgba(255, 255, 255, 0.14)` to `rgba(255, 255, 255, 0.24)` (or dark mode equivalent) |
| **Border Stroke** | `1px solid rgba(255, 255, 255, 0.15–0.30)` |
| **Backdrop Filter** | `backdrop-filter: blur(12px)` to `blur(24px)` |
| **Box Shadow** | Soft, multi-layered, low-opacity shadow (`0 20px 40px rgba(0,0,0,0.08)`) |
| **Border Radius** | `18px`–`30px` for hero cards & containers; `10px`–`16px` for compact UI components |

> [!WARNING]
> Do not make every card on the page glass. Use clean solid surfaces for testimonials, long-form content, and heavy data sections.

---

## 7. Motion Taste & Timing

Motion must feel **expensive, purposeful, and quiet**:

- **Scroll Reveal**: Entrance animations use opacity fade + 16–32px translation.
- **Hover Micro-interactions**: Gentle card elevation (1–8px lift) with smooth shadows.
- **Continuous Motion**: Reserve marquees strictly for logo rails, proof badges, or horizontal data feeds.
- **Reduced Motion**: Always honor `prefers-reduced-motion: reduce` settings.
- **Avoid**: Aggressive bouncing, rotating icons, intrusive parallax, or animations that block content reading.

### Motion Specifications

| Motion Type | Duration | Easing Function | Description |
| :--- | :--- | :--- | :--- |
| **Section Reveal** | `700ms`–`900ms` | `cubic-bezier(0.22, 1, 0.36, 1)` | Smooth fade & vertical slide up on scroll. |
| **Card Hover** | `250ms`–`500ms` | `ease-out` | Subtle lift & shadow expansion. |
| **Logo Marquee** | `24s`–`40s` | `linear infinite` | Continuous seamless horizontal scroll. |
| **Hero Scroll Fade** | Tied to scroll | `linear` | Opacity and translation linked to scroll position. |

---

## 8. Component Guidelines

### Collaboration Logo Rail
Position directly after the hero section to establish immediate credibility.

- **Loop Direction**: Smooth right-to-left continuous scroll.
- **Seamless Loop**: Duplicate logo array elements to eliminate jumpiness.
- **Edge Masks**: Apply CSS `mask-image` linear gradients on left and right edges for smooth fading.
- **Typography Fallback**: Use stylized typographic brand names if SVG logo files are unavailable.
- **Proportions**: Keep the band slim and clean so it complements the hero without drawing excess attention.

### Testimonials Section
Design testimonials as premium editorial callouts rather than generic cards.

- **Background**: Light or neutral contrast background band.
- **Header**: Centered section badge/eyebrow and title.
- **Grid Layout**: 3 columns on desktop, 1–2 columns on tablet/mobile.
- **Card Aesthetics**: Neutral card fills with soft borders and subtle shadow.
- **Decorations**: Large pale background quotation marks (`"`).
- **Author Chip**: Avatar photo, name, and title chip overlapping or anchoring the bottom of each card.
- **Volume**: Include 3 to 6 distinct testimonials.

---

## 9. Color Direction

If no brand color palette is specified, select a tailored scheme based on the industry:

| Niche / Style | Base & Background | Primary Text & Surface | Accent & Polish |
| :--- | :--- | :--- | :--- |
| **Clean Tech** | Deep Slate / Dark Blue | Crisp White & Light Gray | Electric Cyan or Teal |
| **Luxury / Fashion** | Deep Onyx / True Black | Warm White & Cream | Restrained Metallic / Champagne |
| **SaaS / B2B** | Neutral Off-White / Off-Black | Dark Slate (`#0F172A`) | Confident Indigo / Blue Accent |
| **Creative / Agency** | High Contrast Monochrome | Crisp Stark Typography | Vibrant Expressive Accent |
| **Health / Wellness** | Soft Neutral Warm Cream | Deep Charcoal | Natural Sage Green or Ocean Blue |

> [!NOTE]
> Avoid single-hue monochrome palettes. Use primary accents intentionally to guide user action and highlight proof points rather than saturating every surface.

---

## 10. Responsive & Mobile Rules

Mobile layouts must be specifically tailored, not squeezed desktop designs.

- **Mobile First Viewport**: Keep the main CTA clearly visible above the fold on mobile screens.
- **Typography Scaling**: Use `clamp()` for fluid display headlines; do not scale body text aggressively with viewport width.
- **Simplified Hero**: Hide or streamline secondary decorative metric clusters on mobile viewports.
- **Touch Ergonomics**: Ensure buttons and navigation items meet minimum tap target sizes ($\ge 44 \times 44\text{px}$).
- **Overflow Prevention**: Prevent horizontal scrolling except for intentional swipeable carousels.
- **Viewport Checks**: Always verify layouts across standard breakpoints: `390px` (Mobile), `768px` (Tablet), and `1440px` (Desktop).

---

## 11. Implementation Standards

### Next.js & React Projects
- **Images**: Use `next/image` with optimized dimensions and placeholder handling.
- **Background Video**: Use native `<video>` elements directly for local hero media.
- **Semantic HTML**: Structure pages using `<header>`, `<main>`, `<section>`, `<nav>`, and `<footer>`.
- **Client Components**: Keep `use client` directives scoped tightly to interactive components.
- **Static Export**: Include `output: 'export'` in `next.config.js` only when static output is explicitly required.

### General Web Stack
- **Asset Naming**: Use clean, descriptive slugified filenames (`hero-background-video.mp4`, `client-avatar-01.webp`).
- **Accessibility**: Provide descriptive `alt` text for informational media; set `alt=""` or `aria-hidden="true"` on decorative elements.
- **Performance Optimization**: Compress image/video assets, lazy-load offscreen media, and minimize bundle bloat.

---

## 12. Copywriting Taste

Write with the clarity, confidence, and precision of a top-tier brand team.

- **Tone**: Direct, specific, and authoritative.
- **Conciseness**: Keep supporting paragraph text to 1–2 sharp sentences.
- **Outcome Focus**: Replace generic buzzwords with concrete value metrics and clear benefits.

```text
❌ Avoid (Generic AI Cliché):
"We provide innovative solutions to transform your business future and revolutionize workflow."

✅ Prefer (Direct & Premium):
"Build faster, cleaner workflows with reliable tools your team can trust every day."
```

---

## 13. Verification Checklist

Execute these verification checks prior to final submission:

### Visual & Layout Quality
- [ ] Page loads cleanly without layout shift or missing assets.
- [ ] Headline text maintains crisp contrast over background media.
- [ ] Background video loops continuously, remains muted, and plays inline (`playsInline`).
- [ ] Testimonials and content cards align cleanly without overlapping text.
- [ ] Hero nav overlay operates without blocking headline content.

### Functionality & Mobile Polish
- [ ] Zero console warnings or runtime errors.
- [ ] Mobile viewports (390px) display zero horizontal overflow.
- [ ] Mobile navigation drawer opens and closes smoothly.
- [ ] Primary CTA buttons are visible, accessible, and tap-friendly.
- [ ] Logo rail loops infinitely without visual jumps or stutters.
- [ ] Production build (`npm run build` or equivalent) succeeds cleanly.

---

## 14. Anti-Patterns

| Anti-Pattern | Recommended Alternative |
| :--- | :--- |
| ❌ Generic AI-looking gradient hero backgrounds | ✅ High-quality cinematic photo/video asset with gradient overlays |
| ❌ Floating glowing decorative orbs & random bokeh blobs | ✅ Clean, structured layout background with professional depth |
| ❌ Cluttered viewport with excessive cards & competing CTAs | ✅ Single primary headline, clear proof point, and one focused CTA |
| ❌ Applying glassmorphic styling to every container | ✅ Selective glass overlay reserved for float cards; solid cards elsewhere |
| ❌ Over-rounding every UI container with extreme radii | ✅ Balanced radius system (`18-30px` for hero/cards, `8-12px` for buttons) |
| ❌ Generic AI marketing filler copy | ✅ Punchy, concrete outcome-focused copywriting |

---

## 15. Default Build Plan

When commissioned to build or redesign a website, execute this systematic plan:

1. **Intake & Discovery**: Gather requirements or execute the 5 intake questions.
2. **Asset & Codebase Audit**: Inspect existing code, brand assets, images, and project structure.
3. **Design System Setup**: Define font pairings, color tokens, CSS variables, and motion timing.
4. **Hero Construction**: Build the cinematic hero section, overlay mask, floating navigation, and CTA.
5. **Trust & Proof Layers**: Implement the continuous collaboration logo rail and key metric badges.
6. **Core Offer & Content Sections**: Build high-impact value proposition panels and product visual showcases.
7. **Social Proof & Final Call**: Implement the testimonial grid and bold final conversion CTA section.
8. **Mobile & Responsive Optimization**: Refine mobile viewports (390px, 768px), touch targets, and stack order.
9. **Build & Quality Verification**: Run local build checks, verify zero console errors, and check responsiveness.
10. **Delivery & Report**: Provide a concise summary of modified files, verification outcomes, and preview links.
