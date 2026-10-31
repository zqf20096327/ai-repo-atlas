# mazamaka/claude-code-server-ops

⭐ 14 · Python · MIT · 推送 2026-10-03 · [GitHub](https://github.com/mazamaka/claude-code-server-ops) · 个人维护

**Claude Code API 服务器的部署与验证运维工具**

为 schmarta/claude-code-openai-server 提供运维工具集：渲染 systemd 服务单元并检查前置条件、把 Claude CLI token 写入服务环境、执行真实补全的健康探测（区别于 HTTP 存活检查）、覆盖文本/流式/工具调用/图像/会话行为的端到端冒烟测试，并支持另起端口的对照实例。脚本加 Python 标准库实现，冒烟套件无额外依赖；失败冒烟检查可通过退出码阻断发布。要求 Linux+systemd、Python 3.9+、curl 与已认证的 claude CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 渲染 systemd 单元并带 dry-run 安装选项
- 以真实补全作为健康探测，超出 HTTP liveness 检查
- 覆盖文本/流式/工具调用/图像/会话的冒烟套件
- 部署门禁退出码，失败的冒烟检查可阻断发布

## 适用场景

- 把 Claude Code API 服务器以 systemd 服务方式部署到 Linux
- 发布前用端到端冒烟检查验证服务器行为
- 用真实补全探测做服务健康监控

## 场景标签

 · 领域:LLM 基础设施/运维

## 证据(README 行号)

> L3: **Deploy and check a Claude Code API server with systemd, health probes and end-to-end smoke tests.**
> L11: - 🩺 **Health checks** — test a real completion, beyond the HTTP liveness endpoint.
> L12: - 🧪 **Smoke tests** — exercise text, streaming, tool calls, images and session behaviour.

## 星数曲线

```mermaid
xychart-beta
    title "mazamaka/claude-code-server-ops 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `af9395ade84b` · [字段定义](../../DATASET.md)*
