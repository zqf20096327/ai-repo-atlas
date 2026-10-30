# zimodzh/dsh-plugin-dev-skills

⭐ 15 · MIT · 推送 2026-09-04 · [GitHub](https://github.com/zimodzh/dsh-plugin-dev-skills) · [官网](https://github.com/zimodzh/dsh-plugin-dev-skills) · 个人维护 · 中文 README

**教 agent 开发 DeepSeek Harness 插件的技能包**

遵循 Agent Skills 规范的技能包（SKILL.md + 13 份 references），将 DeepSeek Harness（DSH）官方文档中的插件开发约定收敛为可执行标准：覆盖插件生命周期、事件分发、工具开发、LLM 适配器协议、五种插件形态与打包安装等。加载该技能的 agent 可按统一方式开发 DSH 插件。技能本身免构建免配置，git clone 到对应 agent 的技能目录即可；实际开发需 Node.js、pnpm 与 DSH 环境。社区维护，与 DeepSeek 官方无隶属关系。

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

- SKILL.md 含 9 条硬规则、6 个场景工作流与完成前检查清单
- 13 份 references 覆盖插件形态、事件分发、工具、LLM 适配器、打包安装
- 兼容 DSH、Claude Code、Codex、VS Code Copilot 等技能目录约定
- 附 12 正例 + 9 负例的 description 触发回归评测集与两个示例插件

## 适用场景

- 让 agent 按统一标准帮我编写 DSH 插件、工具或适配器
- 查阅 DSH 插件形态、事件分发与打包安装的详细规范
- 在多个 agent 框架间复用同一套 DSH 插件开发技能

## 场景标签

 · 领域:AI Agent 开发工具/知识

## 证据(README 行号)

> L13: 一套遵循 Agent Skills 规范 的技能，用于开发 **DeepSeek Harness（DSH）** 插件。
> L15: DSH 是一个插件化的 Agent Harness SDK：模型适配器、工具注册表、会话日志、甚至 agent loop 本身，全都是可以从配置里替换的 Cordis 插件。本技能把官方文档里散落在教程、参考手册与生成目录中的约定
> L24: ├── references/   # 13 份详细标准，按需加载；索引见 references/README.md

## 星数曲线

```mermaid
xychart-beta
    title "zimodzh/dsh-plugin-dev-skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `82adeb6a82b0` · [字段定义](../../DATASET.md)*
