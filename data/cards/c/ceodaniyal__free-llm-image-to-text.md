# ceodaniyal/free-llm-image-to-text

⭐ 25 · Python · 推送 2025-12-11 · [GitHub](https://github.com/ceodaniyal/free-llm-image-to-text) · 个人维护

**用 OpenRouter 免费视觉 LLM 做图片文字提取的 Python 脚本**

Python 脚本项目，调用 OpenRouter 免费档位的视觉 LLM 完成 OCR：读取图片 URL 或本地图片（转 Base64），发送指令提示词与图像，返回模型提取的文本并可保存为 .txt 文件。提供三个函数（Base64 编码、URL 提取、Base64 提取），模型名可改换为任意 OpenRouter 免费视觉模型。需 Python 3.7+、requests、OpenRouter API key（免费档），无付费 API。面向学生、爱好者及文档预处理场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持图片 URL 与本地图片（Base64）两种输入
- 模型无关：可切换任意 OpenRouter 免费视觉模型
- 提取结果可保存为 .txt 文件
- 仅需 OpenRouter 免费 API key，无需付费服务

## 适用场景

- 提取收据、发票、证件上的文字
- 笔记数字化与 PDF（转图后）文字提取
- ML 流水线中的文档预处理

## 场景标签

`OCR` · 领域:感知与多模态

## 证据(README 行号)

> L3: This project performs **OCR (Optical Character Recognition)** using **free vision-enabled LLMs** available on **Open
> L61: Downloads the image → sends to LLM → extracts text.
> L67: Both functions call a free OpenRouter LLM.

## 星数曲线

```mermaid
xychart-beta
    title "ceodaniyal/free-llm-image-to-text 星数(近 5 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23", "2026-10-24", "2026-10-28"]
    y-axis "stars" 20 --> 26
    line [21, 22, 24, 25, 25]
```

2026-10-18 21 → 2026-10-28 25（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `39feb8a7fdfc` · [字段定义](../../DATASET.md)*
