# MEMOIR VISUAL IDENTITY GUIDE
## Brand Design System - L'Oréal Brandstorm 2026

**Document Version:** 1.0
**Purpose:** Complete visual identity specifications for MEMOIR brand
**Audience:** Designers, developers, marketing team, manufacturing partners

---

## TABLE OF CONTENTS

1. [Brand Essence](#brand-essence)
2. [Logo System](#logo-system)
3. [Typography](#typography)
4. [Color Palette](#color-palette)
5. [Photography Style](#photography-style)
6. [Bottle Design](#bottle-design)
7. [Packaging Design](#packaging-design)
8. [Digital Interface Design](#digital-interface-design)
9. [Marketing Materials](#marketing-materials)
10. [Brand Guidelines](#brand-guidelines)

---

## 1. BRAND ESSENCE

### Brand Personality

**MEMOIR is:**
- **Sophisticated** but not stuffy (modern luxury, not old-world formal)
- **Emotional** but not sentimental (genuine feeling, not manipulative)
- **Technological** but not cold (AI is invisible magic, not machinery)
- **Personal** but not solipsistic (your story matters, shared with community)
- **Timeless** but not dated (classic design with contemporary edge)

### Visual Language Principles

1. **ELEGANCE THROUGH SIMPLICITY**
   - Minimal ornamentation
   - Clean lines, generous white space
   - Typography does the heavy lifting
   - Let the user's photo be the hero

2. **WARMTH THROUGH MATERIALITY**
   - Matte finishes (soft, tactile)
   - Gold accents (warmth, not flashiness)
   - Natural materials where possible (glass, paper, metal—not plastic)
   - Textures that invite touch

3. **EMOTION THROUGH STORYTELLING**
   - Every touchpoint tells part of the story (upload → create → unbox → wear)
   - User's memory is always central (not brand ego)
   - Visual hierarchy guides emotional journey

4. **INNOVATION THROUGH RESTRAINT**
   - Technology is felt, not seen (AI works behind the scenes)
   - No sci-fi aesthetics (avoid blue circuits, robot imagery)
   - Modern but not trendy (design should age well)

### Brand Archetypes

**Primary:** The Creator (bringing something new into existence)
**Secondary:** The Lover (passion, intimacy, cherishing moments)
**Tertiary:** The Sage (wisdom, understanding, scientific knowledge)

---

## 2. LOGO SYSTEM

### Primary Logo: MEMOIR Wordmark

**Design Concept:**
```
╔════════════════════════════════════════╗
║                                        ║
║         M E M O I R                   ║
║        _______________                 ║  ← Gold underline
║       by L'Oréal Luxe                  ║  ← Light weight, smaller
║                                        ║
╚════════════════════════════════════════╝
```

**Typography Specifications:**
- **Main Text ("MEMOIR"):**
  - Font: **Futura Bold** (or Avenir Next Bold if Futura unavailable)
  - Weight: Bold (700)
  - Tracking: +100 (generous letter-spacing for elegance)
  - Size: Relative (scales based on application)
  - Case: ALL CAPS
  - Color: Black (#000000) or Gold (#D4AF37) depending on background

- **Underline:**
  - Stroke: 2pt solid
  - Color: Gold (#D4AF37)
  - Width: Slightly shorter than "MEMOIR" text (95% width)
  - Position: 8pt below baseline of "MEMOIR"

- **Subtext ("by L'Oréal Luxe"):**
  - Font: **Avenir Light** (or Futura Light)
  - Weight: Light (300)
  - Size: 30% of "MEMOIR" size
  - Tracking: +50 (letter-spaced)
  - Color: Gray (#6B6B6B)
  - Position: Centered, 4pt below underline

**Clearspace:**
- Minimum clearspace: Height of letter "M" on all sides
- Never place logo closer than this to other elements

**Minimum Size:**
- Print: 15mm width minimum
- Digital: 120px width minimum
- Below these sizes, use icon logo instead

### Secondary Logo: Icon Mark

**Design Concept:**
```
    ╭──────────╮
   ╱            ╲
  │      M      │    ← Stylized "M" in center
  │              │    ← Circular frame (memory/lens/perfume cap)
   ╲            ╱
    ╰──────────╯
```

**Icon Specifications:**
- **Circle:**
  - Diameter: 100pt (relative scale)
  - Stroke: 4pt
  - Color: Gold (#D4AF37)
  - Fill: Transparent or white (depending on background)

- **Letter "M":**
  - Font: **Futura Bold**
  - Size: 60pt (60% of circle diameter)
  - Color: Black (#000000) or Gold (#D4AF37)
  - Position: Optically centered (not mathematically—adjust 2pt up for visual balance)

**Usage:**
- App icon
- Social media profile images
- Small-scale applications (business cards, bottle caps)
- Favicon

### Logo Variations

**1. PRIMARY LOCKUP (Full logo with subtext)**
- Use for: Marketing materials, packaging, website headers
- Preferred version in most contexts

**2. WORDMARK ONLY (No subtext)**
- Use for: Bottle labels, compact spaces where L'Oréal is implied

**3. ICON ONLY**
- Use for: App icon, social media, very small applications

**4. HORIZONTAL LOCKUP (Text and icon side-by-side)**
```
     ╭───╮
    │ M │  MEMOIR
     ╰───╯   by L'Oréal Luxe
```
- Use for: Website navigation, email signatures

### Color Versions

**1. BLACK + GOLD (Primary)**
- Text: Black
- Underline/accents: Gold
- Background: White or cream
- **Use for:** Print materials, premium packaging, main brand applications

**2. WHITE + GOLD (Reversed)**
- Text: White
- Underline/accents: Gold
- Background: Black
- **Use for:** Dramatic hero images, video overlays, dark mode interfaces

**3. ALL BLACK (Monotone)**
- Text: Black
- Underline: Black
- Background: White
- **Use for:** Legal documents, invoices, utilitarian applications

**4. ALL WHITE (Reversed Monotone)**
- Text: White
- Underline: White
- Background: Black or dark image
- **Use for:** Photography overlays where gold would clash

**DO NOT:**
- ❌ Use logo in colors other than specified (no blue, red, etc.)
- ❌ Outline the logo
- ❌ Add drop shadows or effects
- ❌ Rotate or skew the logo
- ❌ Rearrange elements
- ❌ Change fonts
- ❌ Use low-resolution or pixelated versions

---

## 3. TYPOGRAPHY

### Font Families

**PRIMARY FONT: Futura**
- **Usage:** Headlines, logo, emphasis, packaging
- **Weights:** Light (300), Regular (400), Medium (500), Bold (700)
- **Character:** Geometric, modern, timeless, European luxury heritage
- **Pairing:** Works with Avenir for contrast

**SECONDARY FONT: Avenir**
- **Usage:** Body copy, descriptions, UI text, technical information
- **Weights:** Light (300), Book (400), Medium (500), Heavy (800)
- **Character:** Humanist, readable, friendly but sophisticated
- **Rationale:** Designed by Adrian Frutiger (legendary typographer), excellent readability

**ACCENT FONT: Optima**
- **Usage:** Perfumer signatures, handwritten-style notes, special occasions
- **Weights:** Regular (400), Italic
- **Character:** Classic elegance, serif-like without serifs, sophisticated
- **Rationale:** Designed for Lufthansa, timeless luxury association

**WEB FALLBACKS:**
```css
font-family: 'Futura', 'Avenir Next', 'Trebuchet MS', Arial, sans-serif;
font-family: 'Avenir', 'Avenir Next', 'Helvetica Neue', Helvetica, Arial, sans-serif;
font-family: 'Optima', 'Palatino', Georgia, serif;
```

### Typography Scale

**Responsive Type Scale (base 16px):**

| Style | Desktop | Mobile | Font | Weight | Usage |
|-------|---------|--------|------|--------|-------|
| **H1 Display** | 72px | 48px | Futura | Bold | Homepage hero |
| **H1** | 48px | 32px | Futura | Bold | Page titles |
| **H2** | 36px | 28px | Futura | Medium | Section headers |
| **H3** | 28px | 24px | Futura | Medium | Subsection headers |
| **H4** | 24px | 20px | Avenir | Heavy | Card titles |
| **Body Large** | 20px | 18px | Avenir | Book | Introductions |
| **Body** | 16px | 16px | Avenir | Book | Standard text |
| **Body Small** | 14px | 14px | Avenir | Book | Supporting text |
| **Caption** | 12px | 12px | Avenir | Medium | Labels, metadata |
| **Accent** | varies | varies | Optima | Regular | Perfumer signatures |

### Typography Rules

**Line Height:**
- Headlines: 1.2x (tight for impact)
- Body: 1.6x (generous for readability)
- Captions: 1.4x

**Letter Spacing:**
- All caps text: +50 to +100 tracking (improved legibility)
- Body text: 0 (default)
- Headlines: -10 to 0 (tighter for premium feel)

**Paragraph Spacing:**
- Between paragraphs: 1.5em
- After headings: 0.5em

**Text Alignment:**
- Body copy: Left-aligned (never justified—uneven spacing is amateurish)
- Headlines: Can be centered for impact (use sparingly)
- UI elements: Left-aligned (consistency)

**Emphasis:**
- **Preferred:** Use weight changes (light → bold) instead of italics
- **Avoid:** Underlines (confusing with links), ALL CAPS body text (hard to read)

---

## 4. COLOR PALETTE

### Primary Colors

**BLACK** `#000000` `rgb(0, 0, 0)`
- **Usage:** Primary text, logo, sophisticated backgrounds
- **Psychology:** Timeless luxury, sophistication, modernity
- **Application:** 60% of brand touchpoints

**GOLD** `#D4AF37` `rgb(212, 175, 55)`
- **Usage:** Accents, underlines, highlights, premium details
- **Psychology:** Warmth, memory preservation, quality, heritage
- **Application:** 10% of brand touchpoints (sparingly for impact)
- **Note:** Not shiny metallic—use matte gold in print

**CREAM** `#F7F4ED` `rgb(247, 244, 237)`
- **Usage:** Backgrounds, packaging interiors, soft surfaces
- **Psychology:** Soft, olfactive warmth, neutral canvas
- **Application:** 30% of brand touchpoints

### Secondary Colors (Olfactive Families)

These colors correspond to fragrance note families. Use to color-code accords in UI.

| Family | Color Name | Hex | RGB | Usage |
|--------|-----------|-----|-----|-------|
| **Aquatic** | Deep Blue | `#1E3A5F` | rgb(30, 58, 95) | Ocean, water, aquatic accords |
| **Floral** | Soft Pink | `#F4C2D4` | rgb(244, 194, 212) | Floral accords, romance |
| **Woody** | Warm Brown | `#8B5A3C` | rgb(139, 90, 60) | Woody, forest, earthy accords |
| **Gourmand** | Caramel | `#C88D5C` | rgb(200, 141, 92) | Gourmand, food, sweet accords |
| **Green** | Fresh Green | `#7A9B76` | rgb(122, 155, 118) | Herbal, green, fresh accords |
| **Atmospheric** | Misty Gray | `#B8B8C8` | rgb(184, 184, 200) | Atmospheric, ambient accords |

**Usage Rules:**
- Use secondary colors ONLY for functional categorization (accord families)
- Never use secondary colors for branding/logo
- Maximum 2 secondary colors per layout (avoid rainbow effect)

### Grayscale

| Shade | Hex | RGB | Usage |
|-------|-----|-----|-------|
| **Black** | `#000000` | rgb(0, 0, 0) | Text, strong contrast |
| **Charcoal** | `#333333` | rgb(51, 51, 51) | Body text (softer than pure black) |
| **Gray Dark** | `#6B6B6B` | rgb(107, 107, 107) | Secondary text, subtext |
| **Gray Medium** | `#9B9B9B` | rgb(155, 155, 155) | Disabled states, borders |
| **Gray Light** | `#D1D1D1` | rgb(209, 209, 209) | Dividers, subtle borders |
| **Off-White** | `#F7F4ED` | rgb(247, 244, 237) | Backgrounds (cream) |
| **White** | `#FFFFFF` | rgb(255, 255, 255) | Pure white (use sparingly) |

### Color Combinations

**APPROVED PAIRINGS:**
✅ Black + Gold + Cream (Primary brand palette)
✅ Black + Cream (Clean, minimal)
✅ Gold + Cream (Warm, premium)
✅ White + Black (High contrast, dramatic)
✅ Cream + Charcoal (Soft, readable)

**AVOID:**
❌ Gold + Black on black background (illegible)
❌ Secondary colors as backgrounds (only use as accents)
❌ More than 3 colors in one layout (visual chaos)

### Accessibility

**Text Contrast Ratios (WCAG AA Standard):**
- Black (#000000) on Cream (#F7F4ED): **19.2:1** ✅ (excellent)
- Charcoal (#333333) on Cream: **14.1:1** ✅ (excellent)
- Gold (#D4AF37) on Black: **6.8:1** ✅ (passes AA large text)
- Gray Medium (#9B9B9B) on White: **3.7:1** ✅ (passes AA)

**DO NOT:**
- Use gold text on cream background (fails contrast)
- Use light gray on white (illegible)

---

## 5. PHOTOGRAPHY STYLE

### Principles

**1. USER'S MEMORY IS THE HERO**
- Customer-uploaded photos are always featured prominently
- Brand photography supports, never overshadows user content
- Authentic memories > styled perfection

**2. WARM, NATURAL LIGHT**
- Golden hour aesthetics (warm, nostalgic, glowing)
- Avoid harsh flash or cold lighting
- Soft shadows, diffused light

**3. INTIMATE, CLOSE-UP PERSPECTIVE**
- Macro shots of bottle details, hands holding fragrances, perfume droplets
- Medium shots of people experiencing the scent (eyes closed, smiling, peaceful)
- Avoid wide, impersonal shots

**4. EMOTION OVER PRODUCT**
- Show people reacting (joy, nostalgia, surprise during unboxing)
- Hands in frame (human element)
- Faces can be partially obscured (focus on feeling, not model's identity)

### Photography Checklist

**FRAGRANCE PRODUCT SHOTS:**
- ✅ Matte black bottle on cream background (classic)
- ✅ Bottle with visible user photo label (personalization hero)
- ✅ Hand holding bottle (human scale, intimate)
- ✅ Open bottle with golden liquid visible (olfactive promise)
- ✅ Flatlay: Bottle + memory card + packaging (full experience)
- ✅ Bottle in natural setting (on nightstand, in travel bag—contextual)

**LIFESTYLE IMAGERY:**
- ✅ Person uploading photo on phone (creation process)
- ✅ Unboxing moment (hands opening magnetic box, emotional reveal)
- ✅ Applying fragrance (pulse point close-up, intimate ritual)
- ✅ Person smelling fragrance (eyes closed, transported to memory)
- ✅ Gifting moment (one person giving to another, emotional)
- ✅ Memory recreation (person at location holding their MEMOIR bottle)

**USER-GENERATED CONTENT (SOURCED):**
- ✅ Customer's original memory photo (beach, wedding, childhood, etc.)
- ✅ Customer holding bottle with their photo (proud ownership)
- ✅ Instagram-style testimonials (authentic, unpolished is OK)

### Color Grading

**Post-Processing Style:**
- **Warmth:** +10-15 (golden, nostalgic)
- **Saturation:** -5 to 0 (natural, not oversaturated)
- **Contrast:** +10 (rich blacks, clear highlights)
- **Shadows:** Lift slightly (avoid pure black crush)
- **Highlights:** Preserve (don't blow out whites)
- **Grain:** Subtle (5-10%, adds texture and nostalgia)

**LUT Reference:** "Fuji 400H" film emulation (warm, soft, timeless)

### Photography DON'Ts

❌ **Cold, clinical lighting** (feels medical, not luxury)
❌ **Overly styled perfection** (feels fake, not authentic)
❌ **Generic stock photography** (smiling model holding generic bottle)
❌ **Busy backgrounds** (distracts from subject)
❌ **Heavy filters** (Instagram-trendy filters age poorly)
❌ **Multiple product shots in one frame** (cluttered, not premium)

---

## 6. BOTTLE DESIGN

### Bottle Specifications

**SHAPE: Cylindrical Column**

```
         TOP VIEW              SIDE VIEW
       ╭─────────╮           ┌─────────┐
      │  ╭─────╮  │          │ ┌─────┐ │  ← Cap (2cm tall)
      │  │ CAP │  │          │ │     │ │
      │  ╰─────╯  │          │ └─────┘ │
       ╰─────────╯           │         │
                             │         │  ← Bottle (9cm tall)
       ╭─────────╮           │ ┌─────┐ │
      │           │          │ │     │ │
      │  PHOTO    │          │ │PHOTO│ │  ← User photo label
      │  LABEL    │          │ │     │ │
      │           │          │ │     │ │
      │           │          │ │     │ │
       ╰─────────╯           │ └─────┘ │
                             │         │
                             │┌───────┐│  ← Liquid (30ml)
                             ││~~~~~~~││
                             │└───────┘│
                             └─────────┘
    Diameter: 3.5cm           Height: 11cm total
```

**DIMENSIONS:**
- **Bottle Height:** 9cm (3.5 inches)
- **Bottle Diameter:** 3.5cm (1.4 inches)
- **Cap Height:** 2cm (0.8 inches)
- **Total Height:** 11cm (4.3 inches) with cap
- **Capacity:** 30ml (1.0 fl oz)
- **Weight (empty):** 150g (5.3 oz)
- **Weight (filled):** 180g (6.3 oz) - substantial, premium feel

**MATERIALS:**

**1. Glass Bottle:**
- **Type:** Flint glass (clear, colorless)
- **Thickness:** 3mm wall (sturdy, premium weight)
- **Finish:** Polished (high clarity, shows fragrance color)
- **Base:** Flat, stable (thick glass bottom for weight: 8mm)

**Why clear glass?**
- Shows fragrance liquid (visual appeal of golden amber color)
- Transparency contrasts with matte black cap (modern elegance)
- Allows user to see when refill is needed
- Heritage nod (classic perfume bottles are glass)

**2. Cap:**
- **Material:** Anodized aluminum (matte black)
- **Shape:** Cylindrical with subtle taper (10° angle)
- **Weight:** 30g (adds heft, satisfying to hold)
- **Closure:** Friction fit (no threading—smooth on/off)
- **Detail:** Gold band at base (2mm stripe, color matches brand gold)
- **Engraving:** "MEMOIR" embossed on top surface (subtle, not loud)

**Why aluminum cap?**
- Matte black contrasts with clear glass (modern luxury)
- Anodized finish resists wear (won't scratch or fade)
- Lighter than glass cap (balances weight distribution)
- Gold band = brand signature (instant recognition)

**3. Labels:**

**FRONT LABEL (Integrated Photo):**

```
╔═══════════════════════╗
║                       ║
║                       ║
║   ┌─────────────┐    ║  ← User's photo
║   │             │    ║     (high-res print)
║   │   USER      │    ║     4cm x 5.5cm
║   │   PHOTO     │    ║
║   │             │    ║
║   │             │    ║
║   └─────────────┘    ║
║                       ║
║   "Maui, June 2024"  ║  ← Memory title (small gold text)
║                       ║
╚═══════════════════════╝
```

- **Substrate:** High-quality label paper (120gsm)
- **Printing:** Photo-quality inkjet (300 DPI minimum)
- **Protection:** Clear resin overlay (3mm thick, domed effect)
  - Creates glossy finish
  - Protects photo from moisture, scratches
  - Adds depth (3D effect, photo appears to float)
- **Border:** Gold foil frame (2mm thick) around photo
- **Adhesive:** Permanent (won't peel or lift)
- **Size:** 4.5cm x 6cm total (photo + title)

**Why resin overlay?**
- Elevates perceived value (feels custom, crafted)
- Durability (photo won't fade or smudge)
- Tactile interest (smooth dome, pleasant to touch)
- Instagram-worthy (catches light, looks expensive in photos)

**BACK LABEL (Information):**

```
╔══════════════════════════╗
║ MEMOIR by L'Oréal Luxe  ║
║ Eau de Parfum 30ml      ║
║                          ║
║ "Maui Honeymoon"        ║
║ Crafted for Jane Smith   ║
║                          ║
║ TOP: Bergamot, Coconut  ║
║ HEART: Plumeria, Ylang  ║
║ BASE: Driftwood, Vanilla ║
║                          ║
║ Perfumer: Sophie Laurent ║
║ Batch No: MEMOIR 03847  ║
║                          ║
║         [QR CODE]        ║
║    Scan to revisit       ║
║      your memory         ║
║                          ║
║    Made in France        ║
╚══════════════════════════╝
```

- **Substrate:** Cream label paper (matches brand cream)
- **Printing:** Black text + gold accents (note category icons)
- **Font:** Avenir (body text), Optima (perfumer signature)
- **Size:** 3cm x 7cm (fits on back of bottle)
- **QR Code:** Links to digital memory page (reorder, story, gallery)

### Bottle Variants

**STANDARD (€220):**
- Clear glass bottle
- Matte black aluminum cap with gold band
- Photo front label + info back label
- 30ml capacity

**GIFT SET (€280):**
- Same bottle as standard
- Premium packaging (see Packaging section)
- Additional framed photo card (8cm x 10cm, stand-back frame)
- Perfumer's handwritten note (printed calligraphy)

**REFILL (€120):**
- Same bottle design
- Same photo label (re-printed from original order)
- Simplified packaging (no full box, just protective wrap + card)

**SUBSCRIPTION (€180/season):**
- Same bottle design
- Subscriber-exclusive detail: Gold cap instead of black (premium tier differentiation)
- Rest identical to standard

### Manufacturing Notes

**Production Partner:** Pochet du Courval or Verescence (luxury glass bottle manufacturers)

**Lead Time:**
- Custom label printing: 2 days
- Bottle filling + quality control: 1 day
- Packaging assembly: 1 day
- Total: 4 days production + 3-5 days shipping = 7-9 days total

**Cost Breakdown (per unit):**
- Glass bottle: €3
- Aluminum cap: €2
- Photo label (printed + resin): €4
- Back label: €0.50
- Fragrance liquid (30ml): €8
- Assembly + QC: €1
- **Total Bottle COGS: €18.50**

---

## 7. PACKAGING DESIGN

### Outer Box Specifications

**BOX DESIGN: Premium Rigid Box (Drawer-Style)**

```
         TOP VIEW                    SIDE VIEW (CLOSED)
    ╔══════════════════╗           ┌────────────────┐
    ║                  ║           │ ╔════════════╗ │  ← Lid (slides off)
    ║    M E M O I R   ║           │ ║ MEMOIR     ║ │
    ║   ___________    ║           │ ║ by L'Oréal ║ │
    ║  by L'Oréal Luxe ║           │ ╚════════════╝ │
    ║                  ║           │                 │
    ╚══════════════════╝           │  ┌──────────┐  │  ← Drawer (slides out)
                                    │  │          │  │
    12cm x 12cm                     │  │ Contents │  │
                                    │  │          │  │
                                    │  └──────────┘  │
                                    └────────────────┘
                                         12cm tall
```

**DIMENSIONS:**
- **Outer:** 12cm x 12cm x 12cm (cube shape)
- **Material:** Rigid cardboard (3mm thick, museum-quality)
- **Weight:** 200g empty (substantial, luxury feel)

**EXTERIOR FINISH:**
- **Color:** Matte black (RAL 9005)
- **Coating:** Soft-touch laminate (velvet-like texture)
  - Pleasant to touch (tactile luxury)
  - Fingerprint-resistant
  - Matte appearance (not glossy—sophisticated)
- **Printing:** Gold foil embossing on top surface
  - "MEMOIR by L'Oréal Luxe" logo
  - Raised (3D effect, catch light)
  - Centered on lid

**CLOSURE:** Magnetic flap
- Hidden magnets in corners (4 total)
- Satisfying "click" when closed (ASMR-friendly)
- Easy to open (pull ribbon or lift edge)
- Stays closed during shipping (secure)

**INTERIOR FINISH:**
- **Lining:** Gold satin fabric
  - Luxurious reveal when opened (surprise & delight)
  - Protects contents (soft cushion)
  - Color matches brand gold (#D4AF37)
- **Insert:** Custom foam cutouts (black)
  - Holds bottle, sample, card in place (no rattling)
  - Precision-cut (each item fits perfectly)

### Box Contents Layout

**UNBOXING SEQUENCE (Top to Bottom):**

```
LAYER 1 (Top):
┌────────────────────────────┐
│  [Memory Card]             │  ← Placed on top, lifted out first
│  (Frameable photo + note)  │
└────────────────────────────┘

LAYER 2 (Middle):
┌─────────────────┬──────────┐
│                 │          │
│  [Bottle 30ml]  │ [Sample  │  ← Nestled in foam cutouts
│                 │  2ml]    │
│                 │          │
└─────────────────┴──────────┘

LAYER 3 (Bottom):
┌────────────────────────────┐
│  [Fragrance Story Booklet] │  ← Underneath everything
│  (8-page folded guide)     │
└────────────────────────────┘
```

### Box Contents Specifications

**1. MEMORY CARD (Frameable)**

**Dimensions:** 10cm x 15cm (4" x 6" photo size, standard frame-compatible)

**Front Side:**
- User's photo (high-resolution reprint)
- Matte finish (museum-quality photo paper)
- No text (clean, frameable)

**Back Side:**
```
╔═══════════════════════════════╗
║                               ║
║  Dear [User Name],            ║
║                               ║
║  Your Maui memory reminded    ║
║  me of plumeria blooms at     ║
║  sunset. I used Hawaiian      ║
║  plumeria absolute and        ║
║  driftwood from sustainably   ║
║  sourced coastal oak.         ║
║                               ║
║  May this scent bring you     ║
║  back to that perfect moment. ║
║                               ║
║  - Sophie Laurent             ║  ← Perfumer signature (Optima font)
║    Master Perfumer            ║
║                               ║
╚═══════════════════════════════╝
```

- **Font:** Optima (elegant, handwritten feel)
- **Color:** Charcoal on cream background
- **Tone:** Personal note from perfumer (human touch)

**2. FRAGRANCE STORY BOOKLET**

**Format:** 8-page folded booklet (accordion-style)

**Dimensions:** 10cm x 10cm folded (opens to 40cm length)

**Content:**
- **Page 1 (Cover):** MEMOIR logo + user's memory title
- **Page 2:** "Your Fragrance Story" (intro paragraph)
- **Page 3:** Ingredient origins (map showing where materials sourced)
- **Page 4-5:** Note pyramid explanation (what each accord smells like, when it appears)
- **Page 6:** How to wear (pulse points diagram, layering tips)
- **Page 7:** Care instructions (store away from light, recap after use)
- **Page 8:** Refill information (QR code, website, €120 pricing)

**Design:** Cream pages, black text, gold accents (icons, dividers)

**3. SAMPLE VIAL (2ml)**

**Purpose:** Try fragrance before opening main bottle (satisfaction guarantee)

**Packaging:**
- Small glass vial (2ml)
- Black spray cap (miniature version of main bottle cap)
- Wrapped in gold tissue paper (nested in foam cutout)
- Label: "Sample - Try First"

**4. MAIN BOTTLE (30ml)** - See Bottle Design section

### Gift Set Packaging (€280 SKU)

**Additional Elements:**

**1. Framed Photo Card:**
- 8cm x 10cm standing photo frame (matte black, premium)
- User's memory photo inside (removable)
- Back: Perfumer note (same as memory card)

**2. Premium Ribbon:**
- Black satin ribbon wrapped around box
- Gold wax seal (embossed "M" logo)
- Elegant unwrapping experience

**3. Greeting Card Holder:**
- Small cream envelope (for personal message if gift)
- User can write note to recipient
- Tucked under ribbon on top of box

**Gift Set Box:** Same design as standard, but 15cm x 15cm (larger to fit frame)

### Refill Packaging (€120 SKU)

**Simplified for Repeat Customers:**

- **NO rigid box** (customer already has it)
- **YES protective wrap:** Bubble wrap + gold tissue paper
- **YES memory card reprint:** Same photo + updated note from perfumer
- **YES small booklet:** Single-page care reminder + refill discount code
- **Shipped in:** Padded mailer (MEMOIR-branded, black with gold logo)

**Cost Savings:** €10 per unit (no rigid box) = justifies lower refill price

---

## 8. DIGITAL INTERFACE DESIGN

### Website Design (MEMOIR.com)

**DESIGN PRINCIPLES:**
- Visual-first (large imagery, minimal text)
- Storytelling flow (guides user from discovery → creation → purchase)
- Elegant minimalism (black, gold, cream palette)
- Mobile-first (60% of luxury shoppers browse on mobile)

#### Homepage Layout

**HERO SECTION (Full-screen):**
```
┌──────────────────────────────────────────────────────┐
│                                                      │
│              [Autoplay Video Background]            │  ← Time-lapse: fragrance creation
│        (User photos fading in/out, perfumer          │     + user memories montage
│         working, bottles being labeled)              │
│                                                      │
│                                                      │
│           ─────────────────────────                  │
│           Every Memory Deserves a Scent             │  ← H1 (White, Futura Bold)
│           ─────────────────────────                  │
│                                                      │
│        Turn your favorite photo into a              │  ← Subhead (White, Avenir)
│        custom luxury fragrance                      │
│                                                      │
│         ┌────────────────────────┐                 │
│         │  CREATE YOUR MEMOIR    │                 │  ← CTA (Gold button, black text)
│         └────────────────────────┘                 │
│                                                      │
│            [Scroll indicator: arrow down]           │
│                                                      │
└──────────────────────────────────────────────────────┘
```

**SOCIAL PROOF SECTION:**
```
┌──────────────────────────────────────────────────────┐
│                                                      │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐  │
│  │  [Photo]   │  │  [Photo]   │  │  [Photo]   │  │  ← Customer testimonials
│  │  + Bottle  │  │  + Bottle  │  │  + Bottle  │  │     (carousel, 3 visible)
│  │            │  │            │  │            │  │
│  │ "This      │  │ "I gave    │  │ "Smells    │  │
│  │  captured  │  │  this to   │  │  exactly   │  │
│  │  my        │  │  my mom"   │  │  like      │  │
│  │  wedding"  │  │            │  │  Paris"    │  │
│  │  - Sarah   │  │  - Michael │  │  - Emma    │  │
│  └────────────┘  └────────────┘  └────────────┘  │
│                                                      │
│         "2,847 memories bottled and counting"       │  ← Social proof number
│                                                      │
└──────────────────────────────────────────────────────┘
```

**HOW IT WORKS SECTION:**
```
┌──────────────────────────────────────────────────────┐
│                                                      │
│                 How MEMOIR Works                    │  ← H2 (Black, Futura)
│                 ────────────────                    │
│                                                      │
│  ┌─────────┐      ┌─────────┐      ┌─────────┐   │
│  │    1    │      │    2    │      │    3    │   │  ← Step numbers (Gold circles)
│  │ Upload  │  →   │  AI     │  →   │ Receive │   │
│  │ Photo   │      │ Creates │      │ Custom  │   │
│  │         │      │ Formula │      │Fragrance│   │
│  │ [Icon]  │      │ [Icon]  │      │ [Icon]  │   │
│  └─────────┘      └─────────┘      └─────────┘   │
│                                                      │
│  Upload your    Our AI analyzes   Crafted by       │  ← Descriptions (Avenir)
│  favorite       your memory and   master           │
│  memory photo   suggests olfac-   perfumer,        │
│                 tive notes        delivered in      │
│                                   2-3 weeks         │
│                                                      │
│         ┌────────────────────────┐                 │
│         │     GET STARTED        │                 │  ← CTA
│         └────────────────────────┘                 │
│                                                      │
└──────────────────────────────────────────────────────┘
```

**EXPLORE GALLERY SECTION:**
```
┌──────────────────────────────────────────────────────┐
│                                                      │
│              Explore Memory Gallery                 │  ← H2
│              ──────────────────────                 │
│                                                      │
│  [Filter: ▼All Categories] [Search: 🔍]           │  ← Filters
│   • Travel  • Family  • Romance  • Childhood       │
│                                                      │
│  ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐     │
│  │Img │ │Img │ │Img │ │Img │ │Img │ │Img │     │  ← Masonry grid
│  │    │ │    │ │    │ │    │ │    │ │    │     │     (Pinterest-style)
│  └────┘ └────┘ └────┘ └────┘ └────┘ └────┘     │
│  "Maui"  "Paris" "Grand-  "Child-  "Wedding" "Hike" │
│                   ma's     hood                      │
│                   Garden"  Bakery"                   │
│                                                      │
│  [Click to see scent descriptions + customer story] │
│                                                      │
└──────────────────────────────────────────────────────┘
```

**FOOTER:**
```
┌──────────────────────────────────────────────────────┐
│                                                      │
│  MEMOIR by L'Oréal Luxe                            │
│  ───────────────────────                            │
│                                                      │
│  SHOP           ABOUT           SUPPORT             │
│  • Create       • Our Story     • FAQs              │
│  • Refill       • Perfumers     • Contact           │
│  • Gift Set     • Technology    • Shipping          │
│  • Subscribe    • Press         • Returns           │
│                                                      │
│  FOLLOW US:  [Instagram] [TikTok] [Pinterest]      │
│                                                      │
│  © 2026 L'Oréal Luxe. All rights reserved.         │
│                                                      │
└──────────────────────────────────────────────────────┘
```

### Creation Flow UI

**STEP 1: UPLOAD PAGE**
```
┌──────────────────────────────────────────────────────┐
│  [← Back]                            MEMOIR          │  ← Header
│                                                      │
│              Create Your MEMOIR                     │  ← H1
│              ──────────────────                     │
│                                                      │
│                                                      │
│        ┌──────────────────────────────┐            │
│        │                              │            │
│        │  ┌────────────────────────┐ │            │
│        │  │                        │ │            │
│        │  │   Drag & drop photo   │ │            │  ← Upload area
│        │  │      or click here     │ │            │     (dashed border)
│        │  │                        │ │            │
│        │  │   [📷 Upload Icon]    │ │            │
│        │  │                        │ │            │
│        │  └────────────────────────┘ │            │
│        │                              │            │
│        │  Supported: JPG, PNG, HEIC  │            │
│        │  Max size: 20MB              │            │
│        └──────────────────────────────┘            │
│                                                      │
│  OR connect your Instagram                          │  ← Alternative upload
│  [Instagram icon] Import from Instagram             │
│                                                      │
└──────────────────────────────────────────────────────┘
```

**STEP 2: PHOTO PREVIEW + CONTEXT**
```
┌──────────────────────────────────────────────────────┐
│  Progress: ▮▮▮▯▯▯ (Step 2 of 5)                    │
│                                                      │
│  ┌─────────────────┐  Tell us about this memory   │
│  │                 │                                │
│  │   [User Photo]  │  Where was this?              │  ← Context form
│  │                 │  [Maui, Hawaii___________]    │     (optional but
│  │                 │                                │      recommended)
│  │                 │  When was this?               │
│  └─────────────────┘  [June 2024______________]    │
│                                                      │
│                       What do you remember smelling?│
│                       [Plumeria flowers, coconut    │
│                        sunscreen, ocean____________]│
│                                                      │
│                       How did this feel?            │
│                       ☐ Peaceful  ☐ Joyful         │
│                       ☑ Romantic  ☐ Adventurous    │
│                       ☐ Nostalgic ☐ Energizing     │
│                                                      │
│              ┌────────────────────────┐            │
│              │   CONTINUE TO AI       │            │  ← CTA
│              └────────────────────────┘            │
│                                                      │
└──────────────────────────────────────────────────────┘
```

**STEP 3: AI ANALYSIS (Loading State)**
```
┌──────────────────────────────────────────────────────┐
│                                                      │
│                                                      │
│                                                      │
│              Analyzing your memory...               │  ← H2
│              ────────────────────────               │
│                                                      │
│                   [Animated Spinner]                │  ← Loading animation
│                   (Gold, pulsing)                   │     (takes 10-20 seconds)
│                                                      │
│         Our AI is detecting visual elements         │
│         and mapping them to olfactive notes         │
│                                                      │
│              This takes about 20 seconds            │
│                                                      │
│                                                      │
│                                                      │
└──────────────────────────────────────────────────────┘
```

**STEP 4: FORMULA PREVIEW**
```
┌──────────────────────────────────────────────────────┐
│  Progress: ▮▮▮▮▮▯ (Step 4 of 5)                    │
│                                                      │
│         Your MEMOIR has been created                │  ← H1
│         ───────────────────────────                 │
│                                                      │
│  ┌──────────────┐  ┌──────────────────────────┐   │
│  │              │  │ Visual Analysis:          │   │
│  │ [User Photo] │  │ We detected:              │   │
│  │              │  │ • Tropical beach          │   │  ← AI results summary
│  │              │  │ • Ocean waves             │   │
│  └──────────────┘  │ • Plumeria flowers        │   │
│                     │ • Golden sunset           │   │
│                     └──────────────────────────┘   │
│                                                      │
│              Your Olfactive Formula                 │
│              ──────────────────────                 │
│                                                      │
│   ╭────────────╮                                    │
│   │ TOP NOTES  │ (First 5-15 minutes)              │  ← Pyramid visualization
│   │ • Bergamot │                                    │     (interactive: hover
│   │ • Coconut  │                                    │      for details)
│   │ • Sea Salt │                                    │
│   ╰────────────╯                                    │
│       ║                                              │
│   ╭────────────╮                                    │
│   │HEART NOTES │ (30-120 minutes)                  │
│   │ • Plumeria │                                    │
│   │ • Ylang    │                                    │
│   │ • Solar    │                                    │
│   ╰────────────╯                                    │
│       ║                                              │
│   ╭────────────╮                                    │
│   │BASE NOTES  │ (3-8 hours)                       │
│   │ • Driftwood│                                    │
│   │ • Vanilla  │                                    │
│   │ • Ambergris│                                    │
│   ╰────────────╯                                    │
│                                                      │
│   Your Perfumer: Sophie Laurent [View Bio]         │
│   ┌──────────────────────┐ ┌───────────────────┐  │
│   │ APPROVE & ORDER      │ │ REQUEST CHANGES   │  │  ← CTAs
│   │       €220           │ │   (free editing)  │  │
│   └──────────────────────┘ └───────────────────┘  │
│                                                      │
│   ☐ Add perfumer consultation (+€50)               │  ← Upsell
│                                                      │
└──────────────────────────────────────────────────────┘
```

**STEP 5: CHECKOUT**
(Standard e-commerce checkout - not shown here)

### Mobile App Design (Key Screens)

**APP HOME SCREEN:**
```
┌────────────────────────┐
│   [MEMOIR Logo]        │  ← Header (fixed)
│                        │
│  [+ Create New]        │  ← Primary CTA (large, gold button)
│                        │
│  Your MEMOIRs          │  ← Section title
│  ────────────          │
│                        │
│  ┌──────────────────┐ │
│  │ [Bottle Photo]   │ │  ← Card (user's past MEMOIRs)
│  │                  │ │     Swipe left to see more
│  │ "Maui Honeymoon" │ │
│  │ June 2024        │ │
│  │ [Reorder €120]   │ │  ← Quick reorder button
│  └──────────────────┘ │
│                        │
│  Explore Gallery       │
│  ────────────          │
│  [Grid of user photos] │  ← Inspiration (tappable)
│                        │
│                        │
│ [Home][Gallery][Profile]│  ← Bottom nav
└────────────────────────┘
```

**CAMERA INTEGRATION (Upload Flow):**
- Opens native camera (iOS/Android)
- Or accesses photo library
- Instagram import integration (OAuth)

**PUSH NOTIFICATIONS:**
- "Your MEMOIR is in production! See behind-the-scenes →"
- "Your formula has been finalized. Shipping soon!"
- "Your MEMOIR has arrived! Ready to unbox?"
- "Time for a refill? Reorder your Maui Honeymoon →"

---

## 9. MARKETING MATERIALS

### Social Media Templates

**INSTAGRAM POST TEMPLATE:**

**Design Specs:**
- Format: Square 1080x1080px
- Background: User's photo (subtle 30% opacity overlay)
- Centered text overlay:
  - Memory location + date (white, Futura Bold, 48px)
  - "Now a MEMOIR" (white, Avenir, 24px)
- Bottom right: Bottle mockup (15% of frame size)
- Brand logo: Bottom left corner (small, unobtrusive)
- Hashtag in caption: #MEMOIRfragrance

**Example Caption Template:**
```
From Maui to my dresser ✨

This bottle captures our honeymoon—plumeria flowers, ocean breeze, and golden sunsets. Every time I wear it, I'm back on that beach with you. 🌺🌊

Created with @memoirbyloreal using AI + master perfumer artistry.

#MEMOIRfragrance #CustomPerfume #MemoryInABottle #LuxuryFragrance #LorealLuxe
```

**INSTAGRAM STORY TEMPLATE:**

**Format:** Vertical 1080x1920px

**Sequence (5-slide story):**
1. **Slide 1:** "Watch me create a custom fragrance from my honeymoon photo"
2. **Slide 2:** Screen recording of upload process
3. **Slide 3:** AI analysis results (formula preview)
4. **Slide 4:** Unboxing video (box opening, bottle reveal)
5. **Slide 5:** Close-up applying fragrance + "Smells like Maui ✨" + Swipe-up link

**TIKTOK VIDEO TEMPLATE:**

**Hook Examples (First 3 seconds):**
- "POV: Your wedding photo just became a luxury perfume"
- "I turned my favorite memory into a $220 fragrance"
- "This AI created a custom perfume from my vacation pics"

**Video Structure (60 seconds):**
- 0-3s: Hook (text overlay + attention-grabbing visual)
- 3-10s: Show upload process (screen recording, fast-forward)
- 10-20s: AI analysis (show visual elements detected)
- 20-35s: Unboxing (ASMR sounds, slow reveal)
- 35-50s: Bottle reveal (focus on photo label, describe scent)
- 50-60s: Apply fragrance + emotional reaction ("I'm literally crying, it smells exactly like...")

**Music:** Emotional piano or nostalgic indie song (licensed from TikTok library)

**Text Overlays (Throughout):**
- "Step 1: Upload photo"
- "Step 2: AI analyzes"
- "Step 3: Perfumer creates"
- "2 weeks later..."
- "IT SMELLS LIKE [memory description]"

### Print Advertisements

**MAGAZINE AD (Full Page):**

**Layout:**
```
┌─────────────────────────────────┐
│                                 │
│                                 │
│     [Large bottle image]       │  ← Hero image (75% of page)
│   (Clear glass, user photo      │     Dramatic lighting, shadow
│    visible on label, matte      │
│    black cap, gold accent)      │
│                                 │
│                                 │
│                                 │
├─────────────────────────────────┤
│                                 │
│  "Maui, June 2024"             │  ← Memory title (quote style)
│   ────────────                  │
│                                 │
│  Every memory deserves a scent  │  ← Tagline
│                                 │
│  MEMOIR by L'Oréal Luxe        │  ← Brand lockup
│  MEMOIR.com                     │
│                                 │
└─────────────────────────────────┘
```

**Publications:**
- Vogue, GQ, Wallpaper*, Kinfolk, Monocle
- Frequency: Year 2-3 (post-expert validation)
- Placement: Right-hand page (premium position)

**OUT-OF-HOME (OOH) BILLBOARD:**

**Design:**
```
┌──────────────────────────────────────────────────────┐
│                                                      │
│                                                      │
│               [LARGE USER PHOTO]                    │  ← Customer memory photo
│        (Beach sunset, emotionally evocative)        │     (50% of billboard)
│                                                      │
│                                                      │
├──────────────────────────────────────────────────────┤
│                                                      │
│            "This photo is now a fragrance"          │  ← Headline (Futura Bold)
│                                                      │
│               MEMOIR by L'Oréal Luxe               │  ← Brand + CTA
│                   MEMOIR.com                        │
│                                                      │
└──────────────────────────────────────────────────────┘
```

**Locations:** NYC Subway (High Line stations), London Underground (luxury stops), Paris Metro (Champs-Élysées), LAX/JFK airports

**Timing:** Year 3 (Newcomer scaling phase)

---

## 10. BRAND GUIDELINES

### Voice & Tone

**Brand Voice Attributes:**
- **Warm** (not cold/clinical): "We're here to help you bottle what matters"
- **Sophisticated** (not pretentious): "Custom luxury, made accessible"
- **Personal** (not generic): "Your story, your signature scent"
- **Confident** (not arrogant): "The world's first..." (state facts, don't boast)
- **Authentic** (not manufactured): "Real memories, real emotions, real science"

**Writing Style:**
- **Sentence structure:** Short to medium length (10-20 words). Vary for rhythm.
- **Active voice preferred:** "We create" not "Fragrances are created by us"
- **Personal pronouns:** "Your memory" "You deserve" (direct address)
- **Avoid jargon:** Explain technical terms ("olfactive" → "scent-related")
- **Contractions OK:** "You'll love" feels warmer than "You will love"

**Tone by Context:**

| Context | Tone | Example |
|---------|------|---------|
| **Homepage hero** | Inspiring, warm | "Every memory deserves a scent" |
| **Product descriptions** | Informative, sophisticated | "Crafted by master perfumers using 8 exclusive accords" |
| **Error messages** | Apologetic, helpful | "Oops! That image format isn't supported. Try JPG or PNG." |
| **Emails (transactional)** | Professional, friendly | "Your MEMOIR is on its way! Track your shipment..." |
| **Social media** | Conversational, emotional | "This story made us cry happy tears 😭✨" |
| **Customer service** | Empathetic, solution-focused | "We're so sorry you're not in love with your fragrance. Let's make it right." |

### Writing Dos and Don'ts

**DO:**
- ✅ Use sensory language ("warm vanilla," "crisp ocean breeze," "velvety rose")
- ✅ Tell stories (customer testimonials, perfumer interviews, ingredient origins)
- ✅ Acknowledge emotion ("We know how precious memories are")
- ✅ Be specific ("2-3 week turnaround" not "soon")
- ✅ Use "you" and "your" (customer-centric)

**DON'T:**
- ❌ Use clichés ("game-changer," "revolutionary" overused)
- ❌ Overpromise ("This will change your life forever")
- ❌ Talk down to customer ("As you probably don't know...")
- ❌ Use excessive exclamation marks (one per paragraph max!!!)
- ❌ Write walls of text (break up with headings, bullets, white space)

### Visual Dos and Don'ts

**DO:**
- ✅ Use generous white space (elegance through restraint)
- ✅ Let user photos be the hero (not brand imagery)
- ✅ Maintain color palette consistency (black, gold, cream)
- ✅ Use high-quality photography (sharp, well-lit, professional)
- ✅ Align elements to grid (visual order = sophistication)

**DON'T:**
- ❌ Clutter layouts with too many elements
- ❌ Use colors outside brand palette (no random blues, reds, etc.)
- ❌ Stretch or distort logos/images (maintain aspect ratios)
- ❌ Use low-resolution images (pixelation kills luxury perception)
- ❌ Mix too many fonts (stick to Futura + Avenir + Optima)

### Logo Usage Rules (Summary)

**Always:**
- ✅ Maintain minimum clearspace (height of "M")
- ✅ Use approved color versions only
- ✅ Keep proportions (don't stretch/compress)
- ✅ Use high-resolution files (vector preferred)

**Never:**
- ❌ Change colors outside specified palette
- ❌ Add effects (shadows, glows, outlines)
- ❌ Rotate, skew, or distort
- ❌ Recreate or modify (use official files)
- ❌ Place on busy backgrounds (needs contrast)

---

## APPENDIX: DESIGN ASSETS CHECKLIST

### Files to Create for Production:

**LOGO FILES:**
- [ ] Primary logo (black + gold) - AI, EPS, PNG, SVG
- [ ] Logo (all white) - AI, EPS, PNG, SVG
- [ ] Icon mark - AI, EPS, PNG, SVG
- [ ] Horizontal lockup - AI, EPS, PNG, SVG
- [ ] Minimum sizes (web favicon, app icon)

**TYPOGRAPHY FILES:**
- [ ] Futura font family (licensed for brand use)
- [ ] Avenir font family (licensed)
- [ ] Optima font family (licensed)
- [ ] Web fonts (WOFF, WOFF2 formats)

**COLOR FILES:**
- [ ] Color palette swatch file (ASE for Adobe)
- [ ] Hex/RGB/CMYK specifications document

**PACKAGING FILES:**
- [ ] Bottle label template (AI, with photo placement guides)
- [ ] Box design dieline (AI, with fold marks)
- [ ] Memory card template (AI, front + back)
- [ ] Booklet template (InDesign, 8 pages)

**DIGITAL FILES:**
- [ ] Website design mockups (Figma or Sketch)
- [ ] Mobile app screens (Figma or Sketch)
- [ ] Social media templates (PSD, 1080x1080 Instagram, 1080x1920 Story, 1080x1920 TikTok)
- [ ] Email templates (HTML, responsive)

**PHOTOGRAPHY:**
- [ ] Product shots (10-15 angles, high-res)
- [ ] Lifestyle imagery (20-30 photos, diverse scenarios)
- [ ] Perfumer portraits (5 perfumers, professional headshots)

**PRINT MATERIALS:**
- [ ] Magazine ad layout (InDesign, full-page)
- [ ] Brochure template (InDesign, tri-fold)
- [ ] Business cards (InDesign, standard size)

---

## CONCLUSION

**MEMOIR's visual identity balances:**
- Modern sophistication (clean typography, minimal design)
- Emotional warmth (gold accents, user photo prominence)
- Luxury credibility (premium materials, elegant packaging)
- Technological innovation (sleek interfaces, AI-powered UX)

**The design system is:**
- **Scalable** (works across web, app, print, packaging, OOH)
- **Flexible** (allows for seasonal campaigns, regional variations)
- **Timeless** (avoids trends, will age gracefully over 5+ years)
- **Distinctive** (instantly recognizable as MEMOIR, not generic luxury)

**Every touchpoint reinforces the brand promise:**
*"Where technology meets memory, science serves emotion, and your story becomes your signature scent."*

---

**Document Status:** Visual identity guide complete
**Next Steps:**
1. Create design mockups (HTML visualization)
2. Build AI prototype (50 visual-olfactive mappings)
3. Develop financial model
4. Create pitch deck

**Design Approval:** Ready for stakeholder review
