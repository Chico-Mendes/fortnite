-- schema.sql

CREATE TABLE IF NOT EXISTS sprites (
    code TEXT PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
)

CREATE TABLE IF NOT EXISTS variants (
    code TEXT PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
)

CREATE TABLE IF NOT EXISTS sprite_variants (
    sprite_code TEXT NOT NULL,
    variant_code TEXT NOT NULL,
    image_url TEXT NOT NULL,

    PRIMARY KEY (sprite_code, variant_code),

    FOREIGN KEY (sprite_code) REFERENCES sprites(code),
    FOREIGN KEY (variant_code) REFERENCES variants(code)
)