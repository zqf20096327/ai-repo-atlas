# qdxiao/llmjsonrepair

⭐ 12 · Go · MIT · 推送 2026-11-27 · [GitHub](https://github.com/qdxiao/llmjsonrepair) · 个人维护 · 中文 README

**修复 LLM 输出残缺 JSON 的 Go 库**

Go 语言库，针对 LLM 输出的 JSON 因截断、缺少引号、括号未闭合、缺少分隔符等问题无法解析的场景，提供结构修复。提供 Repair()（返回修复后的 JSON 字符串）与 Loads()（返回解析后的 Go 数据结构）两个 API，支持深度嵌套结构与连续多 JSON 对象流的处理。README 明确修复边界：无法恢复未生成的值，要求修复后校验根类型与必填字段，关键数据缺失时应重试上游请求；还给出用指针字段区分 null、缺失与显式 0 的方法。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Repair/Loads 两个 API：返回格式化 JSON 或解析后的 Go 值
- 支持深度嵌套、多 JSON 对象流截断等修复场景
- 上下文感知推断缺失结构，明确声明修复边界
- 提供 Go Playground 在线试用入口

## 适用场景

- LLM 返回的 JSON 被截断且不便重试请求时做修复
- 解析含多 JSON 对象的连续输出流
- 结构化输出管道中对解析前文本做兜底处理

## 场景标签

 · 领域:LLM 基础设施/开发工具库

## 证据(README 行号)

> L7: Go library for salvaging malformed LLM JSON when retrying is not an option.
> L44: 专门用于修复大模型输出 JSON 格式错误的 Go 语言库
> L121: A Go library specifically designed to repair malformed JSON output from Large Language Models (LLMs)


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `79dcd161d1e7` · [字段定义](../../DATASET.md)*
