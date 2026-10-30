# chroma-core/agent-skills

⭐ 24 · TypeScript · MIT · 推送 2026-04-20 · [GitHub](https://github.com/chroma-core/agent-skills) · 组织维护

**Chroma 官方 AI Agent 技能包：指导 agent 接入 Chroma**

Chroma 团队发布的官方 Agent 技能仓库，含 chroma-local 与 chroma-cloud 两个技能：前者面向开源与自托管的 Chroma，后者覆盖 Chroma Cloud 的 CloudClient、Schema、Search 及云 CLI 工作流。用户通过 npx skills add 命令安装技能后，可对 agent 说“用 Chroma local 给项目加搜索”等指令，由对应技能指导集成。仓库提供构建流程生成 skills/registry.json 机器可读索引，并含技能模板脚手架与 Python/TypeScript 代码示例校验。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两个技能：chroma-local（开源/自托管）与 chroma-cloud（云工作流）
- npx skills add 命令行安装技能
- 构建时生成机器可读的 skills/registry.json 索引
- 提供新技能模板脚手架与 TS/Python 双语示例校验

## 适用场景

- 让 AI agent 按官方技能指引把 Chroma 检索集成进项目
- 为使用 Chroma Cloud 的 agent 提供 CloudClient 与云 CLI 工作流指导
- 为 agent 框架扩展 Chroma 向量库相关能力

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L3: Official AI Agent skills from the Chroma team for building with Chroma.
> L12: `chroma-local` helps with open source and self-hosted Chroma. `chroma-cloud` helps with Chroma Cloud, including Clo

## 星数曲线

```mermaid
xychart-beta
    title "chroma-core/agent-skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-30 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `546482fd6214` · [字段定义](../../DATASET.md)*
