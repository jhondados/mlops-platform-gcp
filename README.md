# 🔄 MLOps Platform — GCP

[![Vertex AI](https://img.shields.io/badge/Vertex%20AI%20Pipelines-✓-blue)](.)
[![Models](https://img.shields.io/badge/Models%20in%20Production-47-green)](.)
[![Drift Detection](https://img.shields.io/badge/Drift%20Detection-Automated-orange)](.)

> Complete MLOps platform managing **47 production ML models** with automated retraining, drift detection, shadow deployment and instant rollback. Reduced model deployment time from 3 weeks to 4 hours.

## 🏆 Platform Stats
- **47 ML models** in production across 12 business units
- Deployment time: **3 weeks → 4 hours** (12x faster)
- **Zero failed deployments** with blue/green strategy (18 months)
- **100% automated retraining** — triggered by data drift or performance degradation

## 🏗️ Platform Components

```
CODE PUSH ──▶ CI/CD ──▶ TRAIN ──▶ EVALUATE ──▶ REGISTER ──▶ DEPLOY
               │           │           │              │           │
               ▼           ▼           ▼              ▼           ▼
           Unit Tests   Vertex AI   Champion/     Model       Blue/Green
           Data Tests   Pipelines   Challenger    Registry    + Canary
                                    Testing       + Tags      + Rollback
```

## ✨ Features
- **Automated retraining**: Triggered by drift score > 0.15 or F1 drop > 3%
- **Shadow mode**: New models serve shadow traffic before promotion
- **A/B testing**: Statistical significance testing before full rollout
- **Explainability**: SHAP values logged for every prediction batch
- **Lineage**: Full data → model → prediction lineage in Vertex AI
