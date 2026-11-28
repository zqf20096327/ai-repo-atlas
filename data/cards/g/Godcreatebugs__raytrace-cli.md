# Godcreatebugs/raytrace-cli

⭐ 113 · JavaScript · MIT · 推送 2026-11-27 · [GitHub](https://github.com/Godcreatebugs/raytrace-cli) · [官网](https://www.raytracer.si/) · 组织维护 · 中文 README

**为 coding agent 提供本地沙箱隔离与运行证据审计的 CLI**

raytrace-cli 将 Claude Code 或 Codex 运行在隔离环境中：每个本地沙箱是 Lima 创建的 Linux VM 内、gVisor 下的 Docker 容器，并运行项目的副本。沙箱外的采集器记录每个命令的真实退出码、文件读写与网络连接，与 agent 自报的 tool calls 在仪表盘中分层对照。仪表盘提供 Changes（逐提示 diff 与补丁）、Playground（从任意步骤分叉重跑）、链路追溯与搜索。本地沙箱 MIT 许可且不上传数据，云沙箱为可选的团队共享仪表盘。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 沙箱外采集器记录命令、文件与网络，agent 无法关闭或篡改
- Tool calls（agent 自报）与 Sandbox evidence（机器所见）双层对照
- Playground 从任意步骤分叉重跑并可用 npm test 等检查评分
- Initial scan 按 1-5 评分文件修改风险并可限制文件被 agent 修改

## 适用场景

- 审查 coding agent 实际执行的命令与网络连接
- 在隔离副本中运行 agent，保护本机文件与私网
- 对比不同模型或提示在同一项目上的运行结果
- 在 PR 评论中生成带退出码与成本的运行报告

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L53: RayTrace runs Claude Code or Codex in that isolated copy, records what actually
> L56: Each local sandbox is a Docker container under gVisor,
> L63: The dashboard has two layers. **Tool calls** are what the agent reported.

## 星数曲线

```mermaid
xychart-beta
    title "Godcreatebugs/raytrace-cli 星数(近 5 点)"
    x-axis ["2026-11-20", "2026-11-22", "2026-11-23", "2026-11-26", "2026-11-28"]
    y-axis "stars" 16 --> 121
    line [25, 24, 25, 111, 113]
```

2026-11-20 25 → 2026-11-28 113（+88）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `79250795a23b` · [字段定义](../../DATASET.md)*
