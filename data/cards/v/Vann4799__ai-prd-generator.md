# Vann4799/ai-prd-generator

⭐ 24 · JavaScript · MIT · 推送 2026-09-29 · [GitHub](https://github.com/Vann4799/ai-prd-generator) · 个人维护

**通过对话式访谈生成产品需求文档的 agent 技能**

以 SKILL.md 形式分发的 PRD 生成技能，运行于 Claude Code、Codex、OpenCode、Hermes Agent、Qoder CLI 等编码 agent。机制：先读取现有仓库并预填代码可证实的答案，再以每轮至多 4 题（共 16 题，涉支付/隐私等场景追加第 5 轮）的印尼语/英语双语访谈收集信息，按固定模板写出含 11 个章节的 PRD，用无依赖 Node 脚本确定性校验，并可导出 JSON 任务清单、Mermaid 路线图与 .cursorrules 交接文件。经 npx 或手工复制安装，无网络与外部依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 读仓库预填答案，只追问代码无法证实的问题
- 16 题 4 轮（条件触发第 5 轮）的双语对话式访谈
- 无依赖 Node 校验脚本强制 11 章节、P0 需有用户故事与验收标准
- 导出 JSON 任务清单、Mermaid 路线图与 .cursorrules 交接文件

## 适用场景

- 让编码 agent 通过对话替我写出 PRD 而非从零起草
- 基于现有代码库生成预填的 PRD 草稿
- 把 PRD 校验通过后导出为可执行任务清单供编码 agent 消费

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L8: Generate a Product Requirements Document through a short conversational
> L9: interview instead of making someone write one. Works with Claude Code, Codex,
> L13: first and pre-fills every answer the code can prove, writes the PRD from a fixed

## 星数曲线

```mermaid
xychart-beta
    title "Vann4799/ai-prd-generator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-31 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `7a4e37107f0c` · [字段定义](../../DATASET.md)*
