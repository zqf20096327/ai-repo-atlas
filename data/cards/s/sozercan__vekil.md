# sozercan/vekil

⭐ 22 · Go · MIT · 推送 2026-10-28 · [GitHub](https://github.com/sozercan/vekil) · 个人维护

**本地 AI 网关：用统一端点代理多上游模型服务**

Go 编写的反向代理，在本地暴露 Anthropic Messages、Gemini 与 OpenAI Chat Completions/Responses 兼容 API，将请求路由至 GitHub Copilot、Azure OpenAI、OpenAI Codex 或通用 OpenAI/Anthropic 兼容上游。支持 schema v2 显式路由、有序故障转移与语义策略路由，可通过 vekil launch 以短时会话启动 Claude Code、Codex CLI、Copilot CLI。提供 Docker 镜像、原生二进制与 macOS 托盘应用（Homebrew 安装，应用未签名）。

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

- 统一暴露 Anthropic/Gemini/OpenAI 三种客户端 API 面
- 多上游路由：GitHub Copilot、Azure OpenAI、Codex 与通用兼容服务，含有序故障转移
- 一条命令启动 Claude Code / Codex CLI / Copilot CLI 的回环代理会话
- 零配置模式可直接对接 GitHub Copilot 订阅

## 适用场景

- 让 Claude Code 使用 GitHub Copilot 订阅额度
- 不改客户端配置即可切换上游模型供应商
- 将 Codex CLI 指向 Azure OpenAI 或自建兼容服务

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L7: Vekil is a Go reverse proxy that exposes Anthropic, Gemini, and OpenAI-compatible APIs behind one local endpoint. Ru
> L20: - **Multi-provider routing** across GitHub Copilot, Azure OpenAI, OpenAI Codex, and generic compatible providers; s

## 星数曲线

```mermaid
xychart-beta
    title "sozercan/vekil 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-29 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `3d8a21a5bb67` · [字段定义](../../DATASET.md)*
