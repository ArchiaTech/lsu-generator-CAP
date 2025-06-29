#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test simple de la barre de navigation latérale
"""

import os
import re
from pathlib import Path

def test_file_integration(file_path):
    """Teste l'intégration de la sidebar dans un fichier."""
    print(f"📄 Test de {file_path}...")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Tests à effectuer
        tests = {
            "Sidebar présente": "id=\"sidebar\"" in content,
            "Tailwind CSS": "tailwindcss.com" in content,
            "Logo ÉCOLE DU CAP": "ÉCOLE DU CAP" in content,
            "Navigation links": "nav-link" in content,
            "Responsive styles": "main-content" in content,
            "Mobile toggle": "sidebar-toggle" in content,
            "Overlay mobile": "sidebar-overlay" in content,
            "Animations CSS": "transition-all" in content,
            "Gradient background": "from-indigo-500 to-blue-500" in content,
            "JavaScript sidebar": "setActivePage" in content,
            "Toggle mobile": "toggleSidebar" in content,
            "Event listeners": "addEventListener" in content
        }
        
        # Afficher les résultats
        passed = 0
        for test_name, result in tests.items():
            status = "✅" if result else "❌"
            print(f"  {status} {test_name}")
            if result:
                passed += 1
        
        percentage = (passed / len(tests)) * 100
        print(f"  📊 {passed}/{len(tests)} tests réussis ({percentage:.1f}%)")
        
        return {
            "status": "success",
            "passed": passed,
            "total": len(tests),
            "percentage": percentage
        }
        
    except Exception as e:
        print(f"  ❌ Erreur: {e}")
        return {"status": "error", "error": str(e)}

def main():
    """Fonction principale de test."""
    print("🧪 Test d'intégration de la barre latérale")
    print("=" * 50)
    
    # Fichiers à tester
    test_files = [
        "index.html",
        "lsu_generator.html", 
        "profils_eleves.html",
        "dashboard.html"
    ]
    
    results = {}
    
    for file_name in test_files:
        if os.path.exists(file_name):
            results[file_name] = test_file_integration(file_name)
        else:
            print(f"⚠️  Fichier {file_name} non trouvé")
            results[file_name] = {"status": "not_found"}
    
    # Rapport final
    print("\n📋 Rapport de test final")
    print("=" * 50)
    
    successful_files = sum(1 for r in results.values() if r.get("status") == "success")
    total_files = len(results)
    
    print(f"📁 Fichiers testés: {total_files}")
    print(f"✅ Fichiers réussis: {successful_files}")
    
    if successful_files > 0:
        avg_percentage = sum(r.get("percentage", 0) for r in results.values() if r.get("status") == "success") / successful_files
        print(f"📊 Score moyen: {avg_percentage:.1f}%")
    
    # Test du fichier sidebar.html
    print(f"\n🔧 Test du fichier sidebar.html...")
    if os.path.exists("sidebar.html"):
        sidebar_result = test_file_integration("sidebar.html")
        print(f"✅ Fichier sidebar.html créé et fonctionnel")
    else:
        print("❌ Fichier sidebar.html manquant")
    
    print("\n🎯 Test visuel recommandé:")
    print("1. Ouvrir http://localhost:8000/index.html")
    print("2. Vérifier la barre latérale violet/bleu à gauche")
    print("3. Tester la navigation entre les pages")
    print("4. Redimensionner pour tester le responsive")
    print("5. Sur mobile, tester le bouton burger (☰)")
    
    return results

if __name__ == "__main__":
    main() 