#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test de l'intégration des icônes Font Awesome
"""

import os
import re

def test_icons_in_file(file_path):
    """Teste l'intégration des icônes dans un fichier."""
    print(f"🎨 Test des icônes dans {file_path}...")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Tests à effectuer
        tests = {
            "Font Awesome CDN": "cdnjs.cloudflare.com" in content and "font-awesome" in content,
            "Styles icônes": "btn-with-icon i" in content,
            "Icônes présentes": "fas fa-" in content,
            "Pas de texte brut": "class=\"btn-with-icon\">" not in content,
            "Syntaxe correcte": "class=\"btn-with-icon\"" in content
        }
        
        # Compter les icônes
        icon_count = len(re.findall(r'fas fa-[^"\s]+', content))
        
        # Afficher les résultats
        passed = 0
        for test_name, result in tests.items():
            status = "✅" if result else "❌"
            print(f"  {status} {test_name}")
            if result:
                passed += 1
        
        print(f"  📊 {passed}/{len(tests)} tests réussis")
        print(f"  🎯 {icon_count} icônes Font Awesome trouvées")
        
        return {
            "status": "success",
            "passed": passed,
            "total": len(tests),
            "icon_count": icon_count
        }
        
    except Exception as e:
        print(f"  ❌ Erreur: {e}")
        return {"status": "error", "error": str(e)}

def main():
    """Fonction principale de test."""
    print("🎨 Test d'intégration des icônes Font Awesome")
    print("=" * 50)
    
    # Fichiers à tester
    test_files = [
        'index.html',
        'lsu_generator.html',
        'profils_eleves.html',
        'dashboard.html',
        'student_profile_page.html',
        'create_student.html',
        'student_list.html',
        'photos_classe_pro.html'
    ]
    
    results = {}
    total_icons = 0
    
    for file_name in test_files:
        if os.path.exists(file_name):
            results[file_name] = test_icons_in_file(file_name)
            if results[file_name].get("status") == "success":
                total_icons += results[file_name].get("icon_count", 0)
        else:
            print(f"⚠️  Fichier {file_name} non trouvé")
    
    # Rapport final
    print("\n📋 Rapport final")
    print("=" * 50)
    
    successful_files = sum(1 for r in results.values() if r.get("status") == "success")
    print(f"📁 Fichiers testés: {len(test_files)}")
    print(f"✅ Fichiers réussis: {successful_files}")
    print(f"🎯 Total d'icônes: {total_icons}")
    
    if successful_files > 0:
        avg_icons = total_icons / successful_files
        print(f"📊 Moyenne d'icônes par fichier: {avg_icons:.1f}")
    
    print("\n🎯 Test visuel recommandé:")
    print("1. Ouvrir http://localhost:8000/student_profile_page.html")
    print("2. Vérifier que les boutons ont des icônes")
    print("3. Tester les boutons Modifier, Supprimer, etc.")
    print("4. Vérifier que les icônes sont colorées")
    
    return results

if __name__ == "__main__":
    main() 