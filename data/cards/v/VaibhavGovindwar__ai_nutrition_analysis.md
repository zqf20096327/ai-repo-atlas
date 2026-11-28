# VaibhavGovindwar/ai_nutrition_analysis

⭐ 3 · HTML · MIT · 推送 2026-11-26 · [GitHub](https://github.com/VaibhavGovindwar/ai_nutrition_analysis) · [官网](https://ainutritionanalysis.vercel.app) · 个人维护

**上传食物照片估算营养成分的 Flask 多模态 AI 应用**

基于 Flask 的 Web 应用：用户上传最多两张食物图片，调用 Google Gemini 视觉能力识别可见食物项并估算可食用克数，经食物别名与模糊匹配映射到 USDA FoodData Central 检索词，获取每 100 克营养值后按份量换算，聚合成一餐级结果并通过响应式仪表盘展示。部署支持 Vercel。声明为教育用途，结果为估算值；每次分析最多两张图片，需联网调用 Gemini 与 USDA API。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Gemini 视觉识别多种食物项并估算可食用克数，排除骨头果壳等不可食部分
- 别名精确匹配 + difflib 模糊匹配的食物名映射层（当前未用向量检索）
- USDA FoodData Central 集成，按估算份量计算热量与蛋白质/碳水/脂肪/纤维
- 浏览器端图片压缩与响应式结果仪表盘，可部署至 Vercel

## 适用场景

- 拍下餐食照片快速估算整餐的热量和主要营养素
- 为饮食记录工具补充基于照片的份量与营养估算参考
- 学习多模态识别 + 外部数据库检索的应用架构

## 场景标签

`RAG` `多模态` · 领域:知识与检索

## 证据(README 行号)

> L18: **AI Nutrition Analysis** is a multimodal AI application that identifies food items from uploaded meal images and e
> L20: The application combines Google's Gemini vision capabilities, a lightweight retrieval-based food mapping system, an
> L105: Google Gemini is used as the multimodal AI engine. The model receives the uploaded food image and structured instr


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `d8672f2935a5` · [字段定义](../../DATASET.md)*
