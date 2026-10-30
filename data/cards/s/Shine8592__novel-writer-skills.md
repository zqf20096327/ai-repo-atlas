# Shine8592/novel-writer-skills

⭐ 15 · Python · 推送 2026-04-06 · [GitHub](https://github.com/Shine8592/novel-writer-skills) · [官网](https://clawhub.ai) · 个人维护 · 中文 README

**零 API 成本写中文长篇网文的 3 个 OpenClaw 技能包**

包含 3 个 OpenClaw 技能：novel-outliner 负责章节大纲与情感弧线、zh-novel-writer 负责整本小说生成流水线、novel-quality-checker 负责 3 阶段质量审查。生成环节仅调用免费 API 档位（ModelScope 的 DeepSeek-V3.2、智谱 GLM-4-Flash、Fyra.im 等），流水线为 Think→Plan→Build→Review→Ship→Retro。作者以 900K+ 字、90+ 章的作品《太初道果》作为实测记录，质量通过率 >90%，月度 API 花费为 ¥0。通过 openclaw skills install 命令安装，需先具备 OpenClaw 环境。

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

- 3 个技能覆盖大纲、生成、质量审查全流程
- 仅使用免费 API 档位，实测月花费 ¥0
- 900K+ 字、90+ 章长篇小说实测记录
- Think→Plan→Build→Review→Ship→Retro 六阶段流水线

## 适用场景

- 想零成本生成中文长篇网文的作者
- 为 OpenClaw agent 添加小说创作能力
- 参考免费 API 组合进行长文本生成实验

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L11: **3 OpenClaw skills** that write Chinese web novels from outline to final draft — using **only free API tiers**.
> L54: - **Build**: Main generation via free APIs

## 星数曲线

```mermaid
xychart-beta
    title "Shine8592/novel-writer-skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `ec068e52d5f3` · [字段定义](../../DATASET.md)*
