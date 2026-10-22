# BerriAI/moyai

⭐ 276 · Python · MIT · 推送 2026-10-21 · [GitHub](https://github.com/BerriAI/moyai) · 组织维护

**自托管的共享 AI 编码工作区：后台运行编码 agent**

自托管的多用户 AI 编码工作区应用：通过聊天界面与 agent 交互、指挥其工作、查看其运行的计算机并保留文件与历史。技术栈为 Pydantic AI 与 Harness 提供 agent 能力，Temporal 提供持久化执行，Modal 或 AWS Lambda MicroVMs 提供执行计算机，LiteLLM 作为模型网关接入模型。以 Docker 镜像部署为主，本地快速启动自动管理 SQLite、加密文件存储与本地 Temporal 开发服务器；团队部署需自备 PostgreSQL、S3 兼容存储与 HTTPS 域名。源码开发需 Python 3.13、Node.js 22、Rust 1.88 与 uv。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Pydantic AI + Temporal 持久执行 + Modal/Lambda MicroVM 沙箱计算机 + LiteLLM 模型网关的架构
- 本地 Docker 快速启动自动管理 SQLite、加密存储与 Temporal 开发服务器
- 团队部署支持 standalone/split 拓扑与外部或内置 Temporal
- Swarms：持久 agent 团队、共享发现、成员独立计算机、Pause/Resume 时间控制

## 适用场景

- 在团队服务器上部署一个共享的编码 agent 工作区，笔记本离线时任务仍持续运行
- 通过聊天让 agent 在沙箱计算机上完成编码与联网服务任务并保留产物
- 审批、Slack 集成等方式监督与介入 agent 的后台工作

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: Moyai is a shared AI workspace for coding and connected-service tasks. Chat with
> L6: runs durable execution, Modal or AWS Lambda MicroVMs provide its computer, and LiteLLM supplies models.
> L5: resulting files and history. Pydantic AI and Harness provide the agent; Temporal

## 星数曲线

```mermaid
xychart-beta
    title "BerriAI/moyai 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 265 --> 273
    line [266, 268, 272]
```

2026-10-18 266 → 2026-10-22 272（+6）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `7bac8f446fde` · [字段定义](../../DATASET.md)*
