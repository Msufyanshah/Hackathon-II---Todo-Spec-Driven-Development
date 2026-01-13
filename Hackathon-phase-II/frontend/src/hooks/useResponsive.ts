// frontend/src/hooks/useResponsive.ts
import { useState, useEffect } from 'react';
import { getCurrentScreenSize, isScreenSize, Breakpoint } from '../utils/responsive';

export const useResponsive = () => {
  const [screenSize, setScreenSize] = useState(() => {
    if (typeof window !== 'undefined') {
      return getCurrentScreenSize();
    }
    return 'xs'; // default for SSR
  });

  useEffect(() => {
    const handleResize = () => {
      setScreenSize(getCurrentScreenSize());
    };

    window.addEventListener('resize', handleResize);

    // Cleanup event listener on unmount
    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []);

  return {
    screenSize,
    isXs: screenSize === 'xs',
    isSm: screenSize === 'sm' || screenSize === 'xs',
    isMd: screenSize === 'md' || screenSize === 'sm' || screenSize === 'xs',
    isLg: screenSize === 'lg' || screenSize === 'md' || screenSize === 'sm' || screenSize === 'xs',
    isXl: screenSize === 'xl' || screenSize === 'lg' || screenSize === 'md' || screenSize === 'sm' || screenSize === 'xs',
    is2Xl: screenSize === '2xl',
    isScreenSize: (breakpoint: Breakpoint) => isScreenSize(breakpoint)
  };
};