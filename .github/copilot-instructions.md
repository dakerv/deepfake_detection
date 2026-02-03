# Copilot Instructions for is-this-real

## Project Overview
This is a **Create React App (CRA)** project using React 19 with Tailwind CSS for styling. The project is in early stages with a standard CRA scaffold and recently integrated Tailwind (v4.1.18) via craco.

**Key files:**
- [src/App.js](../src/App.js) - Root React component
- [src/index.js](../src/index.js) - App entry point with ReactDOM rendering
- [package.json](../package.json) - Dependencies and npm scripts

## Architecture & Setup

### Build System
- **Runner:** Create React App (react-scripts 5.0.1)
- **CSS Framework:** Tailwind CSS v4.1.18 with PostCSS
- **Build Tool:** Craco (@craco/craco 7.1.0) for CRA configuration without ejecting
- **Status:** Tailwind dependencies installed but configuration files not yet created

### Critical Next Steps
1. Create `tailwind.config.js` and `postcss.config.js` in project root (required for Tailwind to work)
2. Update [src/index.css](../src/index.css) to include Tailwind directives: `@tailwind base; @tailwind components; @tailwind utilities;`
3. Create `craco.config.js` to wire PostCSS into CRA build pipeline
4. Reference: See official [Tailwind CRA integration guide](https://tailwindcss.com/docs/guides/create-react-app)

## Development Workflow

### Standard Commands
```bash
npm start      # Dev server on http://localhost:3000 (HMR enabled)
npm test       # Jest runner in watch mode (@testing-library/react, @testing-library/jest-dom)
npm run build  # Production bundle to /build folder
npm run eject  # ⚠️ One-way operation - extracts webpack config
```

### Testing
- Framework: Jest (via react-scripts)
- Testing Library: React + DOM testing utilities
- Test files: `*.test.js` pattern (co-located with source)
- Run: `npm test` watches for changes, press `a` to run all tests

## Code Patterns & Conventions

### React Components
- **Style:** Functional components (no class components in current codebase)
- **Export:** Named function export + `export default` pattern (see [src/App.js](../src/App.js))
- **Styling approach:** Will transition to Tailwind utility classes once configured (currently using CSS modules in `App.css`)

### CSS Architecture
**Before Tailwind config is complete:** CSS Modules in `src/` folder
**After Tailwind setup:** Prefer Tailwind utility classes over inline CSS; reserve `*.css` for global styles only

### import Statements
- React, React-DOM imports required in files using JSX (React 19 allows skipping in some cases but best practice is explicit)
- CSS imports use relative paths: `import './App.css'`
- SVG/assets: Use direct import statements (webpack handles bundling)

## Testing & Validation

### ESLint
- Config: Extends `react-app` and `react-app/jest` presets (defined in package.json eslintConfig)
- Run validation: `npm test` shows linting errors alongside test results

### Performance Monitoring
- File: [src/reportWebVitals.js](../src/reportWebVitals.js) - Measures Core Web Vitals
- Integration: Called in [index.js](../src/index.js) but currently unused (can pass `console.log` or send to analytics)

## Key Dependencies
- **React 19.2.4** - Latest major version with minor syntax improvements
- **react-scripts 5.0.1** - Abstraction layer for webpack/babel/eslint configs
- **Testing Library** - DOM + React testing (prefer for integration tests over enzyme)
- **Tailwind CSS 4.1.18** - Pending configuration to integrate with build

## Common AI Agent Tasks

### Adding New Components
1. Create component file in `src/` as `.js` (e.g., `src/Button.js`)
2. Use functional component with default export
3. Once Tailwind is configured, use utility classes for styling instead of CSS files
4. Add corresponding `.test.js` file for coverage

### Modifying Styling
1. **Global styles:** Update [src/index.css](../src/index.css)
2. **Component styles:** Use Tailwind utilities (preferred) or component-scoped CSS modules
3. After Tailwind is live, avoid creating new `.css` files for new components

### Running Checks Before Commit
```bash
npm test -- --coverage     # Run all tests with coverage
npm run build              # Verify production build succeeds
```

## Configuration Blockers
⚠️ **The following config files are missing and MUST be created before Tailwind works:**
- `tailwind.config.js`
- `postcss.config.js`
- `craco.config.js`
- Update [src/index.css](../src/index.css) with `@tailwind` directives

---
*Last updated: February 2026 | Project stage: Initial scaffold with Tailwind dependencies installed*
