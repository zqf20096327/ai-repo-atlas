# RobinaMirbahar/Comic-Studio-Ai

⭐ 16 · HTML · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/RobinaMirbahar/Comic-Studio-Ai) · [官网](https://github.com/RobinaMirbahar/Comic-Studio-Ai) · 个人维护

**面向创作者的多智能体漫画生成器：文本提示生成多格漫画**

基于 FastAPI 的多智能体漫画生成服务，调用 Google Gemini API（nano-banana-pro-preview 与 gemini-3.1-flash-image-preview 模型）完成故事撰写、分镜、对白与图像渲染。通过角色档案注入每格提示词实现跨分格角色一致性；支持 7 种语言（含阿拉伯语/乌尔都语 RTL）、1–6 格漫画、6 种气泡类型、7 种画风、语音输入、图片上传、对话式修改故事，并导出 PDF/小册子。以无状态容器服务运行于 Google Cloud Run，也可 Docker 或本地源码运行；需自备 Gemini API key。作者为个人开发者，为 Gemini Live Agent Challenge 参赛作品。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多智能体流水线（故事→角色设定→分镜→排版）锁定角色描述保证跨格一致性
- 7 种语言本地化输出，含 RTL 支持
- 6 种气泡类型自动对白排版，PDF 与小册子两种导出
- 提供 Docker 与 Google Cloud Run 一键部署

## 适用场景

- 把一句话想法快速生成分格漫画用于教学或创作
- 用自然语言对话迭代修改故事与角色
- 面向多语言读者生成本地化漫画内容

## 场景标签

`多智能体` `图像生成` `AI 写作` · 领域:Agent 开发

## 证据(README 行号)

> L26: **Turn simple prompts into professional comics — with AI-powered storytelling, automatic speech bubbles, and a conv
> L53: |📝 **Story Generation**|AI crafts complete narratives with characters|Gemini + nano-banana-pro-preview|
> L61: |🖼️ **Real Image Generation**|Comic panels via Imagen|gemini-3.1-flash-image-preview|

## 星数曲线

```mermaid
xychart-beta
    title "RobinaMirbahar/Comic-Studio-Ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `2dc66ee1f5e7` · [字段定义](../../DATASET.md)*
