# 3ALLBUY14/h3-prompt-builder

⭐ 18 · MIT · 推送 2026-10-11 · [GitHub](https://github.com/3ALLBUY14/h3-prompt-builder) · 个人维护 · 中文 README

**MiniMax H3 视频提示词编写 skill，供 AI agent 使用**

纯文档型 skill：将 MiniMax H3 官方手册提炼为提示词编写规则库，覆盖 T2VA/I2VA/FL2VA/L2VA/Ref2VA 五种生成模式、10 种风格模板、运镜/对白/音频规则、六大冗余压缩原则、镜头拆解与视频编辑指令、多语种对白与商用场景选型等，并含常见坑对策与质量自检清单。面向 WorkBuddy / Claude Code 等 AI agent 用户，将仓库放入 agent 的 skills 目录即可使用，当前版本 v2.4.0。

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

- 覆盖 H3 五种生成模式的提示词规则
- 10 种风格模板与运镜/对白/音频规则
- 六大压缩原则与字段级精简指南
- 常见坑对策与质量自检清单

## 适用场景

- 在 AI agent 中编写 MiniMax H3 视频生成提示词
- 查 H3 各生成模式与视频编辑模式的输入规格与硬限制
- 对既有提示词做冗余压缩与质量自检

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: MiniMax H3 视频提示词生成 skill（适用于 WorkBuddy / Claude Code 等 AI agent）。
> L9: - 官方使用手册增量提炼：完整输入规格与硬限制、三段式提示词公式、镜头拆解规则、视频编辑模式（角色/背景/台词替换与高精度指令）、出海多语种对白、商用场景十类选型、文字乱码解法

## 星数曲线

```mermaid
xychart-beta
    title "3ALLBUY14/h3-prompt-builder 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-30"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-30 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `86a9524bcfd4` · [字段定义](../../DATASET.md)*
