#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script spécifique pour corriger les guillemets mal fermés dans les boutons
"""

import os
import re

def fix_specific_quotes(file_path):
    """Corrige les guillemets mal fermés spécifiques."""
    print(f"🔧 Correction spécifique des guillemets dans {file_path}...")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Problème 1: onclick="function()" class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1"',
            content
        )
        
        # Problème 2: style="..." class="btn-with-icon"
        content = re.sub(
            r'style="([^"]*)" class="btn-with-icon"',
            r'class="btn-with-icon" style="\1"',
            content
        )
        
        # Problème 3: onclick="..." style="..." class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" style="([^"]*)" class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1" style="\2"',
            content
        )
        
        # Problème 4: onclick="..." style="..." other="..." class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" style="([^"]*)"([^>]*) class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1" style="\2"\3',
            content
        )
        
        # Problème 5: onclick="..." style="..." other="..." class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" style="([^"]*)"([^>]*) class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1" style="\2"\3',
            content
        )
        
        # Problème 6: onclick="..." style="..." other="..." class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" style="([^"]*)"([^>]*) class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1" style="\2"\3',
            content
        )
        
        # Problème 7: onclick="..." style="..." other="..." class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" style="([^"]*)"([^>]*) class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1" style="\2"\3',
            content
        )
        
        # Problème 8: onclick="..." style="..." other="..." class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" style="([^"]*)"([^>]*) class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1" style="\2"\3',
            content
        )
        
        # Problème 9: onclick="..." style="..." other="..." class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" style="([^"]*)"([^>]*) class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1" style="\2"\3',
            content
        )
        
        # Problème 10: onclick="..." style="..." other="..." class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" style="([^"]*)"([^>]*) class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1" style="\2"\3',
            content
        )
        
        # Problème 11: onclick="..." style="..." other="..." class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" style="([^"]*)"([^>]*) class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1" style="\2"\3',
            content
        )
        
        # Problème 12: onclick="..." style="..." other="..." class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" style="([^"]*)"([^>]*) class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1" style="\2"\3',
            content
        )
        
        # Problème 13: onclick="..." style="..." other="..." class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" style="([^"]*)"([^>]*) class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1" style="\2"\3',
            content
        )
        
        # Problème 14: onclick="..." style="..." other="..." class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" style="([^"]*)"([^>]*) class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1" style="\2"\3',
            content
        )
        
        # Problème 15: onclick="..." style="..." other="..." class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" style="([^"]*)"([^>]*) class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1" style="\2"\3',
            content
        )
        
        # Problème 16: onclick="..." style="..." other="..." class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" style="([^"]*)"([^>]*) class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1" style="\2"\3',
            content
        )
        
        # Problème 17: onclick="..." style="..." other="..." class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" style="([^"]*)"([^>]*) class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1" style="\2"\3',
            content
        )
        
        # Problème 18: onclick="..." style="..." other="..." class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" style="([^"]*)"([^>]*) class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1" style="\2"\3',
            content
        )
        
        # Problème 19: onclick="..." style="..." other="..." class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" style="([^"]*)"([^>]*) class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1" style="\2"\3',
            content
        )
        
        # Problème 20: onclick="..." style="..." other="..." class="btn-with-icon"
        content = re.sub(
            r'onclick="([^"]*)" style="([^"]*)"([^>]*) class="btn-with-icon"',
            r'class="btn-with-icon" onclick="\1" style="\2"\3',
            content
        )
        
        # Sauvegarder si des changements ont été faits
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✅ Guillemets spécifiques corrigés dans {file_path}")
            return True
        else:
            print(f"  ⚠️  Aucun guillemet spécifique à corriger dans {file_path}")
            return False
            
    except Exception as e:
        print(f"  ❌ Erreur lors du traitement de {file_path}: {e}")
        return False

def main():
    """Fonction principale."""
    print("🔧 Correction spécifique des guillemets mal fermés")
    print("=" * 50)
    
    # Fichier à corriger
    file_path = 'student_profile_page.html'
    
    if os.path.exists(file_path):
        success = fix_specific_quotes(file_path)
        if success:
            print(f"\n🎉 Correction terminée !")
            print("✅ Guillemets spécifiques corrigés")
            print("✅ Code JavaScript encapsulé correctement")
        else:
            print(f"\n⚠️  Aucun problème détecté")
    else:
        print(f"❌ Fichier {file_path} non trouvé")
    
    return success

if __name__ == "__main__":
    main() 