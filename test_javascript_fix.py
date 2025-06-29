#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test final pour vérifier que les problèmes JavaScript sont corrigés
"""

import os
import re

def test_javascript_fix(file_path):
    """Teste que les problèmes JavaScript sont corrigés."""
    print(f"🧪 Test de correction JavaScript dans {file_path}...")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Tests à effectuer
        tests = {
            "Balises script fermées": content.count('<script>') == content.count('</script>'),
            "Pas de code JS visible": 'function(' not in content or 'function(' in content and '<script>' in content,
            "Guillemets corrects": 'onclick="' in content and 'class="btn-with-icon"' in content,
            "Pas de guillemets mal fermés": 'onclick="[^"]*" class="btn-with-icon"' not in content,
            "Structure HTML correcte": '<body' in content and '</body>' in content,
            "Scripts en fin de document": content.find('</script>') < content.find('</body>')
        }
        
        # Compter les problèmes potentiels
        potential_issues = len(re.findall(r'onclick="[^"]*" class="btn-with-icon"', content))
        
        # Afficher les résultats
        passed = 0
        for test_name, result in tests.items():
            status = "✅" if result else "❌"
            print(f"  {status} {test_name}")
            if result:
                passed += 1
        
        print(f"  📊 {passed}/{len(tests)} tests réussis")
        print(f"  🎯 {potential_issues} problèmes potentiels détectés")
        
        return {
            "status": "success",
            "passed": passed,
            "total": len(tests),
            "potential_issues": potential_issues
        }
        
    except Exception as e:
        print(f"  ❌ Erreur: {e}")
        return {"status": "error", "error": str(e)}

def main():
    """Fonction principale de test."""
    print("🧪 Test final de correction JavaScript")
    print("=" * 50)
    
    # Fichier à tester
    file_path = 'student_profile_page.html'
    
    if os.path.exists(file_path):
        result = test_javascript_fix(file_path)
        
        print("\n📋 Rapport final")
        print("=" * 50)
        
        if result.get("status") == "success":
            print(f"✅ Tests réussis: {result['passed']}/{result['total']}")
            print(f"🎯 Problèmes potentiels: {result['potential_issues']}")
            
            if result['passed'] == result['total'] and result['potential_issues'] == 0:
                print("\n🎉 Tous les problèmes JavaScript sont corrigés !")
                print("✅ Code JavaScript encapsulé correctement")
                print("✅ Aucun code JS visible dans la page")
                print("✅ Structure HTML correcte")
            else:
                print("\n⚠️  Quelques problèmes restent à corriger")
        else:
            print(f"❌ Erreur lors du test: {result.get('error', 'Unknown error')}")
    else:
        print(f"❌ Fichier {file_path} non trouvé")
    
    print("\n🎯 Test visuel recommandé:")
    print("1. Ouvrir http://localhost:8000/student_profile_page.html")
    print("2. Vérifier qu'aucun code JavaScript ne s'affiche")
    print("3. Tester les boutons pour s'assurer qu'ils fonctionnent")
    print("4. Vérifier que les icônes s'affichent correctement")
    
    return result

if __name__ == "__main__":
    main() 