const express = require('express');
const cors = require('cors');
const multer = require('multer');
const sharp = require('sharp');
const path = require('path');
const axios = require('axios');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 8000;

// ================= MIDDLEWARE =================
app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, 'frontend')));

const upload = multer({
    storage: multer.memoryStorage(),
    limits: { fileSize: 5 * 1024 * 1024 }
});

// ================= WEATHER API =================
const WEATHER_API = process.env.WEATHER_API_KEY;

// ================= SAMPLE DATA =================
const CROPS = {
    low: [
        { name: "Jowar", profit: 18000 },
        { name: "Ragi", profit: 20000 },
        { name: "Tur Dal", profit: 25000 }
    ],
    moderate: [
        { name: "Groundnut", profit: 30000 },
        { name: "Cotton", profit: 45000 }
    ],
    high: [
        { name: "Sugarcane", profit: 80000 },
        { name: "Pomegranate", profit: 120000 }
    ]
};

const MARKET_PRICES = [
    { crop: "Jowar", market: "Hubli", price: 3200 },
    { crop: "Ragi", market: "Dharwad", price: 4500 },
    { crop: "Cotton", market: "Haveri", price: 7600 },
    { crop: "Tur Dal", market: "Kalaburagi", price: 8900 }
];

const SCHEMES = [
    {
        name: "PM-KISAN",
        subsidy: "₹6000/year",
        eligibility: "All small farmers"
    },
    {
        name: "KUSUM",
        subsidy: "60% Solar Pump Subsidy",
        eligibility: "Farmers with land"
    },
    {
        name: "PMEGP",
        subsidy: "35% Subsidy",
        eligibility: "Rural Entrepreneurs"
    }
];

const TRANSLATIONS = {
    english: {
        welcome: "Welcome to Sahayak AI",
        weather: "Weather Forecast",
        market: "Market Prices"
    },
    kannada: {
        welcome: "ಸಹಾಯಕ AI ಗೆ ಸ್ವಾಗತ",
        weather: "ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ",
        market: "ಮಾರುಕಟ್ಟೆ ಬೆಲೆ"
    },
    hindi: {
        welcome: "सहायक AI में आपका स्वागत है",
        weather: "मौसम पूर्वानुमान",
        market: "बाज़ार मूल्य"
    }
};

// ================= FARMER MARKETPLACE =================
let MARKETPLACE = [];

// ================= HEALTH =================
app.get('/api/health', (req, res) => {
    res.json({
        success: true,
        message: "Sahayak AI Running Successfully"
    });
});

// ================= WEATHER FORECAST =================
app.get('/api/weather/:city', async (req, res) => {

    try {

        const city = req.params.city;

        const response = await axios.get(
            `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${WEATHER_API}&units=metric`
        );

        const data = response.data;

        let alert = "✅ Weather Normal";

        if (data.main.temp > 38) {
            alert = "🔥 Heat Alert";
        }

        if (data.weather[0].main === "Rain") {
            alert = "🌧 Rain Alert";
        }

        if (data.wind.speed > 15) {
            alert = "🌪 Strong Wind Alert";
        }

        res.json({
            success: true,
            city: data.name,
            temperature: data.main.temp,
            humidity: data.main.humidity,
            weather: data.weather[0].description,
            wind: data.wind.speed,
            alert
        });

    } catch (error) {

        res.status(500).json({
            success: false,
            message: "Weather Fetch Failed"
        });
    }
});

// ================= SMART CROP ADVISORY =================
app.post('/api/crop/advisory', (req, res) => {

    const { soil, water, season } = req.body;

    let recommendations = [];

    if (soil === 'black' && water === 'low') {

        recommendations = CROPS.low;

    } else if (soil === 'red' && water === 'moderate') {

        recommendations = CROPS.moderate;

    } else {

        recommendations = CROPS.high;
    }

    res.json({
        success: true,
        season,
        recommendations
    });
});

// ================= MARKET PRICE TRACKING =================
app.get('/api/market-prices', (req, res) => {

    res.json({
        success: true,
        prices: MARKET_PRICES
    });
});

// ================= FARMER TO BUYER CONNECTIVITY =================
app.post('/api/marketplace/add', (req, res) => {

    const {
        farmer,
        product,
        quantity,
        price,
        phone,
        location
    } = req.body;

    const item = {
        id: Date.now(),
        farmer,
        product,
        quantity,
        price,
        phone,
        location
    };

    MARKETPLACE.push(item);

    res.json({
        success: true,
        message: "Product Added Successfully",
        item
    });
});

app.get('/api/marketplace', (req, res) => {

    res.json({
        success: true,
        products: MARKETPLACE
    });
});

// ================= GOVERNMENT SCHEMES =================
app.get('/api/schemes', (req, res) => {

    res.json({
        success: true,
        schemes: SCHEMES
    });
});

// ================= FARM MANAGEMENT TOOLS =================
app.post('/api/farm/calculate', (req, res) => {

    const {
        seeds,
        fertilizer,
        labor,
        transport,
        expectedIncome
    } = req.body;

    const totalExpense =
        seeds +
        fertilizer +
        labor +
        transport;

    const estimatedProfit =
        expectedIncome - totalExpense;

    res.json({
        success: true,
        totalExpense,
        expectedIncome,
        estimatedProfit
    });
});

// ================= MULTILINGUAL SUPPORT =================
app.get('/api/translations/:lang', (req, res) => {

    const lang = req.params.lang;

    res.json({
        success: true,
        data: TRANSLATIONS[lang] || TRANSLATIONS.english
    });
});

// ================= SOIL ANALYSIS =================
app.post('/api/soil/analyze', upload.single('file'), async (req, res) => {

    try {

        const imageBuffer = req.file.buffer;

        const image = await sharp(imageBuffer)
            .resize(50, 50)
            .raw()
            .toBuffer();

        let rSum = 0;

        for (let i = 0; i < image.length; i += 3) {
            rSum += image[i];
        }

        const avgR = rSum / (image.length / 3);

        let soilType = "Alluvial";

        if (avgR > 100 && avgR < 180) {
            soilType = "Red Soil";
        }

        if (avgR < 60) {
            soilType = "Black Soil";
        }

        res.json({
            success: true,
            soil: soilType,
            confidence: "85%"
        });

    } catch (error) {

        res.status(500).json({
            success: false,
            message: "Soil Analysis Failed"
        });
    }
});

// ================= VOICE ASSISTANT =================
app.get('/api/voice/respond', (req, res) => {

    const question =
        (req.query.question || '').toLowerCase();

    let response = '';

    if (question.includes('crop')) {

        response =
            "Jowar and Ragi are best for low rainfall.";

    } else if (question.includes('scheme')) {

        response =
            "PM-KISAN and KUSUM schemes are available.";

    } else {

        response =
            "Please ask about crops, weather, or schemes.";
    }

    res.json({ response });
});

// ================= FRONTEND ROUTES =================
app.get('/', (req, res) => {

    res.sendFile(
        path.join(__dirname, 'frontend', 'welcome.html')
    );
});

app.get('/dashboard', (req, res) => {

    res.sendFile(
        path.join(__dirname, 'frontend', 'index.html')
    );
});

// ================= START SERVER =================
app.listen(PORT, () => {

    console.log('================================');
    console.log('🌾 Sahayak AI Running');
    console.log(`🚀 http://localhost:${PORT}`);
    console.log('================================');
});
