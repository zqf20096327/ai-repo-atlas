# SimaDevelopment/opsiforce

⭐ 38 · TypeScript · AGPL-3.0 · 推送 2026-10-22 · [GitHub](https://github.com/SimaDevelopment/opsiforce) · 组织维护

**自托管平台：在自有 Kubernetes 上构建、托管 AI 生成的应用与 agent**

面向团队的自托管多租户 Web 平台：用户在浏览器中与基于 OpenCode 的 AI agent 对话，agent 在隔离的 Linux/Kubernetes 工作区中编写真实代码、运行命令、安装包并直接托管生成的应用（含 HTTPS 路由、Dev/Production 多环境、持久化文件系统）。平台提供 LLM 网关（Bifrost，虚拟密钥与预算控制）、服务网关、定时任务、SSO/RBAC 与白标集成。需部署到 Kubernetes 集群运行，是托管服务而非桌面应用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每个项目独立 K8s pod：OpenCode agent、VS Code web IDE、数据库查看器与持久化工作区
- 构建同时托管：反向代理 HTTPS 路由、Development/Production 多环境、git 增量发布
- Bifrost LLM 网关提供虚拟密钥、用量追踪与预算控制，不向 pod 暴露真实 provider 密钥
- 白标嵌入、SSO/OIDC、组织级 RBAC 与权限字符串贯通前后端

## 适用场景

- 团队在自有基础设施上用对话式 agent 构建并托管内部仪表盘、表单与门户应用
- 将 AI 应用构建能力作为白标功能嵌入现有产品
- 让 agent 生成的应用带持久状态、多环境与凭证隔离地长期运行

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: Opsiforce is a self-hosted, multi-tenant **web platform** for building and running AI-generated apps inside your own
> L52: |AI coding workspace|A chat-driven agent powered by OpenCode, embedded into the Opsiforce frontend rather than ifra
> L61: |LLM gateway|Bifrost gives each project virtual LLM keys, usage tracking, and budget enforcement without exposing r

## 星数曲线

```mermaid
xychart-beta
    title "SimaDevelopment/opsiforce 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-25 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d8883cd8ec4d` · [字段定义](../../DATASET.md)*
