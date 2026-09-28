# 🎨 Olympian Siege - Graphics & Visual Design Guide

## Overview
This document outlines the visual design, character aesthetics, and graphics specifications for the Olympian Siege game.

---

## 📐 Character Design Specifications

### Character SVG Dimensions
- **Canvas Size:** 200x250 pixels
- **Head Radius:** 30-35px
- **Body Height:** 80-90px
- **Overall Proportion:** ~7-8 heads tall (heroic proportions)

### Character Color Palette

| Character | Primary | Secondary | Accent | Aura |
|-----------|---------|-----------|--------|------|
| Zeus | #FFD700 (Gold) | #C0C0C0 (Silver) | #1E90FF (Dodger Blue) | Blue Electric |
| Athena | #B0C4DE (Light Steel Blue) | #C0C0C0 (Silver) | #4169E1 (Royal Blue) | Blue Glow |
| Ares | #8B0000 (Dark Red) | #2F4F4F (Dark Slate) | #DC143C (Crimson) | Red Aura |
| Poseidon | #4682B4 (Steel Blue) | #20B2AA (Light Sea Green) | #00CED1 (Turquoise) | Cyan Sparkles |
| Aphrodite | #FFB6D9 (Pink) | #F5DEB3 (Wheat) | #FF69B4 (Hot Pink) | Pink Particles |
| Apollo | #DAA520 (Goldenrod) | #FFD700 (Gold) | #FFD700 (Gold) | Golden Glow |

### Visual Elements by Character

#### ⚡ ZEUS
```
Crown Style:      Golden with lightning spikes
Helmet/Head:      Mature, authoritative
Facial Hair:      Prominent beard
Armor:           White & Gold ceremonial
Weapon:          Master Bolt (staff)
Aura:            Blue electrical crackling
Animation:       Lightning flashes around body
```

#### 🛡️ ATHENA
```
Helmet Style:     Golden helmet with owl crest
Eyes:            Wise, strategic gray
Armor:           Silver & Bronze battle suit
Weapon:          Golden spear
Shield:          Aegis with Medusa emblem
Aura:            Blue strategic glow
Animation:       Shield pulses with protection
```

#### ⚔️ ARES
```
Helmet:          Black iron with red plume
Face:            Battle scars, aggressive
Build:           Massive, muscular
Armor:           Dark red & black warrior
Weapon:          Great battle axe
Aura:            Red intense glow
Animation:       Aggressive stance, flexing
```

#### 🌊 POSEIDON
```
Crown:           Trident crown with gems
Hair:            Long and wavy (ocean-like)
Facial Hair:     Flowing beard
Armor:           Sea-blue scale mail
Weapon:          Trident (glowing)
Aura:            Cyan water droplets
Animation:       Fluid movements, water ripples
```

#### 💖 APHRODITE
```
Crown:           Ornate with hearts
Hair:            Long golden flowing
Face:            Beautiful, serene
Dress:           Silken rose-pink gown
Weapon:          Golden bow with rose arrows
Aura:            Pink sparkles & rose petals
Animation:       Graceful, swaying motion
```

#### ☀️ APOLLO
```
Hair:            Golden and radiant
Helmet:          None (celestial glow instead)
Armor:           Golden & white celestial
Weapon:          Bow of light (golden arrows)
Aura:            Golden rays of sun
Animation:       Constant golden glow, rays
```

---

## 🏰 Fortress Design Specifications

### Fortress Canvas
- **Canvas Size:** 200x250 pixels
- **Base Width:** 120-130px
- **Height:** 120-130px

### Fortress Characteristics

#### TROY - The Legendary
```
Style:           Wooden palisade construction
Materials:       Wood (#8B4513), Bronze accents
Features:        Wooden stakes, watchtower
Famous Detail:   Trojan Horse monument
Color Scheme:    Browns (#8B4513, #654321)
Special Mark:    Red flag
Defensive Feel:  Ancient, iconic
```

#### SPARTA - The Warrior
```
Style:           Stone fortress (hoplite base)
Materials:       Stone (#808080, #606060)
Features:        Training grounds, military barracks
Defense Style:   Red banners (#FF0000)
Garrison Size:   Largest (150 troops)
Resource Value:  Highest (800)
Defensive Feel:  Disciplined, military
```

