// frontend/src/utils/responsive.ts
export const BREAKPOINTS = {
  sm: 640,  // Small screens
  md: 768,  // Medium screens
  lg: 1024, // Large screens
  xl: 1280, // Extra large screens
  '2xl': 1536 // 2x extra large screens
};

export type Breakpoint = keyof typeof BREAKPOINTS;

/**
 * Checks if the current screen width is greater than or equal to the specified breakpoint
 */
export const isScreenSize = (breakpoint: Breakpoint): boolean => {
  if (typeof window === 'undefined') return false;
  
  const breakpointWidth = BREAKPOINTS[breakpoint];
  return window.innerWidth >= breakpointWidth;
};

/**
 * Gets the current screen size based on breakpoints
 */
export const getCurrentScreenSize = (): Breakpoint | 'xs' => {
  if (typeof window === 'undefined') return 'xs';
  
  const width = window.innerWidth;
  
  if (width < BREAKPOINTS.sm) return 'xs';
  if (width < BREAKPOINTS.md) return 'sm';
  if (width < BREAKPOINTS.lg) return 'md';
  if (width < BREAKPOINTS.xl) return 'lg';
  if (width < BREAKPOINTS['2xl']) return 'xl';
  
  return '2xl';
};