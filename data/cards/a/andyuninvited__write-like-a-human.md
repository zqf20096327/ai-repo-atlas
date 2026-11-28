# andyuninvited/write-like-a-human

⭐ 3 · TypeScript · MIT · 推送 2026-11-02 · [GitHub](https://github.com/andyuninvited/write-like-a-human) · [官网](https://its-giving-ai-vibes.vercel.app) · 个人维护

**从你的真实修改中学习写作风格的 Claude Code 技能与 CLI**

以 Claude Code 技能加可选 CLI 的形式提供：从用户粘贴的 3–10 篇真实写作样本建立风格基线，将用户每次对 AI 草稿的修改记录下来，同一修改出现两次即转为规则，被违反三次即固化为 rules.json 中的正则检查，用于在下一次草稿交付前执行 lint。检查为本地机械规则，无运行时依赖，数据不外发；另提供确定性 eval 套件检验规则覆盖率。要求 Node 20+，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从 draft/final 编辑对中学习，第二次重复的修改自动升为规则
- 机械正则检查与词预算（如 --max-words）在草稿交付前 lint
- 确定性 eval 套件（Ban recall、Lard factor 等指标），无需调用模型
- 全部本地运行，style/ 目录默认加入 .gitignore

## 适用场景

- 让 Claude 写出的邮件和文章符合我自己的语气和用词习惯
- 把反复手动改 AI 草稿的纠正固化成自动检查规则
- CI 或脚本中对文本跑风格 lint（exit 1 报错）

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L11: write-like-a-human learns from the signal most AI writing tools throw away, which is your edits. Every time you rew
> L13: It's a Claude Code skill plus a small CLI, MIT licensed. It runs locally, so nothing leaves your machine.
> L84: Node 20 or newer. No runtime dependencies.

## 星数曲线

```mermaid
xychart-beta
    title "andyuninvited/write-like-a-human 星数(近 2 点)"
    x-axis ["2026-11-01", "2026-11-28"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-01 3 → 2026-11-28 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `3d417086fb34` · [字段定义](../../DATASET.md)*
