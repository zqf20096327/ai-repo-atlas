# alexandrevilain/ollama-machine

⭐ 42 · Go · Apache-2.0 · 推送 2026-02-23 · [GitHub](https://github.com/alexandrevilain/ollama-machine) · 个人维护

**为 Ollama 供给 GPU 云实例的 docker-machine 式管理工具**

受 docker-machine 启发的开源命令行工具，用于在云上创建、列出、重启和删除预配置 Ollama 的 GPU 实例。云凭据存入系统 keyring 加密保存；默认实例不暴露公网，需通过 SSH 隧道或 Tailscale 访问。已支持 OpenStack、OVHcloud、AWS，GCP、Azure 等在路线图中。提供预编译二进制与源码构建（make build）两种安装方式，面向需要弹性 GPU 资源运行 Ollama 的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 云凭据存入系统 keyring 加密存储
- GPU 实例自动化供给，预装 Ollama 及依赖
- 默认不暴露公网，支持 SSH 隧道与 Tailscale 访问
- 支持 OpenStack、OVHcloud、AWS，跨 macOS/Linux/Windows

## 适用场景

- 按小时在云端开 GPU 实例跑 Ollama 模型，用完即删
- 在多个云厂商间切换管理运行 Ollama 的实例
- 不把 Ollama 暴露公网，通过隧道或 Tailscale 私有访问

## 场景标签

 · 领域:AI 基础设施/云资源管理

## 证据(README 行号)

> L3: Think `docker-machine` but for GPU cloud instances running Ollama, with a focus on safe cloud credentials storage an
> L9: **Ollama-machine** is an open-source tool designed to simplify and secure the management of GPU-powered cloud instan

## 星数曲线

```mermaid
xychart-beta
    title "alexandrevilain/ollama-machine 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-31 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `5227fa46f744` · [字段定义](../../DATASET.md)*
