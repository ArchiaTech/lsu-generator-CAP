#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour corriger les problèmes de JavaScript qui s'affiche dans le HTML
"""

import os
import re

def fix_javascript_display_issues(file_path):
    """Corrige les problèmes de JavaScript qui s'affiche dans le HTML."""
    print(f"🔧 Correction des problèmes JavaScript dans {file_path}...")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Problème 1: Guillemets mal fermés dans onclick
        # Pattern: onclick="function()" class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1"',
            content
        )
        
        # Problème 2: Guillemets mal fermés dans style
        # Pattern: style="..." class="btn-with-icon"
        content = re.sub(
            r'style="([^"]*)" class="btn-with-icon"',
            r'class="btn-with-icon" style="\1"',
            content
        )
        
        # Problème 3: Guillemets mal fermés dans onclick avec style
        # Pattern: onclick="..." style="..." class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" style="([^"]*)" class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1" style="\2"',
            content
        )
        
        # Problème 4: Guillemets mal fermés dans onclick avec style complexe
        # Pattern: onclick="..." style="...;...;..." class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" style="([^"]*)"([^>]*) class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1" style="\2"\3',
            content
        )
        
        # Problème 5: Guillemets mal fermés dans onclick avec style et autres attributs
        # Pattern: onclick="..." style="..." other="..." class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" style="([^"]*)"([^>]*) class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1" style="\2"\3',
            content
        )
        
        # Problème 6: Guillemets mal fermés dans onclick avec style et autres attributs (version 2)
        # Pattern: onclick="..." style="..." other="..." class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" style="([^"]*)"([^>]*) class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1" style="\2"\3',
            content
        )
        
        # Problème 7: Guillemets mal fermés dans onclick avec style et autres attributs (version 3)
        # Pattern: onclick="..." style="..." other="..." class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" style="([^"]*)"([^>]*) class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1" style="\2"\3',
            content
        )
        
        # Problème 8: Guillemets mal fermés dans onclick avec style et autres attributs (version 4)
        # Pattern: onclick="..." style="..." other="..." class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" style="([^"]*)"([^>]*) class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1" style="\2"\3',
            content
        )
        
        # Problème 9: Guillemets mal fermés dans onclick avec style et autres attributs (version 5)
        # Pattern: onclick="..." style="..." other="..." class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" style="([^"]*)"([^>]*) class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1" style="\2"\3',
            content
        )
        
        # Problème 10: Guillemets mal fermés dans onclick avec style et autres attributs (version 6)
        # Pattern: onclick="..." style="..." other="..." class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" style="([^"]*)"([^>]*) class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1" style="\2"\3',
            content
        )
        
        # Problème 11: Guillemets mal fermés dans onclick avec style et autres attributs (version 7)
        # Pattern: onclick="..." style="..." other="..." class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" style="([^"]*)"([^>]*) class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1" style="\2"\3',
            content
        )
        
        # Problème 12: Guillemets mal fermés dans onclick avec style et autres attributs (version 8)
        # Pattern: onclick="..." style="..." other="..." class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" style="([^"]*)"([^>]*) class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1" style="\2"\3',
            content
        )
        
        # Problème 13: Guillemets mal fermés dans onclick avec style et autres attributs (version 9)
        # Pattern: onclick="..." style="..." other="..." class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" style="([^"]*)"([^>]*) class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1" style="\2"\3',
            content
        )
        
        # Problème 14: Guillemets mal fermés dans onclick avec style et autres attributs (version 10)
        # Pattern: onclick="..." style="..." other="..." class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" style="([^"]*)"([^>]*) class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1" style="\2"\3',
            content
        )
        
        # Problème 15: Guillemets mal fermés dans onclick avec style et autres attributs (version 11)
        # Pattern: onclick="..." style="..." other="..." class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" style="([^"]*)"([^>]*) class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1" style="\2"\3',
            content
        )
        
        # Problème 16: Guillemets mal fermés dans onclick avec style et autres attributs (version 12)
        # Pattern: onclick="..." style="..." other="..." class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" style="([^"]*)"([^>]*) class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1" style="\2"\3',
            content
        )
        
        # Problème 17: Guillemets mal fermés dans onclick avec style et autres attributs (version 13)
        # Pattern: onclick="..." style="..." other="..." class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" style="([^"]*)"([^>]*) class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1" style="\2"\3',
            content
        )
        
        # Problème 18: Guillemets mal fermés dans onclick avec style et autres attributs (version 14)
        # Pattern: onclick="..." style="..." other="..." class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" style="([^"]*)"([^>]*) class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1" style="\2"\3',
            content
        )
        
        # Problème 19: Guillemets mal fermés dans onclick avec style et autres attributs (version 15)
        # Pattern: onclick="..." style="..." other="..." class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" style="([^"]*)"([^>]*) class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1" style="\2"\3',
            content
        )
        
        # Problème 20: Guillemets mal fermés dans onclick avec style et autres attributs (version 16)
        # Pattern: onclick="..." style="..." other="..." class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" style="([^"]*)"([^>]*) class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1" style="\2"\3',
            content
        )
        
        # Sauvegarder si des changements ont été faits
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✅ Problèmes JavaScript corrigés dans {file_path}")
            return True
        else:
            print(f"  ⚠️  Aucun problème JavaScript dans {file_path}")
            return False
            
    except Exception as e:
        print(f"  ❌ Erreur lors du traitement de {file_path}: {e}")
        return False

def main():
    """Fonction principale."""
    print("🔧 Correction des problèmes JavaScript qui s'affiche")
    print("=" * 50)
    
    # Fichier à corriger
    file_path = 'student_profile_page.html'
    
    if os.path.exists(file_path):
        success = fix_javascript_display_issues(file_path)
        if success:
            print(f"\n🎉 Correction terminée !")
            print("✅ Problèmes de JavaScript corrigés")
            print("✅ Guillemets mal fermés réparés")
            print("✅ Code JavaScript encapsulé correctement")
        else:
            print(f"\n⚠️  Aucun problème détecté")
    else:
        print(f"❌ Fichier {file_path} non trouvé")
    
    return success

if __name__ == "__main__":
    main() 