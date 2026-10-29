# seungmanchoi/react-native-fsd-agent-template

⭐ 51 · TypeScript · 推送 2026-10-27 · [GitHub](https://github.com/seungmanchoi/react-native-fsd-agent-template) · 个人维护 · 中文 README

**React Native + Expo 项目模板：内置 FSD 架构与 10 个 Claude Code agent**

面向 React Native + Expo 的生产级项目模板，采用 Feature-Sliced Design 架构，内置 10 个 Claude Code agents 与 10 个 skills 组成的 AI agent harness：一条命令可运行从市场调研、PRD、设计系统、FSD 模块脚手架、API 集成到 QA 验证的完整流水线，上线后通过 /iterate-app 循环持续迭代。同时附带 AdMob 广告、Firebase 分析、安全 token 存储、应用内评分等生产模块。基于 Claude Code / Codex CLI 使用，通过模板克隆与 npm 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 10 个 Claude Code agents 覆盖从构思到 QA 验证的全生命周期流水线
- /iterate-app 上线后持续改进循环（按 KPI 差距/技术债/覆盖率排序）
- 生产模块已接线：AdMob（UMP/ATT）、Firebase、expo-secure-store、评分策略引擎
- 代码智能 codegraph（tree-sitter 知识图谱，可选）与 ponytail 编码原则

## 适用场景

- 用 AI agent 团队从零搭建一个 React Native 应用并持续迭代
- 以 FSD 架构快速启动带广告、分析、认证的生产级移动应用
- 为 Claude Code / Codex CLI 提供结构化 agent harness 开发环境

## 场景标签

`代码生成` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L7: > **What makes this different?** This template includes 10 Claude Code agents and 10 skills that understand FSD arch
> L24: |**idea-researcher**|Market research, app idea generation|"Find app ideas"|
> L219: ### 6. Using the AI Agent Harness (Claude Code · Codex)

## 星数曲线

```mermaid
xychart-beta
    title "seungmanchoi/react-native-fsd-agent-template 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-29 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `37cb40c5328d` · [字段定义](../../DATASET.md)*
