# alexandrevilain/tabcoder

⭐ 15 · TypeScript · Apache-2.0 · 推送 2025-11-06 · [GitHub](https://github.com/alexandrevilain/tabcoder) · [官网](https://marketplace.visualstudio.com/items?itemName=alexandrevilain.tabcoder) · 个人维护

**VS Code 扩展：专注 AI 行内代码自动补全，多模型可选**

VS Code 扩展，提供以 Tab 接受的行内 AI 补全建议，不包含聊天或 Agent 功能。支持自带模型提供方（OpenRouter、OpenAI、Ollama 等），通过命令面板创建/切换/删除 AI Profile 配置 API 端点与密钥，凭据存于 VS Code 安全存储。项目因 KiloCode 移除实验性补全功能（PR #1565）而启动，从零重写并参考 Continue 的补全实现，定位为纯自动补全场景。采用 Apache 2.0 许可证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 行内 AI 建议，按 Tab 接受
- 自带提供方：OpenRouter、OpenAI、Ollama 等可配置多 Profile
- 凭据存于 VS Code 安全存储
- 功能范围限定为补全，无聊天/Agent

## 适用场景

- 在 VS Code 中边输入边获取 AI 补全建议
- 用自有 API 端点与本地模型（如 Ollama）做代码补全
- 替代已停止维护补全功能的工具补齐自动补全场景

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L3: **AI-driven code suggestions.**
> L28: - ⚡️ Inline AI suggestions accepted with **Tab**

## 星数曲线

```mermaid
xychart-beta
    title "alexandrevilain/tabcoder 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `2dca5f652667` · [字段定义](../../DATASET.md)*
