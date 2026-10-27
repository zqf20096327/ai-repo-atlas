# parolkar/context-engineering-for-writers

⭐ 22 · Shell · NOASSERTION · 推送 2026-07-22 · [GitHub](https://github.com/parolkar/context-engineering-for-writers) · 个人维护

**面向写作者的上下文工程框架：用 Claude 多代理生成深度文章**

一套在 Claude CLI 上运行的写作上下文框架：通过 CLAUDE.md 全局写作规则、示例文章库与 INITIAL.md 选题描述，用 /generate-wrp 生成写作需求提示（WRP）蓝图，再由 /execute-wrp 分段起草、校验、修订成文。增强流程以 Claude Swarm 启动多代理写作团队，含研究、上下文工程、风格分析、写作与质量评审五类代理，支持会话保存与恢复。运行需 Ruby 3.2+、Bundler 与已配置的 Claude CLI，通过 bundle install 与 bin/launch 使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- WRP（写作需求提示）两步工作流：生成蓝图后执行写作
- Claude Swarm 多代理写作团队（研究/上下文/风格/写作/评审）
- CLAUDE.md 全局写作规则与 examples/ 范文模式学习
- 会话管理：可按 session-id 恢复写作进度

## 适用场景

- 让 AI 按我的写作风格和结构偏好起草深度文章
- 通过多代理团队完成从研究到定稿的文章流程
- 积累个人范文库，让后续写作持续对齐风格

## 场景标签

 · 领域:AI 写作/上下文工程

## 证据(README 行号)

> L88: Run in Claude Code:
> L107: The AI writing assistant will:
> L275: 1. **Launch the Writing Research & Essay Generation Swarm**:

## 星数曲线

```mermaid
xychart-beta
    title "parolkar/context-engineering-for-writers 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-27 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `2848fbb5ecf4` · [字段定义](../../DATASET.md)*
