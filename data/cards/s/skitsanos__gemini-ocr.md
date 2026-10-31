# skitsanos/gemini-ocr

⭐ 15 · Shell · 推送 2026-01-27 · [GitHub](https://github.com/skitsanos/gemini-ocr) · [官网](https://www.linkedin.com/pulse/pdf-screenshot-ocr-analysis-google-gemini-pro-evgenios-skitsanos-htapf) · 个人维护

**用 Gemini Pro 对 PDF 截图做 OCR 文本提取的脚本**

自动化脚本项目：将 PDF 截图放入 data/ 目录，读取 prompt.txt 中的提示词，脚本获取每张图片的 MIME 类型并做 Base64 编码，连同生成配置（topP、temperature）组装为 JSON 载荷，通过 API 端点发送给 Google Gemini Pro 执行 OCR，响应保存至 response.json，提取的文本保存至 response.txt。JSON 构建依赖 jq。适用于文档数字化、数据提取与可访问性场景。README 未给出安装或运行命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PDF 截图 Base64 编码后交由 Gemini Pro API 执行 OCR
- 生成参数（topP、temperature）可配置
- 响应与提取文本分别保存为 response.json / response.txt
- 使用 jq 构建 JSON 载荷

## 适用场景

- 把 PDF 截图批量转成可编辑文本
- 文档数字化与数据提取
- 将 OCR 结果进一步用于分析或 RAG 流程

## 场景标签

`OCR` · 领域:感知与多模态

## 证据(README 行号)

> L3: This project involves automating converting PDF document screenshots into text using Google's Gemini Pro model. The 
> L14: 6. **API Request**: The payload is sent to the Google Gemini Pro model via an API endpoint to perform OCR.

## 星数曲线

```mermaid
xychart-beta
    title "skitsanos/gemini-ocr 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `36c1fc17795e` · [字段定义](../../DATASET.md)*
