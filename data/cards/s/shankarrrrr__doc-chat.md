# shankarrrrr/doc-chat

⭐ 18 · Python · 推送 2026-01-29 · [GitHub](https://github.com/shankarrrrr/doc-chat) · 组织维护

**面向患者与医生的 AI 医疗平台：ECG 分析、语音症状采集、医患门户**

团队协作开发的全栈医疗辅助平台：Django REST 后端 + React 19 前端，功能包括 AI 健康洞察（Google Gemini API）、基于 Scikit-learn 模型的 ECG 分析、Web Speech API 语音症状采集，以及医生-患者门户系统。身份验证使用 Supabase（Google OAuth），地图功能依赖 Google Maps API，支持 Railway 一键部署或本地开发。运行需配置 Gemini API key、PostgreSQL 等多项环境变量，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Gemini API 提供的 AI 健康洞察
- Scikit-learn 模型进行 ECG 分析
- Web Speech API 语音症状采集
- 医生-患者门户系统与 Supabase 认证

## 适用场景

- 患者通过语音描述症状并获得 AI 健康洞察
- 上传 ECG 数据由机器学习模型分析
- 医生通过门户查看与管理患者信息

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L3: A comprehensive healthcare assistance platform built with Django REST API and React, featuring AI-powered health ins
> L12: - **AI/ML**: Google Gemini API + Scikit-learn (ECG Models)

## 星数曲线

```mermaid
xychart-beta
    title "shankarrrrr/doc-chat 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `4e9c31e0b286` · [字段定义](../../DATASET.md)*
