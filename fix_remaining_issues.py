#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour corriger les derniers problèmes de syntaxe HTML
"""

import os
import re

def fix_html_syntax(file_path):
    """Corrige les problèmes de syntaxe HTML restants."""
    print(f"🔧 Correction finale de {file_path}...")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Corriger les guillemets mal fermés dans les boutons
        patterns_to_fix = [
            # Pattern: class="btn btn-primary" onclick="..." class="btn-with-icon"
            (r'class="([^"]*)" onclick="([^"]*)" class="btn-with-icon"', 
             r'class="\1 btn-with-icon" onclick="\2"'),
            
            # Pattern: style="..." class="btn-with-icon"
            (r'style="([^"]*)" class="btn-with-icon"', 
             r'class="btn-with-icon" style="\1"'),
            
            # Pattern: onclick="..." class="btn-with-icon"
            (r'onclick="([^"]*)" class="btn-with-icon"', 
             r'class="btn-with-icon" onclick="\1"'),
            
            # Pattern: > class="btn-with-icon"><i class="fas fa-...
            (r'> class="btn-with-icon"><i class="fas fa-([^"]+)"></i>([^<]+)', 
             r' class="btn-with-icon"><i class="fas fa-\1"></i>\2'),
            
            # Pattern: > class="btn-with-icon"><i class="fas fa-...
            (r'> class="btn-with-icon"><i class="fas fa-([^"]+)"></i>', 
             r' class="btn-with-icon"><i class="fas fa-\1"></i>'),
        ]
        
        for pattern, replacement in patterns_to_fix:
            content = re.sub(pattern, replacement, content)
        
        # Sauvegarder si des changements ont été faits
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✅ Syntaxe corrigée dans {file_path}")
            return True
        else:
            print(f"  ⚠️  Aucun problème de syntaxe dans {file_path}")
            return False
            
    except Exception as e:
        print(f"  ❌ Erreur lors du traitement de {file_path}: {e}")
        return False

def main():
    """Fonction principale."""
    print("🔧 Correction finale de la syntaxe HTML")
    print("=" * 40)
    
    # Fichiers à corriger
    html_files = [
        'student_profile_page.html',
        'create_student.html',
        'student_list.html',
        'photos_classe_pro.html'
    ]
    
    success_count = 0
    for file_name in html_files:
        if os.path.exists(file_name):
            if fix_html_syntax(file_name):
                success_count += 1
        else:
            print(f"  ⚠️  Fichier {file_name} non trouvé")
    
    print(f"\n🎉 Correction terminée ! {success_count} fichiers corrigés")
    return success_count

if __name__ == "__main__":
    main() 