# 1nn0k3sh4/trendevourer

⭐ 20 · Python · MIT · 推送 2026-01-18 · [GitHub](https://github.com/1nn0k3sh4/trendevourer) · 个人维护

**本地 AI 分析服装照片并生成穿搭报告的桌面应用**

基于 PyQt6 的桌面应用：上传至少 3 张服装照片，通过本地 Ollama 运行双模型流水线——BakLLaVA 视觉模型描述每张图，Mistral 7B 文本模型汇总生成含色彩与单品分析、潮流识别、3-5 条搭配建议的风格报告，可导出 PDF。全部处理在本地完成，不依赖云服务。面向造型师与整理衣橱的个人用户。限制：需预下载模型、大图处理耗时、PDF 仅支持基础排版。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- BakLLaVA 视觉描述 + Mistral 7B 报告生成的双模型流水线
- 报告含色彩单品分析、潮流识别与 3-5 条搭配建议
- PDF 导出（WeasyPrint）
- 全程本地处理，照片不出本机

## 适用场景

- 整理衣橱并获得穿搭组合建议
- 造型师为客户批量分析着装照片生成风格报告
- 在无云端依赖的环境下离线生成时尚趋势报告

## 场景标签

`图像视频处理` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L6: **Trend Devourer** is an intelligent desktop application that analyzes clothing photos using local AI models and gen
> L12:  — **BakLLaVA** (computer vision) describes each look
> L13:  — **Mistral 7B** (text model) creates a coherent style report

## 星数曲线

```mermaid
xychart-beta
    title "1nn0k3sh4/trendevourer 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-28 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `285e4489a378` · [字段定义](../../DATASET.md)*
