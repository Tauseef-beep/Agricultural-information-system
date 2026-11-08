# Crop diseases database.
# Keys must be lowercase crop names. Each crop has a list of disease dictionaries.

crop_problems = {
    "wheat": [
        {
            "problem": "Yellow Rust",
            "symptoms": "Yellow stripes of powdery spores on leaves.",
            "cause": "Fungus Puccinia striiformis, favoured by cool, humid weather.",
            "solution": "Spray a recommended fungicide such as propiconazole.",
            "prevention": "Grow resistant varieties and sow at the recommended time.",
        },
        {
            "problem": "Loose Smut",
            "symptoms": "Grain heads turn into black powdery masses.",
            "cause": "Seed-borne fungus Ustilago tritici.",
            "solution": "Remove and destroy infected plants.",
            "prevention": "Use certified, fungicide-treated seed.",
        },
        {
            "problem": "Powdery Mildew",
            "symptoms": "White powdery patches on leaves and stems.",
            "cause": "Fungus Blumeria graminis in cool, humid, dense crops.",
            "solution": "Apply a suitable fungicide at the first signs.",
            "prevention": "Avoid dense sowing and excess nitrogen; use resistant varieties.",
        },
    ],
    "rice": [
        {
            "problem": "Rice Blast",
            "symptoms": "Diamond-shaped grey spots with brown borders on leaves.",
            "cause": "Fungus Magnaporthe oryzae, favoured by high humidity.",
            "solution": "Apply a suitable fungicide such as tricyclazole.",
            "prevention": "Avoid excess nitrogen and use resistant varieties.",
        },
        {
            "problem": "Bacterial Leaf Blight",
            "symptoms": "Yellow to white stripes along leaf edges that dry out.",
            "cause": "Bacterium Xanthomonas oryzae, spread by water and wind.",
            "solution": "Drain the field and apply recommended copper-based sprays.",
            "prevention": "Use resistant varieties and healthy seed.",
        },
    ],
    "maize": [
        {
            "problem": "Maize Leaf Blight",
            "symptoms": "Long, tan-coloured lesions on leaves.",
            "cause": "Fungus Exserohilum turcicum in humid conditions.",
            "solution": "Apply fungicide if infection is severe.",
            "prevention": "Rotate crops and plant resistant hybrids.",
        },
        {
            "problem": "Stalk Rot",
            "symptoms": "Stalks become soft and weak, and plants lodge (fall over).",
            "cause": "Fungi such as Fusarium, favoured by plant stress and poor drainage.",
            "solution": "Harvest early where possible and remove crop residue.",
            "prevention": "Maintain balanced fertilisation and good drainage.",
        },
    ],
    "sorghum": [
        {
            "problem": "Grain Smut",
            "symptoms": "Grains replaced by small, hard, spore-filled galls.",
            "cause": "Seed-borne fungus Sporisorium sorghi.",
            "solution": "Remove and destroy infected heads before spores spread.",
            "prevention": "Treat seed with a fungicide before sowing.",
        },
    ],
    "tomatoes": [
        {
            "problem": "Early Blight",
            "symptoms": "Brown spots with concentric rings on older leaves.",
            "cause": "Fungus Alternaria solani in warm, humid weather.",
            "solution": "Remove infected leaves and apply a recommended fungicide.",
            "prevention": "Rotate crops, avoid overhead watering, and space plants well.",
        },
        {
            "problem": "Leaf Curl Virus",
            "symptoms": "Curled, yellowing leaves and stunted plants.",
            "cause": "Virus spread by whiteflies.",
            "solution": "Remove infected plants and control whiteflies.",
            "prevention": "Use virus-resistant varieties and insect nets.",
        },
    ],
    "eggplants": [
        {
            "problem": "Fruit and Shoot Borer",
            "symptoms": "Wilting shoots and fruits with holes and larval droppings.",
            "cause": "Larvae of the moth Leucinodes orbonalis.",
            "solution": "Cut and destroy affected shoots and fruits; apply a recommended insecticide.",
            "prevention": "Rotate crops and use pheromone traps.",
        },
    ],
    "cabbages": [
        {
            "problem": "Black Rot",
            "symptoms": "V-shaped yellow patches on leaf edges and blackened veins.",
            "cause": "Bacterium Xanthomonas campestris.",
            "solution": "Remove infected plants and apply copper-based sprays.",
            "prevention": "Use disease-free seed and rotate crops.",
        },
    ],
    "mangoes": [
        {
            "problem": "Powdery Mildew",
            "symptoms": "White powdery growth on flowers and young fruits, causing flower drop.",
            "cause": "Fungus Oidium mangiferae in cool, humid weather.",
            "solution": "Spray sulphur-based or other recommended fungicides.",
            "prevention": "Prune for airflow and spray before flowering.",
        },
        {
            "problem": "Anthracnose",
            "symptoms": "Dark sunken spots on leaves, flowers, and fruits.",
            "cause": "Fungus Colletotrichum gloeosporioides in humid conditions.",
            "solution": "Apply copper-based or recommended fungicides.",
            "prevention": "Prune dead twigs and avoid fruit injury.",
        },
    ],
    "bananas": [
        {
            "problem": "Panama Disease",
            "symptoms": "Yellowing and wilting of older leaves; brown discolouration inside the stem.",
            "cause": "Soil-borne fungus Fusarium oxysporum.",
            "solution": "Remove and destroy infected plants; there is no effective cure.",
            "prevention": "Plant resistant varieties and use disease-free planting material.",
        },
    ],
    "mustard": [
        {
            "problem": "White Rust",
            "symptoms": "White blister-like pustules on leaves and stems.",
            "cause": "Fungus Albugo candida in cool, humid conditions.",
            "solution": "Spray a recommended fungicide.",
            "prevention": "Use clean seed and rotate crops.",
        },
        {
            "problem": "Aphid Infestation",
            "symptoms": "Clusters of small insects on shoots; curled, sticky leaves.",
            "cause": "Mustard aphids feeding on plant sap.",
            "solution": "Spray a recommended insecticide or neem-based product.",
            "prevention": "Sow on time and monitor the crop regularly.",
        },
    ],
    "sunflowers": [
        {
            "problem": "Downy Mildew",
            "symptoms": "Stunted plants with yellow patches on leaves and white growth underneath.",
            "cause": "Fungus-like organism Plasmopara halstedii.",
            "solution": "Remove infected plants early.",
            "prevention": "Use treated seed and resistant varieties.",
        },
    ],
    "chillies": [
        {
            "problem": "Leaf Curl",
            "symptoms": "Upward-curled leaves, stunted growth, and reduced fruiting.",
            "cause": "Virus spread by whiteflies and thrips.",
            "solution": "Remove affected plants and control insect vectors.",
            "prevention": "Use resistant varieties and keep fields free of weeds.",
        },
        {
            "problem": "Anthracnose (Fruit Rot)",
            "symptoms": "Dark, sunken spots on ripening fruits.",
            "cause": "Fungus Colletotrichum capsici in warm, wet weather.",
            "solution": "Apply a recommended fungicide and remove infected fruits.",
            "prevention": "Use healthy seed and avoid overhead irrigation.",
        },
    ],
}
