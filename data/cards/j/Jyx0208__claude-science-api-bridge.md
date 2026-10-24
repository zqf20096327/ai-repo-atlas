# Jyx0208/claude-science-api-bridge

⭐ 50 · Python · MIT · 推送 2026-07-07 · [GitHub](https://github.com/Jyx0208/claude-science-api-bridge) · [官网](https://github.com/Jyx0208/claude-science-api-bridge/releases/latest) · 个人维护 · 中文 README

**让 Claude Science 使用第三方 OpenAI 兼容 API 的 macOS 本地代理**

运行在本机的 Anthropic 兼容代理：接收 Claude Science 发出的 /v1/messages、/v1/models 与 OAuth/profile 请求，翻译成第三方 API（DeepSeek、OpenAI、硅基流动 Kimi 及任意 OpenAI 兼容 endpoint）可理解的格式，支持流式、工具调用、图片输入与 reasoning 过滤，并提供 Dashboard 配置管理、模型菜单补丁、一键更新。macOS 提供一键安装脚本与 DMG，Linux 从源码安装本地代理与 systemd 服务，但不会启动 Claude Science 桌面应用。另附给本地 AI agent 的完整操作手册。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Anthropic→OpenAI 请求翻译，支持流式、工具调用、图片 block
- Dashboard 管理 provider 配置档、模型映射与诊断日志
- 仅修改用户目录内 daemon 复制件的模型菜单补丁，不动系统网络配置
- 提供面向本地 AI agent 的安装/验收 prompt 与 runbook 文档

## 适用场景

- 在 Claude Science 中改用 DeepSeek、Kimi 等自有第三方 API key
- 把模型菜单显示为第三方真实模型名并按别名路由
- 让本地 agent 自动完成安装、配置与验证

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L7: Claude Science API Bridge 是一个运行在本机的 Anthropic-compatible 代理。它接收 Claude Science 发出的 `/v1/messages`、`/v1/models` 和 OAu
> L52: Claude Science 默认面向 Anthropic API。很多用户希望在 Claude Science 里使用自己的第三方 API，例如 DeepSeek、硅基流动 Kimi、OpenAI、DashScope、智谱或自建

## 星数曲线

```mermaid
xychart-beta
    title "Jyx0208/claude-science-api-bridge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-24 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `0f1314488395` · [字段定义](../../DATASET.md)*
