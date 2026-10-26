# thomwebb/gac

⭐ 316 · Python · MIT · 推送 2026-10-19 · [GitHub](https://github.com/thomwebb/gac) · 个人维护 · 中文 README

**用 LLM 生成 git 提交信息的命令行工具**

Python 编写的命令行工具，以 `uvx gac` 替代 `git commit -m`：读取已暂存的代码变更，由大语言模型分析改动意图并生成多种格式（单行/标准/详细/50-72 规则）的提交信息，支持 35+ 个 LLM 提供商、25+ 种输出语言、智能变更分组（--group）、交互式反馈（重掷/编辑/自然语言修改）与使用统计（本地存储、可随时关闭）。内置提交前密钥检测。面向使用 git 的开发者，通过 uvx/PyPI 安装运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 35+ 个 LLM 提供商（含 OAuth 方式与自定义端点）
- 三种消息格式 + 50/72 规则 + DCO 签署
- --group 自动将相关变更拆分为多个逻辑提交
- 提交前自动扫描 API key、密码等敏感信息
- uvx gac serve 可作为 MCP server 向 AI agent 暴露提交工具

## 适用场景

- 我不想手写 commit message，让 LLM 根据代码改动生成
- 把一次大改动自动拆成多个符合逻辑的提交
- 用非英语（如中文、日语）生成提交信息
- 让 AI agent 通过 MCP 调用提交功能

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L17: **Automate your commits!** Replace `git commit -m "..."` with `uvx gac` for contextual, well-formatted commit messa
> L29: uvx gac  # Generate and commit with LLM

## 星数曲线

```mermaid
xychart-beta
    title "thomwebb/gac 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 315 --> 317
    line [316, 316]
```

2026-10-18 316 → 2026-10-26 316（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `10306636fdce` · [字段定义](../../DATASET.md)*
