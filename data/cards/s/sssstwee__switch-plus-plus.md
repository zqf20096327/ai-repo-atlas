# sssstwee/switch-plus-plus

⭐ 14 · TypeScript · NOASSERTION · 推送 2026-10-16 · [GitHub](https://github.com/sssstwee/switch-plus-plus) · [官网](https://sssstwee.github.io/switch-plus-plus/) · 个人维护 · 中文 README

**给开发者：Claude Code/Codex 第三方模型配置切换与本地兼容网关**

桌面端工具（Tauri），为 Claude Code、Claude Desktop、Codex CLI/Desktop 管理多套模型配置，在官方账号与第三方模型配置间切换。内置本地兼容网关，处理 OpenAI-compatible、Anthropic-compatible、Responses 与 Chat Completions 协议差异，支持模型映射、认证隔离与请求记录/统计。提供环境检查、CLI 工具一键安装卸载、写入前预览与备份。注意：仓库为 source-available 部分源码，核心网关实现保留在私有 core，采用非商业专有许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多套配置保存、切换、写入前预览与自动备份
- 本地兼容网关处理 OpenAI/Anthropic/Responses/Chat Completions 协议差异
- 网关请求记录、token 统计、缓存与错误趋势图表
- 本机应用/CLI/配置路径环境检查与常用 CLI 工具一键安装升级

## 适用场景

- 在 Claude Code 或 Codex 中接入 DeepSeek/Kimi/GLM 等第三方模型
- 在官方账号与第三方厂商配置之间快速切换
- 排查本地 agent 请求链路与配置写入问题

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: Switch++ 是一个桌面端配置切换、模型路由和本地兼容网关工具，用来把第三方模型接入 Claude Code、Claude Desktop、Codex CLI和 Codex Desktop。也可以按 Claude Code 第三
> L37: - 统一承接 Claude 和 Codex 的第三方模型调用。
> L38: - 处理 OpenAI-compatible、Anthropic-compatible、Responses 和 Chat Completions 协议差异。

## 星数曲线

```mermaid
xychart-beta
    title "sssstwee/switch-plus-plus 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `3d6eb0b9a7d8` · [字段定义](../../DATASET.md)*
