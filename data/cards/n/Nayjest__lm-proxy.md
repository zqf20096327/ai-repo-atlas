# Nayjest/lm-proxy

⭐ 157 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/Nayjest/lm-proxy) · 个人维护

**面向开发者的 OpenAI 兼容多提供商 LLM 代理网关**

基于 Python/FastAPI 的轻量 HTTP 代理服务，将 OpenAI、Anthropic、Google（Vertex AI / AI Studio）及本地 PyTorch 推理统一到单一 OpenAI 兼容 API 端点，可作为 Python 库或独立服务运行。机制包括按模型名通配符的动态路由、实时 token 流式传输、虚拟 API Key 与上游 Key 分离管理、用户组访问控制与外部 OIDC 验证（Keycloak/Auth0/Okta），支持 TOML/YAML/JSON/Python 配置及官方 Docker 镜像。需 Python 3.11+，Anthropic/Google 连接器为可选依赖安装。

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

- 单一 OpenAI 兼容端点统一接入 OpenAI/Anthropic/Google/本地 PyTorch 推理
- 按模型名通配符的动态路由与随机负载均衡
- 虚拟 API Key 与上游 Provider Key 分离，支持用户组粒度访问控制
- 可作为 Python 库或独立 HTTP 服务/Docker 容器运行

## 适用场景

- 不改客户端代码即可在云提供商与本地模型间切换
- 团队内按用户组分配可用模型与配额
- 通过 OIDC（Keycloak/Auth0/Okta）令牌做 API 鉴权

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3:  Lightweight, OpenAI-compatible HTTP proxy server / gateway unifying access to multiple Large Language Model provide
> L15: Built with Python, FastAPI and MicroCore, **LM-Proxy** seamlessly integrates cloud providers like Google, Anthropic
> L17: It works as a drop-in replacement for OpenAI's API, allowing you to switch between cloud providers and local models

## 星数曲线

```mermaid
xychart-beta
    title "Nayjest/lm-proxy 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 155 --> 158
    line [156, 157, 157]
```

2026-10-18 156 → 2026-10-30 157（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `ae34ef8ddaf2` · [字段定义](../../DATASET.md)*
