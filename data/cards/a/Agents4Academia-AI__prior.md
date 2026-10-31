# Agents4Academia-AI/prior

⭐ 15 · HTML · Apache-2.0 · 推送 2026-09-24 · [GitHub](https://github.com/Agents4Academia-AI/prior) · [官网](https://agents4academia.github.io) · 组织维护

**读取原始文献构建可审计贡献图谱的 agentic 系统，面向科研人员**

开源 agentic 系统 Prior：从 OpenAlex 与 arXiv 读取原始文献，经 Scoper（语料圈定）、Contributor（贡献与声明抽取）、Cartographer（跨论文关系连线）、Navigator（基于图谱的带引用回答）四个 agent，构建每条声明可溯源到 DOI 的贡献图谱，标记 supports/builds_on/refines/contradicts 关系与矛盾。提供 Graph/Papers/Eval/Report 四视图 UI，内置 152 篇论文的示例图谱（无需 API key 即可查看）。自评显示关系抽取正确率仅 21–53%，README 明确列出六项局限。Python ≥3.11，pip 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 四 agent 流水线：语料圈定→贡献抽取→跨论文关系→基于图谱的回答
- 声级溯源：每个节点一步到达来源论文与 DOI
- 标记跨论文矛盾（contradicts 边）与共识分层
- 三个可独立复用阶段（Explore/全文获取/Extract），免费通道无需 key

## 适用场景

- 梳理某领域已被声称、有争议与缺失的研究版图
- 查找论文间矛盾与知识前沿
- 获取带节点级引用的文献综述式回答
- 复用语料圈定与全文获取脚本做自己的文献管线

## 场景标签

`知识图谱` `科研工具` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: > An open-source agentic system that reads primary literature and builds an
> L63: Prior pipeline — SCOPE (Scoper) · EXTRACT (Contributor) · CONNECT (Cartographer) · NAVIGATE (Navigator), topic → an
> L65: - **Scoper** — topic → a scoped corpus (recall-then-precision + citation snowball to

## 星数曲线

```mermaid
xychart-beta
    title "Agents4Academia-AI/prior 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `883d2df4f459` · [字段定义](../../DATASET.md)*
