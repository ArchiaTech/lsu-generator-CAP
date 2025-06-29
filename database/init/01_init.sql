-- Script d'initialisation de la base de données LSU
-- Création des tables et données de base

-- Extension pour les UUID
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Table des utilisateurs (enseignants)
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(20) DEFAULT 'teacher' CHECK (role IN ('admin', 'teacher', 'director')),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table des élèves
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    birth_date DATE,
    gender VARCHAR(10) CHECK (gender IN ('M', 'F', 'Autre')),
    level VARCHAR(20) NOT NULL CHECK (level IN ('CP', 'CE1', 'CE2', 'CM1', 'CM2')),
    class_name VARCHAR(50),
    school_year VARCHAR(9) NOT NULL CHECK (school_year ~ '^\d{4}-\d{4}$'),
    teacher_id INTEGER REFERENCES users(id),
    
    -- Informations de contact
    address TEXT,
    phone VARCHAR(20),
    email VARCHAR(100),
    
    -- Informations familiales
    parent1_name VARCHAR(100),
    parent1_phone VARCHAR(20),
    parent1_email VARCHAR(100),
    parent1_profession VARCHAR(100),
    
    parent2_name VARCHAR(100),
    parent2_phone VARCHAR(20),
    parent2_email VARCHAR(100),
    parent2_profession VARCHAR(100),
    
    -- Points forts et difficultés
    strengths TEXT,
    difficulties TEXT,
    objectives TEXT,
    
    -- Statut
    is_active BOOLEAN DEFAULT TRUE,
    notes TEXT,
    
    -- Métadonnées
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table des compétences
CREATE TABLE IF NOT EXISTS competences (
    id SERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL REFERENCES students(id) ON DELETE CASCADE,
    domain VARCHAR(50) NOT NULL CHECK (domain IN (
        'francais_lecture', 'francais_ecriture', 'francais_oral',
        'maths_calcul', 'maths_geometrie', 'maths_resolution',
        'sciences', 'histoire_geo', 'arts', 'eps', 'langue_vivante',
        'competences_sociales'
    )),
    subdomain VARCHAR(100),
    level VARCHAR(20) NOT NULL CHECK (level IN ('insuffisant', 'fragile', 'satisfaisant', 'excellent')),
    score INTEGER CHECK (score >= 1 AND score <= 4),
    comment TEXT,
    strengths TEXT,
    difficulties TEXT,
    evaluation_date TIMESTAMP WITH TIME ZONE NOT NULL,
    period VARCHAR(50) NOT NULL,
    evaluator_id INTEGER NOT NULL REFERENCES users(id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table des évaluations
CREATE TABLE IF NOT EXISTS evaluations (
    id SERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL REFERENCES students(id) ON DELETE CASCADE,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    subject VARCHAR(50) NOT NULL,
    evaluation_date TIMESTAMP WITH TIME ZONE NOT NULL,
    period VARCHAR(50) NOT NULL,
    evaluator_id INTEGER NOT NULL REFERENCES users(id),
    results JSONB,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table des commentaires LSU
CREATE TABLE IF NOT EXISTS comments (
    id SERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL REFERENCES students(id) ON DELETE CASCADE,
    period VARCHAR(50) NOT NULL,
    school_year VARCHAR(9) NOT NULL,
    content TEXT NOT NULL,
    author_id INTEGER NOT NULL REFERENCES users(id),
    is_draft BOOLEAN DEFAULT TRUE,
    is_published BOOLEAN DEFAULT FALSE,
    published_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table des sessions utilisateur
CREATE TABLE IF NOT EXISTS user_sessions (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    session_token VARCHAR(255) UNIQUE NOT NULL,
    expires_at TIMESTAMP WITH TIME ZONE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Index pour optimiser les performances
CREATE INDEX IF NOT EXISTS idx_students_level ON students(level);
CREATE INDEX IF NOT EXISTS idx_students_school_year ON students(school_year);
CREATE INDEX IF NOT EXISTS idx_students_teacher_id ON students(teacher_id);
CREATE INDEX IF NOT EXISTS idx_students_active ON students(is_active);

CREATE INDEX IF NOT EXISTS idx_competences_student_id ON competences(student_id);
CREATE INDEX IF NOT EXISTS idx_competences_domain ON competences(domain);
CREATE INDEX IF NOT EXISTS idx_competences_level ON competences(level);
CREATE INDEX IF NOT EXISTS idx_competences_evaluation_date ON competences(evaluation_date);

CREATE INDEX IF NOT EXISTS idx_evaluations_student_id ON evaluations(student_id);
CREATE INDEX IF NOT EXISTS idx_evaluations_subject ON evaluations(subject);
CREATE INDEX IF NOT EXISTS idx_evaluations_evaluation_date ON evaluations(evaluation_date);

CREATE INDEX IF NOT EXISTS idx_comments_student_id ON comments(student_id);
CREATE INDEX IF NOT EXISTS idx_comments_period ON comments(period);
CREATE INDEX IF NOT EXISTS idx_comments_school_year ON comments(school_year);

CREATE INDEX IF NOT EXISTS idx_user_sessions_token ON user_sessions(session_token);
CREATE INDEX IF NOT EXISTS idx_user_sessions_expires ON user_sessions(expires_at);

-- Triggers pour mettre à jour updated_at
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_users_updated_at BEFORE UPDATE ON users
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_students_updated_at BEFORE UPDATE ON students
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_competences_updated_at BEFORE UPDATE ON competences
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_evaluations_updated_at BEFORE UPDATE ON evaluations
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_comments_updated_at BEFORE UPDATE ON comments
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Données de base
INSERT INTO users (username, email, full_name, password_hash, role) VALUES
('admin', 'admin@lsu-system.com', 'Administrateur', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj4J/HS.iK8i', 'admin'),
('teacher1', 'teacher1@lsu-system.com', 'Marie Dubois', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj4J/HS.iK8i', 'teacher'),
('teacher2', 'teacher2@lsu-system.com', 'Jean Martin', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj4J/HS.iK8i', 'teacher')
ON CONFLICT (username) DO NOTHING;

-- Élèves de démonstration
INSERT INTO students (first_name, last_name, birth_date, gender, level, class_name, school_year, teacher_id) VALUES
('Léa', 'Martin', '2015-03-15', 'F', 'CM1', 'CM1-A', '2024-2025', 2),
('Thomas', 'Bernard', '2015-07-22', 'M', 'CM1', 'CM1-A', '2024-2025', 2),
('Emma', 'Petit', '2015-01-10', 'F', 'CM1', 'CM1-A', '2024-2025', 2),
('Lucas', 'Moreau', '2015-11-05', 'M', 'CM1', 'CM1-A', '2024-2025', 2),
('Chloé', 'Durand', '2015-05-18', 'F', 'CM1', 'CM1-A', '2024-2025', 2)
ON CONFLICT DO NOTHING; 