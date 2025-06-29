#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour corriger automatiquement l'affichage des icônes Font Awesome
dans tous les fichiers HTML de l'application ÉCOLE DU CAP.
"""

import os
import re
from pathlib import Path

def add_font_awesome_to_head(html_content):
    """Ajoute Font Awesome CDN dans le head si pas déjà présent."""
    font_awesome_link = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">'
    
    # Vérifier si Font Awesome est déjà présent
    if 'font-awesome' not in html_content.lower() and 'cdnjs.cloudflare.com' not in html_content:
        # Ajouter après la balise <head>
        if '<head>' in html_content:
            html_content = html_content.replace('<head>', f'<head>\n    {font_awesome_link}')
        else:
            # Si pas de head, ajouter au début
            html_content = f'<head>\n    {font_awesome_link}\n</head>\n{html_content}'
    
    return html_content

def fix_broken_btn_with_icon(html_content):
    """Corrige les boutons avec class="btn-with-icon" mal formatés."""
    
    # Pattern pour détecter les boutons cassés
    patterns_to_fix = [
        # Pattern 1: class="btn-with-icon"> visible en texte
        (r'> class="btn-with-icon"><i class="fas fa-([^"]+) icon-fa"></i><i class="fas fa-\1 fa-fallback"></i>([^<]+)', 
         r' class="btn-with-icon"><i class="fas fa-\1"></i>\2'),
        
        # Pattern 2: class="btn-with-icon"> seul
        (r'> class="btn-with-icon">([^<]+)', 
         r' class="btn-with-icon">\1'),
        
        # Pattern 3: class="btn-with-icon"> avec icônes dupliquées
        (r' class="btn-with-icon"><i class="fas fa-([^"]+) icon-fa"></i><i class="fas fa-\1 fa-fallback"></i>', 
         r' class="btn-with-icon"><i class="fas fa-\1"></i>'),
        
        # Pattern 4: class="btn-with-icon"> mal placé
        (r'([^>]) class="btn-with-icon">', 
         r'\1" class="btn-with-icon">'),
    ]
    
    for pattern, replacement in patterns_to_fix:
        html_content = re.sub(pattern, replacement, html_content)
    
    return html_content

def add_missing_icons(html_content):
    """Ajoute des icônes manquantes basées sur le texte du bouton."""
    
    # Mapping texte → icône Font Awesome
    icon_mapping = {
        'modifier': 'fa-edit',
        'éditer': 'fa-edit',
        'edit': 'fa-edit',
        'supprimer': 'fa-trash',
        'delete': 'fa-trash',
        'ajouter': 'fa-plus',
        'add': 'fa-plus',
        'créer': 'fa-plus',
        'create': 'fa-plus',
        'sauvegarder': 'fa-save',
        'save': 'fa-save',
        'enregistrer': 'fa-save',
        'générer': 'fa-magic',
        'generate': 'fa-magic',
        'commentaire': 'fa-comments',
        'comment': 'fa-comments',
        'évaluation': 'fa-chart-bar',
        'evaluation': 'fa-chart-bar',
        'photo': 'fa-image',
        'image': 'fa-image',
        'voir': 'fa-eye',
        'view': 'fa-eye',
        'liste': 'fa-list',
        'list': 'fa-list',
        'importer': 'fa-download',
        'import': 'fa-download',
        'exporter': 'fa-upload',
        'export': 'fa-upload',
        'annuler': 'fa-times',
        'cancel': 'fa-times',
        'fermer': 'fa-times',
        'close': 'fa-times',
        'accueil': 'fa-home',
        'home': 'fa-home',
        'compétences': 'fa-bullseye',
        'competences': 'fa-bullseye',
        'famille': 'fa-users',
        'family': 'fa-users',
        'tableau de bord': 'fa-tachometer-alt',
        'dashboard': 'fa-tachometer-alt',
        'csv': 'fa-file-csv',
        'excel': 'fa-file-excel',
        'pdf': 'fa-file-pdf',
        'réinitialiser': 'fa-sync',
        'reset': 'fa-sync'
    }
    
    # Chercher les boutons sans icônes
    button_pattern = r'<button([^>]*class="[^"]*btn-with-icon[^"]*"[^>]*)>([^<]+)</button>'
    
    def add_icon_to_button(match):
        button_attrs = match.group(1)
        button_text = match.group(2).strip().lower()
        
        # Chercher une icône appropriée
        icon_class = None
        for text_key, icon in icon_mapping.items():
            if text_key in button_text:
                icon_class = icon
                break
        
        if icon_class:
            return f'<button{button_attrs}><i class="fas {icon_class}"></i> {match.group(2)}</button>'
        else:
            return match.group(0)
    
    html_content = re.sub(button_pattern, add_icon_to_button, html_content, flags=re.IGNORECASE)
    
    return html_content

def fix_icon_styles(html_content):
    """Ajoute des styles CSS pour les icônes si manquants."""
    
    icon_styles = """
    /* Styles pour les icônes Font Awesome */
    .btn-with-icon i {
        margin-right: 8px;
        font-size: 14px;
    }
    
    .btn-with-icon:hover i {
        transform: scale(1.1);
        transition: transform 0.2s ease;
    }
    
    /* Masquer les icônes de fallback */
    .fa-fallback {
        display: none;
    }
    
    /* Icônes spécifiques */
    .btn-with-icon .fa-edit { color: #007bff; }
    .btn-with-icon .fa-trash { color: #dc3545; }
    .btn-with-icon .fa-plus { color: #28a745; }
    .btn-with-icon .fa-save { color: #17a2b8; }
    .btn-with-icon .fa-magic { color: #6f42c1; }
    .btn-with-icon .fa-comments { color: #fd7e14; }
    .btn-with-icon .fa-chart-bar { color: #20c997; }
    .btn-with-icon .fa-image { color: #e83e8c; }
    .btn-with-icon .fa-eye { color: #6c757d; }
    .btn-with-icon .fa-download { color: #28a745; }
    .btn-with-icon .fa-upload { color: #ffc107; }
    .btn-with-icon .fa-times { color: #6c757d; }
    .btn-with-icon .fa-home { color: #007bff; }
    .btn-with-icon .fa-bullseye { color: #dc3545; }
    .btn-with-icon .fa-users { color: #28a745; }
    .btn-with-icon .fa-tachometer-alt { color: #17a2b8; }
    """
    
    # Ajouter les styles dans le head si pas déjà présents
    if 'btn-with-icon i' not in html_content:
        if '</head>' in html_content:
            html_content = html_content.replace('</head>', f'    <style>{icon_styles}</style>\n</head>')
        elif '<head>' in html_content:
            html_content = html_content.replace('<head>', f'<head>\n    <style>{icon_styles}</style>')
    
    return html_content

def process_html_file(file_path):
    """Traite un fichier HTML pour corriger les icônes."""
    print(f"🔧 Traitement de {file_path}...")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Étapes de correction
        content = add_font_awesome_to_head(content)
        content = fix_broken_btn_with_icon(content)
        content = add_missing_icons(content)
        content = fix_icon_styles(content)
        
        # Sauvegarder si des changements ont été faits
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✅ Icônes corrigées dans {file_path}")
            return True
        else:
            print(f"  ⚠️  Aucun changement nécessaire dans {file_path}")
            return False
            
    except Exception as e:
        print(f"  ❌ Erreur lors du traitement de {file_path}: {e}")
        return False

def main():
    """Fonction principale."""
    print("🎨 Correction automatique des icônes Font Awesome")
    print("=" * 50)
    
    # Fichiers HTML à traiter
    html_files = [
        'index.html',
        'lsu_generator.html',
        'profils_eleves.html',
        'dashboard.html',
        'student_profile_page.html',
        'create_student.html',
        'student_list.html',
        'photos_classe_pro.html',
        'improved_lsu_generator.html'
    ]
    
    # Traiter chaque fichier
    success_count = 0
    for file_name in html_files:
        if os.path.exists(file_name):
            if process_html_file(file_name):
                success_count += 1
        else:
            print(f"  ⚠️  Fichier {file_name} non trouvé")
    
    print("\n" + "=" * 50)
    print(f"🎉 Correction terminée ! {success_count}/{len(html_files)} fichiers traités")
    print("\n📋 Résumé des corrections :")
    print("✅ Font Awesome 6 CDN ajouté")
    print("✅ Boutons cassés corrigés")
    print("✅ Icônes manquantes ajoutées")
    print("✅ Styles CSS pour icônes ajoutés")
    print("\n🚀 Testez maintenant vos pages pour voir les icônes !")
    
    return success_count

if __name__ == "__main__":
    main() 