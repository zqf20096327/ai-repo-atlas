# ErickWendel/ollama-webui-traefik-docker

⭐ 92 · Shell · MIT · 推送 2026-04-08 · [GitHub](https://github.com/ErickWendel/ollama-webui-traefik-docker) · [官网](https://ewbr.cc/ai-local-ew) · 个人维护

**用 Docker Compose 一键部署 Ollama 与 Open WebUI 并以 Traefik 反代的模板**

面向在 VPS 上自托管 LLM 服务的开发者：以 Docker Compose 编排四个服务——Traefik 反向代理（Let's Encrypt 自动 HTTPS）、Ollama 推理引擎（自动下载 gemma:2b、deepseek-r1:1.5b 等预设小模型）、模型下载辅助服务、Open WebUI 前端。提供安装脚本、域名配置（.env）、发送提示词的 Bash 脚本及 SCP 上传脚本。README 声明示例面向双核 8GB 内存的小型 VPS，且仅作示例用途、不建议直接用于生产环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Docker Compose 单命令启动 Ollama + Open WebUI + Traefik 全套服务
- 自动下载预设小模型（gemma:2b、deepseek-r1:1.5b、qwen2.5-coder:1.5b、codegemma:2b）
- Traefik 反向代理 + Let's Encrypt 自动 HTTPS
- 附带 request-ollama.sh 提示词脚本与 install-docker.sh 安装脚本

## 适用场景

- 在低配 VPS 上快速搭建可域名访问的私有 LLM 服务
- 为 Ollama 部署配备 Web 聊天界面与 HTTPS
- 作为 Docker 编排自托管 LLM 的参考示例

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: This repository provides a simple setup for running Ollama and Open WebUI with Traefik as a reverse proxy using **Do
> L49: ### 2. **Ollama (LLM Inference Engine)**

## 星数曲线

```mermaid
xychart-beta
    title "ErickWendel/ollama-webui-traefik-docker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 91 --> 93
    line [92, 92]
```

2026-10-18 92 → 2026-10-27 92（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `3e0f81c7448a` · [字段定义](../../DATASET.md)*
