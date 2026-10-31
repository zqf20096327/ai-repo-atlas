# Blacksujit/ArogyaKrishi

⭐ 24 · Jupyter Notebook · 推送 2026-08-24 · [GitHub](https://github.com/Blacksujit/ArogyaKrishi) · 组织维护

**面向农户的作物病害检测与施肥推荐 Web 应用（SIH 2024 原型）**

SIH 2024 黑客松（问题 SIH-1638，Agri&tech 主题）的原型项目：基于 Flask 的 Web 应用，用图像分类模型（含 ResNet 等预训练模型、transformers）识别多种作物病害，提供基于土壤分析的作物推荐、按作物与土壤状况生成施肥建议，并集成实时天气数据与多语言支持、聊天机器人。模型文件需从 Google Drive 下载并放入 models 目录，配置 OpenWeather 与 Hugging Face API key 后 pip 安装依赖并运行 app.py。移动端应用标注为开发中。

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

- 多作物病害图像识别（机器学习图像分类）
- 基于土壤分析的作物推荐与施肥建议
- 集成实时天气数据与多语言支持（含 Google 翻译）
- Flask + SQL-alchemy 技术栈，模型经 Jupyter notebook 训练

## 适用场景

- 上传作物照片识别病害并获取处置信息
- 根据土壤状况获得作物与施肥建议
- 结合实时天气规划种植与灌溉决策

## 场景标签

`聊天机器人` `目标检测` · 领域:对话与助手

## 证据(README 行号)

> L99: Solution: Arogya Krishi utilizes advanced image classification techniques powered by machine learning to analyze im
> L130: * Multi Crop Disease Prediction .

## 星数曲线

```mermaid
xychart-beta
    title "Blacksujit/ArogyaKrishi 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-31 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `5dae042a5320` · [字段定义](../../DATASET.md)*
