// Script de correction des notifications
// Remplace tous les appels à showNotification par showToastNotification

const fs = require('fs');
const path = require('path');

// Lire le fichier HTML
const filePath = path.join(__dirname, 'lsu_generator.html');
let content = fs.readFileSync(filePath, 'utf8');

// Remplacer tous les appels à showNotification
content = content.replace(/showNotification\(/g, 'showToastNotification(');

// Écrire le fichier corrigé
fs.writeFileSync(filePath, content, 'utf8');

console.log('✅ Corrections appliquées : showNotification -> showToastNotification'); 