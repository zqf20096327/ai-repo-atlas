# PSPDFKit/ai-assistant-demo

⭐ 68 · JavaScript · 推送 2026-08-25 · [GitHub](https://github.com/PSPDFKit/ai-assistant-demo) · 组织维护

**用自然语言操作 PDF 的 AI 助手演示（Nutrient Web SDK）**

PSPDFKit/Nutrient 官方演示工程：在 Nutrient Web SDK 文档查看器中集成 AI Assistant，通过自然语言命令对 PDF 进行文档分析与交互。提供两个形态：默认演示用 Docker Compose 运行 ai-assistant 容器，另一目录演示用 Nutrient Document Engine 存储文档。运行需 Docker Compose 3.8+、Node 20+ 和 OpenAI API Key，通过 ./start 脚本启动 Web 应用。定位为功能演示而非生产库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在 Nutrient Web SDK 查看器中以自然语言与 PDF 交互
- Docker Compose 一键启动（docker compose up -d + ./start）
- 另含基于 Document Engine 存储文档的演示变体

## 适用场景

- 评估 Nutrient AI Assistant 的 PDF 交互能力
- 作为将 AI 助手集成到自家 PDF 工作流的参考实现

## 场景标签

`AI 助手` `文档问答` · 领域:对话与助手

## 证据(README 行号)

> L3: This project demonstrates the functionality of Nutrient AI Assistant. The AI-powered assistant enhances PDF document
> L30: Head over to URL listed on the command line, where you'll see a PDF loaded in the Nutrient Web SDK, our document vi

## 星数曲线

```mermaid
xychart-beta
    title "PSPDFKit/ai-assistant-demo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 67 --> 69
    line [68, 68]
```

2026-10-18 68 → 2026-10-30 68（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `55482de64a7b` · [字段定义](../../DATASET.md)*
