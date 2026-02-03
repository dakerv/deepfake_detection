# Copilot Instructions for is-this-real

## Project Overview
This is a **Create React App (CRA)** project using React 19 + TypeScript with Tailwind CSS for styling. The project is configured with Tailwind CSS (v4.1.18) and fully typed with TypeScript.

**Key files:**
- [src/App.tsx](../src/App.tsx) - Root React component
- [src/index.tsx](../src/index.tsx) - App entry point with ReactDOM rendering
- [tsconfig.json](../tsconfig.json) - TypeScript configuration
- [package.json](../package.json) - Dependencies and npm scripts

## Architecture & Setup

### Build System
- **Runner:** Create React App with Craco (@craco/craco 7.1.0) for CRA configuration without ejecting
- **Language:** TypeScript 4.9.5 (strict mode enabled)
- **CSS Framework:** Tailwind CSS v4.1.18 with PostCSS
- **React:** 19.2.4 with React 19 JSX transform (`jsx: "react-jsx"`)
- **Status:** ✅ Fully configured with Tailwind + TypeScript

### Configuration Overview
- `tsconfig.json` - Strict TypeScript settings, ES2020 target, path aliases (`@/*` → `src/*`)
- `tailwind.config.js` - Scans .tsx/.ts files in src/
- `postcss.config.js` - PostCSS plugin chain (Tailwind + Autoprefixer)
- `craco.config.js` - Wires PostCSS into CRA build

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

### Language:** TypeScript (.tsx files for components)
- **Style:** Functional components with return type `React.JSX.Element`
- **Export:** Default export pattern (see [src/App.tsx](../src/App.tsx))
- **Typing:** Use explicit function return types and prop interfaces

Example:
```typescript
// src/components/Button.tsx
interface ButtonProps {
  label: string;
  onClick: () => void;
}

function Button({ label, onClick }: ButtonProps): React.JSX.Element {
  return <button onClick={onClick}>{label}</button>;
}
Testing Setup
- Framework: Jest (via react-scripts)
- Testing Library: React + DOM utilities with TypeScript support
- Test files: `*.test.tsx` pattern (co-located with source)
- Config: [src/setupTests.ts](../src/setupTests.ts) - Imports @testing-library/jest-dom matchers
- Run: `npm test` watches for changes, press `a` to run all tests

Example test file:
```typescript
// src/App.test.tsx
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  render(<App />);
  const link = screen.getByText(/learn react/i);
  expect(link).toBeInTheDocument();
});
```

### TypeScript Linting
- ESLint: Extends `react-app` and `react-app/jest` presets
- Type checking: `tsc --noEmit` validates TypeScript without output
- Strict settings enabled via [tsconfig.json](../tsconfig.json)

### Performance Monitoring
- File: [src/reportWebVitals.ts](../src/reportWReact 19 JSX transform
- **TypeScript 4.9.5** - Type safety with strict mode enabled
- **react-scripts 5.0.1** - Abstraction layer for webpack/babel/eslint/typescript
- **@craco/craco 7.1.0** - CRA configuration extension for custom PostCSS pipeline
- **Tailwind CSS 4.1.18** - Utility-first CSS framework with PostCSS integration
- **Testing Library** - DOM + React testing with TypeScript support/>`

### Type Safety
- Strict mode enabled: Alas `.tsx` (e.g., `src/components/Button.tsx`)
2. Define prop interface with TypeScript
3. Export function with explicit return type `React.JSX.Element`
4. Use Tailwind utility classes for styling
5. Add corresponding `.test.tsx` test file

Example:
```typescript
// src/components/Card.tsx
interface CardProps {
  title: string;
  children: React.ReactNode;
}

function Card({ title, children }: CardProps): React.JSX.Element {
  return (
    <div className="p-4 border border-gray-200 rounded-lg shadow">
      <h2 className="text-lg font-bold">{title}</h2>
      {children}
    </div>
  );
}

export default Card;
```

### Modifying Styling
1. **Global styles:** Update [src/index.css](../src/index.css)
2. **Component styles:** Use Tailwind utilities in className attributes
3. Avoid creating new `.css` files for component-specific styling

### Type Checking & Validation
```bash
npm test                   # Run tests with type checking
npm run build              # Full production build with TS verification
npx tsc --noEmit           # Type check without emitting output
```

### Port Aliases
Use `@/*` alias to import from src: `import Button from '@/components/Button'`

### Adding New Components
1. Create component file in `src/` as `.js` (e.g., `src/Button.js`)
2. Use functional component with default export
3. Once Tailwind is configured, use utility classes for styling instead of CSS files
4. Add corresponding `.test.js` file for coverage
React 19 + TypeScript + Tailwind CSS configur
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
