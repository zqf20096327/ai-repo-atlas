# arc53/doc2md

⭐ 18 · TypeScript · MIT · 推送 2026-06-20 · [GitHub](https://github.com/arc53/doc2md) · [官网](https://doc2md.arc53.com/) · 组织维护

**将 PDF 与图片转为 Markdown 以供 LLM 流程摄取的工具**

通过调用公开 LLM 端点（doc2md）将文档（.pdf/.png/.jpg/.jpeg）转换为 Markdown：端点把 PDF 转为图片后交给视觉模型（示例使用 meta-llama/Llama-3.2-11B-Vision-Instruct），由模型生成 Markdown 文本，便于后续接入 LLM 工作流。README 仅给出 Python 调用片段（基于 OpenAI 兼容客户端），未提供本产品的安装命令或部署说明。适合需要为 LLM 摄取准备文本化文档的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 .pdf/.png/.jpg/.jpeg 转 Markdown
- 依赖公开 LLM 端点（doc2md）的视觉模型完成转换
- 示例通过 OpenAI 兼容客户端调用

## 适用场景

- 把 PDF 文档转成 Markdown 用于 LLM 摄取
- 将图片资料文本化后接入 LLM 工作流

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L1: This project helps users to convert Documents (.pdf, .png, .jpg, .jpeg) into Markdown for you ease of ingestion into
> L4: This endpoint simply gives images or pdfs (converted to images) to visual model and asks it to conver it into markdo

## 星数曲线

```mermaid
xychart-beta
    title "arc53/doc2md 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `227b2a29389e` · [字段定义](../../DATASET.md)*
