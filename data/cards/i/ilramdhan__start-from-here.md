# ilramdhan/start-from-here

⭐ 7 · JavaScript · MIT · 推送 2026-11-23 · [GitHub](https://github.com/ilramdhan/start-from-here) · [官网](https://ilramdhan.github.io/start-from-here/) · 个人维护

**面向 AI 编码代理的访谈式项目蓝图生成技能**

一个遵循 Agent Skills 开放标准的技能包：让用户的编码代理先进行多轮访谈（每题带推荐默认值、可跳过），再生成一套相互交叉核对的文档，包括 PRD、TRD、架构（C4/Mermaid）、ERD、威胁模型、测试、法务草案及 AGENTS.md，并输出就绪清单与首条实现提示词。不写应用代码，未知项标记 TBD/ASSUMPTION。支持 Lite/Standard/Enterprise 三档，进度可保存与续接，提供 session mode 适配小上下文窗口模型与纯聊天工具。

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

- 多轮访谈生成 PRD/TRD/架构/ERD/安全/法务等成套文档，共享 ID 交叉核对
- 不写应用代码；未知项标注 TBD，建议项标注 PROPOSAL/ASSUMPTION
- 进度写入 STATE.md，任意工具中可 resume；session mode 拆分工作包适配 8–32k 本地模型
- 8 种安装通道（npm CLI、gh、Claude Code/Codex 插件、Zip 上传、粘贴提示词等）

## 适用场景

- 用 AI 编码代理开发新应用前先生成完整项目蓝图
- 在现有仓库中补充缺失的架构、安全与协作文档
- 用小上下文本地模型分会话完成 Enterprise 级文档生成

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L18: **Plan first, then build. One Agent Skill that interviews you and writes the approved docs your AI coding agent nee
> L61: It is model-agnostic. It follows the Agent Skills open standard and also ships as a single pasteable prompt for cha
> L121: - **Resumable.** Progress is saved to `docs/.start-from-here/STATE.md` after every step. In any tool, with any mod

## 星数曲线

```mermaid
xychart-beta
    title "ilramdhan/start-from-here 星数(近 3 点)"
    x-axis ["2026-10-26", "2026-11-08", "2026-11-24"]
    y-axis "stars" 5 --> 8
    line [6, 7, 7]
```

2026-10-26 6 → 2026-11-24 7（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `07b2fdd6e8f9` · [字段定义](../../DATASET.md)*
