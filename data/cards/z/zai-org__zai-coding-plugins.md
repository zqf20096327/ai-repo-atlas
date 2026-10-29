# zai-org/zai-coding-plugins

⭐ 130 · JavaScript · Apache-2.0 · 推送 2026-02-22 · [GitHub](https://github.com/zai-org/zai-coding-plugins) · 组织维护 · 中文 README

**Z.ai 的 Claude Code 插件市场：GLM Coding Plan 用量查询与反馈**

Z.ai（zai-org）维护的 Claude Code 插件集合，当前包含两个插件：glm-plan-usage 查询 GLM Coding Plan 的配额与用量统计，glm-plan-bug 提交问题反馈，后者会汇总当前对话上下文以辅助定位问题（README 两次提示）。安装方式为在 Claude Code 内添加 marketplace 后安装插件，或用 npx @z_ai/coding-helper 工具管理。前置条件为 Node.js 18+ 与 Claude Code CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- glm-plan-usage 查询 GLM Coding Plan 配额与用量统计
- glm-plan-bug 提交反馈并汇总对话上下文辅助定位
- 通过 claude plugin 命令或 npx @z_ai/coding-helper 安装

## 适用场景

- 在 Claude Code 中查看 GLM Coding Plan 的剩余配额
- 向 Z.ai 提交 GLM Coding Plan 的问题反馈

## 场景标签

 · 领域:开发者工具/LLM 服务配套

## 证据(README 行号)

> L5: A collection of plugins to enhance coding productivity and provide GLM Coding Plan relate service for Claude Code.
> L11: |**glm-plan-usage**|Query quota and usage statistics for GLM Coding Plan|

## 星数曲线

```mermaid
xychart-beta
    title "zai-org/zai-coding-plugins 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-29"]
    y-axis "stars" 129 --> 132
    line [130, 131, 130]
```

2026-10-18 130 → 2026-10-29 130（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `d5ef5c8dde4f` · [字段定义](../../DATASET.md)*
