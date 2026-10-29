# BigJk/snd

⭐ 676 · TypeScript · MIT · 推送 2026-07-10 · [GitHub](https://github.com/BigJk/snd) · [官网](https://sales-and-dungeons.app/) · 个人维护

**用热敏打印机为 D&D 跑团打印手办物、法术卡等资料的桌面工具**

Sales & Dungeons 是面向龙与地下城等桌上角色扮演游戏 GM/DM 的热敏打印机工具：通过 HTML+Nunjucks 模板系统生成手办物、法术、信件、迷你角色卡等打印内容，支持多种打印机连接方式（USB、CUPS、串口等），可从 Open5e、CSV、FoundryVTT、5eTools 导入数据，内置随机生成器。AI 部分：接入 OpenAI/OpenRouter 或本地 LLM（如 LM Studio），按 prompt 生成或翻译条目、在模板中执行 AI 提示。仅支持 ESC/POS 控制码的热敏打印机。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- HTML+Nunjucks 模板系统与随机生成器，可导入导出模板与数据源
- 接入 Open5e、FoundryVTT 模组、5eTools、CSV 等外部数据
- AI LLM 支持（OpenAI、OpenRouter、自定义本地端点，兼容 OpenAI API）
- 跨 Windows/Mac/Linux/树莓派运行，另有 headless Docker 容器版

## 适用场景

- 跑团时在桌边即时打印魔法物品、法术卡、信件等手办物
- 为玩家快速生成迷你角色卡作为 DM 备注
- 用 prompt 让 AI 生成或翻译条目后直接打印

## 场景标签

 · 领域:游戏/桌面工具

## 证据(README 行号)

> L8: **Sales & Dungeons** — Thermal Printer as D&amp;D Utility.
> L49: - AI LLM Support (OpenAI, OpenRouter, Custom Local)
> L50:  - Generate entries by prompt using the power of AI

## 星数曲线

```mermaid
xychart-beta
    title "BigJk/snd 星数(近 5 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27", "2026-10-28", "2026-10-29"]
    y-axis "stars" 673 --> 677
    line [676, 674, 675, 676, 676]
```

2026-10-18 676 → 2026-10-29 676（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `932bd7887bd9` · [字段定义](../../DATASET.md)*
