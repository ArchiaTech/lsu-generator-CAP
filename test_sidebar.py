#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de test automatisé pour la barre de navigation latérale
"""

import requests
import re
from pathlib import Path

def test_sidebar_integration():
    """Teste l'intégration de la sidebar dans tous les fichiers HTML."""
    print("🧪 Test d'intégration de la barre latérale")
    print("=" * 50)
    
    base_url = "http://localhost:8000"
    test_files = [
        "index.html",
        "lsu_generator.html", 
        "profils_eleves.html",
        "dashboard.html"
    ]
    
    results = {}
    
    for file_name in test_files:
        print(f"\n📄 Test de {file_name}...")
        
        try:
            # Test de connexion
            response = requests.get(f"{base_url}/{file_name}", timeout=5)
            if response.status_code == 200:
                content = response.text
                
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
                    "Gradient background": "from-indigo-500 to-blue-500" in content
                }
                
                # Afficher les résultats
                passed = 0
                for test_name, result in tests.items():
                    status = "✅" if result else "❌"
                    print(f"  {status} {test_name}")
                    if result:
                        passed += 1
                
                results[file_name] = {
                    "status": "success",
                    "passed": passed,
                    "total": len(tests),
                    "percentage": (passed / len(tests)) * 100
                }
                
                print(f"  📊 {passed}/{len(tests)} tests réussis ({results[file_name]['percentage']:.1f}%)")
                
            else:
                print(f"  ❌ Erreur HTTP: {response.status_code}")
                results[file_name] = {"status": "error", "code": response.status_code}
                
        except requests.exceptions.RequestException as e:
            print(f"  ❌ Erreur de connexion: {e}")
            results[file_name] = {"status": "connection_error", "error": str(e)}
    
    return results

def test_sidebar_functionality():
    """Teste les fonctionnalités JavaScript de la sidebar."""
    print("\n🔧 Test des fonctionnalités JavaScript")
    print("=" * 50)
    
    base_url = "http://localhost:8000"
    
    try:
        # Test de la page d'accueil
        response = requests.get(f"{base_url}/index.html", timeout=5)
        content = response.text
        
        js_tests = {
            "Script sidebar présent": "setActivePage" in content,
            "Toggle mobile": "toggleSidebar" in content,
            "Event listeners": "addEventListener" in content,
            "Responsive handling": "window.innerWidth" in content,
            "Active page detection": "currentPage" in content
        }
        
        print("📄 Test JavaScript sur index.html...")
        passed = 0
        for test_name, result in js_tests.items():
            status = "✅" if result else "❌"
            print(f"  {status} {test_name}")
            if result:
                passed += 1
        
        print(f"  📊 {passed}/{len(js_tests)} tests JavaScript réussis")
        
    except Exception as e:
        print(f"  ❌ Erreur lors du test JavaScript: {e}")

def generate_test_report(results):
    """Génère un rapport de test."""
    print("\n📋 Rapport de test final")
    print("=" * 50)
    
    total_files = len(results)
    successful_files = sum(1 for r in results.values() if r.get("status") == "success")
    
    print(f"📁 Fichiers testés: {total_files}")
    print(f"✅ Fichiers réussis: {successful_files}")
    print(f"❌ Fichiers échoués: {total_files - successful_files}")
    
    if successful_files > 0:
        avg_percentage = sum(r.get("percentage", 0) for r in results.values() if r.get("status") == "success") / successful_files
        print(f"📊 Score moyen: {avg_percentage:.1f}%")
    
    print("\n🎯 Résultats détaillés:")
    for file_name, result in results.items():
        if result.get("status") == "success":
            print(f"  ✅ {file_name}: {result['passed']}/{result['total']} tests ({result['percentage']:.1f}%)")
        else:
            print(f"  ❌ {file_name}: {result.get('status', 'unknown')}")

def main():
    """Fonction principale de test."""
    print("🚀 Test automatisé de la barre de navigation latérale")
    print("=" * 60)
    
    # Test d'intégration
    results = test_sidebar_integration()
    
    # Test des fonctionnalités JavaScript
    test_sidebar_functionality()
    
    # Rapport final
    generate_test_report(results)
    
    # Recommandations
    print("\n💡 Recommandations de test manuel:")
    print("1. Ouvrir http://localhost:8000/index.html")
    print("2. Vérifier que la barre latérale est visible à gauche")
    print("3. Tester la navigation entre les pages")
    print("4. Redimensionner la fenêtre pour tester le responsive")
    print("5. Sur mobile, tester le bouton burger (☰)")
    print("6. Vérifier que la page active est mise en surbrillance")
    
    return results

if __name__ == "__main__":
    main() 