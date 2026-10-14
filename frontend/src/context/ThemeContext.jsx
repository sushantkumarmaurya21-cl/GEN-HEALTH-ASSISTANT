import React, { createContext, useContext, useState, useEffect } from 'react';

const ThemeContext = createContext();

export function ThemeProvider({ children }) {
  const [darkMode, setDarkMode] = useState(() => {
    const saved = localStorage.getItem('healthcare_theme');
    if (saved) return saved === 'dark';
    return window.matchMedia('(prefers-color-scheme: dark)').matches;
  });

  const [language, setLanguage] = useState(() => {
    return localStorage.getItem('healthcare_lang') || 'en';
  });

  useEffect(() => {
    if (darkMode) {
      document.documentElement.classList.add('dark');
      localStorage.setItem('healthcare_theme', 'dark');
    } else {
      document.documentElement.classList.remove('dark');
      localStorage.setItem('healthcare_theme', 'light');
    }
  }, [darkMode]);

  useEffect(() => {
    localStorage.setItem('healthcare_lang', language);
  }, [language]);

  const toggleDarkMode = () => setDarkMode(prev => !prev);
  const toggleLanguage = () => setLanguage(prev => (prev === 'en' ? 'hi' : 'en'));

  return (
    <ThemeContext.Provider value={{ darkMode, toggleDarkMode, language, setLanguage, toggleLanguage }}>
      {children}
    </ThemeContext.Provider>
  );
}

export function useTheme() {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error('useTheme must be used within a ThemeProvider');
  }
  return context;
}
