# treeleaves30760/all-code

⭐ 11 · Rust · MIT · 推送 2026-11-18 · [GitHub](https://github.com/treeleaves30760/all-code) · [官网](https://treeleaves30760.github.io/all-code/) · 个人维护 · 中文 README

**一次配置多家 LLM 提供方，启动 Claude Code/Codex CLI 等编码代理**

一个 CLI 工具（alc）：将同一 Codex/ChatGPT 登录凭证接入 Claude Code、OpenCode、Codex CLI、Antigravity CLI 等多种编码代理。机制上在本地回环端口启动适配器，把 Anthropic Messages、OpenAI Responses、Chat Completions、Google Code Assist 等三种线协议指向同一登录，无需 API key；支持会话镜像到浏览器页面远程操作、后台会话持久化、会话内 /model 切换模型。适配层为第三方兼容层，非 OpenAI/Anthropic 官方集成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同一 codex login 驱动 8 种以上编码代理，三种线协议共享一次登录
- 本地回环端口适配器，不要求 API key，无配置文件
- 任意会话镜像到浏览器页面，可从手机或其他设备操作
- 后台会话由独立 hub 持有，终端退出后仍存活

## 适用场景

- 用已付费的 ChatGPT/Codex 订阅登录运行 Claude Code
- 在同一台机器上统一切换多个编码代理的模型提供方
- 从手机或另一台设备远程操作终端里的编码会话

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: **Run Claude Code on the Codex/ChatGPT subscription you already pay for** — and
> L104: |Agent|Reaches the bridge over|Switching models|
> L112: alc starts its own Codex adapter on a loopback port and points only the launched


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 mid · 依据 README sha `0ba9be1307ce` · [字段定义](../../DATASET.md)*
