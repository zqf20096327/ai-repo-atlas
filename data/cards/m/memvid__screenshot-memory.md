# memvid/screenshot-memory

⭐ 23 · TypeScript · MIT · 推送 2026-01-23 · [GitHub](https://github.com/memvid/screenshot-memory) · [官网](https://memvid.com) · 组织维护

**本地 CLI 工具：按截图内容（文本/图像）搜索截图**

命令行工具 ssm，通过 OCR 提取截图文本、本地 AI 视觉模型（llava-phi3，经 Ollama 运行）生成照片描述，再用 memvid 做语义向量检索，支持按含义而非文件名查找截图。全部流程本地运行，无需云端与 API key。setup.sh 自动安装 Bun、Ollama 与模型；数据存储在单个 .mv2 文件；提供 index/find/watch 等 7 个命令。带 OCR worker 并行与 keep-alive 配置项。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OCR 提取文本 + 本地 AI 视觉描述 + memvid 语义搜索
- 全本地运行，无需云端与 API key
- ssm watch 自动索引新增截图
- 索引存储在单个 .mv2 文件

## 适用场景

- 在数千张截图中按内容找某张截图
- 按画面含义搜索照片（非文件名）
- 自动索引新截图并随时语义查询

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L29: - **OCR** extracts text from screenshots
> L30: - **AI vision** describes photos (local, runs on your machine)

## 星数曲线

```mermaid
xychart-beta
    title "memvid/screenshot-memory 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `3dbf126df4d7` · [字段定义](../../DATASET.md)*
