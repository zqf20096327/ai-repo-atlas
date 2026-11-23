# kagandurmus/marienplatz-3d-model

⭐ 3 · MIT · 推送 2026-10-30 · [GitHub](https://github.com/kagandurmus/marienplatz-3d-model) · 个人维护

**用本地 LLM 单提示词生成 Marienplatz 3D 模型的提示词集**

该项目以提示词集形式提供可复现的 text-to-3D 工作流：README 记录一次用单个工程化提示词驱动本地运行的大模型（Qwen3.8-27b），在 LM Studio 的 Bionic harness 下经约 3 小时代码生成得到 Marienplatz 3D 模型，并附展示视频与引用格式。仓库内容为提示词本身（MIT 许可），不包含可执行代码；README 明确说明生成结果受模型、harness 与高级设置影响而波动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 公开发布复现用的单提示词（MIT 许可）
- 记录完整复现配置：Qwen3.8-27b + LM Studio（Bionic harness）
- 本地运行，无需云端 API
- 附展示视频与引用/署名说明

## 适用场景

- 复现从零开始用单提示词生成 3D 模型的工作流
- 在本地硬件上运行大模型进行 agentic 3D 建模
- 参考文本到 3D 提示词的工程化写法

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: This project aims to provide reproducible text-to-3D workflows using local AI. All prompts will be released under th
> L9: Model: Qwen3.8-27b
> L10: Hardware: M2 Ultra 24C/60C

## 星数曲线

```mermaid
xychart-beta
    title "kagandurmus/marienplatz-3d-model 星数(近 2 点)"
    x-axis ["2026-11-18", "2026-11-23"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-18 3 → 2026-11-23 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `dcbc33e8be45` · [字段定义](../../DATASET.md)*
