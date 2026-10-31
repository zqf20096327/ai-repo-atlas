# Code-Hdez/pokemon-firered-llm-mod

⭐ 14 · Python · NOASSERTION · 推送 2026-02-25 · [GitHub](https://github.com/Code-Hdez/pokemon-firered-llm-mod) · [官网](https://www.codehdez.com) · 个人维护

**将宝可梦火红 NPC 对话实时改写为 LLM 生成内容的模拟器桥接工具**

Lua+Python 桥接层，在 mGBA 模拟器中运行宝可梦火红时拦截 NPC 对话文本，经 TCP IPC 发送到 Python 端，调用 Gemini 对原文进行改写后实时注入回游戏，使每次对话措辞不同；当前版本仅改写原文语义而非自由生成。基于指纹机制对 NPC/对象交互分类，并提供内存扫描、文本注入测试、指纹收集等辅助模式。需要 mGBA 0.10+、Python 3.10+、美版火红 ROM（非 Rev 1），LLM 模式需 Gemini API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Lua↔Python TCP IPC（127.0.0.1:35600，行分隔 JSON）实时拦截并注入对话
- 通过 Gemini 改写 NPC 对话，保持语义但每次措辞不同
- 指纹机制对每个 NPC 交互进行分类
- 提供内存扫描、注入测试、指纹收集等 4 种运行模式

## 适用场景

- 玩火红时让每个 NPC 的对话措辞每次不同
- 探索 GBA 游戏内存与自定义字符编码
- 研究模拟器脚本与游戏对话注入的桥接方式

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3: A bridge between **mGBA** and a **Large Language Model** that gives every NPC in Pokémon FireRed a unique personalit
> L7: In this version the LLM takes the original NPC message and **paraphrases** it into a new line of dialog, keeping the
> L70: - **Gemini API key** - needed for LLM Inject mode (option 4). See `.env.example` for setup.

## 星数曲线

```mermaid
xychart-beta
    title "Code-Hdez/pokemon-firered-llm-mod 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `93f5adee0033` · [字段定义](../../DATASET.md)*