#### ATHENS - The Intellectual
```
Style:           Acropolis / Parthenon design
Materials:       Marble (#F5F5F5, #D3D3D3)
Features:        Columns, scrolls (knowledge)
Resource Focus:  Cultural/academic
Defense Value:   Lowest but resourceful
Aesthetic:       Classical Greek beauty
Defensive Feel:  Elegant, scholarly
```

#### OLYMPUS - The Divine (BOSS)
```
Style:           Celestial divine palace
Materials:       Gold (#FFD700), white, rainbow
Features:        Spires, divine throne room
Special Effect:  Cloud shrouds, heavenly glow
Difficulty:      Highest defense (200)
Resources:       Maximum (1000 gold)
Garrison:        Largest (200 elite troops)
Defensive Feel:  Impossible to breach, godly
```

---

## 🎨 Visual Design System

### Color Themes

**Background Gradient:**
- Start: `#667eea` (Periwinkle Blue)
- End: `#764ba2` (Purple)

**UI Colors:**
- Primary: `#667eea` (Periwinkle)
- Secondary: `#764ba2` (Purple)
- Success: `#4CAF50` (Green) - Health
- Info: `#2196F3` (Blue) - Defense
- Warning: `#F44336` (Red) - Defeated
- Gold: `#FFD700` - Divine/Premium

### Typography

**Font Choices:**
- Headers: Georgia, serif (classical look)
- Body: Arial, sans-serif (readable)
- Abilities: Italicized (special emphasis)

**Font Sizes:**
- Main Title: 2.5-3em (bold)
- Section Headers: 1.5em
- Character Names: 1.1em (bold)
- Stats: 1.3em
- Ability Text: 0.9em (italic)

### Card Styles

**Character Cards:**
- Border: 4px solid left border
- Rounded: 8-10px corners
- Shadow: 5-15px blur
- Hover: Lift effect (translateY -10px)
- Dead State: 50% opacity, red background

**Fortress Cards:**
- Border: None (visual enough)
- Rounded: 15px
- Shadow: 10-30px blur
- Hover: Scale 1.05
- Conquered: 50% opacity, red tint

---

## ✨ Animation & Effects

### Character Animations

**Zeus - Lightning Strike**
```css
Animation: flash 0.3s (3 times)
Effect: Blue electrical aura pulses
Sound: Thunder crack
Particle: Lightning bolts
```

**Athena - Strategic Defense**
```css
Animation: pulse 0.5s smooth
Effect: Blue shield glow around entire body
Sound: Shield impact
Particle: Blue energy rings
```

**Ares - War Fury**
```css
Animation: shake 0.2s intense
Effect: Red violent glow
Sound: War cry
Particle: Red explosion effect
```

**Poseidon - Tidal Wave**
```css
Animation: wave 0.6s flowing
Effect: Blue water waves ripple outward
Sound: Ocean whoosh
Particle: Water droplets
```

**Aphrodite - Charm Spell**
```css
Animation: float 1s gentle
Effect: Pink heart particles
Sound: Magical chime
Particle: Rose petals and hearts
```

**Apollo - Solar Beam**
```css
Animation: glow 0.5s radiant
Effect: Golden rays emanate
Sound: Light hum
Particle: Golden sparkles
```

### UI Animations

**Health/Defense Bars:**
- Smooth width transition: 0.3s ease
- Color gradient fill
- Percentage text display

**Battle Log:**
- Fade in new entries: 0.3s
- Victory entries: Green highlight
- Conquest entries: Large & bold

**Button Hover:**
- Scale: 1.02
- Shadow: Increase
- Color: Brighten

---

## 📊 Icon & Symbol Guide

| Symbol | Meaning | Color | Context |
|--------|---------|-------|---------|
| ⚡ | Lightning/Electricity | #1E90FF | Zeus, attacks |
| 🛡️ | Defense/Protection | #4169E1 | Athena, shields |
| ⚔️ | Combat/War | #DC143C | Ares, battle |
| 🌊 | Water/Ocean | #00CED1 | Poseidon, waves |
| 💖 | Love/Charm | #FF69B4 | Aphrodite, support |
| ☀️ | Sun/Light | #FFD700 | Apollo, rays |
| 🏰 | Fortress/Defense | #D2691E | Structures |
| 👥 | Garrison/Troops | #696969 | Military |
| ❤️ | Health | #4CAF50 | Life points |
| 💀 | Death/Defeat | #F44336 | Game over |

---

## 🎬 SVG Drawing Guidelines

### SVG Best Practices

