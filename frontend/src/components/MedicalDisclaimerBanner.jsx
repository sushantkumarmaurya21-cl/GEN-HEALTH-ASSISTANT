import React, { useState } from 'react';
import { AlertTriangle, X, ShieldAlert, ArrowRight } from 'lucide-react';
import { useTheme } from '../context/ThemeContext';

export default function MedicalDisclaimerBanner({ onNavigateToAbout }) {
  const [minimized, setMinimized] = useState(false);
  const { language } = useTheme();

  if (minimized) {
    return (
      <div className="bg-amber-500/10 border-b border-amber-500/20 px-4 py-1.5 flex items-center justify-between text-xs text-amber-800 dark:text-amber-300">
        <div className="flex items-center gap-2">
          <ShieldAlert className="w-3.5 h-3.5 text-amber-600 dark:text-amber-400" />
          <span>
            {language === 'hi' 
              ? 'शैक्षिक सूचना: यह चिकित्सीय सलाह या निदान का विकल्प नहीं है।' 
              : 'Educational Notice: Not a substitute for professional medical diagnosis or care.'}
          </span>
        </div>
        <button
          onClick={() => setMinimized(false)}
          className="text-xs font-semibold underline hover:text-amber-900 dark:hover:text-amber-200"
        >
          {language === 'hi' ? 'विस्तार देखें' : 'View Full Disclaimer'}
        </button>
      </div>
    );
  }

  return (
    <div className="bg-gradient-to-r from-amber-50 via-orange-50 to-amber-50 dark:from-amber-950/40 dark:via-orange-950/30 dark:to-amber-950/40 border-b border-amber-200 dark:border-amber-900/60 px-4 py-2 text-xs md:text-sm text-amber-900 dark:text-amber-200 transition-all">
      <div className="max-w-7xl mx-auto flex items-center justify-between gap-3">
        <div className="flex items-center gap-2.5">
          <span className="flex-shrink-0 p-1 bg-amber-100 dark:bg-amber-900/60 rounded-full text-amber-700 dark:text-amber-300">
            <AlertTriangle className="w-4 h-4" />
          </span>
          <p className="leading-snug">
            <strong className="font-semibold">
              {language === 'hi' ? 'महत्वपूर्ण चिकित्सीय अस्वीकरण: ' : 'Strict Medical Disclaimer: '}
            </strong>
            {language === 'hi'
              ? 'HealthCare AI केवल सामान्य स्वास्थ्य शिक्षा के लिए है। यह किसी बीमारी का निदान नहीं करता और डॉक्टर की सलाह का विकल्प नहीं है। गंभीर स्थिति में तुरंत 112 डायल करें।'
              : 'HealthCare AI provides general health education only. It does not provide medical diagnoses, treatment plans, or emergency care. In an emergency, dial 112 / 911 immediately.'}
          </p>
        </div>
        
        <div className="flex items-center gap-3 flex-shrink-0">
          <button
            onClick={() => onNavigateToAbout && onNavigateToAbout()}
            className="hidden sm:inline-flex items-center gap-1 font-medium text-amber-800 dark:text-amber-300 hover:text-amber-950 dark:hover:text-amber-100 underline decoration-amber-400 underline-offset-2"
          >
            <span>{language === 'hi' ? 'पूरी नीति पढ़ें' : 'Read Full Policy'}</span>
            <ArrowRight className="w-3.5 h-3.5" />
          </button>
          <button
            onClick={() => setMinimized(true)}
            aria-label="Minimize disclaimer"
            className="p-1 text-amber-700 dark:text-amber-400 hover:bg-amber-200/50 dark:hover:bg-amber-800/40 rounded transition-colors"
          >
            <X className="w-3.5 h-3.5" />
          </button>
        </div>
      </div>
    </div>
  );
}
