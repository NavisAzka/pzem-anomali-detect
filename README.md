# AC Anomaly Detection System (Random Forest + Sensor + Weather Forecast)

## Overview

This project implements a real-time anomaly detection system for a single air conditioner (AC) using:

- **PZEM-004T 100A** sensor (to measure voltage, current, power, frequency)
- **DHT11** sensor for room temperature
- **BMKG weather forecast API** for outside and forecasted temperature
- **Random Forest classifier** for anomaly detection
- **Relay module** to control AC on/off
- **Telegram Bot** for alert notifications

## Objectives

Detect and respond to anomalies in AC operation such as:

- AC running while the room is already cold and no heat is forecasted
- AC not running despite forecasted high external temperatures
- Abnormal current/power draw (possible damage or inefficiency)
- Proactive cooling required before temperature rises

## Data Features

Each sample includes:

- `timestamp`
- `arus` (ampere)
- `voltase` (volts)
- `daya` (watt)
- `frekuensi` (Hz)
- `suhu_dalam` (internal temperature)
- `suhu_luar` (external temperature)
- `prakiraan_suhu_luar` (forecasted external temperature in 30 min)
- `label_anomali` (0 = normal, 1 = anomaly)

## Anomaly Conditions (Rule-Based Definitions)

1. **AC ON when unnecessary**:

   - `arus > 0.2`, `suhu_dalam < 23`, `suhu_luar < 25`, and `prakiraan_suhu_luar < 28`

2. **AC OFF when needed soon**:

   - `arus <= 0.2`, `suhu_dalam < 23`, and `prakiraan_suhu_luar > 45`

3. **Overload or inconsistency**:

   - `daya > 1200 W` or `arus > 5 A`, or high current but low power

4. **Room already hot but AC off**:

   - `arus <= 0.2` and `suhu_dalam > 28` and `prakiraan_suhu_luar > 30`

5. **Overcooling without justification**:

   - `arus > 0.2`, `suhu_dalam < 20`, and `prakiraan_suhu_luar < 28`

<!-- ## Project Structure

- `train.py`: Training script for Random Forest classifier
- `model_rf.pkl`: Trained model (generated after running train.py)
- `predict.py`: Predicts anomaly from live or sample data
- `data/`: Folder containing CSV datasets
- `relay_control.py`: Controls relay (AC ON/OFF)
- `telegram_alert.py`: Sends Telegram messages upon anomaly

## Libraries Used

- `pandas`, `numpy` for data handling
- `scikit-learn` for model training and prediction
- `prometheus-api-client` (if connected to Prometheus)
- `python-telegram-bot` for Telegram integration
- `gpiozero` or `RPi.GPIO` or `pyserial` for controlling relays -->

## Usage

1. Place labeled training data in `data/` (CSV format)
2. Run `train.py` to build and export model
3. In deployment, call `predict.py` periodically using scheduler or cron
4. On anomaly, the system:

   - Logs the event
   - Sends a Telegram alert
   - Optionally turns OFF AC via relay

---