1. **Viewbox:** Always define 0 0 200 250
2. **Scaling:** Use percentages for responsive sizing
3. **Performance:** Limit paths and complex shapes
4. **Colors:** Use hex codes or named colors
5. **Strokes:** Keep stroke-width consistent (1-3px)

### Common SVG Elements

```svg
<!-- Circles (heads, orbs) -->
<circle cx="100" cy="100" r="30" fill="#color"/>

<!-- Rectangles (bodies, armor) -->
<rect x="70" y="120" width="60" height="80" fill="#color" rx="5"/>

<!-- Paths (complex shapes) -->
<path d="M 100 100 L 150 150 Q 200 100 250 150 Z" fill="#color"/>

<!-- Lines (weapons, details) -->
<line x1="100" y1="100" x2="150" y2="150" stroke="#color" stroke-width="3"/>

<!-- Polygons (shields, spikes) -->
<polygon points="100,100 150,120 120,150" fill="#color"/>
```

---

## 🎮 Game UI Layout

### Main Game Screen Structure
```
┌─────────────────────────────────────────┐
│    ⚡ Olympian Siege ⚡                 │  ← Title
│  Battle for control of fortresses       │  ← Subtitle
├──────────────────┬──────────────────────┤
│   🏛️ Olympians  │   🏰 Fortresses     │  ← Character/Fortress Cards
│   [Card Grid]    │   [Card Grid]       │
├──────────────────────────────────────────┤
│            ⚔️ Combat Arena              │  ← Battle Section
│  Choose Warrior: [Dropdown]             │
│  Choose Target:  [Dropdown]             │
│  [⚡ ATTACK ⚡]                          │  ← Action Button
│                                          │
│  Recent Battle Events:                   │
│  [Battle Log - Last 5 entries]           │
└──────────────────────────────────────────┘
```

### Character Card Template
```
┌─────────────────────────────┐
│  [SVG Character Art]        │  300px height
│  ─────────────────────────  │
│  ⚡ Zeus                    │  Character Name
│  King of the Gods           │  Title
│  ┌──────────────┬─────────┐ │
│  │ Health: 100  │ Atk: 25 │ │  Stats Grid
│  └──────────────┴─────────┘ │
│  ┌─────────────────────────┐ │
│  │ Special: Lightning      │ │  Ability
│  │         Strike          │ │
│  └─────────────────────────┘ │
└─────────────────────────────┘
```

---

## 🖼️ Asset Requirements

### Character Assets Needed
- 6 SVG avatars (200x250px each)
- 6 Character card borders/frames
- Health bar styling
- Ability icons (6 types)

### Fortress Assets Needed
- 4 SVG fortress illustrations (200x250px)
- Fortress comparison icons
- Defense bar styling
- Garrison indicator icons

### UI Assets
- Button styles (normal, hover, active, disabled)
- Progress bars (health, defense)
- Icons for abilities
- Battle log styling
- Game over screen design

---

## 📱 Responsive Design Breakpoints

**Desktop (1200px+):**
- Full 2-column layout
- 300x300 character cards
- Hover animations enabled

**Tablet (768px - 1199px):**
- Single or flexible column
- Slightly smaller cards
- Touch-friendly buttons

**Mobile (< 768px):**
- Single column layout
- Scaled-down graphics
- Simplified interface
- No hover effects (touch instead)

---

## 🚀 Future Enhancement Ideas

1. **Animated Character Portraits**
   - Walking/idle animations
   - Attack animations
   - Defeat animations

2. **Particle Systems**
   - Attack effects (lightning, water, fire)
   - Victory effects (confetti)
   - Defeat effects (dust, fading)

3. **Dynamic Lighting**
   - Character glow effects
   - Environmental lighting
   - Combat flash effects

4. **Advanced Graphics**
   - WebGL 3D models
   - Actual sprite sheets
   - High-resolution artwork

5. **Interactive Elements**
   - Character preview hover tooltips
   - Fortress breakaway animations
   - Combat replays

---

## 📋 Checklist for Implementation

- [ ] SVG character avatars created
- [ ] SVG fortress illustrations created
- [ ] Character graphics page (character_graphics.html) tested
- [ ] Character profiles guide created
- [ ] Color scheme applied consistently
- [ ] Responsive design verified
- [ ] Animation CSS finalized
- [ ] Icons and symbols standardized
- [ ] Battle effects implemented
- [ ] Game over screen designed

---

**Last Updated:** September 28, 2026  
**Version:** 1.0.0 - Initial Release
