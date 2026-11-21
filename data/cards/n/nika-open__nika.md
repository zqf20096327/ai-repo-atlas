# nika-open/nika

⭐ 100 · Rust · AGPL-3.0 · 推送 2026-11-20 · [GitHub](https://github.com/nika-open/nika) · [官网](https://nika.sh) · 组织维护

**把重复的 AI 工作固化为可检查、可验证的工作流文件**

Nika 是一个开源（AGPL-3.0）的本地优先工作流引擎：将自然语言描述编译为 `.nika` 工作流文件，运行前通过静态检查展示将使用的模型、工具、访问范围与费用上限（不调用模型），运行时可使用用户选择的模型（本地或 API），每次运行生成哈希链式记录可事后验证。包含 lethal trifecta 安全检查（私有读取+不可信输入+外发需人工放行）、人工审批门与费用预算拒绝机制。Rust 单二进制提供 CLI/TUI，附带 TypeScript SDK。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言编译为 `.nika` 工作流文件，静态检查不调用模型
- lethal trifecta 检测：数据泄露路径需人工门禁放行
- 运行前费用上限估算，超预算拒绝启动
- 哈希链运行记录 `nika trace verify` 可验证篡改

## 适用场景

- 每周例行从会议记录提取行动项并保存为可复用文件
- 在本地模型上运行不外发数据的工作流
- CI 中带人工审批门的构建/发布流程
- 需要留存可验证运行记录的自动化任务

## 场景标签

`工作流自动化` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L43: tamper-evident record you can verify. One Rust binary with a terminal
> L44: Session and a command line, plus a TypeScript SDK for your applications;
> L295: (Ollama, llama.cpp, LM Studio, vLLM) work too: `nika catalog` lists them.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `f3519bfccab5` · [字段定义](../../DATASET.md)*
