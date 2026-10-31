# ceodaniyal/local-llm-ocr-ollama

⭐ 13 · Python · 推送 2025-12-11 · [GitHub](https://github.com/ceodaniyal/local-llm-ocr-ollama) · 个人维护

**本地 Ollama 视觉模型做免费离线 OCR 的 Python 脚本**

基于 Python 的 OCR 项目：将本地图片或在线图片 URL 转为 Base64 后，发送给通过 Ollama 本地运行的视觉 LLM（如 qwen2.5vl:3b、llava、moondream），返回提取文本并可保存为 .txt，全程离线、无 API key。提供图像转 Base64、URL 下载转换、文本提取三个函数，模型名可在脚本中一行替换。运行需 Python 3.8+、本地安装 Ollama 并拉取视觉模型，另需 pip 安装 requests。以 MIT 许可发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地图片与在线 URL 图片两种输入，均转 Base64 后送视觉 LLM
- 支持任意 Ollama 视觉模型，替换模型名即可切换
- 离线运行，图片不离开本机，无 API 费用
- 输出可保存为 .txt，可改造成结构化 JSON 输出

## 适用场景

- 离线提取扫描文档、收据发票中的文字
- 转写手写笔记或低质量图片文本
- 无网络或注重隐私环境下做图片转文字

## 场景标签

`OCR` · 领域:感知与多模态

## 证据(README 行号)

> L3: This project demonstrates **OCR (Optical Character Recognition)** using **locally running LLMs** via **Ollama** — co
> L53: Downloads the image → converts to Base64 → sends to local LLM.

## 星数曲线

```mermaid
xychart-beta
    title "ceodaniyal/local-llm-ocr-ollama 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `d07be2fd1fdd` · [字段定义](../../DATASET.md)*
