# hangar-hub/hangar

⭐ 3 · Go · NOASSERTION · 推送 2026-11-22 · [GitHub](https://github.com/hangar-hub/hangar) · [官网](https://hangar.page) · 组织维护

**自托管模型与数据集仓库：私有 Hugging Face Hub 替代与镜像**

自托管的模型与数据集存储服务，兼容 Hugging Face Hub API，保持上游 Repo ID 与 Commit SHA 不变；支持 HF 客户端（设置 HF_ENDPOINT 后 transformers/diffusers/vLLM 等不改代码）、git/git-lfs、Ollama 与 LM Studio 拉取；含 Web UI、GGUF 查看器、Dataset Viewer，支持仅按指定量化文件拉取。部署形式为单容器、Docker Compose、Helm 或二进制，可基于 Postgres 与 S3 兼容存储横向扩展，支持 OIDC 与 OpenTelemetry。服务仅存储和分发文件，不运行模型；许可证为 Elastic License 2.0（禁止对外提供托管服务）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 兼容 Hugging Face Hub API，HF 客户端设置 HF_ENDPOINT 即可用
- 支持从 huggingface.co 拉取一次后离线（air-gapped）分发的镜像模式
- 支持 Ollama 拉取 GGUF 仓库与 LM Studio 安装命令
- 提供 Web UI、GGUF 查看器与 Dataset Viewer

## 适用场景

- 在公司内网或离线环境搭建私有模型仓库
- 为自有模型建立带版本历史的模型 registry
- 减少重复从 huggingface.co 拉取大模型
- 用 Dataset Viewer 预览和检索自有数据集

## 场景标签

 · 领域:MLOps/模型分发基础设施

## 证据(README 行号)

> L10: Hangar is a self-hosted model and dataset hub, compatible with the Hugging Face Hub API, git, Ollama and LM Studio.
> L31: Hangar stores and serves files; it doesn't run models. To see how it compares with olah, JFrog Artifactory, Sonatyp


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `66265e4649b3` · [字段定义](../../DATASET.md)*
