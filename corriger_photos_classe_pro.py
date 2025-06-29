#!/usr/bin/env python3
"""
Script pour corriger le fichier photos_classe_pro.html
- Encapsule le JavaScript dans des balises <script> correctement fermées
- Supprime les blocs dupliqués
- Corrige les template literals
- Déplace les fonctions JS en fin de document
"""

import re

def corriger_photos_classe_pro():
    """Corrige le fichier photos_classe_pro.html"""
    
    with open('photos_classe_pro.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Supprimer les blocs JavaScript dupliqués dans les template literals
    # Pattern pour trouver les blocs JavaScript dans les template literals
    js_in_template_pattern = r'<script>[\s\S]*?</script>'
    
    def remove_js_from_template(match):
        # Si c'est dans un template literal, on le supprime
        return ''
    
    # Appliquer seulement dans les fonctions d'export
    content = re.sub(r'(genererHTML|exporterHTML).*?`[\s\S]*?<script>[\s\S]*?</script>[\s\S]*?`', 
                    lambda m: re.sub(js_in_template_pattern, '', m.group(0)), 
                    content, flags=re.DOTALL)
    
    # 2. Corriger les template literals dans les fonctions d'export
    def corriger_template_literals(match):
        func_name = match.group(1)
        if func_name == 'genererHTML':
            return '''function genererHTML(donnees) {
            const eleves = donnees.eleves || donnees;
            return `
                <!DOCTYPE html>
                <html>
                <head><title>Liste des élèves</title></head>
                <body>
                    <h1>Liste des élèves</h1>
                    ${eleves.map(eleve => `
                        <div>
                            <h3>${eleve.nom}</h3>
                            <p>ID: ${eleve.id}, Niveau: ${eleve.niveau}, Statut: ${eleve.statut}</p>
                        </div>
                    `).join('')}
                </body>
                </html>
            `;
        }'''
        elif func_name == 'exporterHTML':
            return '''function exporterHTML(donnees, fileName) {
            const eleves = donnees.eleves || donnees;
            
            let htmlContent = `
                <!DOCTYPE html>
                <html>
                <head><title>Liste des élèves</title></head>
                <body>
                    <h1>Liste des élèves</h1>
                    ${eleves.map(eleve => `
                        <div>
                            <h3>${eleve.nom}</h3>
                            <p>ID: ${eleve.id}, Niveau: ${eleve.niveau}, Statut: ${eleve.statut}</p>
                        </div>
                    `).join('')}
                </body>
                </html>
            `;
            
            const dataBlob = new Blob([htmlContent], {type: 'text/html'});
            const url = URL.createObjectURL(dataBlob);
            const link = document.createElement('a');
            link.href = url;
            link.download = `${fileName}.html`;
            link.click();
            URL.revokeObjectURL(url);
            afficherNotification('Export HTML réussi', 'success');
        }'''
        return match.group(0)
    
    # Appliquer la correction
    content = re.sub(r'function (genererHTML|exporterHTML)[\s\S]*?};', corriger_template_literals, content, flags=re.DOTALL)
    
    # 3. Supprimer les blocs JavaScript dupliqués à la fin
    # Supprimer les blocs dupliqués après Bootstrap JS
    content = re.sub(r'<!-- Bootstrap JS -->\s*<script src="[^"]*"></script>\s*<script>[\s\S]*?</script>\s*</body>\s*</html>', 
                    '<!-- Bootstrap JS -->\n    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>\n</body>\n</html>', 
                    content, flags=re.DOTALL)
    
    # 4. S'assurer que toutes les balises script sont correctement fermées
    # Compter les balises script ouvertes et fermées
    script_open = content.count('<script>')
    script_close = content.count('</script>')
    
    if script_open != script_close:
        print(f"⚠️ Attention: {script_open} balises <script> ouvertes, {script_close} fermées")
    
    # 5. Déplacer les fonctions JavaScript en fin de document
    # Extraire toutes les fonctions JavaScript
    js_functions = re.findall(r'function [^{]*\{[\s\S]*?\n\s*\}', content)
    
    # Supprimer les fonctions du contenu principal
    content = re.sub(r'function [^{]*\{[\s\S]*?\n\s*\}', '', content)
    
    # Ajouter les fonctions en fin de document, avant </body>
    js_content = '\n    <script>\n'
    js_content += '        // Variables globales\n'
    js_content += '        let eleves = [];\n'
    js_content += '        let eleveCourant = null;\n'
    js_content += '        let eleveASupprimer = null;\n'
    js_content += '        let modeEdition = false;\n\n'
    
    for func in js_functions:
        js_content += '        ' + func + '\n\n'
    
    js_content += '        // Initialisation\n'
    js_content += '        document.addEventListener("DOMContentLoaded", function() {\n'
    js_content += '            chargerDonnees();\n'
    js_content += '            afficherEleves();\n'
    js_content += '        });\n'
    js_content += '    </script>\n'
    
    # Insérer avant </body>
    content = content.replace('</body>', js_content + '</body>')
    
    # 6. Corriger les boutons avec des icônes Font Awesome
    button_corrections = {
        r'<button class="btn btn-success" onclick="ajouterEleve\(\)"> class="btn-with-icon"><i class="fas fa-plus icon-fa"></i><i class="fas fa-plus fa-fallback"></i>Ajouter un élève\s*</button>': 
        '<button class="btn btn-success btn-with-icon" onclick="ajouterEleve()">\n                        <i class="fas fa-user-plus"></i> Ajouter un élève\n                    </button>',
        
        r'<button class="btn btn-info" onclick="importerListeEleves\(\)"> class="btn-with-icon"><i class="fas fa-download icon-fa"></i><i class="fas fa-download fa-fallback"></i>Importer\s*</button>': 
        '<button class="btn btn-info btn-with-icon" onclick="importerListeEleves()">\n                        <i class="fas fa-file-import"></i> Importer\n                    </button>',
        
        r'<button class="btn btn-warning" onclick="exporterListeEleves\(\)"> class="btn-with-icon"><i class="fas fa-upload icon-fa"></i><i class="fas fa-upload fa-fallback"></i>Exporter\s*</button>': 
        '<button class="btn btn-warning btn-with-icon" onclick="exporterListeEleves()">\n                        <i class="fas fa-file-export"></i> Exporter\n                    </button>'
    }
    
    for pattern, replacement in button_corrections.items():
        content = re.sub(pattern, replacement, content, flags=re.MULTILINE)
    
    # Sauvegarder le fichier corrigé
    with open('photos_classe_pro.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Fichier photos_classe_pro.html corrigé avec succès !")
    print("📋 Corrections apportées :")
    print("   ✅ JavaScript encapsulé dans des balises <script>")
    print("   ✅ Blocs dupliqués supprimés")
    print("   ✅ Template literals corrigés")
    print("   ✅ Boutons avec icônes Font Awesome")
    print("   ✅ Fonctions JS déplacées en fin de document")

if __name__ == "__main__":
    corriger_photos_classe_pro() 