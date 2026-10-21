# CoderLuii/HolyClaude

⭐ 2,583 · JavaScript · MIT · 推送 2026-10-18 · [GitHub](https://github.com/CoderLuii/HolyClaude) · [官网](https://holyclaude.coderluii.dev) · 个人维护

**容器化 AI 编码工作站：一条命令运行 Claude Code 与 8 个 AI CLI**

面向开发者的 Docker 化 AI 开发工作站：单容器打包官方 Claude Code CLI、CloudCLI Web UI（端口 3001）、Chromium+Xvfb+Playwright 无头浏览器、8 个 AI CLI（Gemini、Codex、Cursor、TaskMaster、Junie、OpenCode、Pi 等）与 50+ 开发工具，用 s6-overlay 做进程管理，配置与工作区经 bind mount 持久化。用户以现有 Anthropic Max/Pro 订阅（OAuth）或 API key 登录，工具直接读取容器内凭据联系各提供商，项目本身不中转凭据。提供 full/slim 两类镜像，支持 amd64/arm64；远程访问建议走 Tailscale 或 Cloudflare Tunnel 而非端口转发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单容器集成 Claude Code、Web UI、无头浏览器与 50+ 开发工具
- 8 个 AI CLI 预装，各用自有账号/API key 认证，凭据不经项目中转
- full/slim 双镜像变体，AMD64 与 ARM64 多架构支持
- s6-overlay 进程管理，配置与工作区 bind mount 持久化，docker compose pull 即更新

## 适用场景

- 用现有 Claude 订阅或 API key 在浏览器中使用 Claude Code
- 在服务器/NAS 上搭建常驻的 AI 编码环境，避免重复配置
- 让 AI 编码代理配合无头浏览器完成截图与网页测试

## 场景标签

`编码 Agent` `浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L23: One command. Full AI development workstation. Claude Code, web UI, headless browser, 8 AI CLIs, 50+ dev tools — con
> L27: **Works with your existing Claude Code subscription.** Max/Pro plan, API key — whatever you have, it just works.
> L127: |**AI CLIs**|8 providers, one container|Install each one separately across 3 package managers|

## 星数曲线

```mermaid
xychart-beta
    title "CoderLuii/HolyClaude 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-21"]
    y-axis "stars" 2582 --> 2584
    line [2583, 2583]
```

2026-10-18 2,583 → 2026-10-21 2,583（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `50d8d893fd2a` · [字段定义](../../DATASET.md)*
