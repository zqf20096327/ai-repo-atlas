# AgustiPuigserver/opus-prompt-architect

⭐ 126 · HTML · 推送 2026-10-23 · [GitHub](https://github.com/AgustiPuigserver/opus-prompt-architect) · 个人维护

**面向 LLM 的提示词架构设计工具，浏览器本地构建与导出提示词**

名为 MythosCraft 的提示词构建套件：以核心意图、语气矩阵、上下文锚点与触发-响应映射组成模块化节点图，由引擎将其线性化为面向 Claude、GPT-4 等模型的优化提示词，并提供 Token 预算规划、变体对照测试、版本历史与 12+ 格式导出。默认在浏览器会话内本地处理提示词数据，不上传服务器；接入外部 LLM API 的功能列于 2026 路线图 Q2，尚未实现。README 声明其不保证模型输出质量。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 意图+语气向量+上下文锚点+触发映射的模块化提示词组装
- Token 预算规划与提示词变体并排对照测试
- 12+ 格式导出（JSON、YAML、Markdown 等）与版本历史追踪
- 默认浏览器本地处理提示词数据，不外传服务器

## 适用场景

- 为不同语气与技术场景构建可复用的提示词模板
- 对照测试多个提示词变体并追踪演进历史
- 标准化客服聊天机器人等产品的 AI 行为指令

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L17: MythosCraft is **not** a simple prompt editor. It is a full-spectrum prompt development suite that includes:
> L46: MythosCraft is built on a **modular node system**. Each prompt is a *weave* — a directed graph of instruction nodes
> L82: |Q2|Integration with external LLM APIs (streamlined dispatch)|

## 星数曲线

```mermaid
xychart-beta
    title "AgustiPuigserver/opus-prompt-architect 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 125 --> 127
    line [126, 126]
```

2026-10-18 126 → 2026-10-24 126（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `d468ffa8cb96` · [字段定义](../../DATASET.md)*
